n, k = map(int, input().split())
arra = list(map(int, input().split()))
arrb = list(map(int, input().split()))

arra=sorted(arra)
arrb=sorted(arrb)
temp=0
for i in range(k):
    temp = arra[i]
    arra[i] = arrb[n-1-i]
    arrb[n-1-i] = temp

print(sum(arra))


