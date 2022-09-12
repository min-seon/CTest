#큰수의 법칙 : m번 더하여 (k번 초과 불가)
n,m,k =map(int, input().split(' '))
arr=list(map(int,input().split(' ')))

sum=0
arr.sort()
fnum=arr[n]
snum=arr[n-1]

count=int(m/k+1)*k
count += m%(k+1)

print(sum)