from collections import Counter

a=map(int,input().split())
b=map(int,input().split())
c=map(int,input().split())
d=map(int,input().split())

count=0

sumAB=set()
counterAB=Counter()

for A in a:
	for B in b:
		sumAB.add(a+b)