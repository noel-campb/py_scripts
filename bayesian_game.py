import random

name = input("Enter player name:")
print(f"Your chosen name is: {name}")
rename = input("Is that correct? (y/n):")
if rename == "y":
    pass
else:
    name = input("Enter player name:")

print("#"*30,"\n",f"Hi {name}! Welcome to the bayesian game\n", "#"*30,"\n")
print("""
There are 3 doors in front of you, labelled A, B and C.
Behind one of these doors is a prize of $10000.
However, behind each of the remaining doors is a stinking pile of dung.
You must guess which door contains the prize.
""")

first_choice = input("Choose your door (A/B/C):")

keys = ["A", "B", "C"]
values = ["$10000", "dung", "dung"]
random.shuffle(values)
random_dict = dict(zip(keys, values))

prize_door = [key for key, value in random_dict.items() if value == "$10000"][0]

if first_choice == prize_door:
    first_revelation = random.choice([i for i in keys if i != prize_door])
    print(f"\nYou have selected door {first_choice}")
    print(f"The game host opens door {first_revelation} to reveal dung")
    print("Would you like to stick to your original choice or select a new door?")
    new_choice = input("Choose a different door? (y/n):")
    if new_choice == "n":
        print(f"The host opens up door {first_choice} to reveal $10000. Congratulations!")
    else:
        print(f"The host opens up door {[i for i in keys if i not in [first_choice, first_revelation]][0]} to reveal dung. Better luck next time.")
else:
    first_revelation = [i for i in keys if i not in [first_choice, prize_door]][0]
    print(f"\nYou have selected door {first_choice}")
    print(f"The game host opens door {first_revelation} to reveal dung")
    print("Would you like to stick to your original choice or select a new door?")
    new_choice = input("Choose a different door? (y/n):")
    if new_choice == "n":
        print(f"The host opens up door {first_choice} to reveal dung. Better luck next time.")
    else:
        print(f"The host opens up door {prize_door} to reveal $10000. Congratulations!")
