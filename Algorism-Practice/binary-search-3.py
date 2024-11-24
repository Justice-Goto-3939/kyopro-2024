def binary_search(ok,ng,isOK):
	while abs(ok-ng) > 1:
		mid=(ok+ng)//2
		if isOK(mid):
			ok=mid
		else:
			ng=mid
	return ok

n,m,k=map(int,input().split())
a=
b=map(int,input().split())

