import random
import sys

LEVEL_SET = {'초급': (9, 9, 10), '중급': (16, 16, 40), '고급': (30, 16, 99)}  # (width, height, mine)


class MineSweeper:
    def __init__(self, level):
        self.width = LEVEL_SET[level][0]
        self.height = LEVEL_SET[level][1]
        self.mine = LEVEL_SET[level][2]
        self.flag = LEVEL_SET[level][2]

        # create initial boards of size (width * height).
        self.board = [[0] * self.width for _ in range(self.height)]
        self.game_board = [['.'] * self.width for _ in range(self.height)]

        # variable for win.
        self.no_mine = 0

    def set_mines(self) -> None:
        # set mines randomly.
        mine_cnt = 0
        while mine_cnt < self.mine:
            row, col = random.randint(0, self.height - 1), random.randint(0, self.width - 1)
            if self.board[row][col] != '*':
                self.board[row][col] = '*'
                mine_cnt += 1

                # increase the number around a mine.
                directions = ((row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                              (row, col - 1), (row, col + 1),
                              (row + 1, col - 1), (row + 1, col), (row + 1, col + 1))
                for row, col in directions:
                    if (0 <= row <= self.height - 1) and (0 <= col <= self.width - 1) and self.board[row][col] != '*':
                        self.board[row][col] += 1

    def graphic(self) -> tuple:
        print('!!! 지뢰찾기 게임 !!!\n')
        print('   |  ' + '  '.join(str(i % 10) for i in range(1, self.width + 1)))
        print('------' + '--'.join('-' for _ in range(1, self.width + 1)))

        for row in range(self.height):
            print(f'{(row + 1) % 10}  |  ' + '  '.join(str(self.game_board[row][col]) for col in range(self.width)))
        print()
        print(f'깃발: {self.flag}')
        print()
        coord = input('원하는 타일의 행과 열을 입력하시오. (깃발은 F): ').split()

        if len(coord) == 2:
            row, col = coord
            on_flag = None
        elif len(coord) == 3:
            row, col, on_flag = coord

        return int(row) - 1, int(col) - 1, on_flag

    def find_mine(self, row: int, col: int, on_flag) -> None:
        def expand_board(r: int, c: int) -> None:
            if self.board[r][c] != 0:
                self.game_board[r][c] = self.board[r][c]
                self.no_mine += 1
                return

            # the number around mines is 0.
            self.game_board[r][c] = ' '
            self.no_mine += 1

            directions = ((r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
                          (r, c - 1), (r, c + 1),
                          (r + 1, c - 1), (r + 1, c), (r + 1, c + 1))
            for r, c in directions:
                if (0 <= r <= self.height - 1) and (0 <= c <= self.width - 1) and self.game_board[r][c] == '.':
                    expand_board(r, c)

        # plant a flag.
        if on_flag:
            if on_flag in ('F', 'f') and self.flag > 0 and self.game_board[row][col] == '.':
                self.game_board[row][col] = 'P'
                self.flag -= 1
        # cancel a flag.
        elif self.game_board[row][col] == 'P':
            self.game_board[row][col] = '.'
            self.flag += 1
        # select a mine
        elif self.board[row][col] == '*':
            print('!!! GAME OVER !!!')
            sys.exit()
        # not select a mine.
        elif self.game_board[row][col] == '.':
            expand_board(row, col)

    def play(self):
        self.set_mines()
        while True:
            if self.no_mine == self.width * self.height - self.mine:
                print('!!! WIN !!!')
                sys.exit()
            row, col, flag = self.graphic()
            self.find_mine(row, col, flag)


if __name__ == '__main__':
    print('!!! 지뢰찾기 게임 !!!\n')
    game = MineSweeper(input('난이도를 입력하시오. (초급, 중급, 고급): '))
    game.play()
