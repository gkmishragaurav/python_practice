# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station
# to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
# Given two integer arrays gas and cost, return the starting gas station's index if you can travel
# around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution,
# it is guaranteed to be unique
# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3
# https://leetcode.com/problems/gas-station/

def find_starting_points(gas, cost):
    ans = []
    i=0
    while i<len(gas):
        if cost[i] <= gas[i]:
            ans.append(i)
        i=i+1

    return ans

def complete_circle(gas, cost, start):
    curr=0
    i=start
    while 1:
        i=i%len(gas)
        curr = curr + gas[i] - cost[i]
        if curr<0:
            return -1
        i=i+1
        if i%len(gas) == start:
            return start

def gas_station(gas, cost):
    stations = find_starting_points(gas, cost)
    print(stations)
    for station in stations:
        if station == complete_circle(gas, cost, station):
            return station

    return -1

gas = [3]
cost = [3]
print(gas_station(gas, cost))
