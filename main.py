# IMPORTS
import random
import os
from hangman_art import stages, logo
from hangman_words import word_list

# Choose a random element from word_list
chosen_word = random.choice(word_list)

# Set lives to six
lives = 6

# Make a list with "_" representing
# each letter of the chosen word
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
# print(display)

# Show the logo
print(logo)

# ONLY FOR TEST
# print(f"La palabra es: {chosen_word}.")

# Make a condition to play the game
end_of_game = False
while not end_of_game:
    os.system("clear")
    # Make an input and transform to lower case
    guess = input("Guess a letter: ").lower()
    
    # Show a message when guess a letter
    if guess in chosen_word:
        print(f"\nCORRECT CHOICE. CONTINUE...")

    # Replace "_" with correct letter
    # in "display" array ["a","_","a","_","a",]
    for position in range(word_length):
        # Storage the value iteration
        # of "choosen_word" on letter variable
        letter = chosen_word[position]
        if letter == guess:
            # Replace the value in the position of "_", 
            # with letter in display array
            display[position] = letter
    
    if guess not in chosen_word:
        # Show a message when don't guess a letter
        print(f"\nINCORRECT CHOICE. LOSE A LIFE. CONTINUE...")
        lives -= 1
        if lives == 0:
            os.system("clear")
            end_of_game = True
            print(f"\nY O U  L O S E")

    # Show display
    # print(display)
    
    # Join all elements in a list  
    # and convert in a string
    print(f"\n{' '.join(display)}")

    # If there is no more "_" in display array
    # end of game
    if "_" not in display:
        os.system("clear")
        end_of_game = True
        print(f"\nJ A L L A L L A!\n6ANA$T3!")

    # Print the figure depends of lives left
    print(stages[lives])