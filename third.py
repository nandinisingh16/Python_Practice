import random
#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘
"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"
#rolling a dice game and give total
dice_art = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ),

    2: (
        "┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"
    ),

    3: (
        "┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"
    ),

    4: (
        "┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"
    ),

    5: (
        "┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"
    ),

    6: (
        "┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘"
    )
}
dice=[]
total=0
num_of_dice=int(input("how many dice ? "))
for die in range(num_of_dice):
    dice.append(random.randint(1,6))

for die in range(num_of_dice):
    for line in dice_art.get(dice[die]):
        print(line)
for die in dice:
    total+=die
print(f"total:{total}")

#arbitrary arguments
def add(*args):
    total=0
    for a in args:
        total+=a
    return total
print(add(1,2,3,4,5))

def printAdrr(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

printAdrr(street="123 lane", city="nyc", country="America")

#member ship overator
a=input("input your gmail id to check if it is valid")
if "@" in a and ".com" in a:
    print("Valid Email")
else:
    print("NO invallid")

#list comprehension
triples=[x*3 for x in range(1,11)]
print(triples)
fruits=["apple", "banana", "orange"]
fruit=[f.upper() for f in fruits]
print(fruit)
number=[1,-2,3,-4,5]
neg=[n for n in number if n<0]
print(neg)

#match case statement
def isItWeekend(day):
    match day:
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return "Its not the weekend"
        case "saturday" | "sunday":
            return "Its the weekend"
        case _:
            return "invalid input"
a=input("enter the day of the week").lower()
print(isItWeekend(a))
