# 내 풀이
def solution(board, moves):
    check = []
    result = 0
    for k in moves:
        for x in range(len(board)):
            if board[x][k - 1] != 0:
                if check and check[-1] == board[x][k - 1]:
                    print("check2")
                    print(check[-1], board[x][k - 1])
                    check.pop()
                    board[x][k - 1] = 0
                    result += 2
                    break

                else:
                    check.append(board[x][k - 1])
                    board[x][k - 1] = 0
                    break

            else:
                continue
    return result

# 다른 사람 풀이
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                break

    return answer