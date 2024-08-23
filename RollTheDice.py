import random

def rolldice(min,max):
    while True:
        print("ROlling the dice....")
        print(f"Your number : {random.randint(min,max)}")
        choice = input("Roll again? y/n ")
        if choice.lower() == 'n':
            break

rolldice(1,6)