class PartyAnimal:
    def __init__(self, z):
        self.x = 0
        self.name = z
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)

s = PartyAnimal('Sally') #1:
s.party() #1:
j = PartyAnimal('Jim') #1:

j.party() #1:
s.party() #1:
