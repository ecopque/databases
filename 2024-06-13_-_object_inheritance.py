class PartyAnimal:
    
    def __init__(self, nam):
        self.x = 0
        self.name = nam
        print(self.name, 'constructed')
    
    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)


class FootballFan(PartyAnimal):
    def __init__(self, nam):
        super().__init__(nam)
        self.points = 0

    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, 'points', self.points)

s = PartyAnimal('Sally') #1:
s.party() #2:

j = FootballFan('Jim') #3:
j.party() #4:
j.touchdown() #5:
