import random
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CHANCES = 6

def main():
    file = pre_game()
    chosen_word = start_game(file)
    play_game(chosen_word)

def play_game(chosen_word):
    """
    Function plays the hangman game
    :param chosen_word: the word to be guessed
    """
    count_wrong_guess = 0
    chosen_word_with_space = add_space(chosen_word)
    guess_word = make_blank(chosen_word)
    store_guessed_letters = ""
    available_letter = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
    while CHANCES - count_wrong_guess > 0 and guess_word != chosen_word_with_space:
        print("")
        print(available_letter)
        guessed_letter = ask_for_letter()
        store_guessed_letters += guessed_letter
        available_letter = update_available_letters(store_guessed_letters)
        if guessed_letter in chosen_word and guessed_letter !="" and not check_repeated_guess(guessed_letter, store_guessed_letters):
            print("Your guess is correct. It has letter " + guessed_letter)
        elif guessed_letter not in chosen_word:
            count_wrong_guess += 1
            print("Ooops! There are no " + guessed_letter +"'s. ")
        draw_hangman(count_wrong_guess)
        guess_word = correct_guess(chosen_word, store_guessed_letters)
    game_result(count_wrong_guess,chosen_word)

def game_result(count_wrong_guess, chosen_word):
    '''Function prints the result of the game and the correct answer'''
    if count_wrong_guess == CHANCES:
        print("You lost. The word was "+ chosen_word)
    else:
        print("Congratulations! You guessed it!")

def update_available_letters(store_guessed_letters):
    '''Function removes from the alphabet the chosen letters
        returns letters that the user has not guessed yet'''
    alphabet_letter=""
    for letter in ALPHABET:
        if letter in store_guessed_letters:
            alphabet_letter += ""
        else:
            alphabet_letter += letter + " "
    return alphabet_letter

def check_repeated_guess(guessed_letter, store_guessed_letters):
    ''' Checks if you guessed the same letter again
    return true or false'''
    count = 0
    for letter in store_guessed_letters:
        if letter == guessed_letter:
            count += 1
    return count > 1

def ask_for_letter():
    '''
    Asks users for a letter then corrects the format of the input
    Returns corrected guess letter
    '''
    guessed_letter = input("Choose a letter: ").upper()
    guessed_letter = guessed_letter.strip()
    if len(guessed_letter) != 1:
        print ("Guess is not a single character.")
        guessed_letter=""
    elif guessed_letter not in ALPHABET:
        print ("Guess is not a letter.")
        guessed_letter = ""
    return guessed_letter

def correct_guess(chosen_word, store_guessed_letters):
    '''
    Reveals the letters that the user guessed correctly in guess word
    Returns the guess word
    '''
    guess_word = ""
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter in store_guessed_letters:
            guess_word += letter + " "
        else:
            guess_word = letter_to_blank(letter, guess_word)
    print(guess_word)
    return guess_word

def pre_game():
    """Function asks user to choose a category
    Return the filename"""
    print("")
    print("Welcome to Hangman! Before we start, please choose a category below:")
    print("Enter 1 for Random")
    print("Enter 2 for Movies")
    print("Enter 3 for Olympic Sports")
    print("Enter 4 for Customized")
    category = input("Category: ")
    if category == "1": file="random"
    elif category == "2": file ="movies"
    elif category == "3": file="olympic_sports"
    elif category == "4": file=input("Type filename: ")
    else: file = "random"
    print("You chose "+ file.upper() + ". Let's play hangman!")
    return file

def start_game(file):
    """Function starts the game based on the category chosen"""
    word_list = load_words(file)
    chosen_word = choose_word(word_list)
    initial_drawing()
    return chosen_word

def load_words(file):
    '''Loads and cleans the data from a file into a list'''
    file = open(file + ".txt")
    word_list = []
    for words in file:
        words = words.upper()
        word_list.append(words.strip())
    return word_list

def choose_word(word_list):
    """Choose a random word/s from the list"""
    chosen_word = random.choice(word_list)
    return chosen_word

def make_blank(chosen_word):
    """ hide the letters of the chosen word and each letter is turned to blanks "_" """
    guess_word = ""
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        guess_word = letter_to_blank(letter, guess_word)
    print (guess_word)
    return guess_word

def letter_to_blank(letter, word):
    """ Function turns letters into blank"""
    if letter not in ALPHABET:
        word += letter
    else:
        word += "_ "
    return word

def add_space(chosen_word):
    """Function adds space in between the letters"""
    chosen_word_with_space = ""
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter in ALPHABET:
            chosen_word_with_space += (letter + " ")
        else:
            chosen_word_with_space += letter
    return chosen_word_with_space

def draw_hangman(count_wrong_guess):
    '''
    Function draws hangman based on how many incorrect answer you have
    :param count_wrong_guess: number of incorrect guesses
    :return: Drawing of hangman
    '''
    if count_wrong_guess == 0: initial_drawing()
    elif count_wrong_guess == 1: head_drawing()
    elif count_wrong_guess == 2: body_drawing()
    elif count_wrong_guess ==3: left_hand_drawing()
    elif count_wrong_guess ==4: right_hand_drawing()
    elif count_wrong_guess ==5: left_leg_drawing()
    elif count_wrong_guess ==6: right_leg_drawing()

def initial_drawing():
    print("     _____")
    print("          |")
    print("          |")
    print("          |")
    print("          |")
    print("          |")
    print("       ___|___")
    print("")

def head_drawing():
    print("     _____")
    print("    ( )   |")
    print("          |")
    print("          |")
    print("          |")
    print("          |")
    print("          |")
    print("       ___|___")

def body_drawing():
    print("     _____")
    print("    ( )   |")
    print("     |    |")
    print("     |    |")
    print("     |    |")
    print("          |")
    print("          |")
    print("       ___|___")

def left_hand_drawing():
    print("     _____")
    print("    ( )   |")
    print("   \ |    |")
    print("    \|    |")
    print("     |    |")
    print("          |")
    print("          |")
    print("       ___|___")

def right_hand_drawing():
    print("     _____")
    print("    ( )   |")
    print("   \ | /  |")
    print("    \|/   |")
    print("     |    |")
    print("          |")
    print("          |")
    print("       ___|___")

def left_leg_drawing():
    print("     _____")
    print("    ( )   |")
    print("   \ | /  |")
    print("    \|/   |")
    print("     |    |")
    print("    /     |")
    print("   /      |")
    print("       ___|___")

def right_leg_drawing():
    print("     _____")
    print("    ( )   |")
    print("   \ | /  |")
    print("    \|/   |")
    print("     |    |")
    print("    / \   |")
    print("   /   \  |")
    print("       ___|___")

if __name__ == '__main__':
    main()