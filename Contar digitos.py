from math import log10
def rev(n):
    return int(log10(n))+1

print(rev(int(input())))