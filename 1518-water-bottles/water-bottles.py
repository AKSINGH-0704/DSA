class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empty = numBottles

        while empty >= numExchange:
            exchanged = empty // numExchange
            rem = empty % numExchange
            
            total += exchanged
            empty = rem + exchanged
            
        return total