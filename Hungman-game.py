import random
import string

def hangman():
    # Custom word list as requested
    word_list = ["shryansh", "python", "codealpha", "mewar", "hangman", "accident"]
    
    # Select a random word from the list
    secret_word = random.choice(word_list).lower()
    letters_guessed = set()
    alphabet = set(string.ascii_lowercase)
    max_attempts = 6
    attempts_left = max_attempts
    
    print("Welcome to Hangman!")
    print(f"I'm thinking of a word that is {len(secret_word)} letters long.")
    print("You have", attempts_left, "incorrect guesses left.")
    
    while True:
        # Display current progress
        display_word = [letter if letter in letters_guessed else '_' for letter in secret_word]
        print("\nCurrent word:", ' '.join(display_word))
        
        # Check if player has won
        if '_' not in display_word:
            print("\nCongratulations! You guessed the word:", secret_word)
            break
            
        # Check if player has lost
        if attempts_left <= 0:
            print("\nSorry, you're out of attempts! The word was:", secret_word)
            break
            
        # Get player's guess
        guess = input("Please guess a letter: ").lower()
        
        # Validate input
        if len(guess) != 1 or guess not in alphabet:
            print("Invalid input. Please enter a single letter.")
            continue
            
        if guess in letters_guessed:
            print("You've already guessed that letter. Try again.")
            continue
            
        # Add the guess to the set of guessed letters
        letters_guessed.add(guess)
        
        # Check if the guess is correct
        if guess in secret_word:
            print("Good guess!")
        else:
            attempts_left -= 1
            print(f"Oops! That letter is not in the word. You have {attempts_left} attempts left.")
            
        # Display hangman status (optional visual)
        print_hangman(max_attempts - attempts_left)

def print_hangman(wrong_attempts):
    """Optional visual representation of hangman progress"""
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        """
    ]
    
    if wrong_attempts < len(stages):
        print(stages[wrong_attempts])

if __name__ == "__main__":
    hangman()
    play_again = input("\nWould you like to play again? (yes/no): ").lower()
    while play_again == 'yes':
        hangman()
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
    print("Thanks for playing Hangman!")