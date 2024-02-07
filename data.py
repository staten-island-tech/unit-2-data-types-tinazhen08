""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """
""" 
my_favorite_color = input("what colors are in the rainbow?")
if my_favorite_color  == "Blue":
    print("correct")
else:
    print("incorrect") """
10
""" x = "friend"
print(f"hello {x}") """

""" temp = 68
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

""" #even or odd
even_or_odd = int (input ("Even or Odd"))
if ((even_or_odd) % 2) == 0:
    print("even")
else:
    print("odd")
 """

print("what is your subtotal?")

def subtotal():
    global subtotal
    subtotal = float(input("> $"))

def tip():
    print("how was the service?")

    service = input(">")
    if ((service) == "bad"):
        print(f"do not tip")
    elif((service) == "okay"):
        print(f"tip them ${subtotal * float(0.15)}")
    elif((service) == "good"):
        print(f"tip them ${subtotal * float(0.20)}")
    elif((service) == "great"):
        print(f"tip them ${subtotal * float(0.25)}")

subtotal()
tip()
    