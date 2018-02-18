def pot (x,y):
    if (y==0):
        return 1
    else:
        return x * pot(x,y-1)


print(pot(int(input()), int(input())))