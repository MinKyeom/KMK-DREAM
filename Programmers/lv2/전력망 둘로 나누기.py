# 내 풀이 (개선 중)
# 네트워크 2개로 분활 (나누어진 송전탑 개수 거의 비슷하게!)
# 목표 나누어진 송전탑들의 차이를  return

def solution(n, wires):
    from collections import deque
    result = 100  # 송전탑의 최대갯수로 설정
    wires.sort()
    root_dic = {}
    all_node = []  # 전체 노드 확인

    for v, w in wires:
        if v not in root_dic:
            root_dic[v] = [w]
        else:
            root_dic[v] += [w]
        if w not in root_dic:
            root_dic[w] = [v]
        else:
            root_dic[w] += [v]

        if v not in all_node:
            all_node.append(v)
        elif w not in all_node:
            all_node.append(w)

    print(all_node)
    print(root_dic, "모집단")

    # 선 하나씩 제거 후 나누어진 여부 체크 후 송전탑 개수 체크
    for a in range(len(wires)):
        k = wires.copy()
        new_root = root_dic.copy()
        print(new_root)
        check_1 = k[a][0]
        check_2 = k[a][1]

        del k[a]
        """    
        for b,c in k: #지워야 할 루트 제거
            if c in new_root[b]:
                new_root[b].remove(c)
            if b in new_root[c]:
                new_root[c].remove(b)
        """
        new_root[check_1].remove(check_2)
        new_root[check_2].remove(check_1)

        print(new_root)
        # print(new_root[check_1],"확인")
        # print(new_root[check_2],"확인")

        root_1 = []

        for d in new_root[check_1]:
            root_1 += new_root[d]

        root_2 = []

        for e in new_root[check_2]:
            root_2 += new_root[e]

        print(root_1, "root_1")
        print(root_2, "root_2")

        if len(set(root_1) | set(root_2)) == len(set(all_node)) and len(set(root_1) & set(root_2)) == 0:
            num = abs(len(set(root_1)) - len(set(root_2)))
            if num <= result:
                result = num
                print(result)

    answer = -1
    return answer

# 다른 사람 풀이