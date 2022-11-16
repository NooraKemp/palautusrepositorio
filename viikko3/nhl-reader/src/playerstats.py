from player import Player


class PlayerStats:

    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        data = self.reader.get_players()
        players = []

        for player_dict in data:
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['assists'],
                player_dict['goals'],
                player_dict['penalties'],
                player_dict['team'],
                player_dict['games']
            )
            if player.nationality == nationality:
               players.append(player)
        
        players.sort(key=lambda player: player.points, reverse=True)
        return  players