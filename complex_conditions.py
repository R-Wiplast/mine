A_grade = float(input("What's your average grade? "))
L_grade = float(input("What's your lowest grade? "))

if 90 > A_grade >= 80 and 80 > L_grade >= 75:
    Fine = True
else:
    Fine = False

if A_grade >= 90 and L_grade >= 80:
    Great = True
else:
    Great = False

if Fine: 
    print("You did fine.")
elif Great:
    print("You did great!")
else:
    print("I don't know what to say.")
