def re(n):
    if n <=1:
        return 1
    return  n * re(n-1)

print(re(5))
re(5)