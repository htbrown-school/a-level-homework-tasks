print("CLASS HELPER")
print("============")
print()

scores = []

name = input("Enter student name (-1 to finish): ")
score = int(input("Enter student score: "))
while name != "-1":
    scores.append([name, score])
    name = input("Enter student name: ")
    if name == "-1":
        break
    else:
        score = int(input("Enter student score: "))

sorted_scores = sorted(scores, key=lambda score: score[1], reverse=True)

print()
print("Statistics:")
print(f" Minimum: {sorted_scores[len(sorted_scores) - 1][0]} ({sorted_scores[len(sorted_scores) - 1][1]})")
print(f" Maximum: {sorted_scores[0][0]} ({sorted_scores[0][1]})")
print(f" Average: {sum([scores[i][1] for i in range(len(scores))]) / len(scores)}")
print()

input("Press enter to view table and exit...")
print()

format_name = "{:<30}"
format_score = "{:<30}"

print(format_name.format("Student"), format_score.format("Score"))
print("=" * 60)

for i in sorted_scores:
    print(format_name.format(i[0]), format_score.format(i[1]))

