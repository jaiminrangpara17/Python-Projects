import random

words = ["apple", "banana", "mango", "orange", "grapes", "kiwi", "strawberry", "watermelon", "pineapple",]

word = random.choice(words)
guessed = []
wrong_guess = 0
max_guesses = 6

hangman = [
    """

     +----+
     |    |
          |
          |
          |
    ========
    """,
    """

     +----+
     |    |
     O    |
          | 
          |
    ========
    """,
    """

     +----+
     |    |
     O    |
     |    | 
          |
    ========
    """,
    """

     +----+
     |    |
     O    |
    /|    |
          |
    ========
    """,
    """

     +----+
     |    |
     O    |
    /|\\   |
          |
    ========
    """,
    """

     +----+
     |    |
     O    |
    /|\\   |
    /     | 
    ========
    """,
    """

     +----+
     |    |
     O    |
    /|\\   |
    / \\   |
    ========
    """,
]

print("Welcome to Hangman!")
print("Hint: The word is fruits")

while wrong_guess < max_guesses:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    print(hangman[wrong_guess])
    print(display)

    if "_" not in display:
        print("congratulations!, you won!")
        print("The word was:", word)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please  enter a single letter")
        continue

    if guess in guessed:
        print("You already guessed the letter")
        continue
    guessed.append(guess)

    if guess in word:
        print("correct guess!")
    else:
        wrong_guess += 1
        print("Wrong guess!")

else:
    print(hangman[wrong_guess])
    print("Game Over!")
    print("The fruit was:", word)