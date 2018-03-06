def multiplicacion(x,y):
    if (y==0):
        return 0
    return x + multiplicacion(x,y-1)



def division(x,y):
    if (y>x):
        return 0
    elif(y==0):
        print("Ideterminado division por 0")
    elif(y<=x):
        return 1 + division(x-y,y)


def fib(n):
    if(n==0) or (n==1):
        return 1
    else:
        return fib(n-1) + fib(n-2)


def digitNumber(n):
    if (n<10):
        return n
    return 1+digitNumber(n/10)

def palindromo(n):
    def rec(n, diez):
        if n < 10:
            return n
        else:
            return n % 10 * diez + rec(n // 10, diez // 10)  # double slash means integer division :'v
    if rec(n, 10 ** (digitNumber(n)-1)) == n:
        print("Es palindromo")
    else:
        print("No es palindromo")


def sumaDigt(n):
    def rec(n, diez):
        if n < 10:
            return n
        else:
            return n % 10 + rec(n // 10, diez // 10)
    return rec(n,  10 ** (digitNumber(n)-1))

def reverse(n):
    def rec(n, diez):
        if n < 10:
            return n
        else:
            return n % 10 * diez + rec(n // 10, diez // 10)  # double slash means integer division :'v
    return rec(n, 10 ** (digitNumber(n)-1))

def bigggest(n):
    def rec(n, diez):
        if n < 10:
            return n
        else:
            if (n % 10 >= rec(n // 10, diez // 10)):
                return n % 10
            elif(n % 10 <= rec(n // 10, diez // 10)):
                return rec(n // 10, diez // 10)
    return rec(n,  10 ** (digitNumber(n)-1))


def potencia (x,y):
    if (y==0) and (x<>0):
        return 1
    elif(y==0) and (x==0):
        print("indeterminado 0 ^ 0")
    elif(x==0) and (y<>0):
        return 0
    elif(y<>0) and (x<>0):
        return x * potencia(x,y-1)
