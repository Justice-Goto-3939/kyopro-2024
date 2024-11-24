
def binary_search(ok,ng,isOK):
	while abs(ok-ng) > 1:
		mid=(ok+ng)//2
		if isOK(mid):
			ok=mid
		else:
			ng=mid
	return ok

n,k=map(int,input().split)
a=list(map(int,input().split()))

for i in range(n):
	locals