x = int(input("give me a number"))
y = int(input("give me another number"))

def GCF(x,y):
    if x < y:
        smaller_number = x
    else:
        smaller_number = y
    for i in range(1,smaller_number + 1):
        if((x%i == 0) and (y%i == 0)):
            gcf = i
    return gcf

print("The GCF is:", GCF(x,y))