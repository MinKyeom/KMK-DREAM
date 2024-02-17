# 내 풀이(개선 중)
def solution(temperature, t1, t2, a, b, onboard):
    result = 0  # 전력소모량
    p = onboard  # 승객 탑승 여부
    t = temperature  # 현재온도 #temperature: 실외온도

    # want: 희망온도 off: 전원 temperature: 시간에 따른 온도
    check = [[temperature, temperature, "off"] for _ in range(len(p))]  # 시간에 따른 에어컨 전원 및 온도 변경여부 0,1,-1

    print(check, "before")

    #### 목표 ####
    # 승객이 탑승중일때 최적화된 실내 온도를 최소의 전력으로 맞추기
    # 승객이 탑승할때도 에어컨이 켜져있다면 외부 온도와 관계없이 에어컨의 조건에 따른다!
    # 사이인거 등호 포함!
    # 더 더울경우 t2 추울경우 t1
    # 탑승객이 없을경우 최적화를 맞출 필요가 없다 그래야 최소 전력 가능!
    #################################

    # 기준점 t: 현재 온도
    while True:

        for k in range(len(p)):
            if p[k] == 1:
                if not t1 <= check[k][0] <= t2:
                    before = check[k][0]

                    if check[k][0] > t2:
                        check[k][0] = t2

                        for i in range(k - 1, -1, -1):
                            check[i][0] = check[i + 1][0] + 1
                            check[i][1] = t2
                            check[i][2] = "on"
                            if check[i][0] == before:
                                break
                    else:
                        check[k][0] = t1
                        for i in range(k - 1, -1, -1):
                            check[i][0] = check[i + 1][0] - 1
                            check[i][1] = t1
                            check[i][2] = "on"
                            if check[i][0] == before:
                                break

                else:
                    pass

                print(check)

        # 시간 경과에 따른 통과 했을 경우
        else:
            break

    # result 최적화 후 나중에 한 번 더 계산! think

    return result 