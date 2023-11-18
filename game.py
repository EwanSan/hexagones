from diamond import Diamond

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        # self.inputs = {1: ['ABC', 'DEF']}
    
    def _guess(self, diamond, letters):
        self.score += diamond.guess(letters)


class Game:
    def __init__(
            self, nb_rounds=5, diamond_size='regular', start_max=5,
            first_player_name='Equipe 1', second_player_name='Equipe 2'
        ):
        self.nb_rounds = nb_rounds
        self.start_max = start_max
        self.diamond_size = diamond_size
        self.p1 = Player(first_player_name)
        self.p2 = Player(second_player_name)
        self.round = 1

    def _play_round(self, maximum):
        diamond = Diamond(self.diamond_size, minimum=1, maximum=maximum)
        diamond.print_number_matrix()
        diamond.print_letter_matrix()
        print(diamond.goal)
        self.p1._guess(diamond, 'ABC')
        self.p2._guess(diamond, 'ABC')
        # Ajouter une commande manuelle pour passer au prochain round
    
    def _play(self):
        while self.round <= self.nb_rounds:
            self._play_round()
            self.round += 1
