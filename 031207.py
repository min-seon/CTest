#럭키 스트레이트

n=input()
arr=list(map(int,n))
mid=len(arr)//2

le=0
ri=0

for i in range(mid):
    le += arr[i]
    ri += arr[mid+i]

if le == ri:
    print("LUCKY")
else: print("READY")