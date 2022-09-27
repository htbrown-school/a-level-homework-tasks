import locale
locale.setlocale(locale.LC_ALL, '')

people = int(input("How many people are there: "))
tip = float(input("What percentage is the tip: ")) / 100
bill = float(input("How much is the bill: "))
taxi = float(input("How far is the taxi going: "))

total = bill * (tip + 1)
total_with_taxi = total + taxi

print(f"The total bill is {locale.currency(total, '£')}, which is {locale.currency(total / people, '£')} per person.")
print(f"With the taxi the total bill comes to {locale.currency(total_with_taxi, '£')}, which is {locale.currency(total_with_taxi / people, '£')} per person.")