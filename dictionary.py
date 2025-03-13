class Dictionary:
    def __init__(self,dict= []):
        self.dict= dict

    def printAll(self):
        pass

    def controlloCorrispondenze(self,paroleTesto):
        paroleSbagliate=[]
        for i in paroleTesto:
            if i not in self.dict:
                paroleSbagliate.append(i)
        return paroleSbagliate

    def controlloCorrispondenzeDicotomica(self,paroleTesto):
        """
        Controllo ortografico che parte dal centro e non dalla prima occorrenza
        :param paroleTesto:
        :return:
        """
        parole_errate = []

        for parola in paroleTesto:

            start=0 #indice partenza
            end =len(self.dict) - 1 #indicefine
            trovata = False  # Flag per indicare se la parola è stata trovata

            while start <= end: #partenza va sempre dopo fine
                mean = int((start + end) / 2)
                if parola == self.dict[mean]:
                    trovata = True  # La parola è presente
                    break
                elif parola > self.dict[mean]:
                    start = mean + 1
                else:
                    end = mean - 1 #start mi rimane invariato; end diventa l'elemento prima dell'elemento preso prima
                    #all'iterazione successiva abbiamo sempre una ricerca dicotomica

            if not trovata:  # Se la parola non è stata trovata, è errata
                parole_errate.append(parola)

        return parole_errate

