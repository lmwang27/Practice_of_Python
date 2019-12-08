
import time
"""
Design a parking lot.

see CC150 OO Design for details.

n levels, each level has m rows of spots and each row has k spots.So each level has m x k spots.
The parking lot can park motorcycles, cars and buses
The parking lot has motorcycle spots, compact spots, and large spots
Each row, motorcycle spots id is in range [0,k/4)(0 is included, k/4 is not included),
compact spots id is in range [k/4,k/4*3)(k/4*3 is not included) and large spots id is in
range [k/4*3,k)(k is not included).
A motorcycle can park in any spot
A car park in single compact spot or large spot
A bus can park in five large spots that are consecutive and within same row.
it can not park in small spots


Example 1

Input:
level=1
num_rows=1
spots_per_row=11
parkVehicle("Motorcycle_1")
parkVehicle("Car_1")
parkVehicle("Car_2")
parkVehicle("Car_3")
parkVehicle("Car_4")
parkVehicle("Car_5")
parkVehicle("Bus_1")
unParkVehicle("Car_5")
parkVehicle("Bus_1")

Output:
true
true
true
true
true
true
false
true

Explanation: When there is a "Car_5", there is no "Bus_1".
Example 2

Input:
level=1
num_rows=1
spots_per_row=14
parkVehicle("Motorcycle_1")
parkVehicle("Motorcycle_2")
parkVehicle("Motorcycle_3")
parkVehicle("Car_1")
parkVehicle("Car_2")
parkVehicle("Car_3")
parkVehicle("Motorcycle_4")
parkVehicle("Car_4")
parkVehicle("Car_5")
parkVehicle("Car_6")
parkVehicle("Car_7")
parkVehicle("Bus_1")
unParkVehicle("Car_1")
unParkVehicle("Motorcycle_4")
unParkVehicle("Car_3")
unParkVehicle("Car_6")
parkVehicle("Bus_1")
unParkVehicle("Car_7")
parkVehicle("Bus_1")

Output:
true
true
true
true
true
true
true
true
true
true
true
false
false
true

"""
"""
Use cases:
Get available count
Park vehicle
Clear spot
Calculate price
"""

"""
classes:
ParkingLot
Vehicles : Car,Bus,Motorcycle
ParkingSpot
Level

"""

"""
Management类常见Use case:
- Reservation : X
- Serve: Park vehicle
- Check out: Clear spot + Calculate price
"""


# enum type for Vehicle
class VehicleSize:
    motorcycle =1
    compact = 2
    large = 3
    other = 99


class ParkingRate:
    hourly_rate = 3
    daily_rate = 10
    half_day_rate = 8


class Ticket:
    def __init__(self, vehicle):
        self.current_time = time.ctime()
        self.end_time = 0
        self.plate_license = vehicle.license_plate


class Vehicle:
    def __init__(self):
        self.parking_spots = []
        self.spot_needed = 0
        self.size = None
        self.license_plate = None
        self.ticket = 0

    def get_spots_needed(self):
        return self.spot_needed

    def get_size(self):
        return self.size

    def park_in_spot(self, spot):
        self.parking_spots.append(spot)

    def clear_spots(self):
        for spot in self.parking_spots:
            spot.remove_vehicle()
        self.parking_spots = []

    def can_fit_in_spot(self, spot):
        raise NotImplementedError("This method should have implemented.")


class Motorcycle(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.spot_needed = 1
        self.size = VehicleSize.Motorcycle

    def can_fit_in_spot(self, spot):
        return True


class Car(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.spot_needed = 1
        self.size = VehicleSize.compact

    def can_fit_in_spot(self, spot):
        return spot.get_size() == VehicleSize.large or spot.get_size == VehicleSize.compact


class Bus(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.spot_needed = 5
        self.size = VehicleSize.Large

    def can_fit_in_spot(self, spot):
        return spot.get_size() == VehicleSize.large

"""
define one spot with its property and size and 
"""


class ParkingSpot:
    def __init__(self, level, row, number, size):
        self.level = level
        self.row = row
        self.number = number
        self.size = size
        self.vehicle = None

    def is_available(self):
        if self.vehicle is None:
            return True
        else:
            return False

    def can_fit_vehicle(self, vehicle):
        return self.is_available() and vehicle.can_fit_in_spot(self)

    def park(self, v):
        if not self.can_fit_vehicle(v):
            return False

        self.vehicle = v
        self.vehicle.park_in_spot(self)
        return True

    def remove_vehicle(self):
        self.level.spot_freed()
        self.vehicle = None

    def get_row(self):
        return self.row

    def get_spot_number(self):
        return self.spot_number

    def get_size(self):
        return self.spot_size


class Level:
    def __init__(self, floor, num_rows, spots_per_row):
        self.floor = floor
        self.spots_per_row = spots_per_row
        self.number_spots = 0
        self.available_spots = 0
        self.spots = []

        for row in range(num_rows):
            for spot1 in range(0, spots_per_row//4):
                size = VehicleSize.motorcycle
                self.spots.append(ParkingSpot(self, row, self.number_spots, size))
                self.number_spots += 1

            for spot2 in range(spots_per_row//4, spots_per_row//4 *3):
                size = VehicleSize.compact
                self.spots.append(ParkingSpot(self, row, self.number_spots, size))
                self.number_spots += 1

            for spot3 in range(spots_per_row//4 * 3, spots_per_row):
                size = VehicleSize.large
                self.spots.append(ParkingSpot(self, row, self.number_spots, size))
                self.number_spots += 1

        self.available_spots = self.number_spots

    def park_vehicle(self, vehicle):
        if self.get_available_spots() < vehicle.get_spots_needed():
            return False
        spot_num = self.find_available_spots(vehicle)

        if spot_num < 0:
            return False
        return self.park_starting_at_spot(vehicle)

    def get_available_spots(self):
        return self.available_spots

    def find_available_spots(self, vehicle):
        spots_needed = vehicle.get_spots_needed()
        last_row = -1
        spots_found = 0

        for i in range(len(self.spots)):
            spot = self.spots[i]
            if last_row != spot.get_row():
                spots_found = 0
                last_row = spot.get_row()
            if spot.can_fit_vehicle(vehicle):
                spots_found += 1

            else:
                spots_found = 0

            if spots_found == spots_needed:
                return i - (spots_needed -1)

        return -1

    def park_starting_at_spot(self,spot_num,vehicle):
        vehicle.clear_spots()
        success = True

        for i in range(spot_num, spot_num+vehicle.get_spots_needed()):
            success = success and self.spots[i].park(vehicle)
        return success

    def spot_freed(self):
        self.available_spots +=1

    def get_available_spot(self):
        return self.available_spots


class ParkingLot:
    def __init__(self, n, num_rows, spots_per_row):
        self.levels = []
        for i in range(n):
            self.levels.append(Level(i, num_rows, spots_per_row))

    def park_vehicle(self, vehicle):
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        return False

    def unpark_vehicle(self, vehicle):
        vehicle.clear_spots()

    def calculate_fee(self, vehicle):
        return


