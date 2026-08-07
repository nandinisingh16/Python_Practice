from Python.wordslist import words
import random

hangman_art = {
    0: (
        "  ",
        "  ",
        "  "
    ),

    1: (
        "  O",
        "   ",
        "   "
    ),

    2: (
        "  O",
        "  |",
        "   "
    ),

    3: (
        "  O",
        " /|",
        "   "
    ),

    4: (
        "  O",
        " /|\\",
        "   "
    ),

    5: (
        "  O",
        " /|\\",
        " / "
    ),

    6: (
        "  O",
        " /|\\",
        " / \\"
    )
}




def dispalyMan(wrong_guess):
     for line in hangman_art[wrong_guess]:
         print(line)

def displayHint(hint):
    print(" ".join(hint))

def displayAns(ans):
    print(" ".join(ans))
    
def main():
    print("="*30)
    print("      HANGMAN GAME")
    print("="*30)
    answer=random.choice(words)
    hint=["_"]*len(answer)
    wrong_guess=0
    guessed_letter=set()
    is_run=True

    while is_run:
        dispalyMan(wrong_guess)
        displayHint(hint)
        guess=input("Enter a letter: ").lower()
        
        if len(guess)!=1 or not guess.isalpha():
            print("Invalid Input")
            continue
        if guess in guessed_letter:
            print(f"{guess} already guessed")
            print("guessed letters "," ".join(sorted(guessed_letter)))
            continue
        guessed_letter.add(guess)
        if guess in answer:
            for i in range(len(answer)):
                if answer[i]==guess:
                    hint[i]=guess
                    print("correct guess")
        else:
            wrong_guess+=1
            print("wrong guess")

        if "_" not in hint:
            dispalyMan(wrong_guess)
            displayAns(answer)
            print("You win")
            is_run=False
        elif wrong_guess>=len(hangman_art)-1:
            dispalyMan(wrong_guess)
            displayAns(answer)
            print("You Loose")
            is_run=False
        print(f"Lives left: {len(hangman_art)-1-wrong_guess}")
        


if __name__=='__main__':
    main()

