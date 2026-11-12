def judge_exam(scr):
    passing_score = 250
    total = sum(scr)
    print(f"Total: {total}")
    if total >= passing_score:
        return "Pass"
    else:
        return "False"

scores = []
for i in range(5):
    val = int(input(f"Enter the {i+1}'s value = "))
    scores.append(val)

result = judge_exam(scores)
print(f"Recult = {result}")