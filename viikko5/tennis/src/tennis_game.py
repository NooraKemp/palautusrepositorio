class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.score_strings = ["Love", "Fifteen", "Thirty", "Forty", "Advantage ", "Win for "]

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1
 
    def get_score(self):
        if self.player1_score == self.player2_score:
            if self.player1_score >= 4:
                score = "Deuce"
            else:
                score = (f"{self.score_strings[self.player1_score]}-All")

        elif max(self.player1_score, self.player2_score) >= 4:
            if self.player1_score > self.player2_score:
                winning_player = self.player1_name
            else :
                winning_player = self.player2_name
            score_difference = self.player1_score - self.player2_score
            if score_difference == 1 or score_difference == -1:
                score = (f"{self.score_strings[4]}{winning_player}")
            else:
                score = (f"{self.score_strings[5]}{winning_player}")  

        else: 
            score = (f"{self.score_strings[self.player1_score]}-{self.score_strings[self.player2_score]}")
                  
        return score