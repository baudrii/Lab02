# from dictionary import Dictionary
#
# class Translator:
#
#     def __init__(self):
#         #self.dic
#         dizio=Dictionary()
#
#     def printMenu(self):
#         print(f"1. Aggiungi nuova parola")
#         print(f"2. Cerca una traduzione")
#         print(f"3. Cerca con wildcard")
#         print(f"4. Exit")
#
#     def loadDictionary(self, dict):
#         # dict is a string with the filename of the dictionary
#         #dizio = {}
#         with open(dict,"r") as file:
#             for line in file:
#                 word=line.strip().split()
#                 if len(word)==2:
#                     dizio[word[0]] = word[1]
#        # return print(dizionario)
#
#     def handleAdd(self, entry):
#         # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
#         pass
#
#     def handleTranslate(self, query):
#         # query is a string <parola_aliena>
#         pass
#
#     def handleWildCard(self,query):
#         # query is a string with a ? --> <par?la_aliena>
#         pass
#
import re


class Translator:

    def __init__(self):
        self.dizio = {}

    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        print(f"1. Aggiungi nuova parola")
        print(f"2. Cerca una traduzione")
        print(f"3. Cerca con wildcard")
        print(f"4. Stampa tutto il Dizionario")
        print(f"5. Exit")
        print("-----------------------------------")


    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary

        with open(dict,"r",encoding="utf-8") as file:
            for line in file:
             word=line.strip().split()
             if len(word)==2:
                 parola_aliena = word[0].lower()
                 traduzioni = word[1].lower().split()  # 🔹 MODIFICATO: Gestisce più traduzioni
                 self.dizio[parola_aliena] = traduzioni

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        print(entry)
        parola=entry.strip().split()
        #self.dizio[parola[0]] = parola[1]
        parola_aliena = parola[0].lower()
        traduzioni = parola[1:]  # Prendiamo tutte le parole successive come traduzioni

        # Se la parola aliena esiste già, aggiungiamo nuove traduzioni senza duplicati
        if parola_aliena in self.dizio:
            nuove_traduzioni = [t for t in traduzioni if t not in self.dizio[parola_aliena]]
            self.dizio[parola_aliena].extend(nuove_traduzioni)
        else:
            self.dizio[parola_aliena] = traduzioni


    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        return print(self.dizio[query])

    def handleWildCard(self, query):
        if query.count("?") != 1:
            print("Errore: È ammesso un solo '?' per parola.")
            return

            # Convertiamo '?' in '.' per creare l'espressione regolare
        pattern = query.replace("?", ".")

        # Creiamo l'espressione regolare per confrontare parole intere
        regex = re.compile(f"^{pattern}$")

        # Cerchiamo tutte le parole nel dizionario che corrispondono alla regex
        risultati = [parola for parola in self.dizio if regex.fullmatch(parola)]

        # Stampiamo i risultati
        if risultati:
            for parola in risultati:
                print(f"{self.dizio[parola]}")
        else:
            print("Nessuna parola corrispondente trovata.")




    def stampaDizionario(self):
        for parola, traduzioni in self.dizio.items():
            print(f"{parola} -> {', '.join(traduzioni)}")
