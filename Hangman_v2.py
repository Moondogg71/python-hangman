

import random

#global variables

try:
    f = open("hangman_words.txt")
    words = f.read().splitlines()
    f.close
except IOError:
    print "cannot find file 'Hangman'"

words = ["chicken", "dog", "cat", "mouse", "frog", "horse", "skunk", "bigfoot"]
lives_remaining = 14
guessed_letters = ''#Empty Container that will be filled with letters guessed



def play():
    print "Let's play Hangman!!!"
    word = pick_a_word()#Variable that is assigned to Function pick_a_word
    #MAIN LOOP OF THE GAME
    while True:
        #Variable that is assigned to Function get_guess
        guess = get_guess(word)
        if process_guess(guess, word): #Refers to process guest funtion
            print "You Win! Well Done!!!"
            break
        if lives_remaining == 0:
            print "You are Hung!!!"
            print "The word was: " + word
            break


# COMPUTER PICKS RANDOM WORD FOR HANGMAN
def pick_a_word():
    word_position = random.randint(0, len(words) -1)#The actual computer random word selection
    return words[word_position]#Returns words list index derived from word_position random

# USER INPUT FOR GUESS
def get_guess(word):
    print_word_with_blanks(word)
    print "Lives Remaining: " + str(lives_remaining)
    guess = raw_input("Guess a letter or whole word? ")
    guess = guess.lower()
    return guess

#Displays --- if
def print_word_with_blanks(word):
    display_word = ""
    for letter in word:
        if guessed_letters.find(letter) > -1:
            #letter found
            display_word = display_word + letter
        else:
            #letter not found
            display_word = display_word + "*"
    print(display_word)

def process_guess(guess, word):
    if len(guess) > 1:
        return whole_word_guess(guess, word)
    else:
        return single_letter_guess(guess, word)

def whole_word_guess(guess, word):
    global lives_remaining
    if guess == word:
        return True
    else:
        lives_remaining = lives_remaining - 1
        return False

def single_letter_guess(guess, word):
    global guessed_letters
    global lives_remaining
    if word.find(guess) == -1:
        #letter guess was incorrect
        lives_remaining = lives_remaining -1
    guessed_letters = guessed_letters + guess
    if all_letters_guessed(word):
        return True
    return False

def all_letters_guessed(word):
    for letter in word:
        if guessed_letters.find(letter) == -1:
            return False
    return True

play()










