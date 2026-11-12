subject = ["japenese", "math", "society", "science", "english"]
value = [0, 0, 0, 0, 0]
for i in range(5):
    value[i] = int(input(f"Enter the {subject[i]}'s value = "))
total = sum(value)
average = total/len(value)
print(f"Total = {total}")
print(f"Average = {average}")