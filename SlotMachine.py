#python slot machine
import random
def spin_row():
    symbol=["🍉", "🍋", "🍒", "🔔", "⭐"]
    row=[random.choice(symbol) for _ in range(1,4)]
    return row

def print_row(row):
    print("--------------")
    print(" | ".join(row))
    print("--------------")

def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=="🍉":
            bet*=3
            return bet
        elif row[0]=="🍋":
            bet*=5
            return bet
        elif row[0]=="🍒":
            bet*=9
            return bet
        elif row[0]=="🔔":
            bet*=15
            return bet
        elif row[0]=="⭐":
            bet*=25
            return bet
    return 0

def main():
    balance=100
    print("===============================")
    print("= Welcome to Slot Macine Game =")
    print("= Symbols  🍉 🍋 🍒 🔔 ⭐     =")
    print("===============================")

    while balance>0:
        print(f"current available balance is ${balance} ")
        bet=input("enter your bet amount ")
        if not bet.isdigit():
            print("invalid please reenter")
            continue
        bet=int(bet)
        if bet>balance:
            print("Insufficient balance")
            continue
        if bet<=0:
            print("bet must be greater than 0")
            continue
        balance-=bet
        row=spin_row()
        print("Spining......")
        print_row(row)
        pay=get_payout(row,bet)
        if pay>0:
            print(f"You won total ${pay}")
        else:
            print("sorry you lost this round")
        balance+=pay
        play_again=input("do you want to play again (y for yes any key for no)").lower()
        if(play_again!="y"):
            break
    print("game over your final balance is",balance)



if __name__=='__main__':
    main()