#선택정렬
array=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index=i
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            temp=array[j]
            array[j]=array[min_index]
            array[min_index]=temp

print(array)