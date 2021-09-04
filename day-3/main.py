from treasure_island import treasure_island

module = input("Which module do you want to run? (odd / bmi) ")


def odd():
    number = int(input("Give me a number: "))

    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


def bmi():
    height = int(input("How tall are you in cm?"))
    weight = int(input("What's your weight in kg?"))
    bmi = weight / (height / 100) ** 2

    if bmi < 18.5:
        print(f"Your bmi is {bmi}, you are underweight")
    elif bmi < 25:
        print(f"Your bmi is {bmi}, you are normal weight")


def leap():
    year = int(input("What year can I use for my calculation? "))

    if year % 4 == 0:
        if year % 100 == 0:
            print("Not a leap year")
        else:
            if year % 400 == 0:
                print("Not a leap year")
            else:
                print("A leap year")
    else:
        print("Not a leap year")


def pizza():
    print("Welcome to Python Pizza Deliveries!")
    size = input("What size pizza do you want? S, M, L ")
    add_pepperoni = input("Do you want pepperoni? Y or N ")
    extra_cheese = input("Do you want extra cheese? Y or N ")
    cost = 0

    # add size cost
    if size == "S":
        cost += 15
    elif size == "M":
        cost += 20
    else:
        cost += 25

    # add pepperoni
    if add_pepperoni == "Y":
        if size == "S":
            cost += 2
        else:
            cost += 3

    if extra_cheese == "Y":
        cost += 1

    print("Your pizza costs $" + str(cost))


def love():
    name1 = input("What is your name?\n").lower()
    name2 = input("What is their name?\n").lower()
    names = name1 + name2
    score1 = 0
    score2 = 0

    for sub in "true":
        score1 += names.count(sub)

    for sub in "love":
        score2 += names.count(sub)

    score = int(str(score1) + str(score2))

    if score > 90 or score < 10:
        print(f"Your score is {score}, you go together like coke and mentos.")
    elif score < 40 or score < 50:
        print(f"Your score is {score}, you are alright together.")
    else:
        print(f"Your score is {score}")


if module == "bmi":
    bmi()
elif module == "odd":
    odd()
elif module == "leap":
    leap()
elif module == "pizza":
    pizza()
elif module == "love":
    love()
else:
    treasure_island()
