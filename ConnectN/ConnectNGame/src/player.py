class Player(object):
    def __init__(self,boardpiece):
        while True:
            self.name1 = input('Player 1 enter your name: ')
            while self.name1 == '' or self.name1 == ' ':
                print('Your name cannot be the empty string or whitespace.')
                self.name1 = input('Player 1 enter your name: ')
                continue

            self.piece1 = input('Player 1 enter your piece: ')
            if self.piece1 == '' or self.piece1 == ' ':
                print('Your piece cannot be the empty string or whitespace.')
                continue

            elif len(self.piece1) > 1:
                print(self.piece1,'is not a single character. Your piece can only be a single character.')
                continue

            elif self.piece1 == boardpiece:
                print('Your piece cannot be the same as the blank character.')
                continue

            else:
                break

        while True:
            self.name2 = input('Player 2 enter your name: ')
            while self.name2 == '' or self.name2 == ' ':
                print('Your name cannot be the empty string or whitespace.')
                self.name2 = input('Player 2 enter your name: ')
                continue
            if self.name2 == self.name1:
                print('You cannot use qq for your name as someone else is already using it.')
                continue

            self.piece2 = input('Player 2 enter your piece: ')
            if self.piece2 == '' or self.piece2 == ' ':
                print('Your piece cannot be the empty string or whitespace.')
                continue

            elif len(self.piece2) > 1:
                print(self.piece2, 'is not a single character. Your piece can only be a single character.')
                continue

            elif self.piece2 == self.piece1:
                print('You cannot use',self.piece2, 'for your piece as',self.name1,'is already using it.')

            elif self.piece1 == boardpiece:
                print('Your piece cannot be the same as the blank character.')
                continue

            else:
                break






