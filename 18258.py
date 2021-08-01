from collections import deque
import sys
n = int(sys.stdin.readline()) #시간제한이 있으므로 빠르게 받을때 사용함
queue = deque()

for i in range(n):
    k=sys.stdin.readline().split() #얘도 필수
    if k[0] == 'push':
        queue.append(k[1])
    if k[0] == 'pop':
        if len(queue)>0:
            print(queue[0])
            queue.popleft()
        else:
            print(-1)
    if k[0] == 'size':
        print(len(queue))
    if k[0] == 'empty':
        if len(queue) > 0:
            print(0)
        else:
            print(1)
    if k[0] == 'front':
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    if k[0] == 'back':
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)

