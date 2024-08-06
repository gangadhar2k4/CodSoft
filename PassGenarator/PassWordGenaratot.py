import random


def PasswordGenerator(length,
                      includeLowerChars,
                      includeUpperChars,
                      inludeNumbers,
                      includeSymbols):
    LowerCaseLetters = "abcdefghijklmnopqrstuvwxyz"
    UpperCaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Numbers = "0123456789"
    Symbols = "!@#$%^&*?~"

    AllowedChars = ""
    Password = ""

    if includeLowerChars:
        AllowedChars += LowerCaseLetters

    if includeUpperChars:
        AllowedChars += UpperCaseLetters

    if inludeNumbers:
        AllowedChars += Numbers

    if includeSymbols:
        AllowedChars += Symbols

    for i in range(length):
        Password += random.choice(AllowedChars)

    return Password


def PasswordCustomization():
    inludeLowerCaseLetters = None
    inludeUpperCaseLetters = None
    Numbers = None
    Symbols = None

    Length = int(input("Enter Length of Password you need to Generate: "))

    choice = input("If you want to include LowerCase Letters (y/n) or (Y/N): ")
    if choice != 'n' or choice != 'N':
        inludeLowerCaseLetters = True
    else:
        inludeLowerCaseLetters = False

    choice = input("If you want to include UpperCase Letters (y/n) or (Y/N): ")
    if choice != 'n' or choice != 'N':
        inludeUpperCaseLetters = True
    else:
        inludeUpperCaseLetters = False

    choice = input("If you want to include Numbers (y/n) or (Y/N): ")
    if choice != 'n' or choice != 'N':
        Numbers = True
    else:
        Numbers = False

    choice = input("If you want to include Symbols (y/n) or (Y/N): ")
    if choice != 'n' or choice != 'N':
        Symbols = True
    else:
        Symbols = False

    Password = PasswordGenerator(Length, inludeLowerCaseLetters,
                                 inludeUpperCaseLetters,
                                 Numbers,
                                 Symbols
                                 )
    print(f'Generated password : {Password}')


PasswordCustomization()