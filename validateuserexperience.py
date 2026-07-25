# Validate User Experience for Input



name = input("Please enter your name: ")

if len(name) > 12:
    print("Name is too long. Please enter a name with 12 characters or fewer.")

elif not name.find(" ") == -1:
    print("Name cannot have spaces. Please enter a valid name.")

elif not name.isalpha():
    print("Name must contain only letters. Please enter a valid name.")

else:
    print(f"Welcome, {name}!")
   