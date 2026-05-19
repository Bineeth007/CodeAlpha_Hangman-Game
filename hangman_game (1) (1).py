import random

def play_hangman():
    words = ["backend", "database", "middleware", "scalable", "repository"]
    target_word = random.choice(words)
    
    guessed_letters = set()
    incorrect_guesses_allowed = 6
    incorrect_guesses = 0
    
    print("Starting Hangman. You have 6 incorrect guesses allowed.")
    
    while incorrect_guesses < incorrect_guesses_allowed:
        # Build the current state of the word
        display_word = "".join([char if char in guessed_letters else "_" for char in target_word])
        print(f"\nWord: {display_word}")
        print(f"Incorrect guesses left: {incorrect_guesses_allowed - incorrect_guesses}")
        
        if "_" not in display_word:
            print("Status: Victory. You guessed the word correctly.")
            return

        guess = input("Enter a single letter: ").strip().lower()
        
        # Edge Case Handling: Input Validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter exactly one alphabetical character.")
            continue
        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
            continue
            
        guessed_letters.add(guess)
        
        if guess not in target_word:
            incorrect_guesses += 1
            print(f"Letter '{guess}' is not in the word.")
            
    print(f"\nStatus: Defeat. The word was '{target_word}'.")

if __name__ == "__main__":
    play_hangman()
