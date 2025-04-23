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
    garpike and stingray are also present.'''
]
uzivatel = {"bob":123,"ann":"pass123","mike":"password123","liz":"pass123" }

jmeno = input("Zadejte své uživatelské jméno: ")
heslo = input("Zadejte své heslo: ")
carky = "-" * 41

if jmeno in uzivatel.keys() and heslo in str(uzivatel.values()):
    print(f"username: {jmeno}\npassword: {heslo}\n{carky}\nWelcome to the app, {jmeno}.\n"
         f"We have {len(TEXTS)} to be analyzed.\n{carky}")
    
    try:
        vyber = int(input("Zadej číslo od 1 do 3: "))
        if vyber not in range(1, 4):
           print("You should choose a number between 1 and 3, terminating the program.")
           exit()
    except ValueError:
        print("Invalid input, terminating the program.")
        exit()
        
    print(f"{carky}")

    stat = {}
    graf = {}

    if vyber:
        stat["total"] =  len(TEXTS[vyber - 1].split())
        stat["title"] = sum(word.istitle() for word in TEXTS[vyber - 1].split())
        stat["upper"] = sum(word.isupper() for word in TEXTS[vyber - 1].split())
        stat["lower"] = sum(word.islower() for word in TEXTS[vyber - 1].split())
        stat["num_str"] = sum(word.isdigit() for word in TEXTS[vyber - 1].split())
        stat["sumec"] = sum(int(word) for word in TEXTS[vyber - 1].split() if word.isdigit())
    
    for word in TEXTS[vyber - 1].split():
        if len(word) in graf.keys():
            graf[len(word)] += 1
        else:
            graf[len(word)] = 1

    graf = dict(sorted(graf.items()))

    print(
        f"There are: {stat['total']} words in the selected text.\n"
        f"There are: {stat['title']} titlecase words.\n"
        f"There are: {stat['upper']} uppercase words.\n"
        f"There are: {stat['lower']} lowercase words.\n"
        f"There are: {stat['num_str']} numeric strings.\n"
        f"The sum of all the numbers is {stat['sumec']}.\n"
        f"{carky}"
    )

    print(f"LEN|{' '}OCCURENCES{' ' * 3}|NR.\n{carky}")

    max_key_len = max(len(str(key)) for key in graf)
    max_val_len = max(len(str(val)) for val in graf.values())
    max_bar_len = max(graf.values())

    for key, value in graf.items():
        bar = '*' * value
        odstup = ' ' * (max_bar_len - value + 1)
        print(f"{str(key).rjust(max_key_len)} | {bar}{odstup} |{str(value).rjust(max_val_len)}")
else:
    print(f"username: {jmeno}\npassword: {heslo}\nUnregistered user, terminating the program.")
    exit()
