#shopping cart program
foods=[]
prices=[]
total=0
while True:
    food=input("enter item name (q to quit) ")
    if food.lower()=="q":
        break
    else:
        price=float(input(f"enter the price of {food} "))
        foods.append(food)
        prices.append(price)

print("Your shopping cart items are: ")
for x in foods:
    print(x, end=" ")
print()
for y in prices:
    total+=y
print("Total price is ",total)

# 2d keypad
num_pad=((1,2,3),
         (4,5,6),
         (7,8,9),
         ("*",0,"#"))
for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

# python quiz game
questions=("Which keyword is used to define a function in Python?",
           "What is the output of len('Python')?",
           "Which data type is immutable in Python?",
           "Which operator is used for exponentiation in Python?",
           "Which function is used to take input from the user?")

options=(("A. func", "B. define", "C. def", "D. function"),
         ("A. 5", "B. 6", "C. 7", "D. Error"),
         ("A. List", "B. Dictionary", "C. Set", "D. Tuple"),
         ("A. ^", "B. **", "C. //", "D. %"),
         ("A. scanf()", "B. cin", "C. input()", "D. gets()"))
answers=("C","B","D","B","C")
guesses=[]
score=0
question_num=0

for question in questions:
    print("----------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("enter your answer (A,B,C,D) ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+=1
        print("correct answer")
    else:
        print("wrong answer")
    question_num+=1

print("----------------------------------------")
print("Quiz Results:")
print("----------------------------------------")
for answer in answers:
    print(answer, end=" ")
print()
for guess in guesses:
    print(guess, end=" ")
print()
print(f"Your score is: {score}/{len(questions)}")

#concession stand program
menue={"burger":5.99,
       "fries":2.99,
       "soda":1.99,
       "hotdog":3.49,
       "nachos":4.49,
       "popcorn":3.99,
       "candy":1.49}
cart=[]
total=0
for key, value in menue.items():
    print(f"{key:10}: ${value: .2f}")
while True:
    item=input("enter item name (q to quit) ").lower()
    if item.lower()=="q":
        break
    elif menue.get(item) is not None:
        cart.append(item)
for food in cart:
    total+=menue[food]
print("Your order is: ")
for food in cart:
    print(food, end=" ")
print()
print(f"Total cost: ${total: .2f}")

#number guessing game
import random

number = random.randint(1, 20)
guesses = 0

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 20.")

while True:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)

        if guess < 1 or guess > 20:
            print("Out of range! Enter a number between 1 and 20.")
            continue

        guesses += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("🎉 Correct!")
            print(f"You guessed the number in {guesses} guesses.")
            break

    else:
        print("Invalid input! Please enter a number.")

#Rock Paper Scissor
options=["rock", "paper", "scissor"]

runn=True
while runn:
    Player=None
    comp=random.choice(options)
    while Player not in options:
        Player=input("enter your choice ")
    print(f"player choice {Player}")
    print(f"computer choice {comp}")

    if(Player==comp):
        print("its a tie")
    elif (Player=="rock" and comp=="paper"):
        print("computer wins You loose")
    elif (Player=="rock" and comp=="scissor"):
        print("Player wins")
    elif (Player== "paper" and comp=="rock"):
        print("Player wins")
    elif(Player=="paper" and comp=="scissor"):
        print("computer wins you loose")
    elif(Player=="scissor" and comp=="rock"):
        print("computer wins you loose")
    elif(Player=="scissor" and comp=="paper"):
        print("player wins")
    a=input("stop  playing (y/n) ").lower()
    if a=="y":
        runn=False
print("Thanks for playing")



