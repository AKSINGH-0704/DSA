class Solution:
    def countCoveredBuildings(self, n, buildings):
        min_y = {}
        max_y = {}
        min_x = {}
        max_x = {}

        for x, y in buildings:
            if x not in min_y:
                min_y[x] = y
                max_y[x] = y
            else:
                if y < min_y[x]:
                    min_y[x] = y
                if y > max_y[x]:
                    max_y[x] = y

            if y not in min_x:
                min_x[y] = x
                max_x[y] = x
            else:
                if x < min_x[y]:
                    min_x[y] = x
                if x > max_x[y]:
                    max_x[y] = x

        covered = 0
        for x, y in buildings:
            if min_y[x] < y < max_y[x] and min_x[y] < x < max_x[y]:
                covered += 1

        return covered
