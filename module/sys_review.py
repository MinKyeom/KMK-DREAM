# # 한 개의 정수를 입력 받을 때
# import sys
# a= int(sys.stdin.readline())
#
# #정해진 개수의 정수를 한줄에 입력받을때
#
# import sys
#
# a,b,c=map(int,sys.stdin.readline().split())
#
# #임의의 개수의 정수를 한줄에 입력받아 리스트에 저장할 때
#
# import sys
# data =list(map(int,sys.stdin.readline().split()))
#
# #임의의 개수의 정수를 n줄 입력 받아 2차원 리스트에 저장할 때
#
# import sys
# data =[]
# n=int(sys.stdin.readline().split())
#
# for x in range(n):
#     data.append(list(map(int,sys.stdin.readline().split())))
#
# #문자열 n줄을 입력받아 리스트에 저장할 떄
# import sys
#
# n=int(sys.stdin.readline())
#
# data=[sys.stdin.readline().strip() for i in range(n)]
#
# #strip()은 문자열 맨 앞과 맨 띁의 공백문자를 제거합니다.