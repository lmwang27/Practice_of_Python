"""
Description

There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs,
return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them.
If it is impossible to finish all courses, return an empty array.

Example
Example 1:

Input: n = 2, prerequisites = [[1,0]]
Output: [0,1]
Example 2:

Input: n = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]

"""

from queue import Queue


def find_order(num_courses, prerequisites):
    edges = {i: [] for i in range(num_courses)}
    degrees = [0 for i in range(num_courses)]

    for i, j in prerequisites:
        edges[j].append(i)
        degrees[i] += 1

    que = Queue(maxsize=num_courses)

    for i in range(num_courses):
        if degrees[i] == 0:
            que.put(i)

    order = []

    while not que.empty():
        node = que.get()
        order.append(node)

        for x in edges[node]:
            degrees[x] -= 1
            if degrees[x] ==0:
                que.put(x)

    if len(order) == num_courses:
        return order

    return []


if __name__ == "__main__":
    n = 2
    prerequisites = [[1, 0]]
    print(find_order(n, prerequisites))
