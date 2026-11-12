scr = []
Pass = []
num = int(input("Enter the number of score = "))

for i in range(num):
    temp = int(input(f"Enter the score{i+1} = "))
    scr.append(temp)
    if scr[i] >= 80:
        Pass.append(scr[i])
print(scr)
print(len(Pass))
