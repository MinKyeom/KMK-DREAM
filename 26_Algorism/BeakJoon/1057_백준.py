"""
출처: 

아이디어: 매 라운드마다 새롭게 갱신되지만 사실상 첫번째 부여된 번호를 기준으로 그대로 사용해도 문제 없음
지민과 한수가 없는 대결에서는 항상 빠른 번호가 이긴다는 가정을 통해서
매 라운드의 pop,left를 끊임없이 실행 후 대결하는 순간의 라운드 번호를 기록
만약 그럼에도 한 명만 남게되었다면 못만난다는 전제 및 우승자가 나온 순간이므로 -1 출력

"""

from collections import defaultdict,deque
import copy

n,jimin,hansu = list(map(int,input().split(" ")))

jimin = str(jimin)
hansu = str(hansu)

person = defaultdict(int)

# if n%2 ==0:
#   new = n
#   pass
# else:
#   new = n-1

# 번호를 기록 안해도 어짜피 왼쪽이 무조건 이긴다는 가정과 지민과 한수는 항상 이긴다는 가정
# for i in range(1,n+1,2):
#   tone.append([i,i+1])

person = deque([ str(i+1) for i in range(n) ])

new = deque([])

round = 1

while True:
  
  if len(person) >=2:
    first = person.popleft()
    second =person.popleft()

    if first == jimin and second ==  hansu:
      print(round)
      break
    elif first == hansu and second ==  jimin:
      print(round)
      break
    
    elif second == jimin or second == hansu:
      new.append(second)
      continue
    
    else:
      new.append(first)
      
  elif len(person) ==1:
    ext = person.popleft()
    new.append(ext)
    
  else:
    if new == 1:
      print(-1)
      break
    
    else:
      person = copy.deepcopy(new)
      new =deque([])
      round+=1