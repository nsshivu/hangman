# Hangman Game

## Description
This is a simple command-line Hangman game implemented in Python. The player guesses letters to reveal a hidden word, with a limit of 6 incorrect guesses before losing the game. The word is randomly selected from a predefined list.

## Features
- Random word selection from a list of 5 words.
- Tracks guessed letters and incorrect guesses.
- Displays the current state of the word with underscores for unguessed letters.
- Input validation for single letters and repeated guesses.
- Graceful handling of keyboard interrupts.

## Requirements
- Python 3.x

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/hangman-game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd hangman-game
   ```

## Usage
Run the game using Python:
```bash
python hangman.py
```
- Follow the prompts to guess one letter at a time.
- You have 6 incorrect guesses before the game ends.
- The game displays the current word state, guessed letters, and incorrect guess count.

## File Structure
- `hangman.py`: Main Python script containing the game logic.
- `README.md`: Project documentation (this file).
- `.gitignore`: Specifies files to ignore in version control.

## Example Gameplay
```
Welcome to Hangman!
The word has 5 letters: _ _ _ _ _

Incorrect guesses: 0/6
Guessed letters: None
Guess a letter: a
Good guess!
Word: _ _ _ _ a

Incorrect guesses: 0/6
Guessed letters: a
Guess a letter: x
Wrong! 'x' is not in the word.
Word: _ _ _ _ a
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License.