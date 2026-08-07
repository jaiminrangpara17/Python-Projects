import random

while True:
 choice = input("Roll the Dice? (y/n): ").lower()    

 if choice == "y":
    number = random.randint(1, 6)
    print("You rolled ", number)
 
 elif choice == "n":
    print("Thanks for playing!") 
    break

 else :
   print("Enter valid input")
