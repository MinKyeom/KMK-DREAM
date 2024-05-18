# 1차원 누적합
def prefix_sum(n):
    prefixSum = [0]*n # prefixSum을 담을 빈 배열 생성
    prefixSum[0] = arr[0] # 첫번째 값을 넣어줌
    for i in range(1,n): # 두번째 값부터 누적합을 저장
        prefixSum[i] = prefixSum[i-1] + arr[i]
    return prefixSum

n = int(input())
arr = list(map(int, input().split()))
prefixSum = prefix_sum(n)

# 1차원 부분합
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s = prefix_sum(n,m) # 누적합을 구함
i,j = map(int,input().split())

partSum = prefixSum[j] - prefixSum[i-1]
print(partSum)

# 2차원 누적합
def prefix_sum(n,m):
    prefixSum = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1] + arr[i-1][j-1]
    return prefixSum

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
prefixSum = prefix_sum(n,m)


# 2차원 부분합
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
prefixSum = prefix_sum(n,m)
i,j,x,y = map(int,input().split())

# (i,j)칸에서 (x,y)칸까지 포함한 부분합
partSum = prefixSum[x][y] - prefixSum[i-1][y] - prefixSum[x][j-1] + prefixSum[i-1][j-1]
print(partSum)


