'''
projekt_1.py: první projekt do Engeta Online Python Academie

autor: Lucia Luptáková
email: lucy.luptakova@gmail.com
'''
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
    ]
users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
    }

delimiter = '-' * 40
number = len(TEXTS)

name = input('username: ')
password = input('password: ')

'''
First condition:
Checking the registred users.
Registred user can enter to the program and select number of the text.
Unregistred user is not allow to continue.
Terminating the program.
'''

if name in users and password == users.get(name):
    print(delimiter) 
    print(f'Welcome to the app, {name}')
    print(f'We have {number} texts to be analysed.')
    print(delimiter)
    number_of_text = input(f'Enter a number btw. 1 and {number} to select: ')
    print(delimiter)

    '''
    Second condition:
    During selecting of text is necessary to check an input.
    The program will end when input is a number out of range or a text.
    The user will be warned.
    Program will continue when input is a number in defined range.
    '''
    if not number_of_text.isdigit():
        print('The text is not allowed, terminating the program.')
    elif int(number_of_text) > number:
        print('The number is out of range, terminating the program.')
    elif int(number_of_text) <= number:
        N = TEXTS[int(number_of_text)-1]

        '''
        Analyzing of selected text.
        Printing the results via f-strings
        '''

        words_number = len(N.split())
        S_1 = f'There are {words_number} words in the selected text.'

        capital_letters = [word for word in N.split() if word.istitle()]
        CL =len(capital_letters)
        S_2 = f'There are {CL} titlecase words.'

        upper_case = [word for word in N.split() if word.isupper()]
        UC= len(upper_case)
        S_3 = f'There are {UC} uppercase words.'

        lower_case = [word for word in N.split() if word.islower()]
        LC= len(lower_case)
        S_4 = f'There are {LC} lowercase words.'

        numeric_strings = [word for word in N.split() if word.isnumeric()]
        NS = len(numeric_strings)
        S_5 = f'There are {NS} numeric strings.'

        suma = []
        for num in N.split():
             if num.isnumeric():
                suma.append(int(num))
                total = sum(suma)
        S_6 = f'The sum of all numbers {total}.'

        print(S_1,S_2,S_3,S_4,S_5,S_6, sep='\n')
        print(delimiter)

        '''
        Counting the occurrence of words acording to their lenghts.
        Every lenght is counting separetly.
        The words are selected to 11 groups.
        The longer than 11- letters words are NOT considered.
        Output is a simple table.
        '''

        L_1 = 0
        for word in N.split():
            if len(word) == 1 and word.isalnum():
                L_1 += 1
            elif len(word) == 2 and word[-1]  == '.':
                L_1 += 1
            elif len(word) == 2 and word[-1]  == ',':
                L_1 += 1
            
        L_2 = 0
        for word in N.split():
            if len(word) == 2 and word.isalnum():
                L_2 += 1
            elif len(word) == 3 and word[-1]  == '.':
                L_2 += 1
            elif len(word) == 3 and word[-1]  == ',':
                L_2 += 1

        L_3 = 0
        for word in N.split():
            if len(word) == 3 and word.isalnum():
                L_3 += 1
            elif len(word) == 4 and word[-1]  == '.':
                L_3 += 1
            elif len(word) == 4 and word[-1]  == ',':
                L_3 += 1

        L_4 = 0
        for word in N.split():
            if len(word) == 4 and word.isalnum():
                L_4 += 1
            elif len(word) == 5 and word[-1]  == '.':
                L_4 += 1
            elif len(word) == 5 and word[-1]  == ',':
                L_4 += 1

        L_5 = 0
        for word in N.split():
            if len(word) == 5 and word.isalnum():
                L_5 += 1
            elif len(word) == 6 and word[-1]  == '.':
                L_5 += 1
            elif len(word) == 6 and word[-1]  == ',':
                L_5 += 1

        L_6 = 0
        for word in N.split():
            if len(word) == 6 and word.isalnum():
                L_6 += 1
            elif len(word) == 7 and word[-1]  == '.':
                L_6 += 1
            elif len(word) == 7 and word[-1]  == ',':
                L_6 += 1

        L_7 = 0
        for word in N.split():
            if len(word) == 7 and word.isalnum():
                L_7 += 1
            elif len(word) == 8 and word[-1]  == '.':
                L_7 += 1
            elif len(word) == 8 and word[-1]  == ',':
                L_7 += 1

        L_8 = 0
        for word in N.split():
            if len(word) == 8 and word.isalnum():
                L_8 += 1
            elif len(word) == 9 and word[-1]  == '.':
                L_8 += 1
            elif len(word) == 9 and word[-1]  == ',':
                L_8 += 1

        L_9 = 0
        for word in N.split():
            if len(word) == 9 and word.isalnum():
                L_9 += 1
            elif len(word) == 10 and word[-1]  == '.':
                L_9 += 1
            elif len(word) == 10 and word[-1]  == ',':
                L_9 += 1

        L_10 = 0
        for word in N.split():
            if len(word) == 10 and word.isalnum():
                L_10 += 1
            elif len(word) == 11 and word[-1]  == '.':
                L_10 += 1
            elif len(word) == 11 and word[-1]  == ',':
                L_10 += 1

        L_11 = 0
        for word in N.split():
            if len(word) == 11 and word.isalnum():
                L_11 += 1
            elif len(word) == 12 and word[-1]  == '.':
                L_11 += 1
            elif len(word) == 12 and word[-1]  == ',':
                L_11 += 1

        print("{0: >5} {1: <18} {2: <1} ".format
              ("LEN |", "OCCURRENCES", '| NR.'))
        print(delimiter)
        print("{0: >5} {1: <18} {2: <1} {3: <3}".format
              ("1 |", "*" * L_1, '|', L_1))
        print("{0: >5} {1: <18} {2: <1} {3: <3}".format
              ("2 |", "*" * L_2, '|', L_2))
        print("{0: >5} {1: <18} {2: <1} {3: <3}".format
              ("3 |", "*" * L_3, '|', L_3))
        print("{0: >5} {1: <18} {2: <1} {3: <3}".format
              ("4 |", "*" * L_4, '|', L_4))
        print("{0: >5} {1: <18} {2: <1} {3: <3}".format
              ("5 |", "*" * L_5, '|', L_5))
        print("{0: >5} {1: <18} {2: <1} {3: <3}".format
              ("6 |", "*" * L_6, '|', L_6))
        print("{0: >5} {1: <18} {2: <1} {3: <3}".format
              ("7 |", "*" * L_7, '|', L_7))
        print("{0: >5} {1: <18} {2: <1} {3: <3}".format
              ("8 |", "*" * L_8, '|', L_8))
        print("{0: >5} {1: <18} {2: <1} {3: <3}".format
              ("9 |", "*" * L_9, '|', L_9))
        print("{0: >5} {1: <18} {2: <1} {3: <3}".format
              ("10 |", "*" * L_10, '|', L_10))
        print("{0: >5} {1: <18} {2: <1} {3: <3}".format
              ("11 |", "*" * L_11, '|', L_11))
                
else:
    print('unregistered user, terminating the program..')