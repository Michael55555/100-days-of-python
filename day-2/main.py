def get_tip():
    tip = input("How much is the tip? (10 / 12 / 15) ")
    tip = int(tip)
    if tip == 10:
        return tip
    if tip == 12:
        return tip
    if tip == 15:
        return tip
    print("Sorry it seems like you provided a number apart from (10 / 12 / 15), which is not accepted.")
    get_tip()


print("Welcome to my bill splitter v1.0")
bill = input("How much is the bill? ")
tip = get_tip()
people = input("How many people are splitting the bill? ")

bill = float(bill)
tip = int(bill)
people = int(people)

total = bill + bill * (tip / 100)
total_per_capita = total / people

print(f"Everyone has to pay {total_per_capita}")
