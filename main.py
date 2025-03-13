import datetime

from dictionary import Dictionary

def printMenu():
    print("______________________________\n" +
          "      SpellChecker 101\n" +
          "______________________________\n " +
          "Seleziona la lingua desiderata\n"
          "1. Italiano\n" +
          "2. Inglese\n" +
          "3. Spagnolo\n" +
          "4. Exit\n" +
          "______________________________\n")

def toStringParole(array):
    risultato=""
    for i in array:
        risultato+=f"{i}\n"

    return risultato

def loadDictionary(filename):
    """
    :param self:
    :param path: nome del dizionario
    :return: oggetto dizionario, composto solo dalla lista di parole che lo compongono
    """
    with open(filename,'r') as file:
        dizionario= Dictionary(file.read().splitlines())
    return dizionario

def controlloOrtografico(testo,dizionario):
    """
    metodo per controllare le parole sbagliate nel testo
    :param testo:
    :param dizionario:
    :return:
    """
    #porto tutto in minuscolo e rimpiazzo segni particolari
    testo= sistemaTesto(testo)
    #per ogni parola confronto se è presente nel dizionario con contains, se non è presente la metto in un array con le parole sbagliate
    paroleTesto= testo.split() #array con le parole
    tic = datetime.datetime.now()
    paroleSbagliate= dizionario.controlloCorrispondenze(paroleTesto)
    toc = datetime.datetime.now()
    paroleSbagliateStringa=toStringParole(paroleSbagliate)

    risultato= f"Ci sono {len(paroleSbagliate)}:\n {paroleSbagliateStringa} e l'operazione è stata svolta in {toc-tic}"

    return risultato

def sistemaTesto(testo):
    #prima porto in minuscolo
    testo= testo.lower()
    #poi rimpiazzo segni di punteggiatura particolari
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        testo.replace(c, "")
    return testo

printMenu()

txtIn = input("Digita la tua preferenza qui:")

# Add input control here!


if int(txtIn) == 1:
    dizionario = loadDictionary("resources/Italian.txt")
    print("Inserisci la tua frase in Italiano\n")
    txtIn = input()
    controllo = controlloOrtografico(txtIn,dizionario)
    print("______________________________")
    print(controllo)
    print("______________________________")


elif int(txtIn) == 2:
    dizionario = loadDictionary("resources/English.txt")
    print("Inserisci la tua frase in Inglese\n")
    txtIn = input()
    controllo = controlloOrtografico(txtIn,dizionario)
    print("______________________________")
    print(controllo)
    print("______________________________")


elif int(txtIn) == 3:
    dizionario = loadDictionary("resources/Spanish.txt")
    print("Inserisci la tua frase in Spagnolo\n")
    txtIn = input()
    controllo = controlloOrtografico(txtIn, dizionario)
    print("______________________________")
    print(controllo)
    print("______________________________")



elif int(txtIn) == 4:
    print()


