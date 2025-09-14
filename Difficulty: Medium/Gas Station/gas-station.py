class Solution:
    def startStation(self, gas, cost):
        n = len(gas)
        total_gas, total_cost = sum(gas), sum(cost)

        # If total gas is less than total cost, not possible
        if total_gas < total_cost:
            return -1

        start = 0
        tank = 0

        for i in range(n):
            tank += gas[i] - cost[i]
            if tank < 0:
                # Can't start from any station up to i
                start = i + 1
                tank = 0

        return start
