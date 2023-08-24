# 내 풀이
discounts = [10, 20, 30, 40]
answer = [-1, -1]


def solution(users, emoticons):
    n, m = len(users), len(emoticons)
    discount_list = [0] * m

    def search(idx):
        global answer
        if idx == m:
            sale_num, cost_num = 0, 0
            for i in range(n):
                tmp = 0
                for j in range(m):
                    if users[i][0] <= discount_list[j]:
                        tmp += emoticons[j] * (100 - discount_list[j]) // 100
                if tmp >= users[i][1]:
                    sale_num += 1
                else:
                    cost_num += tmp
            if sale_num > answer[0] or sale_num == answer[0] and cost_num > answer[1]:
                answer = [sale_num, cost_num]
            return

        for i in range(4):
            discount_list[idx] = discounts[i]
            search(idx + 1)

    search(0)

    return answer

# 다른 사람 풀이

def solution(users, emoticons):
    answer = [0, 0]
    data = [10, 20, 30, 40]
    discount = []

    def dfs(tmp, d):  # 모든 경우의 할인율 조합을 구함
        if d == len(tmp):
            discount.append(tmp[:])
            return
        else:
            for i in data:
                tmp[d] += i
                dfs(tmp, d + 1)
                tmp[d] -= i

    dfs([0] * len(emoticons), 0)

    for disc in discount:  # 만들어진 모든 조합을 하나씩 살펴봄
        cnt = 0
        get = 0
        for i in users:
            pay = 0
            for j in range(len(disc)):
                if i[0] <= disc[j]:
                    pay += emoticons[j] * (100 - disc[j]) / 100
                if pay >= i[1]:
                    break
            if pay >= i[1]:  # 만약 유저의 제한금액 초과시 플러스 구매
                pay = 0
                cnt += 1
            get += pay
        if cnt >= answer[0]:  # 현재 최대값을 넘어가면 갱신
            if cnt == answer[0]:
                answer[1] = max(answer[1], get)
            else:
                answer[1] = get
            answer[0] = cnt

    return answer
