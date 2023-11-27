# 내 풀이
def solution(dirs):
    result = 0

    before_x = 0
    before_y = 0

    after_x = 0
    after_y = 0

    visit = []

    for k in list(dirs):

        if k == "U":

            if before_y < 5:
                after_y += 1
            else:
                continue

            if not [[before_x, before_y], [after_x, after_y]] in visit or not [[after_x, after_y],
                                                                               [before_x, before_y]] in visit:
                result += 1
                visit.append([[before_x, before_y], [after_x, after_y]])
                visit.append([[after_x, after_y], [before_x, before_y]])
                before_y = after_y
            else:
                before_y = after_y
                continue

        elif k == "D":

            if before_y > -5:
                after_y -= 1
            else:
                continue

            if not [[before_x, before_y], [after_x, after_y]] in visit or not [[after_x, after_y],
                                                                               [before_x, before_y]] in visit:
                result += 1
                visit.append([[before_x, before_y], [after_x, after_y]])
                visit.append([[after_x, after_y], [before_x, before_y]])
                before_y = after_y
            else:
                before_y = after_y
                continue

        elif k == "R":

            if before_x < 5:
                after_x += 1
            else:
                continue

            if not [[before_x, before_y], [after_x, after_y]] in visit or not [[after_x, after_y],
                                                                               [before_x, before_y]] in visit:
                result += 1
                visit.append([[before_x, before_y], [after_x, after_y]])
                visit.append([[after_x, after_y], [before_x, before_y]])
                before_x = after_x
            else:
                before_x = after_x
                continue

        elif k == "L":

            if before_x > -5:
                after_x -= 1
            else:
                continue

            if not [[before_x, before_y], [after_x, after_y]] in visit or not [[after_x, after_y],
                                                                               [before_x, before_y]] in visit:
                result += 1
                visit.append([[before_x, before_y], [after_x, after_y]])
                visit.append([[after_x, after_y], [before_x, before_y]])
                before_x = after_x
            else:
                before_x = after_x
                continue

    return result


# 다른 사람 풀이
def solution(dirs):
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2