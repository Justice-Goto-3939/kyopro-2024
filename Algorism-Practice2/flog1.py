n = int(input())

step = list(map(int, input().split()))

dp = [-1] * (n)
dp[0] = 0
dp[1] = abs(step[1] - step[0])

for i in range(2, n):
    dp[i] = min(
        dp[i - 1] + abs(step[i] - step[i - 1]), dp[i - 2] + abs(step[i] - step[i - 2])
    )

print(dp[n - 1])