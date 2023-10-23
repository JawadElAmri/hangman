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
      if player_guess.lower() in mystery_word:
                 print(f"Good guess! {player_guess} is in the word")
      else:
            print(f"Sorry {player_guess} is not in the word. Try again.")



def ask_for_input(): 
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

