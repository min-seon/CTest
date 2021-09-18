from itertools import permutations
n=int(input())
# 파이썬에서 순열은 permutations를 이용한다.

#임이의 배열에 n까지 숫자 넣기.
arr=[]
for i in range(1,n+1):
    arr.append(i)

result=list(permutations(arr,n))

for i in result:
    for j in i:
        print(j, end=' ')
    print()

