# import translator as tr
# import dictionary as di
# t = tr.Translator()
#
#
# while(True):
#     print("-----------------------------------")
#     print(f"Translator Alien-Italian")
#     print("-----------------------------------")
#     t.printMenu()
#
#     t.loadDictionary("dictionary.txt")
#
#     txtIn = input()
#     # Add input control here!
#
#     if int(txtIn) == 1:
#         print(f"Ok, quale parola devo aggiungere?")
#         str = input()
#         parole = str.strip().split()
#         di.addWord(parole[0], parole[1])
#         print("[")
#         print("Aggiunta")
#
#     if int(txtIn) == 2:
#         pass
#     if int(txtIn) == 3:
#         pass
#     if int(txtIn) == 4:
#         break

import re

import translator as tr

t = tr.Translator()
t.loadDictionary("dictionary.txt")


while(True):
    print("-----------------------------------")
    print(f"Translator Alien-Italian")
    print("-----------------------------------")
    t.printMenu()

    txtIn = input()
    # Add input control here!
    if not txtIn.isdigit() or not (1 <= int(txtIn) <= 5):  #controllo che non è una stringa e sia compreso tra 1 e 5
        print("Errore: Inserisci un numero valido tra 1 e 5.")
        continue  # Torna al menu

    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere?")
        print()
        txtIn1 = input().lower()
        t.handleAdd(txtIn1)
        print("Aggiunta!")

    if int(txtIn) == 2:
        print("Cerca una traduzione")
        print()
        txtIn2 = input().lower()
        t.handleTranslate(txtIn2)

    if int(txtIn) == 3:
        print("Ok, quale parola devo cercare?")
        print()
        txtIn3 = input().lower()
        t.handleWildCard(txtIn3)

    if int(txtIn) == 4:
        print("Stampa dizionario:")
        print()
        t.stampaDizionario()

    if int(txtIn) == 5:
        break