import random

def number_guess_game():
    print("Welcome to the Number Guess Game !")
    print("Guess the number between 1 to 100")
    
    #generate the Secret number
    secret_number = random.randint(1, 100)

    #Loop countinuously until the correct number is guessed
    while True: 

        #Ask the user to guess the number
        num = int(input("guess the number: "))

        #check if the number is correct
        if num > secret_number:
            print("The number is smaller than", num)
        elif num < secret_number:
            print("The number is greater than", num)
        elif num == secret_number:
            print("Congratulations! You guess the correct number")
            break

number_guess_game()