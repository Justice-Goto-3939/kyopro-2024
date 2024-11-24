n = int(input())

score = list(map(int, input().split()))

score.insert(0,0)

dp = [-1] * n
dp[0]=0
dp[1]=score[1]

for i in range(n):
	dp[i]=dp[0][0]+i

print(score)
print(dp)
