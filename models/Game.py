from models import Player


class Game:

    player_list = []

    def __init__(self, questions, question_timer, points_possible, players):
        self.questions = questions
        self.question_timer = question_timer
        self.points_possible = points_possible
        self.players = players
        self.create_players()

    def create_players(self):
        for i in range(self.players):
            # streak, points
            player = Player.Player(0, 0)
            self.player_list.append(player)
