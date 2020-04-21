from enum import Enum
from random import shuffle

from .settings import FieldClassEnum, PlayerEnum
from .player import Player

FIELD = list(FieldClassEnum)

class Card:
    def __init__(self, field, value):
        self.field = field
        self.value = value

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return '{}.{}'.format(self.field.name, self.value)


class CardPile:
    def __init__(self, field):
        self.field = field
        self.stack = {
            player: [] for player in PlayerEnum
        }

    def throw_card(self, player, card):
        self.stack[PlayerEnum.TRASH].append(card)

    def append_card(self, player, card):
        if self._check_validity(player, card):
            self.stack[player].append(card)
        else:
            self._invalid_play()

    def _invalid_play(self):
        raise NotImplementedError('invalid play response not implemented')

    def _check_validity(self, player, card):
        if len(self.stack[player]) == 0:
            return 1
        top_value = self.stack[player][-1].value
        return top_value < card.value

    def __str__(self):
        format_string = '{} :: {}'
        string_per_player = []
        for player in PlayerEnum:
            card_string = ''
            for card in self.stack[player]:
                card_string += '{}, '.format(card.value)
            string_per_player.append(format_string.format(player.name, card_string))

        return '[{}]\n'.format(self.field.name) + '\n'.join(string_per_player)


class GameBoard:
    def __init__(self, id, player_white, player_black):
        self.id = id
        self.card_pile = {field: CardPile(field) for field in FIELD}

        self.white = player_white
        self.black = player_black
        self.white.register_game(self)
        self.black.register_game(self)

        self.deck = []
        for field in FIELD:
            self.deck.extend([Card(field, i) for i in range(2, 11)])
            self.deck.extend([Card(field, 0)]*3)
        shuffle(self.deck)

    def __str__(self):
        hr = '>' + '-'*60 + '<'
        id_str = '[GAME ID : {}]'.format(self.id)
        card_pile_str = []
        for field in FIELD:
            card_pile_str.append(str(self.card_pile[field]))

        player_str = []

        return "{}\n\n{}\n\n{}\n{}\n\n{}".format(
            id_str, '\n\n'.join(card_pile_str),hr, self.white, self.black)

    def print_deck(self):
        print(self.deck)
        print(len(self.deck))

    def draw(self):
        return self.deck.pop()

    def play_card(self, player_side, card):
        card_pile = self.card_pile[card.field]
        card_pile.append_card(player_side, card)

    def throw_card(self, player_side, card):
        card_pile = self.card_pile[card.field]
        card_pile.throw_card(player_side, card)

    def initiate_game(self):
        self.white.draw(num=8)
        self.black.draw(num=8)


if __name__ == '__main__':
    pass