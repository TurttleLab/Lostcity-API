from .settings import PlayerEnum, FieldClassEnum
from .gameboard import Card, CardPile, GameBoard
from .player import Player

# card = Card(FieldClassEnum.LAVA, 3)
# card_stack = CardPile(FieldClassEnum.LAVA)
# card_stack.append_card(PlayerEnum.WHITE, card)

player_1 = Player(PlayerEnum.WHITE, '2t489j')
player_2 = Player(PlayerEnum.BLACK, '4xdok8')
game = GameBoard('osx020d', player_1, player_2)
# game.card_pile[FieldClassEnum.LAVA] = card_stack
print(game)
game.initiate_game()

while(1):
    print("\n\n[Command] p: print game / w : play white / b : play black / e : exit")
    keyboard_io = input('Type Command : ')
    print('\n\n\n')

    if keyboard_io == 'e':
        break
    elif keyboard_io == 'p':
        print(game)
    elif keyboard_io in ('w', 'b'):
        player = game.white if keyboard_io == 'w' else game.black
        print("[Command] p#: play card at # / t#: throw card at # / !!: print hand")
        player_input = input('Type White Command : ')
        if player_input[0] == 't':
            player.throw_card(int(player_input[1]))
        elif player_input[0] == 'p':
            player.play_card(int(player_input[1]))
        elif player_input == '!!':
            print(player)
    else:
        raise NotImplementedError('input not supported')



