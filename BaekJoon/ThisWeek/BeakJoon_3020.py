#sol1

# N,H=map(int,input().split())
#
# #int(input().split())와 위의 문장 차이점 확인!
#
# dongul=[]
# for a in range(N):
#     dongul.append(int(input()))
#
# count_obstacle=0
# count_obstacle_list=[]
# count_section=0
#
# for x in range(1,H+1):
#     count_obstacle=0
#     for y in range(N):
#         if y%2==0:
#             if x<=dongul[y]:
#                 count_obstacle+=1
#
#         elif y%2==1:
#             if x>H-dongul[y]:
#                 count_obstacle+=1
#     count_obstacle_list.append(count_obstacle)
#
# count_obstacle=0
#
# for a in range(1, H + 1):
#     count_obstacle = 0
#     for b in range(N):
#         if b % 2 == 1:
#             if a <= dongul[b]:
#                 count_obstacle += 1
#
#         elif b % 2 == 0:
#             if a > H - dongul[b]:
#                 count_obstacle += 1
#
#     if count_obstacle==min(count_obstacle_list):
#             count_section +=1
#
# print(min(count_obstacle_list)," ",count_section)


#sol2
#
N,H=map(int,input().split())

dongul=[]
for a in range(N):
    dongul.append(int(input()))

count_obstacle=0
count_obstacle_list=[]
count_section=0

for x in range(1,H+1):
    count_obstacle=0
    for y in range(N):
        if y%2==0:
            if x<=dongul[y]:
                count_obstacle+=1

        elif y%2==1:
            if x>H-dongul[y]:
                count_obstacle+=1

    count_obstacle_list.append(count_obstacle)

for z in range(len(count_obstacle_list)):
    if count_obstacle_list[z]==min(count_obstacle_list):
        count_section+=1

print(min(count_obstacle_list)," ",count_section)
