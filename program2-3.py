number = float(input("Enter the number = ")) 
rold = number
for i in range(100):
    rnew = (rold + number/rold)/2
    rold = rnew
print(f"The square root of {number} is {rold}.") 