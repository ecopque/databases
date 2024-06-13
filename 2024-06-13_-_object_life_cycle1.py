class PartyAnimal:
    def __init__(self): #1:
        self.x = 0
        print('I am constructed')

    def party(self): #2:
        self.x = self.x + 1
        print('So far', self.x)

    def __del__(self): #4:
        print('I am destructed', self.x)

an = PartyAnimal()
an.party() #2:
an.party() #2:
an = 42 #3:
print('an contains', an)
