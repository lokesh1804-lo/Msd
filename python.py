"""
Hangman Game
------------
A simple text-based Hangman game.

Key concepts used: random, while loop, if-else, strings, lists.
"""

import random

WORDS = ["python", "hangman", "computer", "developer", "keyboard"]

MAX_INCORRECT_GUESSES = 6

HANGMAN_STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ---------
    """,
]


def choose_word(word_list):
    return random.choice(word_list)


def display_progress(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    word = choose_word(WORDS)
    guessed_letters = []
    incorrect_guesses = 0

    print("Welcome to Hangman!")
    print("Try to guess the word one letter at a time.\n")

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        print(HANGMAN_STAGES[incorrect_guesses])
        print("Word: " + display_progress(word, guessed_letters))
        print("Guessed letters: " + ", ".join(guessed_letters) if guessed_letters else "Guessed letters: none")
        print(f"Incorrect guesses remaining: {MAX_INCORRECT_GUESSES - incorrect_guesses}\n")

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.\n")
            if all(letter in guessed_letters for letter in word):
                print(HANGMAN_STAGES[incorrect_guesses])
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.\n")

            if incorrect_guesses == MAX_INCORRECT_GUESSES:
                print(HANGMAN_STAGES[incorrect_guesses])
                print(f"Game over! You've been hanged. The word was: {word}")
                break


if __name__ == "__main__":
    play_again = "y"
    while play_again == "y":
        play_hangman()
        play_again = input("\nPlay again? (y/n): ").lower().strip()

    print("Thanks for playing Hangman!")
