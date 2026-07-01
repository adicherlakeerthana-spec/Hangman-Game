#jagan hangman
import random

words = ["mango", "guitar", "python", "cloud", "tiger"]

hangman_stages = [
    """
  -----
  |   |
      |
      |
      |
      |
==========""",
    """
  -----
  |   |
  O   |
      |
      |
      |
==========""",
    """
  -----
  |   |
  O   |
  |   |
      |
      |
==========""",
    """
  -----
  |   |
  O   |
 /|   |
      |
      |
==========""",
    """
  -----
  |   |
  O   |
 /|\\  |
      |
      |
==========""",
    """
  -----
  |   |
  O   |
 /|\\  |
 /    |
      |
==========""",
    """
  -----
  |   |
  O   |
 /|\\  |
 / \\  |
      |
==========""",
]

def display_board(wrong_guesses, guessed_letters, word):
    print(hangman_stages[wrong_guesses])
    print(f"\nWrong guesses left: {6 - wrong_guesses}")
    print(f"Letters guessed: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
    display_word = " ".join(letter if letter in guessed_letters else "_" for letter in word)
    print(f"\nWord: {display_word}\n")

def play_hangman():
    word = random.choice(words)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 6

    print("=" * 40)
    print("   Welcome to Hangman! 🎮")
    print("=" * 40)

    while wrong_guesses < max_wrong:
        display_board(wrong_guesses, guessed_letters, word)

        if all(letter in guessed_letters for letter in word):
            print(f"🎉 YOU WIN! The word was: {word.upper()}")
            break

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️  Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"⚠️  You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"✅ Good guess! '{guess}' is in the word!")
        else:
            wrong_guesses += 1
            print(f"❌ Wrong! '{guess}' is not in the word.")

    else:
        display_board(wrong_guesses, guessed_letters, word)
        print(f"💀 GAME OVER! The word was: {word.upper()}")

    play_again = input("\nPlay again? (yes/no): ").lower().strip()
    if play_again == "yes":
        play_hangman()
    else:
        print("Thanks for playing! Goodbye! 👋")

play_hangman()