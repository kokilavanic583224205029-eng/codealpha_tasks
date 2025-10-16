import random

def hangman():
    words = ["apple", "tiger", "chair", "ocean", "plant"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print(" Welcome to Hangman!")

    while attempts > 0:
        # Display word with underscores for unguessed letters
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
        print("\nWord:", " ".join(display_word))
        print(f"Attempts left: {attempts}")
        print("Guessed letters so far:", ", ".join(guessed_letters))

        # Check if player has guessed the word
        if "_" not in display_word:
            print("\n You guessed it! The word was:", word)
            break

        guess = input("Enter a letter: ").lower()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print(" Enter a single letter only.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            print("Wrong guess!")
            attempts -= 1

    if attempts == 0:
        print("\n💀 Game Over! The word was:", word)

# Start the game
hangman()
