number1 = float(input("Enter the number1 = "))
number2 = float(input("Enter the number2 = "))
number3 = float(input("Enter the number3 = "))

if (number1 >= number2) and (number1 >= number3):
    print(f"The largest value is {number1}.")
elif(number2 >= number1) and (number2 >= number3):
    print(f"The largest value is {number2}.")
else:
    print(f"The largest value is {number3}.")