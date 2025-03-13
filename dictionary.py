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