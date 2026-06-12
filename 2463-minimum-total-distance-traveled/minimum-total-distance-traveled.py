class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        robot.sort()
        factory.sort()
        f = []
        for p, l in factory:
            f += [p] * l
            
        n = len(robot)
        d = [float('inf')] * n + [0]
        
        for c in f[::-1]:
            for i in range(n):
                d[i] = min(d[i], abs(robot[i] - c) + d[i+1])
                
        return d[0]