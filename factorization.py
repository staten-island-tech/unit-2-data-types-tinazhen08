number = int(input("give me a number"))

def factor():
    global factor 
    print(f"factors of {number}")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)

factor()