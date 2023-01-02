# ● ┌ ─ ┐ │ └ ┘ 
import random

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}
while(1):
    dice = []
    total = 0
    num_of_dice = int(input("How many dice?: "))

    for die in range(num_of_dice):
        dice.append(random.randint(1, 6))

# PRINT VERTICALLY
# for die in range(num_of_dice):
#    for line in dice_art.get(dice[die]):
#        print(line)

# PRINT HORIZONTALLY
    for line in range(5):
        for die in dice:
            print(dice_art.get(die)[line], end="")
        print()

    for die in dice:
        total += die
    print(f"total: {total}")
    a="a"
    while(a.lower()!="y" and a.lower()!="n"):
        a=input("Do you want to roll again y/n :")
        if(a.lower()=="n"):
            break
        if(a.lower()!="y"):
            print("Enter available choices only")
    if(a.lower()=="n"):
        break

