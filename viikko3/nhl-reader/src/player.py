class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
        self.points = self.assists + self.goals
    
    def __str__(self):
        return f"{self.name:20}{self.team:5}{self.goals} + {self.assists} = {self.points}"
