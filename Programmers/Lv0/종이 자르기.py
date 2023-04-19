# # 풀이1
# def solution(M, N):
#     x=M-1
#     c=0
#     if x>0:
#         for a in range(M):
#             c+= N-1
#     elif x==0:
#         c=N-1
#     answer=x+c
#     return answer
#
# # 풀이2 (team sol)
# def solution(M, N):
#     return (M-1) + (M*(N-1))