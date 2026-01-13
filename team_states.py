class Teams:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

class Team1Server1(Teams):
    def __init__(self, team1: int, team2: int):
        super().__init__(team1, team2)
        self.team = 1
        self.server = 1

    def team1_scored(self):
        return Team1Server1(self.team1 + 1, self.team2)
    
    def team2_scored(self):
        return Team1Server2(self.team1, self.team2)

class Team1Server2(Teams):
    def __init__(self, team1: int, team2: int):
        super().__init__(team1, team2)
        self.team = 1
        self.server = 2

    def team1_scored(self):
        return Team1Server2(self.team1 + 1, self.team2)
    
    def team2_scored(self):
        return Team2Server1(self.team1, self.team2)
    
class Team2Server1(Teams):
    def __init__(self, team1: int, team2: int):
        super().__init__(team1, team2)
        self.team = 2
        self.server = 1

    def team1_scored(self):
        return Team2Server2(self.team1, self.team2)
    
    def team2_scored(self):
        return Team2Server1(self.team1, self.team2 + 1)
    
class Team2Server2(Teams):
    def __init__(self, team1: int, team2: int):
        super().__init__(team1, team2)
        self.team = 2
        self.server = 2
   
    def team1_scored(self):
        return Team1Server1(self.team1, self.team2)
    
    def team2_scored(self):
        return Team2Server2(self.team1, self.team2 + 1)
    
