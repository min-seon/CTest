import sys #재귀함수 이용하기

#최소 공배수
def lcm(a,b):
    return int((a*b)/gcd(a,b))

#최대 공약수
def gcd(a,b):
    if a == 0:
        return b
    else:
        return gcd(b%a,a)

#테스트 케이스 수
n=int(input())

#두 수 입력
for i in range(n):
    a,b=map(int, input().split())
    print(lcm(a,b), gcd(a,b))
