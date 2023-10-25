import random
# import random package so a random word from word_list can be called


class Hangman():
    """ The Hangman class is a Python class that represents a game of Hangman. 
     Which asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives, in this case 5 and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: List 
         consists of words to be used in the game, in my temple the we have list of 5 fruits 
         ["apple", "Plum", "grape", "orange", "apricot"]
    num_lives: int 
        value representling the number of attempts the player has to guess the word 
        In this template the player has 5 lives 
    
    Attributes:
    ----------
    mystery_word: str 
        The word to be guessed from the word_list picked randomly using the random package (random.choice)
    mystery_word_guessed: list
        A list of the letters of the mystery_word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of letters in the mystery_word that have not been guessed 
    num_lives: int
        The number of lives the player has, this will be reduced for each incorect letter
    list_of_guesses: list
        A list of the letters that have already been guessed

    Methods:
    -------
    check_guess(player_guess)
        Checks if the guess is in the word.
    ask_for_input()
        Asks the user to make a guess for a letter they believe to be in the mystery_word.
 
    """

   
    def __init__(self, word_list, num_lives = 5):
        """   The __init__ method initializes a game of Hangman with a random word from a given word list and a
    specified number of lives.
        """
        self.mystery_word = random.choice(word_list)
        #random word generated from word_list
        self.mystery_word_guessed = ['_'] * len(self.mystery_word)
        #list of blank spaces equal to the length of the mystery word
        self.num_letters = len(set(self.mystery_word))
        #length of mystery word
        self.num_lives = num_lives
        #number of lives the player has equal to 5
        self.word_list = word_list
        # list of words to chose from ["apple", "plum", "grape", "orange", "apricot"]  
        self.list_of_guesses = []
        #empty list of for player guesses 
        print(self.mystery_word_guessed)
        #show blank mystery_word
       



    def check_guess(self, player_guess):
        """
        This method checks if the player's guess is in the mystery word and updates the guessed letters
        accordingly, by replacing the '_' in the mystery_word_guessed list with the player_guess character.
        It then prints the mystery_word_guessed with the correctly chosen letters filled in 
        e.g ['a', '_', '_', '_', '_']
        while also keeping track of the number of lives remaining, if an inccorect guess is made then
        num_lives will be reduced by one
        
        Parameters:
        ----------
        player_guess: str
            The players guess for a letter in the mystery word this is to be checked
        """
       
        player_guess = player_guess.lower()
        if player_guess.lower() in self.mystery_word:
                 print(f'Good guess! {player_guess} is in the word')
                 for letter_index, letter in enumerate(self.mystery_word):
                     if letter == player_guess:
                         self.mystery_word_guessed[letter_index] = player_guess
                         print(self.mystery_word_guessed)
                         #shows updated mystery_word_guessed with corecctly guessed letters and blanks to guess
                 self.num_letters = self.num_letters - 1
       
                 
                 
        else:
             print(f'Sorry {player_guess} is not in the word. Try again.')
             self.num_lives = self.num_lives - 1
             print(f"You have {self.num_lives} lives left.") 
       


    def ask_for_input(self): 
        """
        The method asks the player to input a single letter as a guess for a mystery word, checks if
        the input is valid, agaisnt two measures 
         1. if the input had already been entered 
         2. if the input is a single letter
        the check_guess method is then called the to check the guess.
        Also catches exceptions 
        """
        
        while True:  
            try:
                 player_guess = input("Guess a single letter in the mystery word ")
                 
                 if not player_guess.isalpha() or len(player_guess) != 1:
                     print("Invalid letter. Please, enter a single alphabetical character.")
                 
                 elif player_guess in self.list_of_guesses:
                     print("You've already tried that letter")
                 
                 else: 
                     self.check_guess(player_guess)
                     self.list_of_guesses.append(player_guess)  
            except Exception as e:
                 print(e)

word_list = ["apple", "plum", "grape", "orange", "apricot"]             
game_attempt = Hangman(word_list)
game_attempt.ask_for_input()
            
            

    







