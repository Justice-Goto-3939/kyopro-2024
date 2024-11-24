def bainary_search(ok, ng, isok):
	while abs(ok - ng) > 1:
		mid = (ok + ng) // 2
		if isok(mid):
			ok = mid
		else:
			ng = mid
	return ok


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

counter = 0
a.sort()
b.sort()

ans=0

for B in b:
	indexA=bainary_search(-1,n,lambda i:a[i]<B)
	indexC=bainary_search(n,-1,lambda i:B<c[i])
	ans+=(indexA+1)*(n-indexC)

print(ans)