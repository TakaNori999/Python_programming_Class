def gcd(n, m):
    while m != 0:
        n,m = m,n%m
    return n

number1 = int(input("Enter the integer1 = "))
number2 = int(input("Enter the integer2 = "))
result = gcd(number1, number2)
print(f"The greatest common divisor of {number1} and {number2} is {result}.")