import random

with open("words.txt", "r", encoding="utf-8") as file:
    words = [
        word.strip().lower()
        for word in file
        if word.strip().isalpha() and len(word.strip()) >= 4
    ]

if not words:
    raise ValueError("The word list is empty or contains no valid words.")

stages = [
    """
      -----
      |   |
          |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
      |   |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|   |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
     /    |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
     / \\  |
    =========
    """
]


def display_word(secret_word, guessed_letters):
    return " ".join(
        letter.upper() if letter in guessed_letters else "_"
        for letter in secret_word
    )


def play_hangman():
    secret_word = random.choice(words)
    guessed_letters = set()
    incorrect_guesses = 0
    max_attempts = 6

    print("\n================================")
    print("       HANGMAN WORD GAME")
    print("================================")
    print("Guess the hidden word one letter at a time!")
    print("You have 6 incorrect guesses available.")

    while incorrect_guesses < max_attempts:
        print(stages[incorrect_guesses])
        print("Word:", display_word(secret_word, guessed_letters))
        print(f"Incorrect guesses: {incorrect_guesses}/{max_attempts}")

        if guessed_letters:
            print(
                "Guessed letters:",
                " ".join(sorted(letter.upper() for letter in guessed_letters))
            )
        else:
            print("Guessed letters: None")

        guess = input("\nEnter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter only.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another!\n")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct guess!")

            if all(letter in guessed_letters for letter in secret_word):
                print("Word:", display_word(secret_word, guessed_letters))
                print("\nCongratulations! You won!")
                return
        else:
            incorrect_guesses += 1
            print("Wrong guess! Try again.")

        print()

    print(stages[max_attempts])
    print("The secret word was:", secret_word.upper())
    print("\nGame over! You lost. Better luck next time!")


if __name__ == "__main__":
    play_hangman()