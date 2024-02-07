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