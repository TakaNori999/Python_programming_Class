def leap(x):
    if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
        print(f"The year {x} is a leap year.")
    else:
        print(f"The year {x} is not a leap year.")

year = int(input("Enter the year = "))
leap(year)