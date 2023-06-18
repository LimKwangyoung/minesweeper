import random
import sys
import tkinter
from PIL import Image, ImageTk

SQUARE_SIZE = 40
X_PADDING = 20
Y_PADDING = 40

LEVEL_SET = {'초급': (9, 9, 10), '중급': (16, 16, 40), '고급': (30, 16, 99)}  # (width, height, mine)


class MineSweeper:
    def __init__(self, level: str, root: tkinter.Tk):
        self.width = LEVEL_SET[level][0]
        self.height = LEVEL_SET[level][1]
        self.mine = LEVEL_SET[level][2]
        self.flag = LEVEL_SET[level][2]

        # initial boards of size (width * height)
        self.board = [[0] * self.width for _ in range(self.height)]
        self.game_board = [[''] * self.width for _ in range(self.height)]

        # variable for win
        self.no_mine = 0

        # resize images
        resized_flag_img = Image.open('./flag.png').resize((int(SQUARE_SIZE * 0.6), int(SQUARE_SIZE * 0.6)))
        self.flag_img = ImageTk.PhotoImage(resized_flag_img)

        # GUI
        self.root = root
        self.root.title('지뢰 찾기')

        self.ROOT_WIDTH = self.width * SQUARE_SIZE + 3 * X_PADDING
        self.ROOT_HEIGHT = self.height * SQUARE_SIZE + 3 * Y_PADDING + SQUARE_SIZE
        self.root.geometry(f'{self.ROOT_WIDTH}x{self.ROOT_HEIGHT}')
        self.root.resizable(False, False)

        self.main_frame = tkinter.Frame(self.root, relief=tkinter.SUNKEN, bd=2)
        self.main_frame.pack(padx=X_PADDING, pady=(Y_PADDING, 0))

        self.flag_frame = tkinter.Frame(self.root, relief=tkinter.SUNKEN, bd=2)
        self.flag_frame.pack(side='left',
                             padx=int(1.5 * X_PADDING + SQUARE_SIZE), pady=(int(Y_PADDING / 2), Y_PADDING))
        self.flag_label_1 = tkinter.Label(self.flag_frame, image=self.flag_img)
        self.flag_label_1.pack(side=tkinter.LEFT)
        self.flag_label_2 = tkinter.Label(self.flag_frame, text=f'{self.flag}', font=('TkDefaultFont', 20), width=4)
        self.flag_label_2.pack(side=tkinter.LEFT)

        # buttons list
        self.buttons = [[None] * self.width for _ in range(self.height)]

    def set_mines(self) -> None:
        # set mines randomly
        mine_cnt = 0
        while mine_cnt < self.mine:
            row, col = random.randint(0, self.height - 1), random.randint(0, self.width - 1)
            if self.board[row][col] != '*':
                self.board[row][col] = '*'
                mine_cnt += 1

                # increase the number around a mine
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
                self.buttons[r][c]['state'] = tkinter.DISABLED
                return

            # the number around mines is 0
            self.no_mine += 1
            self.game_board[r][c] = '0'
            self.buttons[r][c]['text'] = ''
            self.buttons[r][c]['state'] = tkinter.DISABLED
            self.flag_label_2['text'] = f'{self.flag}'
            directions = ((r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
                          (r, c - 1), (r, c + 1),
                          (r + 1, c - 1), (r + 1, c), (r + 1, c + 1))
            for r, c in directions:
                if (0 <= r <= self.height - 1) and (0 <= c <= self.width - 1) and self.game_board[r][c] == '':
                    expand_board(r, c)

        # plant a flag
        if on_flag and self.flag > 0 and self.game_board[row][col] == '':
            self.flag -= 1
            self.game_board[row][col] = 'P'
            self.buttons[row][col]['image'] = self.flag_img
            self.buttons[row][col]['state'] = tkinter.ACTIVE
            self.flag_label_2['text'] = f'{self.flag}'
        # cancel a flag
        elif self.game_board[row][col] == 'P':
            self.flag += 1
            self.buttons[row][col]['text'] = self.game_board[row][col] = ''
            self.buttons[row][col]['image'] = None
            self.buttons[row][col]['state'] = tkinter.NORMAL
            self.flag_label_2['text'] = f'{self.flag}'
        # select a mine
        elif self.board[row][col] == '*':
            print('!!! GAME OVER !!!')
            sys.exit()
        # not select a mine
        elif self.game_board[row][col] == '':
            expand_board(row, col)

        # win
        if self.no_mine == self.width * self.height - self.mine:
            print('!!! WIN !!!')
            sys.exit()

    def play(self) -> None:
        self.set_mines()

        for row in range(self.height):
            for col in range(self.width):
                # each button frame
                btn_frame = tkinter.Frame(self.main_frame, width=SQUARE_SIZE, height=SQUARE_SIZE,
                                          relief=tkinter.RAISED, bd=1)
                btn_frame.pack_propagate(False)  # fix a frame size regardless of widgets
                btn_frame.grid(row=row, column=col)
                # button
                btn = tkinter.Button(btn_frame, text=f'{self.game_board[row][col]}')
                # btn.bind('<Button-1>', lambda event, r=row, c=col: self.on_click(r, c))
                btn.bind('<Button-1>', lambda event, r=row, c=col: self.on_click(r, c, on_flag=True))
                btn.pack(fill=tkinter.BOTH, expand=tkinter.YES)

                self.buttons[row][col] = btn


if __name__ == '__main__':
    window = tkinter.Tk()
    # game = MineSweeper(input('난이도를 입력하시오. (초급, 중급, 고급): '), window)
    game = MineSweeper('초급', window)
    game.play()
    window.mainloop()
