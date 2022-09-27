name = input("Enter your name: ")
count = int(input("Enter number of tests: "))

tests = []

for i in range(count):
    score = int(input(f"Enter test score {i + 1}: "))
    tests.append(score)

sorted_tests = sorted(tests, reverse=True)
print()

print(f"Student Name: {name}")
print(f"Average Score: {sum(tests) / len(tests)}")
print()

if len(tests) > 3:
    print(f"""Top 3 Scores:
    1. {sorted_tests[0]}
    2. {sorted_tests[1]}
    3. {sorted_tests[2]}""")
    print(f"""Bottom 3 Scores:
    {len(sorted_tests) - 2}. {sorted_tests[len(sorted_tests) - 3]}
    {len(sorted_tests) - 1}. {sorted_tests[len(sorted_tests) - 2]}
    {len(sorted_tests)}. {sorted_tests[len(sorted_tests) - 1]}""")