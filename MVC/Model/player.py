class Player:
    def __init__(self, play_side, id):
        self.play_side = play_side
        self.id = id
        self.hand = []

    def register_game(self, gameboard):
        self.game = gameboard

    def draw(self, num=1):
        for i in range(num):
            self.hand.append(self.game.draw())
    
    def play_card(self, index):
        pop_card = self.hand.pop(index)
        self.game.play_card(self.play_side, pop_card)
        self.draw()
    
    def throw_card(self, index):
        pop_card = self.hand.pop(index)
        self.game.throw_card(self.play_side, pop_card)
        self.draw()

    def __str__(self):
        hand_str = ''
        for card in self.hand:
            hand_str += (str(card) + '  ')
        return '{}.{}\n\tHAND: {}'.format(self.play_side.name, self.id, hand_str)