# Python Program to illustrate
# Hangman Game

import random
from collections import Counter

someWords = '''apple banana'''

someWords = someWords.split(' ')

# randomly choose a secret word from our "someWords" LIST.
word = random.choice(someWords)
if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a fruit')

for i in word:
    # For printing the empty spaces for letters of the word
    print(" " and " ")
    print()

    playing = True
    # list for storing the letters guessed by the player
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0
    try:
        while (chances != 0) and flag == 0:

            # flag is updated when the word is correctly guessed
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter!')
                continue

                # Validation of the guess
            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:

                print('Enter only a SINGLE letter')

                continue
            elif guess in letterGuessed:

                print('You have already guessed that letter')

                continue

            # If letter is guessed correctly
            if guess in word:
                k = word.count(guess)
                # k stores the number of times the guessed letter occurs in the word

                for _ in range(k):
                    letterGuessed += guess
                # The guess letter is added as many times as it occurs
'''banana mango strawberrye orange grape pineapple apricot lemon coconut cherry papaya berry peach lychee muskmelon'''
            # Print the word
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end=' ')
                    correct += 1

                # If user has guessed all the letters
                elif (Counter(letterGuessed) == Counter(word)):

                    # Once the correct word is guessed fully,

                    # the game ends, even if chances remain
                    print("The word is: ", end=' ')
                    print(word)
                    flag = 1
                    print('Congratulations, You won!')
                    break
                    # To break out of the for loop
                    break
                    # To break out of the while loop
                else:
                    print('_', end=' ')

                    # If user has used all of his chances
        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('You lost! Try again..')
            print('The word was {}'.format(word))

    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()










import random
from collections import Counter

def incorrect_attempts():
    attempts_remaining = input("how many incorrect attempts do you want? [1-25]")
    if attempts_remaining.isdigit():
        attempts_remaining = int(attempts_remaining)
        if attempts_remaining >= 25 or attempts_remaining <= 0:
            print("Please Enter number between [1-25]")
        else:
            minimum_word_len(attempts_remaining)
    elif attempts_remaining.lower() == "NaN".lower():
        print("NaN is not an integer between 1 and 25")
    else:
        print("{0}: is not an integer between 1 and 25:".format(attempts_remaining))

def minimum_word_len(attempts_remaining):
    min_word_len = int(input("what minimum word length do you want? [4-16]"))
    print("selecting a word...")
    read_word_frm_txt(min_word_len,attempts_remaining)

def read_word_frm_txt(min_word_len,attempts_remaining):
    with open("words.txt",mode='r') as fd:
        words_lines = fd.readlines()
        for words_line in words_lines:
            words_list = words_line.split(" ")
            select_word(words_list,min_word_len,attempts_remaining)

def select_word(words_list,min_word_len,attempts_remaining):
    selected_words_list = []
    for words in range(0, len(words_list)-1):
        if len(words_list[words]) >= min_word_len:
            selected_words_list.append(words_list[words])
    word = random.choice(selected_words_list)
    replace_star(min_word_len,word,attempts_remaining)

def replace_star(min_word_len,word,attempts_remaining):
    print("word:",end=" ")
    for w in range(0, len(word)-1):
        print("*",end=" ")
    print()
    reduce_attempts(attempts_remaining,word)

def reduce_attempts(attempts_remaining,word):
    flag = 0
    previous_guesses = ""


    try:
        while (attempts_remaining != 0) and flag == 0:
            # attempts_remaining -= 1
            previous = " "
            print()
            print("Attempts Remaining:{0}".format(attempts_remaining))
            print("Previous Guesses:",previous)
            next_letter = input("Choose the next letter:")
            attempts_remaining -= 1
            if next_letter.isalpha():
                if len(next_letter) > 1:
                    print("Enter only Single charecter")
                    continue
                else:
                    if next_letter in previous_guesses:
                        attempts_remaining+=1
                        print("You have already guessed that letter")
                        continue
                    else:
                        if next_letter in word:
                            next_letter_replicate = word.count(next_letter)
                            for letter in range(next_letter_replicate):
                                previous_guesses+=next_letter
                            previous = next_letter
                            print("{0} is in the word!".format(next_letter))
                            print("word:",end=" ")
                            for w in word:
                                if w in previous_guesses:
                                    print(w,end=" ")
                                    if len(word) == len(previous_guesses):
                                        print('Congratulations, You won the game!')
                                        break
                                        break
                                        break
                                else:
                                    print("*",end=" ")

                        else:
                            print("{0} is not in word:".format(next_letter))
            else:
                print("Enter only letter") #watermelone
                continue
    except KeyboardInterrupt:
        print()
        print('Try again.')
        exit()



