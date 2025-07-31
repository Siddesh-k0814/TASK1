import random 
 
def hangman(): 
 
    word_list = ['python', 'hangman', 'programming', 'challenge', 'random', 'guess'] 
 
 
    word = random.choice(word_list) 
    word_letters = set(word)  
    guessed_letters = set()   
    incorrect_guesses = 0 
    max_incorrect = 6 
 
    print("Welcome to Hangman!") 
    print(f"I'm thinking of a word with {len(word)} letters.") 
 
    while incorrect_guesses < max_incorrect and len(word_letters) > 0: 
 
        display_word = [letter if letter in guessed_letters else '_' for letter in word] 
        print("\nWord:", ' '.join(display_word)) 
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}") 
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}") 
 
        guess = input("Guess a letter: ").lower() 
        if len(guess) != 1 or not guess.isalpha(): 
            print("Please guess a single letter.") 
            continue 
 
        if guess in guessed_letters: 
            print("You've already guessed that letter!") 
            continue 
 
        guessed_letters.add(guess) 
        if guess in word_letters: 
            word_letters.remove(guess) 
            print("Good guess!") 
 
        else: 
            incorrect_guesses += 1 
            print("Sorry, that letter is not in the word.") 
 
    if len(word_letters) == 0: 
        print(f"\nCongratulations! You guessed the word: {word}") 
    else: 
        print(f"\nGame over! The word was: {word}") 
 
 
if __name__ == "__main__": 
    hangman()
