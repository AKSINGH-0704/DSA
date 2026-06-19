class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle_minutes = minutes * 6
        
        angle_hour = (hour % 12 + minutes / 60) * 30

        diff = abs(angle_hour - angle_minutes)
        return min(diff, 360 - diff)