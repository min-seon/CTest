n=input().split('-')
list=[]

total=0
for i in n:
    sum = 0 #전역변수로 선언하지 않기.,.
    a=i.split('+')
    for j in a:
        sum += int(j)
    list.append(sum)

total=list[0]
for k in range(1,len(list)):
    total -= list[k]

print(total)



