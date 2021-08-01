import sys
n=int(sys.stdin.readline())
stack=[]

for i in range(n):
    k=sys.stdin.readline().split()

    if k[0]=='push':
        stack.append(k[1])
    if k[0]=='top':
        if len(stack)>0:
            print(stack[-1])
        else:
            print(-1)
    if k[0]=='size':
        print(len(stack))
    if k[0]=='empty':
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    if k[0]=='pop':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)