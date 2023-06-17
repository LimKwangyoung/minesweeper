import random
import sys
import tkinter

ROOT_WIDTH, ROOT_HEIGHT = 600, 600
LEVEL_SET = {'초급': (9, 9, 10), '중급': (16, 16, 40), '고급': (16, 30, 99)}  # (width, height, mine)


class MineSweeper:
    def __init__(self, level):
        self.width = LEVEL_SET[level][0]
        self.height = LEVEL_SET[level][1]
        self.mine = LEVEL_SET[level][2]
        self.flag = LEVEL_SET[level][2]

        # create initial boards of size (width * height).
        self.board = [[0] * self.width for _ in range(self.height)]
        self.game_board = [[''] * self.width for _ in range(self.height)]

        # variable for win.
        self.no_mine = 0

        # buttons
        self.buttons = [[None] * self.width for _ in range(self.height)]

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

    def find_mine(self, row: int, col: int, on_flag=False) -> None:
        def expand_board(r: int, c: int) -> None:
            if self.board[r][c] != 0:
                self.buttons[r][c]['text'] = self.game_board[r][c] = self.board[r][c]
                self.no_mine += 1
                return

            # the number around mines is 0.
            self.buttons[r][c]['text'] = self.game_board[r][c] = '0'
            self.no_mine += 1

            directions = ((r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
                          (r, c - 1), (r, c + 1),
                          (r + 1, c - 1), (r + 1, c), (r + 1, c + 1))
            for r, c in directions:
                if (0 <= r <= self.height - 1) and (0 <= c <= self.width - 1) and self.game_board[r][c] == '':
                    expand_board(r, c)

        # win a game.
        if self.no_mine == self.width * self.height - self.mine:
            print('!!! WIN !!!')
            sys.exit()

        # plant a flag.
        if on_flag:
            if self.flag > 0 and self.game_board[row][col] == '':
                self.game_board[row][col] = 'P'
                self.flag -= 1
            else:
                return
        # cancel a flag.
        elif self.game_board[row][col] == 'P':
            self.game_board[row][col] = ''
            self.flag += 1
        # select a mine.
        elif self.board[row][col] == '*':
            print('!!! GAME OVER !!!')
            sys.exit()
        # not select a mine.
        elif self.game_board[row][col] == '':
            expand_board(row, col)

    def play(self):
        self.set_mines()

        # GUI
        root = tkinter.Tk()
        root.title('지뢰 찾기')
        root.geometry(f'{ROOT_WIDTH}x{ROOT_HEIGHT}')
        root.resizable(False, False)

        main_frame = tkinter.Frame(root, width=ROOT_WIDTH, height=ROOT_HEIGHT)
        main_frame.pack()

        for row in range(self.height):
            for col in range(self.width):
                btn = tkinter.Button(main_frame, text=f'{self.game_board[row][col]}', padx=2, pady=2)
                btn.bind('<Button-1>', lambda event, r=row, c=col: self.find_mine(r, c))
                btn.bind('<Button-3>', lambda event, r=row, c=col: self.find_mine(r, c, on_flag=True))
                btn.grid(row=row, column=col)

                self.buttons[row][col] = btn

        root.mainloop()


if __name__ == '__main__':
    # game = MineSweeper(input('난이도를 입력하시오. (초급, 중급, 고급): '))
    game = MineSweeper('초급')
    game.play()
