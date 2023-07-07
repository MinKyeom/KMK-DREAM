# 내 풀이
def solution(players, callings):
    dic_players = {}
    for a in range(len(players)):
        dic_players[players[a]] = a

    for b in callings:
        x = players[dic_players[b] - 1]  # 이전 등수
        y = players[dic_players[b]]  # 바뀔 사람
        dic_players[b] = dic_players[b] - 1  # 불린 사람 등수 -1
        dic_players[x] = dic_players[x] + 1  # 원래 사람 +1
        players[dic_players[b]] = y
        players[dic_players[b] + 1] = x

    z = sorted(dic_players.items(), key=lambda x: x[1])

    result = []

    for key in dict(z):
        result.append(key)

    return result

# 다른 사람 풀이
# def solution(players, callings):
#     for j in callings:
#         num = players.index(j)
#         players[num-1], players[num] = players[num], players[num-1]
#     return players
def solution(players, callings):
    player_indices = {player: index for index, player in enumerate(players)}

    for j in callings:
        current_index = player_indices[j]
        desired_index = current_index - 1
        if current_index > 0 and players[desired_index] != j:
            players[current_index], players[desired_index] = players[desired_index], players[current_index]
            player_indices[players[current_index]] = current_index
            player_indices[players[desired_index]] = desired_index

    return players