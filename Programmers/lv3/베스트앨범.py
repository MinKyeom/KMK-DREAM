"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/42579
"""


# 내 풀이
from collections import defaultdict


def solution(genres, plays):
    g = defaultdict(int)
    g_num = defaultdict(list)

    for i in range(len(genres)):
        g[genres[i]] += plays[i]
        g_num[genres[i]].append((plays[i], i))

    check = []

    for k in g_num.keys():
        g_num[k].sort(key=lambda x: (-x[0], x[1]))
        check.append((g[k], k))

    check.sort(reverse=True)

    result = []

    for i, j in check:
        n = 0
        for count, num in g_num[j]:
            result.append(num)
            n += 1
            if n == 2:
                break

    return result

# 다른 사람 풀이
def solution(genres, plays):
    answer = []
    dic = {}
    album_list = []
    for i in range(len(genres)):
        dic[genres[i]] = dic.get(genres[i], 0) + plays[i]
        album_list.append(album(genres[i], plays[i], i))

    dic = sorted(dic.items(), key=lambda dic:dic[1], reverse=True)
    album_list = sorted(album_list, reverse=True)



    while len(dic) > 0:
        play_genre = dic.pop(0)
        print(play_genre)
        cnt = 0;
        for ab in album_list:
            if play_genre[0] == ab.genre:
                answer.append(ab.track)
                cnt += 1
            if cnt == 2:
                break

    return answer

class album:
    def __init__(self, genre, play, track):
        self.genre = genre
        self.play = play
        self.track = track

    def __lt__(self, other):
        return self.play < other.play
    def __le__(self, other):
        return self.play <= other.play
    def __gt__(self, other):
        return self.play > other.play
    def __ge__(self, other):
        return self.play >= other.play
    def __eq__(self, other):
        return self.play == other.play
    def __ne__(self, other):
        return self.play != other.play