ages = [28, 50, 8, 20, 78, 25, 22, 10, 27, 33]
num = 3
sample = []
for i in ages:
    if (20 <= i) and (i < 30): #連鎖比較 20<=i<30
        sample.append(i)
        if len(sample) == num:
            break
print(sample)