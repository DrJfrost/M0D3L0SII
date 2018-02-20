def rev(n):
    if (n>10):
        return n
    return 1+rev(n/10)

print(rev(int(input())))
