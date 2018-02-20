def mult(x,y):
    if (y==0):
        return 0
    return x + mult(x,y-1)


def pot (x,y):
    if (y==0):
        return 1
    else:
        return x * pot(x,y-1)

def div(x,y):
    if (y>x):
        return 0
    elif(y<=x):
        return 1 + div(x-y,y)


def fib(n):
    if(n==0) or (n==1):
        return 1
    else:
        return fib(n-1) + fib(n-2)


def cont(n):
    if (n<10):
        return n
    return 1+cont(n/10)

def pali(n):
    def rec(n, diez):
        if n < 10:
            return n
        else:
            return n % 10 * diez + rec(n // 10, diez // 10)  # double slash means integer division :'v
    if rec(n, 10 ** (cont(n)-1)) == n:
        return True
    else:
        return False


def sum(n):
    def rec(n, diez):
        if n < 10:
            return n
        else:
            return n % 10 + rec(n // 10, diez // 10)
    return rec(n,  10 ** (cont(n)-1))

def rev(n):
    def rec(n, diez):
        if n < 10:
            return n
        else:
            return n % 10 * diez + rec(n // 10, diez // 10)  # double slash means integer division :'v
    return rec(n, 10 ** (cont(n)-1))

def big(n):
    def rec(n, diez):
        if n < 10:
            return n
        else:
            if (n % 10 >= rec(n // 10, diez // 10)):
                return n % 10
            elif(n % 10 <= rec(n // 10, diez // 10)):
                return rec(n // 10, diez // 10)
    return rec(n,  10 ** (cont(n)-1))


print(big(int(input())))