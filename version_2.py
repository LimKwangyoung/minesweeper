import random
import sys
import tkinter

ROOT_WIDTH, ROOT_HEIGHT = 600, 600
LEVEL_SET = {'초급': (9, 9, 10), '중급': (16, 16, 40), '고급': (16, 30, 99)}  # (width, height, mine)


class MineSweeper:
    def __init__(self, level: str, root: tkinter.Tk):
        self.width = LEVEL_SET[level][0]
        self.height = LEVEL_SET[level][1]
        self.mine = LEVEL_SET[level][2]
        self.flag = LEVEL_SET[level][2]

        # create initial boards of size (width * height).
        self.board = [[0] * self.width for _ in range(self.height)]
        self.game_board = [[''] * self.width for _ in range(self.height)]

        # variable for win.
        self.no_mine = 0

        # GUI
        self.root = root
        self.root.title('지뢰 찾기')
        self.root.geometry(f'{ROOT_WIDTH}x{ROOT_HEIGHT}')
        self.root.resizable(False, False)

        self.main_frame = tkinter.Frame(self.root, width=ROOT_WIDTH, height=int(ROOT_HEIGHT * 0.7))
        self.main_frame.pack()

        self.flag_frame = tkinter.Frame(self.root, width=ROOT_WIDTH, height=100)
        self.flag_frame.pack()
        self.flag_label = tkinter.Label(self.flag_frame, text=f'깃발 수: {self.flag}')
        self.flag_label.pack()

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

    def on_click(self, row: int, col: int, on_flag=False) -> None:
        def expand_board(r: int, c: int) -> None:
            if self.board[r][c] != 0:
                self.no_mine += 1
                self.buttons[r][c]['text'] = self.game_board[r][c] = self.board[r][c]
                self.flag_label['text'] = f'깃발 수: {self.flag}'
                return

            # the number around mines is 0.
            self.no_mine += 1
            self.buttons[r][c]['text'] = self.game_board[r][c] = '0'
            self.flag_label['text'] = f'깃발 수: {self.flag}'
            directions = ((r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
                          (r, c - 1), (r, c + 1),
                          (r + 1, c - 1), (r + 1, c), (r + 1, c + 1))
            for r, c in directions:
                if (0 <= r <= self.height - 1) and (0 <= c <= self.width - 1) and self.game_board[r][c] == '':
                    expand_board(r, c)

        # plant a flag.
        if on_flag and self.flag > 0 and self.game_board[row][col] == '':
            self.game_board[row][col] = 'P'
            self.flag -= 1
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

        # win a game.
        if self.no_mine == self.width * self.height - self.mine:
            print('!!! WIN !!!')
            sys.exit()

    def play(self):
        self.set_mines()

        for row in range(self.height):
            for col in range(self.width):
                btn = tkinter.Button(self.main_frame, text=f'{self.game_board[row][col]}', padx=5, pady=5)
                btn.bind('<Button-1>', lambda event, r=row, c=col: self.on_click(r, c))
                btn.bind('<Button-3>', lambda event, r=row, c=col: self.on_click(r, c, on_flag=True))
                btn.grid(row=row, column=col)

                self.buttons[row][col] = btn


if __name__ == '__main__':
    window = tkinter.Tk()
    # game = MineSweeper(input('난이도를 입력하시오. (초급, 중급, 고급): '))
    game = MineSweeper('초급', window)
    game.play()
    window.mainloop()
