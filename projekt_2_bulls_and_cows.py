"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Pavel Šmíd
email: 78.78@seznam.cz
discord: Pavel Šmíd#2969

"""

from random  import randrange
from timeit import default_timer as timer

start = timer()

def random_number():
    numbers = []
    while len(numbers) != 4:
        numbers.append(randrange(0, 10))
        if numbers[0] == 0 or len(set(numbers)) < 4 and len(numbers) == 4: 
            numbers.clear()
    return numbers

def rules_game():
    while True:
        numbers = input("enter a tip: ")
        if  not numbers.isnumeric():
            print("Enter a four-digit unique number that does not start with a zero")
        elif len(numbers) != 4:
            print("Enter a four-digit unique number that does not start with a zero")
        elif numbers[0] == "0":
            print("Enter a four-digit unique number that does not start with a zero")
        elif len(set(numbers)) < 4:
            print("Enter a four-digit unique number that does not start with a zero")
        else:
            return numbers

def game():
    try_game = 0
    print(f"\nHi there!\n{'-' * 47}\nI've generated a random 4 digit number for you.\n\
     Let's play a bulls and cows game.\n{'-' * 47}")
    numbers = 1,2,3,4#random_number()
    while True:
        bulls, cows = control(numbers, rules_game())
        try_game += 1
        if bulls == 4:
            break
        singular_plural(cows, bulls)
    end = timer()    
    print(f"guessed it! number of attempts: {try_game}, game time: {round(end - start, 1)} s" )
    print('=' * 47)


def singular_plural(cows, bulls):
    if cows == 1:
        cows_name = "cow"
    else:
        cows_name = "cows"
    if bulls == 1:
        bulls_name = "bull"
    else:
        bulls_name = "bulls"
    print(bulls, bulls_name, ",", cows, cows_name)
    print('-' * 47)
    
def control(numbers, tip):
    bulls, cows = 0, 0
    for i, numbers in enumerate(numbers):
        if numbers == int(tip[i]):
            bulls += 1
        if str(numbers) in tip:
            cows += 1
    cows -= bulls
    return bulls, cows

game()            
            
            
            
            
            
            
            
























