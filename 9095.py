#1,2,3 더하기
t=int(input())
arr=[int(input()) for _ in range(t)]
answer=0
def fro(n):
    if n == 1:
        answer=1
    elif n == 2:
        answer=2
    elif n == 3:
        answer =4
    else: answer= fro(n-1)+fro(n-2)+fro(n-3)
    return answer

for i in arr:
    print(fro(i))