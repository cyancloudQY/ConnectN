class Board:
    def __init__(self, notation, row, col, num_win):
        self.notation = notation
        self.row = row
        self.col = col
        self.num_win = num_win
        self.list = []
        for i in range(self.col):
            self.list.append([self.notation] * self.row)

    def __repr__(self):
        s = ''
        s += '\n  '
        for column in range(self.col):
            s += str(column) + ' '
        s += '\n'
        s += ''
        for i in range(self.row):
            s += str(i) + ' '
            for j in range(self.col):
                s += self.list[j][i] + ' '
            s += '\n'
        return s

    def play_in(self, row, column, piece):
        self.list[row][column] = piece

    def find_row(self, col):
        for i in range(self.row - 1, -1, -1):
            if self.list[col][i] == self.notation:
                return i

    def win_horizontal(self, piece, win):
        num = 1
        for i in range(self.row):
            for j in range(self.col):
                if j + 1 < self.col and self.list[j][i] == self.list[j + 1][i] == piece:
                    num += 1
                    if num >= win:
                        return True
                else:
                    num = 1

    def win_vertical(self, piece, win):
        num = 1
        for j in range(self.col):
            for i in range(self.row):
                if i + 1 < self.row and self.list[j][i] == self.list[j][i + 1] == piece:
                    num += 1
                    if num >= win:
                        return True
                else:
                    num = 1

    def win_diagonal1(self, piece, win):
        num = 1
        for i in range(self.row):
            for j in range(self.col):

                if i + num < self.row and j + 1 < self.col and self.list[j][i+num-1] == self.list[j+1][i + num] == piece:
                    num += 1
                    if num >= win:
                        return True
                else:
                    num = 1

    def win_diagonal2(self, piece, win):
        num = 1
        for i in range(self.row - 1, -1, -1):
            for j in range(self.col):

                if j + 1 < self.col and 0 <= i - num < self.row and self.list[j][i - num+1] == self.list[j + 1][i-num] == piece:
                    num += 1
                    if num >= win:
                        return True
                else:
                    num = 1




