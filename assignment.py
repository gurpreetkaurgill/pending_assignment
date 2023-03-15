import random

def guess():
    guess = input('Enter one alphabet:')
    return guess

def str_to_list(word):
    mylist = []
    for i in word:
        mylist.append(i)
    return mylist

def printlist(mylist):
    word = ''
    for i in mylist:
        word += i
    return word

def update_list(mystring , random_word, myguess):
    for i in range (0, len(random_word)):
        if random_word[i] == myguess and mystring[i] == '_':
            mystring[i] == myguess
#     print(mystring)
    return mystring

fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "watermelon"]

random_word = str_to_list(random.choice(fruits))
print(random_word)
word_length = len(random_word)
chances = 10
mystring = str_to_list(word_length *' _ ')

print('Guess a fruit name')

while chances > 0:
    print(printlist(mystring))
    myguess = guess()
    if len(myguess) == 1:
        if myguess in random_word:
            # x = random_word.index(myguess)
            mystring = update_list(mystring, random_word, myguess)
            # mystring[x] = myguess
        else:
            chances -= 1
            print(f'Wrong guess you have {chances} chances left')
    else:
        print('Enter 1 alphabet only')
        guess()