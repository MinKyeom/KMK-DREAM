# 내 풀이
# 균형잡힌 괄호 문자열인지 체크하는 함수
def isbalanced(s):
	chk=0
	for c in s:
		if c=='(': chk+=1
		elif c==')': chk-=1

	if chk==0: return True
	else: return False

# 올바른 괄호 문자열인지 체크하는 함수
def iscorrect(s):
	stack=[]
	stack.append(s[0])
	for i in range(1,len(s)):
		if len(stack)==0 or stack[-1]==')' or (stack[-1]=='(' and s[i]=='('):
			stack.append(s[i])
		else:
			stack.pop()
	if len(stack)==0: return True
	else: return False


def solution(p):
	answer = ''
	u=""
	v=""
	#빈 문자열이나 올바른 괄호 문자열은 그대로 반환
	if len(p)==0 or iscorrect(p): return p

	#u가 균형잡힌 괄호 문자열이 될 때까지 2개씩 추가해서 u,v 나누기
	for i in range(2,len(p)+1,2):
		if isbalanced(p[0:i]):
			u=p[0:i]
			v=p[i:len(p)]
			break

	if iscorrect(u):
		#u가 올바른 괄호 문자열일 때
		answer+=u+solution(v)
	else:
		#u가 올바른 괄호 문자열이 아닐 때
		answer+='('+solution(v)+')'
		for c in u[1:-1]:
			if c=='(': answer+=')'
			else: answer+='('

	return answer

# 다른 사람 풀이
def solution(p):
    if p=='': return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': c-=1
        else: c+=1
        if c>0: r=False
        if c==0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))