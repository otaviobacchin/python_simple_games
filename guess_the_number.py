#Guess The Number

import random
import time

program = ""

while True:
    #start
    program = input("\n\nWelcome to the 'Guess the Number', let's start?\n\nPress ENTER to start or insert 'exit' to shut down the game.\n" )
    
    #shutdown the game
    if program == "exit":
        break
    
    #random number generator
    random_number = random.randint(0, 100)
    number_try = 1
    print("\nA random between 0 and 100 has been generated, guess what number is?")
    
    #game loop
    while True:
        
        try:
            
            #number input
            number = int(input(f'\n{number_try}° Guess: '))
            
            #if the value is higher message and check
            if number > random_number:
                print('The number you guessed is HIGHER than the correct number.')
                number_try = number_try + 1
                
            #if the value is lower message and check
            elif number < random_number:
                print('The number you guessed is LOWER than the correct number.')
                number_try = number_try + 1
            
            #if the value is correct message and check
            elif number == random_number:
                print(f'\nCongratulations, the correct number is: {random_number}\nYou guessed the correct number after {number_try} tries!')
                time.sleep(3)
                break
                         
        #avoiding possible value errors   
        except ValueError:
            print('\nPlease insert a valid number.')
            