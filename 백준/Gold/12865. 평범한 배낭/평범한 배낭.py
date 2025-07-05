n,K=map(int,input().split())  # Number of items
s=[]
p=[]

for i in range(n):
    s1,p1=map(int,input().split())
    s+=[s1]
    p+=[p1]

def knapsack(s, p, K):
	n = len(s)
	dp = [[0] * (K + 1) for _ in range(n + 1)]

	for i in range(1, n + 1):
		for j in range(K + 1):
			if s[i - 1] <= j:
				dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - s[i - 1]] + p[i - 1])
			else:
				dp[i][j] = dp[i - 1][j]

	return dp[n][K]
print(knapsack(s, p, K))