if __name__ == '__main__':
    print('Starting a game of Hangman....')
    incorrect_attempts()


































































import random
def incorrect_attempts():
    attempts_remaining = input("how many incorrect attempts do you want? [1-25]")
    if attempts_remaining.isdigit():
        attempts_remaining = int(attempts_remaining)
        if attempts_remaining >= 25 or attempts_remaining <= 0:
            print("Please Enter number between [1-25]")
        else:
            minimum_word_len(attempts_remaining)
    elif attempts_remaining.lower() == "NaN".lower():
        print("NaN is not an integer between 1 and 25")
    else:
        print("{0}: is not an integer between 1 and 25:".format(attempts_remaining))

def minimum_word_len(attempts_remaining):
    min_word_len = int(input("what minimum word length do you want? [4-16]"))
    print("selecting a word...")
    read_word_frm_txt(min_word_len,attempts_remaining)

def read_word_frm_txt(min_word_len,attempts_remaining):
    with open("words.txt",mode='r') as fd:
        words_lines = fd.readlines()
        for words_line in words_lines:
            words_list = words_line.split(" ")
            select_word(words_list,min_word_len,attempts_remaining)

def select_word(words_list,min_word_len,attempts_remaining):
    selected_words_list = []
    for words in range(0, len(words_list)-1):
        if len(words_list[words]) >= min_word_len:
            selected_words_list.append(words_list[words])
    word = random.choice(selected_words_list)
    replace_star(min_word_len,word,attempts_remaining)

def replace_star(min_word_len,word,attempts_remaining):
    print("word:",end=" ")
    for w in range(0, len(word)-1):
        print("*",end=" ")
    print()
    reduce_attempts(attempts_remaining,word)

def reduce_attempts(attempts_remaining,word):
    flag = 0
    previous_guesses = ""


    try:
        while (attempts_remaining != 0) and flag == 0:
            # attempts_remaining -= 1
            previous = " "
            print()
            print("Attempts Remaining:{0}".format(attempts_remaining))
            print("Previous Guesses:",previous)
            next_letter = input("Choose the next letter:")
            attempts_remaining -= 1
            if next_letter.isalpha():
                if len(next_letter) > 1:
                    print("Enter only Single charecter")
                    continue
                else:
                    if next_letter in previous_guesses:
                        attempts_remaining+=1
                        print("You have already guessed that letter")
                        continue
                    else:
                        if next_letter in word:
                            next_letter_replicate = word.count(next_letter)
                            for letter in range(next_letter_replicate):
                                previous_guesses+=next_letter
                            previous = next_letter
                            print("{0} is in the word!".format(next_letter))
                            print("word:",end=" ")
                            for w in word:
                                if w in previous_guesses:
                                    print(w,end=" ")
                                    if len(word) == len(previous_guesses):
                                        print('Congratulations, You won the game!')
                                        flag = 1
                                        break
                                        break
                                        break

                                else:
                                    print("*",end=" ")

                        else:
                            print("{0} is not in word:".format(next_letter))
            else:
                print("Enter only letter") #watermelone
                continue


        if attempts_remaining <= 0:
            print()
            print('You lost! Try again..')
            print('The word was {}'.format(word))


    except:
        print()
        print('Try again.')
        exit()


if __name__ == '__main__':
    print('Starting a game of Hangman....')
    incorrect_attempts()
