# 내 풀이
def solution(keyinput, board):
    direction = ["up", "down", "left", "right"]
    x = int(board[0] / 2)
    y = int(board[1] / 2)
    result = [0, 0]
    new_key = []
    for a in keyinput:
        if a == "up":
            result[0] = result[0]
            result[1] = result[1] + 1
            if result[1] > y:
                result[1] = y
            elif result[1] < -y:
                result[1] = -y

        elif a == "down":
            result[0] = result[0]
            result[1] = result[1] - 1
            if result[1] > y:
                result[1] = y
            elif result[1] < -y:
                result[1] = -y

        elif a == "left":
            result[0] = result[0] - 1
            result[1] = result[1]
            if result[0] > x:
                result[0] = x
            elif result[0] < -x:
                result[0] = -x

        elif a == "right":
            result[0] = result[0] + 1
            result[1] = result[1]
            if result[0] > x:
                result[0] = x
            elif result[0] < -x:
                result[0] = -x

    return result

# 다른 사람 풀이

def solution(keyinput, board):
    x_lim,y_lim = board[0]//2,board[1]//2
    move = {'left':(-1,0),'right':(1,0),'up':(0,1),'down':(0,-1)}
    x,y = 0,0
    for k in keyinput:
        dx,dy = move[k]
        if abs(x+dx)>x_lim or abs(y+dy)>y_lim:
            continue
        else:
            x,y = x+dx,y+dy

    return [x,y]