

#내 풀이 오답

N,K=map(int,input().split())
list_use=list(input().split())
list_con=[]
# 처음에는 for문에 넣어서 하나씩 입력받은걸 리스트에 넣으려고 했음!

count=0

for x in list_use:
        if len(list_con)>=N:
            if x in list_con:
                continue

            else:
                list_con.pop()      # 이걸로 빼는 안되는 부분 예상 뒤에 다른 부분을 고려하는 포인트가 필요하다!
                list_con.append(x)
                count +=1
        else:
            if x in list_con:
                continue
            else:
                list_con.append(x)
print(count) 


import heapq

"""
정답 풀이 예시

import sys
input = sys.stdin.readline

N, K = map(int, input().split()) #N 멀티탭 개수, K 총 사용횟수 

multitap = list(map(int, input().split())) #멀티탭 입력 순서 기입

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
  
  multitap_idxs = [] # 다음 멀티탭의 값을 저장.
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
  del plugs[plug_out] # 플러그에서 제거
  plugs.append(multitap[i]) # 플러그에 멀티탭 값 삽입
  count += 1 # 뽑았으므로 1 증가

print(count)

"""










