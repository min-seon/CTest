
n, m = map(int, input().split(' '))

nmap = [[]]
numbers = []
for i in range(n):
    nmap = list(map(int, input().split(' ')))
    numbers.append(min(nmap))


print(max(numbers))
