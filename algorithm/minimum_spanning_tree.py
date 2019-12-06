"""
Description
中文
English
Given a list of Connections, which is the Connection class
(the city name at both ends of the edge and a cost between them),
find edges that can connect all the cities and spend the least amount.
Return the connects if can connect all the cities, otherwise return empty list.

Return the connections sorted by the cost, or sorted city1 name if their cost is same,
or sorted city2 if their city1 name is also same.

Example
Example 1:

Input:
["Acity","Bcity",1]
["Acity","Ccity",2]
["Bcity","Ccity",3]
Output:
["Acity","Bcity",1]
["Acity","Ccity",2]
Example 2:

Input:
["Acity","Bcity",2]
["Bcity","Dcity",5]
["Acity","Dcity",4]
["Ccity","Ecity",1]
Output:
[]

Explanation:
No way

"""
import functools


class Connection:
    def __init__(self,city1, city2, cost):
        self.city1 = city1
        self.city2 = city2
        self.cost = cost


def comp(a, b):
    if a.cost != b.cost:
        return a.cost - b.cost

    if a.city1 != b.city1:
        if a.city1 < b.city1:
            return -1
        else:
            return 1

    if a.city2 == b.city2:
        return 0
    elif a.city2 < b.city2:
        return -1
    else:
        return 1


class Solution:
    # @param {Connection[]} connections given a list of connections include t
    # wo cities and cost
    # @return {Connection[]} a list of connections from results
    def lowestCost(self, connections):
        # Write your code here
        connections.sort(Key=functools.cmp_to_key(comp))
        hash = {}
        n = 0
        for connection in connections:
            if connection.city1 not in hash:
                n += 1
                hash[connection.city1] = n

            if connection.city2 not in hash:
                n += 1
                hash[connection.city2] = n

        father = [0 for _ in range(n + 1)]

        results = []
        for connection in connections:
            num1 = hash[connection.city1]
            num2 = hash[connection.city2]

            root1 = self.find(num1, father)
            root2 = self.find(num2, father)
            if root1 != root2:
                father[root1] = root2
                results.append(connection)

        if len(results) != n - 1:
            return []
        return results

    def find(self, num, father):
        if father[num] == 0:
            return num
        father[num] = self.find(father[num], father)
        return father[num]
