class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        d1 = abs(x - z)
        d2 = abs(y - z)
        if d1 < d2:
            return 1
        elif d2 < d1:
            return 2
        else:
            return 0
