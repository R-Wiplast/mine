#this tool selects the first letter of your name
def get_first_letter(name):
    first_letter = name[0:1].upper()   
    return first_letter

first_name = input("enter your first name: ")
last_name = input("enter your last name: ")
print("your nickname is " + get_first_letter(first_name) + get_first_letter(last_name))
