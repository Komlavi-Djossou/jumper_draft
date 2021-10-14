import random


class Secretword:
    """A code template for the secret word that the 
    computer chooses for each game. The responsibility 
    of this class of object is to get a secret word for 
    the user to guess.
    
    Stereotype:
        Info Holder

    Attributes:
        word (string): The secret word picked.
        word_chart (list): list of letters that make up secret word.
        wrong_letters (list): list of charaters that make 
            up non guessed and guessed letters of secret word
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Secretword): an instance of Secretword
        """
        words_list = []
        with open('vocabulary.txt', mode='rt') as file:
            # Read the contents of the file into a list
            # where each line of text in the file is stored
            # in a separate element in the list.
            for word in file:
                words_list.append(word.strip())
        
        self.word = words_list[random.randint(0, len(words_list))].lower()
              
        self.word_chart = ["_"] * len(self.word)
        self.wrong_letters = []
                

    def guess_done(self):
        """Returns True if secret word guessed, False otherwise.
        
        Args:
            self (Secretword): an instance of Secretword
        """
        if '_' not in self.word_chart:
            return True
        else:
            return False


    def show_letters(self):
        """Returns two strings: the first one with the correct guesses revealed, 
        the second with the wrong guesses.
    
        Args:
            self (Secretword): an instance of Secretword       
        """
        
        w_chart = ''
        for element in self.word_chart:  
            w_chart += element + ' '
                    
        w_letters = ''
        if len(self.wrong_letters) > 0:
            for element in self.wrong_letters:
                w_letters += ' ' + element
            
        return w_chart, w_letters