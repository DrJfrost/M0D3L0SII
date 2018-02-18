def sum(n):
    return ((float(n/10)-int(n/10))*10)+((float(n/100)-int(n/100))*10)


print(int(sum(int(input()))))