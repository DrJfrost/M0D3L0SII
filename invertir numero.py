from math import log10
def rev(n):
    def rec(n, diez):
        if n < 10:
            return n
        else:
            return n % 10 * diez + rec(n // 10, diez // 10)  #double slash means integer division :'v
    return rec(n, 10 ** int(log10(n)))

print(rev(int(input())))