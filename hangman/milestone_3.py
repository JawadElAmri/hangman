import random 
#adding random package

word_list = ["apple", "plum", "grape", "orange", "apricot"] 
#creating list of 5 fruits to be guessed
print(word_list)
#showing list in terminal 
mystery_word = random.choice(word_list)
#choosing a random word from the list
print(mystery_word)

def check_guess(player_guess):
      """
      The function "check_guess" checks if the player's guess is in the mystery word and provides feedback
      accordingly.
      
      :param player_guess: The parameter `player_guess` is the input provided by the player, which is
      their guess for a letter in the mystery word
      """
      if player_guess.lower() in mystery_word:
                 print(f'Good guess! {player_guess} is in the word')
      else:
            print(f'Sorry {player_guess} is not in the word. Try again.')

def ask_for_input(): 
    """
      The function `ask_for_input` prompts the user to enter a single letter and checks if the input is
      valid.
      
      :param player_guess: This is done using a while true loop which is only broken if the correct conditions are met, I have also added an exception block to catch and print any exceptions as e 
       once the player has entered their guess correctly the previous check guess() function will run, checking if the letter is in 
       the mystery_word and will provide feedback accordingly. 
      """
    while True:  
        try: 
            player_guess = input("Enter a single letter ")
            if len(player_guess) == 1 and player_guess.isalpha():
                  print("Good guess!")
                  break
            else: 
                  print("Oops! That is not a vaild input.")

        except Exception as e: 
              print(e) 
    
    
    check_guess(player_guess)

ask_for_input()