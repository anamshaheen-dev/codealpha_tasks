"""
CodeAlpha Python Internship - Task 1
Hangman Game

A simple text-based Hangman game where the player guesses a word
one letter at a time. The player has 6 incorrect guesses allowed.

Author: Anam Shaheen
"""

import random

# A small list of predefined words to choose from
WORD_LIST = ["python", "hangman", "computer", "internship", "developer"]

MAX_ATTEMPTS = 6


def choose_word():
    """Randomly select a word from the word list."""
    return random.choice(WORD_LIST)


def display_progress(word, guessed_letters):
    """Show the word with guessed letters revealed and others as underscores."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    word = choose_word()
    guessed_letters = []
    wrong_guesses = 0

    print("=" * 40)
    print("Welcome to Hangman!")
    print(f"You have {MAX_ATTEMPTS} incorrect guesses allowed.")
    print("=" * 40)

    while wrong_guesses < MAX_ATTEMPTS:
        print("\nWord: " + display_progress(word, guessed_letters))
        print(f"Wrong guesses left: {MAX_ATTEMPTS - wrong_guesses}")

        guess = input("Guess a letter: ").lower().strip()

        # Basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"Wrong! '{guess}' is not in the word.")

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print("\n" + "=" * 40)
            print(f"Congratulations! You guessed the word: {word}")
            print("=" * 40)
            return

    # If loop ends, player lost
    print("\n" + "=" * 40)
    print("Game Over! You ran out of attempts.")
    print(f"The word was: {word}")
    print("=" * 40)


if __name__ == "__main__":
    play_hangman()

    # Allow replay
    while True:
        again = input("\nDo you want to play again? (y/n): ").lower().strip()
        if again == "y":
            play_hangman()
        else:
            print("Thanks for playing! Goodbye.")
            break
