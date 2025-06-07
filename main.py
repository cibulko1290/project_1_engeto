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

name = input('Enter your username: ')
password = input('Enter your password: ')

'''
First condition:
Checking the registred users.
Registred user can enter to the program and select number of the text.
Unregistred user is not allow to continue.
Terminating the program.
'''

if name in users and password == users[name]:
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
        Printing the results via f-string.
        '''

        words_number = len(N.split())

        capital_letters = [word for word in N.split() if word.istitle()]
        CL =len(capital_letters)

        upper_case = [word for word in N.split() if word.isupper()]
        UC= len(upper_case)

        lower_case = [word for word in N.split() if word.islower()]
        LC= len(lower_case)

        numeric_strings = [int(num) for num in N.split() if num.isnumeric()]
        NS = len(numeric_strings)
        total = sum(numeric_strings)

        print(f'''There are {words_number} words in the selected text. 
There are {CL} titlecase words. 
There are {UC} uppercase words. 
There are {LC} lowercase words. 
There are {NS} numeric strings. 
The sum of all numbers {total}.''')
        print(delimiter)

        '''
        Counting the occurrence of words acording to their lenghts.
        Every lenght is counting separetly.
        The words are selected to 11 groups.
        The longer than 11- letters words are NOT considered.
        Output is a simple table.
        '''

        punctation = '.,?!;:\'"'
        words_length = {}
        for word in N.split():
            word_length = len(word.strip(punctation))
            if word_length in words_length:
                words_length[word_length] += 1
            else:
                words_length[word_length] = 1
                
        print('{0: >5} {1: <16} {2: <1} '.format('LEN |', 'OCCURRENCES', '| NR.'))
        print(delimiter)
        for word_length in sorted(words_length):
            print('{0: >3} {1: <1} {2: <16} {3: <1} {4: <3}'.format(word_length, '|', '*' * words_length[word_length], '|', words_length[word_length]))
                     
else:
    print('unregistered user, terminating the program..')