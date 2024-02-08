def GCF(x,y):
    global GCF
    if y == 0:
        return x
    else:
        return GCF(y,x % y)
x = int(input("give me a number"))
y = int(input("give me another number"))

print("The GCF is:", GCF(x,y))
