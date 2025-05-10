"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jakub Heidlberk
email: jakub.heidlberk@seznam.cz
"""
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
    garpike and stingray are also present.''']
    
users = {"bob":123,"ann":"pass123","mike":"password123","liz":"pass123" }

import string

name = input("Enter your name: ")
password = input("Enter your password: ")
commas = "-" * 41

if name in users and users[name] == password:
    print(f"username: {name}\npassword: {password}\n{commas}\nWelcome to the app, {name}.\n"
         f"We have {len(TEXTS)} to be analyzed.\n{commas}")
    
    try:
        selection = int(input("Enter a number btw. 1 and 3 to select: "))
        if selection not in range(1, 4):
           print("You should choose a number between 1 and 3, terminating the program.")
           exit()
    except ValueError:
        print("Invalid input, terminating the program.")
        exit()

    print(f"{commas}")

    stat = {}
    graph = {}

    if selection:
        stat["total"] =  len(TEXTS[selection - 1].split())
        stat["title"] = sum(word.istitle() for word in TEXTS[selection - 1].split())
        stat["upper"] = sum(word.isupper() for word in TEXTS[selection - 1].split())
        stat["lower"] = sum(word.islower() for word in TEXTS[selection - 1].split())
        stat["num_str"] = sum(word.isdigit() for word in TEXTS[selection - 1].split())
        stat["all"] = sum(int(word) for word in TEXTS[selection - 1].split() if word.isdigit())

    for word in TEXTS[selection - 1].split():
        word_clean = word.strip(string.punctuation)
        if len(word_clean) in graph:
            graph[len(word_clean)] += 1
        else:
            graph[len(word_clean)] = 1

    graph = dict(sorted(graph.items()))

    print(
        f"There are: {stat['total']} words in the selected text.\n"
        f"There are: {stat['title']} titlecase words.\n"
        f"There are: {stat['upper']} uppercase words.\n"
        f"There are: {stat['lower']} lowercase words.\n"
        f"There are: {stat['num_str']} numeric strings.\n"
        f"The sum of all the numbers is {stat['all']}.\n"
        f"{commas}"
    )

    print(f"LEN|{' '}OCCURENCES{' ' * 3}|NR.\n{commas}")

    max_key_len = max(len(str(key)) for key in graph)
    max_val_len = max(len(str(val)) for val in graph.values())
    max_bar_len = max(graph.values())

    for key, value in graph.items():
        bar = '*' * value
        distance = ' ' * (max_bar_len - value + 1)
        print(f"{str(key).rjust(max_key_len)} | {bar}{distance} |{str(value).rjust(max_val_len)}")
else:
    print(f"username: {name}\npassword: {password}\nUnregistered user, terminating the program.")
    exit()
