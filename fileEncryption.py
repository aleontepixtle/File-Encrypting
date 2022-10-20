#Name fileencryption.py
#Author Andres Leon T
# Date 03.19.2022
#This program takes user phrases and converts them into encrypted text and displays it in a file

def user_phrase(): # gets phrase from user
    usrinput = input("Enter a word or phrase.\t")
    return usrinput

def make_dictionary(): # genertates encrypted dictionary reference
    letters = {'A': '@',
               'a': '*',
               'B': '!',
               'b': '#',
               'C': '##',
               'c': ')',
               'D': '()',
               'd': '_',
               'E': '=',
               'e': '+',
               'F': '&',
               'f': '$',
               'G': '###',
               'g': '>',
               'H': '.',
               'h': '<',
               'I': '?',
               'i': '"',
               'J': ':',
               'j': '}',
               'K': '{',
               'k': '{}',
               'L': '[',
               'l': ']',
               'M': '[]',
               'm': '`',
               'N': '~',
               'O': '~~~',
               'o': '~!',
               'P': '@!',
               'p': '^&%$',
               'R': '**(',
               'r': '~~+',
               'S': '\\',
               's': '||',
               'T': '|',
               't': '|(',
               'U': '|+',
               'u': '|+|o',
               'V': '{|}',
               'v': ' ',
               'W': ' | + |',
               'w': '|}{',
               'X': '$#!`',
               'x': '?><',
               'Y': '<>>?',
               'y': '<>|<>',
               'Z': '<.><.>',
               'z': '(.)(.)',
               ' ': '(.)(.)'}
    return letters

def convert(userWord, letters): # converts word into special chars
    file = open('encryptedfile.txt', 'w') # creates file
    for char in userWord:
        if char in letters:
            file.write(letters[char]) # writes encrypted phrase
            print(letters[char], end="")
        else:
            print('(*)(*)')
    print('File has been created.') 
    file.close() # closes file

def main():
    userWord = user_phrase()
    diction = make_dictionary()
    convert(userWord, diction)

main()