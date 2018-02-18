from math import log10


def rev(n):
    def rec(n, diez):
        if n < 10:
            return n
        else:
            return n % 10 * diez + rec(n // 10, diez // 10)  # double slash means integer division :'v
    if rec(n, 10 ** int(log10(n))) == n:
        return True
    else:
        return False


print(rev(int(input())))