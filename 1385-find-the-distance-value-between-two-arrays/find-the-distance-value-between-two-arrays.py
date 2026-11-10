class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0

        for x in arr1:
            if all(abs(x - y) > d for y in arr2):
                count += 1

        return count