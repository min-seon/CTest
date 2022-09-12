n=int(input())
sum=0
coin=[500,100,50,10]
for i in coin:
    sum += int(n/i)
    n=n%i
print(sum)

