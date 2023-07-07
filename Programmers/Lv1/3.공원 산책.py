# 내 풀이
def solution(park, routes):
    start = []
    stop = []
    count = 0
    for x in range(len(park)):  # 높이 선택
        for y in range(len(park[0])):  # 가로 선택
            if list(park[x])[y] == "S":
                start.append([x, y])
            elif list(park[x])[y] == "X":
                stop.append([x, y])

    for k in range(len(routes)):
        s = routes[k].split()

        if s[0] == "N":
            if start[0][0] - int(s[1]) < 0:
                continue
            r = [[start[0][0] - k, start[0][1]] for k in range(1, int(s[1]) + 1)]
            print("N")
            for c in r:
                if c in stop:
                    count = 1
                    break
            if count != 1:
                start[0][0] = start[0][0] - int(s[1])
            count = 0
            print("N", start)

        elif s[0] == "S":
            if start[0][0] + int(s[1]) >= len(park):
                continue
            r = [[start[0][0] + k, start[0][1]] for k in range(1, int(s[1]) + 1)]
            print(r)
            print(stop)
            print("S")
            for c in r:
                if c in stop:
                    count = 1
                    break
            if count != 1:
                start[0][0] = start[0][0] + int(s[1])
            count = 0
            print("S", start)

        elif s[0] == "W":
            if start[0][1] - int(s[1]) < 0:
                continue
            r = [[start[0][0], start[0][1] - k] for k in range(1, int(s[1]) + 1)]
            print("W")
            for c in r:
                if c in stop:
                    count = 1
                    break
            if count != 1:
                start[0][1] = start[0][1] - int(s[1])
            count = 0
            print("W", start)

        elif s[0] == "E":
            if start[0][1] + int(s[1]) >= len(park[0]):
                continue
            r = [[start[0][0], start[0][1] + k] for k in range(1, int(s[1]) + 1)]
            print("E")
            for c in r:
                if c in stop:
                    count = 1
                    break
            if count != 1:
                start[0][1] = start[0][1] + int(s[1])
            count = 0
            print("E", start)

    return start[0]

# 다른 사람 풀이
class Dog:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = {"N": (-1, 0), "W": (0, -1), "E": (0, 1), "S": (1, 0)}

    def move(self, park, direction, distance):
        i, j = self.g[direction]
        x, y = self.x + (i * distance), self.y + (j * distance)
        if x < 0 or y < 0 or x >= len(park) or y >= len(park[0]):
            return park
        elif "X" in park[x][min(self.y, y) : max(self.y, y) + 1] or "X" in [
            row[y] for row in park[min(self.x, x) : max(self.x, x)]
        ]:
            return park
        park[self.x][self.y] = "O"
        park[x][y] = "S"
        self.x = x
        self.y = y
        return park

    @classmethod
    def detect_start_dogs_location(self, park):
        for i, row in enumerate(park):
            for j, item in enumerate(row):
                if item == "S":
                    return i, j


def solution(park, routes):
    park = [list(row) for row in park]
    x, y = Dog.detect_start_dogs_location(park)

    dog = Dog(x, y)

    for route in routes:
        direction, distance = route.split()
        park = dog.move(park, direction, int(distance))

    return [dog.x, dog.y]
