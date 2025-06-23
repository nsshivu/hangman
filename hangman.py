import random

def hangman():
    # List of 5 predefined words
    words = ['apple', 'smile', 'chair', 'light', 'music']
    # Select random word
    word = random.choice(words)
    # List to store guessed letters
    guessed_letters = []
    # List to represent current state of word (e.g., ['_', '_', 'p', '_'])
    current_state = ['_'] * len(word)
    # Track incorrect guesses
    incorrect_guesses = 0
    max_incorrect = 6
    
    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters: {' '.join(current_state)}")
    
    while incorrect_guesses < max_incorrect and '_' in current_state:
        print(f"\nIncorrect guesses: {incorrect_guesses}/{max_incorrect}")
        print("Guessed letters:", ' '.join(sorted(guessed_letters)) if guessed_letters else "None")
        
        # Get player input
        guess = input("Guess a letter: ").lower().strip()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        # Add guess to guessed letters
        guessed_letters.append(guess)
        
        # Check if guess is in word
        if guess in word:
            print("Good guess!")
            # Update current state
            for i in range(len(word)):
                if word[i] == guess:
                    current_state[i] = guess
        else:
            print(f"Wrong! '{guess}' is not in the word.")
            incorrect_guesses += 1
        
        # Display current state
        print(f"Word: {' '.join(current_state)}")
    
    # Game outcome
    if '_' not in current_state:
        print(f"\nCongratulations! You guessed the word: {word}")
    else:
        print(f"\nGame Over! The word was: {word}")

if __name__ == "__main__":
    try:
        hangman()
    except KeyboardInterrupt:
        print("\nGame terminated. Goodbye!")