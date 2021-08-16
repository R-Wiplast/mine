# See what the tax rate is
planet = input("What planet are you on?").lower()
tax = 0

if planet == "earth":
    city =  input("What city do you live in?").lower()
    if city in("taipei","tokyo"):
        tax = 0.8
    elif city == "sydney":
        tax = 0.15
    else:
        tax = 0.3
else:
    tax = 0.0
print("Your tax rate is " + str(tax))
