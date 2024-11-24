n = int(input())

happiness = [list(map(int, input().split())) for _ in range(n)]

dp = [-1] * n
dp[0]=max(happiness[0])
dp[1]=max
