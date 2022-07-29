class Game:
    def __init__(self,player1,player2):
        self.player1 = player1
        self.player2 = player2

    def player1_take_turn(self):
        while True:
            try:
                print(self.player1 + ', please enter the column you want to play in: ', end='')
                col = input()
                col = int(col)


            except:
                print(self.player1, 'column needs to be an integer.',col,'is not an integer.')
                continue

            else:
                break
                
        return col

    def player2_take_turn(self):
        while True:
            try:
                print(self.player2 + ', please enter the column you want to play in: ', end='')
                col = input()
                col = int(col)


            except:
                print(self.player2, 'column needs to be an integer.', col, 'is not an integer.')
                continue

            else:
                break

        return col






