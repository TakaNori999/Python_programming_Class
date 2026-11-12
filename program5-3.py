ages = [28, 50, "Secret", 20, 78, 25, 22, 10, "No answer", 33]
sample = []
for i in ages:
    if not isinstance(i, int):
        continue
    if 20 <= i < 30:
        sample.append(i)
print(sample)