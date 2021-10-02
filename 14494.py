import sys
sys.setrecursionlimit(10**6)


n,m = map(int, input().split())
c=[[0]*(m+1) for _ in range(n+1)]


def dp(n,m):
    if n==0 or m ==0:
        return 0
    if n==1 and m==1:
        return 1
    if c[n][m] !=0:
        return c[n][m]

    result = (dp(n,m-1) + dp(n-1,m) + dp(n-1,m-1)) % 1000000007
    c[n][m] = result
    return result

print(dp(n,m)%1000000007)