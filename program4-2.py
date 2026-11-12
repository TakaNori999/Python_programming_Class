import random
number = random.randint(1, 100)

while True:
    guess = int(input("Please enter a integer = "))
    if guess > number:
        print("The value you entered is large.")
    elif guess < number:
        print("The value you entered is small.")
    else:
        print("Correct answer!!")
        break