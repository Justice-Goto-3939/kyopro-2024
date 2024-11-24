
n=int(input())
a=map(int,input().split())

minNum=0

for N in n:

	counter=0

	for i in range(len(a)-N):
		if a[i]=="W":
			counter += 1

	for i in range(N-1):
		if a[i]=="E":
			counter += 1

	if counter<minNum:
		minNum=counter

print(counter)