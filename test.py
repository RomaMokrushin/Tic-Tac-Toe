class TicTacToeBoard:
    def __init__(self):
        self.board = [['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-']]
        self.turn = 'X'
        self.flag_X = False
        self.flag_O = False
        self.flag_D = False

    def new_game(self):
        self.board = [['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-']]
        self.turn = 'X'
        self.flag_X = False
        self.flag_O = False
        self.flag_D = False

    def check_field(self):
        if self.flag_X:
            return 'X'
        elif self.flag_O:
            return '0'
        elif self.flag_D:
            return 'D'
        return None

    def make_move(self, row, col):
        check = set()
        if self.flag_X or self.flag_D or self.flag_O:
            return 'Игра уже завершена'
        if self.turn == 'X':
            if self.board[row - 1][col - 1] != '-':
                return f'Клетка {row}, {col} уже занята'
            self.board[row - 1][col - 1] = 'X'
            self.turn = '0'
        elif self.turn == '0':
            if self.board[row - 1][col - 1] != '-':
                return f'Клетка {row}, {col} уже занята'
            self.board[row - 1][col - 1] = '0'
            self.turn = 'X'
        for i in self.board:
            for j in i:
                check.add(j)
            if len(check) == 1:
                check = list(check)
                if check[0] == 'X':
                    self.flag_X = True
                    return 'Победил игрок X'
                if check[0] == '0':
                    self.flag_O = True
                    return 'Победил игрок 0'
            check = set()
        if self.board[0][0] == self.board[1][0] == self.board[2][0] == 'X':
            self.flag_X = True
            return 'Победил игрок X'
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] == '0':
            self.flag_O = True
            return 'Победил игрок 0'
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] == 'X':
            self.flag_X = True
            return 'Победил игрок X'
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] == '0':
            self.flag_O = True
            return 'Победил игрок 0'
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] == 'X':
            self.flag_X = True
            return 'Победил игрок X'
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] == '0':
            self.flag_O = True
            return 'Победил игрок 0'
        for i in self.board:
            for j in i:
                check.add(j)
        if len(check) == 1:
            self.flag_D = True
            return 'Ничья'
        check = set()
        check.add(self.board[0][0])
        check.add(self.board[1][1])
        check.add(self.board[2][2])
        if len(check) == 1:
            check = list(check)
            if check[0] == 'X':
                self.flag_X = True
                return 'Победил игрок X'
            if check[0] == '0':
                self.flag_O = True
                return 'Победил игрок 0'
        check = set()
        check.add(self.board[0][2])
        check.add(self.board[1][1])
        check.add(self.board[2][0])
        if len(check) == 1:
            check = list(check)
            if check[0] == 'X':
                self.flag_X = True
                return 'Победил игрок X'
            if check[0] == '0':
                self.flag_O = True
                return 'Победил игрок 0'
        return 'Продолжаем играть'

    def get_field(self):
        return self.board