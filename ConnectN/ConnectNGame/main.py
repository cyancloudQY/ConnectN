from ConnectNGame.src.read_from_confi import get_the_value
from ConnectNGame.src.board import Board
from ConnectNGame.src.player import Player
from ConnectNGame.src.game import Game

a = get_the_value()
place = Board(a[0], a[1], a[2], a[3])
players = Player(place.notation)
rule = Game(players.name1, players.name2)
print(place)

turn = 0
while True:
    if turn % 2 == 0:
        col = rule.player1_take_turn()
        row = place.find_row(col)
        place.play_in(col, row, players.piece1)
        print(place)
        if place.win_vertical(players.piece1, place.num_win) == True:
            print(players.name1, 'won the game!')
            break
        elif place.win_horizontal(players.piece1, place.num_win) == True:
            print(players.name1, 'won the game!')
            break
        elif place.win_diagonal1(players.piece1, place.num_win) == True:
            print(players.name1, 'won the game!')
            break
        elif place.win_diagonal2(players.piece1, place.num_win) == True:
            print(players.name1, 'won the game!')
            break



    else:
        col = rule.player2_take_turn()
        row = place.find_row(col)
        place.play_in(col, row, players.piece2)
        print(place)
        if place.win_vertical(players.piece2, place.num_win) == True:
            print(players.name2, 'won the game!')
            break
        elif place.win_horizontal(players.piece2, place.num_win) == True:
            print(players.name2, 'won the game!')
            break
        elif place.win_diagonal1(players.piece2, place.num_win) == True:
            print(players.name2, 'won the game!')
            break
        elif place.win_diagonal2(players.piece2, place.num_win) == True:
            print(players.name2, 'won the game!')
            break

    turn += 1


def main() -> None:
    ...  # program execution begins here


if __name__ == '__main__':
    main()
