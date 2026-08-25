class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(f"Employee Name: {self.name}, ID: {self.id}")

class sports_player:
    def __init__(self, team, sport):
        self.sport = sport
        self.team = team
    def display_sport(self):
        print(f"Sport: {self.sport}")

    def display(self):
        print(f"Team: {self.team}, Sport: {self.sport}")


class player(employee, sports_player):
    def __init__(self, name, id, team, sport):
        employee.__init__(self, name, id)
        sports_player.__init__(self, team, sport)

    def display_sport(self):
        print(f"Sport: {self.sport}, Team: {self.team}")

    


A= player("John Doe", 123, "Warriors", "Basketball")
A.display()
A.display_sport()
