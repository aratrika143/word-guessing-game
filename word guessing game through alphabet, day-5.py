import random

def word_guessing_game():
    words = ["apple", "banana", "cherry", "grape", "orange", "watermelon", "mango"]
    turns = 12

    name = input("Enter your name: ")
    print(f"Welcome, {name}! Let's play the word guessing game.")

    # Select a random word from the list
    word = random.choice(words)
    guessed_letters = []

    while turns > 0:
        failed=0
        # Display the word with guessed letters
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
                failed+=1

        print(f"\nWord: {display_word}")
        print(f"Turns left: {turns}")
        
        if failed == 0:
            print("\nCongratulations! You guessed the word correctly!")
            print(f"The word is:", word)
            break

        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
        else:
            print("Wrong guess!")
            turns -= 1
            
    if turns == 0:
        print(f"\nGame over! You couldn't guess the word. The word was '{word}'.")

# Run the game
word_guessing_game()