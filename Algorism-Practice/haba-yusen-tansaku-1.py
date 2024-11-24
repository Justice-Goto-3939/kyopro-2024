from collections import deque
import pprint

h, w = map(int, input().split())

sx,sy=1,1


board=[]
board.append(["#"]*(w+2))

for a in range(h):
	board.append(list(map(str, "#"+input()+"#")))

board.append(["#"]*(w+2))

board[sy][sx]=0
que=deque()
pprint.pprint(board)

que = deque([()])
