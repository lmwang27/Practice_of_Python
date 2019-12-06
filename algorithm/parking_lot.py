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

# enum type for Vehicle
class VehicleSize:
    motorcycle =1
    compact = 2
    large = 3
    other = 99


class Vehicle:
    def __init__(self):
        self.parking_spots = []
        self.spot_needed = 0
        self.size = None
        self.license_plate = None

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
        self.spot_needed =1
        self.size = VehicleSize.Motorcycle

    def can_fit_in_spot(self,spot):
        return True
