"""
n,k=map(int,input().split())
electric=list(map(int,input().split()))
plug=[]
count=0
use=0
for a in electric:
    count +=1
    if len(plug)<3 and a not in plug:
        plug.append(a)
    if len(plug)==3 and a not in plug:
        for b in plug:
            if b not in electric[count:k]:
                plug.remove(b)
                use+=1
                plug.append(a)
            elif b in electric[count:k]:
                for c in electric[count:k]:



print(use)
"""

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

multitap = list(map(int, input().split()))

plugs = []
count = 0

for i in range(K):
    # 있으면 건너 뛴다.
    if multitap[i] in plugs:
        continue

    # 플러그가 1개라도 비어 있으면 집어넣는다.
    if len(plugs) < N:
        plugs.append(multitap[i])
        continue

    multitap_idxs = []  # 다음 멀티탭의 값을 저장.
    hasplug = True

    for j in range(N):
        # 멀티탭 안에 플러그 값이 있다면
        if plugs[j] in multitap[i:]:
            # 멀티탭 인덱스 위치 값 가져오기.
            multitap_idx = multitap[i:].index(plugs[j])
        else:
            multitap_idx = 101
            hasplug = False

        # 인덱스에 값을 넣어준다.
        multitap_idxs.append(multitap_idx)

        # 없다면 종료
        if not hasplug:
            break

    # 플러그를 뽑는다.
    plug_out = multitap_idxs.index(max(multitap_idxs))
    del plugs[plug_out]  # 플러그에서 제거
    plugs.append(multitap[i])  # 플러그에 멀티탭 값 삽입
    count += 1  # 뽑았으므로 1 증가

print(count)






