from milesto
while True:  #loop to prevent code from stoppping
    try: 
        player_guess = input("Guess a single letter in the mystery word ")
        if len(player_guess) == 1 and player_guess.isalpha() :     
            # if length is equal to 1 and input is alpabetical letter loop will break
            print("Good guess!")
            break
        else: 
            print("Invalid letter. Please Enter a single alphabetical character.")
    except Exception as e: #catch and print exceptions 
        print(e) 


if player_guess.lower() in mystery_word:
    print("Good guess! f'{player_guess}' is in the word")
else:
    print("Sorry f'{player_guess}' is not in the word. Try again.")x