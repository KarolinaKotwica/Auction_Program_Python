import os

clear = lambda: os.system('cls')
people = {}

def takeInfoFromUser(name, amount):
    people[name] = amount

def find_higher_biddest(bidding_record):
    highest = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest:
            highest = bid_amount
            winner = bidder
    print(f"\nThe winner is {winner} and highest bid is {highest}\n")    

def start():
    
    user = input("What is your name? ")
    money = int(input("What's your bid? $"))

    takeInfoFromUser(user, money)

    answer = input("Is there any other user? [Y/N]")
    if answer == "Y" or answer == "y":
        clear()
        start()
    elif answer == "N" or answer == "n":
        find_higher_biddest(people)
    else:
        print("You should write Y - yes or N - no.")
        start()


print("\nWelcome in auction program in Python!")
print("Just write your name and your amount of bid and then, next person the same steps. At the end we will show you which bid was the highest!")
print("Have fun!\n") 

start()    