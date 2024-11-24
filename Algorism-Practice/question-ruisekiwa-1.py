
n=int(input())
a=map(int, input().split())

s=[0]

for A in a:
	s.append(s[-1]+a)

