def div(x,y):
    if (y>x):
        return 0
    elif(y<=x):
        return 1 + div(x-y,y)


print(div(float(input()),float(input())))