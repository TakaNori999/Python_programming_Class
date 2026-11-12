gender = input("Is your gender male or female? ")
age = int(input("What's your age = "))
if "male" == gender:
    if age >= 20:
        print("You can drink alcohol.")
    else:
        print("You can't drink alcohol.")
else:
    if age >= 20:
        pregnant = input("Are you pregnant? yes or no ")
        if "yes" in pregnant:
            print("Sorry. You can't drink alcohol..")
        else:
            print("You can drink alcohol.")
    else:
        print("You can't drink alcohol.")