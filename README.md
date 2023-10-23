# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word from a selected list of fruits and the user tries to guess it. 

## Milestone2 
In this file I have created the list of fruits assigned to the variable word_list 
The list is then printed 
The player will have to guess one of these furits chose at random by python
I imported the random package allowing a word to be selected from the list at random with random.choice(word_list)
The random word is assgined the varible word
The variable is printed 
I created an input option for the player to start guessing the word ("Enter a single letter.")
I made sure the input would prevent anymore more than a single alpbetical letter being entered 
This was done by adding a try except block and using if statments 
if len(guess) == 1 and guess.isalpha() :
            print("Good guess!")
            break 
 else: 
            print("Oops! That is not a vaild input.")

The try except block is in a while loop to enrue the programme does not stop ruuning when an incorrect option is entered 
I then set it to catch exceptions as e and print e in order to catch other exceptions 

