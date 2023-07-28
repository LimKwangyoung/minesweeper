import random
import tkinter
from PIL import Image, ImageTk

SQUARE_SIZE = 40
X_PADDING = 20
Y_PADDING = 40

LEVEL_SET = {'초급': (9, 9, 10), '중급': (16, 16, 40), '고급': (30, 16, 99)}  # (width, height, mine)


class StartWindow:
    def __init__(self, root: tkinter.Tk):
        self.root = root
        self.root.title('지뢰 찾기')
        self.root.geometry('450x600')
        self.root.resizable(False, False)

        self.main_frame = tkinter.Frame(root)
        self.main_frame.pack(pady=90)

        self.level = str()

    def apply_level(self, level: str) -> None:
        self.level = level
        # close a window
        self.root.destroy()
        self.root.quit()

    def select_level(self) -> None:
        label = tkinter.Label(self.main_frame, text='지뢰 찾기', font=('TkDefaultFont', 50))
        label.pack()
        # beginner
        btn_1 = tkinter.Button(self.main_frame, text='초급', command=lambda: self.apply_level('초급'),
                               font=('TkDefaultFont', 30), width=6)
        btn_1.pack(pady=(90, 15))
        # intermediate
        btn_2 = tkinter.Button(self.main_frame, text='중급', command=lambda: self.apply_level('중급'),
                               font=('TkDefaultFont', 30), width=6)
        btn_2.pack(pady=15)
        # advanced
        btn_3 = tkinter.Button(self.main_frame, text='고급', command=lambda: self.apply_level('고급'),
                               font=('TkDefaultFont', 30), width=6)
        btn_3.pack(pady=15)


class MineSweeper:
    def __init__(self, root: tkinter.Tk, level: str):
        self.width = LEVEL_SET[level][0]
        self.height = LEVEL_SET[level][1]
        self.mine = LEVEL_SET[level][2]
        self.flag = LEVEL_SET[level][2]

        # initial boards of size (width * height)
        self.board = [[0] * self.width for _ in range(self.height)]
        self.game_board = [[''] * self.width for _ in range(self.height)]

        # variable for game clear
        self.no_mine = 0

        # resize images
        flag_img = Image.open('./flag.png').resize((int(SQUARE_SIZE * 0.6), int(SQUARE_SIZE * 0.6)))
        self.flag_img = ImageTk.PhotoImage(flag_img)

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
        self.flag_frame.pack(side=tkinter.LEFT, padx=int(self.ROOT_WIDTH * 0.1), pady=(0, Y_PADDING))
        self.flag_label_1 = tkinter.Label(self.flag_frame, image=self.flag_img)
        self.flag_label_1.pack(side=tkinter.LEFT)
        self.flag_label_2 = tkinter.Label(self.flag_frame, text=f'{self.flag}', font=('TkDefaultFont', 20), width=4)
        self.flag_label_2.pack(side=tkinter.LEFT)

        # buttons list
        self.buttons = [[None] * self.width for _ in range(self.height)]

    def set_mines(self, show_mines=False) -> None:
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

        if show_mines:
            for row in range(self.height):
                print(' '.join(map(str, self.board[row])))

    def game_clear_over(self, mode: str) -> None:
        def close_window(win: tkinter.Tk) -> None:
            win.destroy()
            win.quit()
            self.root.destroy()
            self.root.quit()

        window = tkinter.Tk()
        window.title('')
        window.geometry('400x300')
        window.resizable(False, False)

        label = tkinter.Label(window, text=mode, font=('TkDefaultFont', 30))
        label.pack(pady=45)
        btn = tkinter.Button(window, text='게임 종료', font=('TkDefaultFont', 25), width=8,
                             command=lambda: close_window(window))
        btn.pack()

        window.mainloop()

    def on_click(self, row: int, col: int, on_flag=False) -> None:
        def expand_board(r: int, c: int) -> None:
            if self.board[r][c] != 0:
                self.no_mine += 1
                self.game_board[r][c] = self.board[r][c]
                self.buttons[r][c].configure(text=self.game_board[r][c])
                return

            # the number around mines is 0
            self.no_mine += 1
            self.game_board[r][c] = '0'
            self.buttons[r][c].configure(text='', state=tkinter.DISABLED)
            directions = ((r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
                          (r, c - 1), (r, c + 1),
                          (r + 1, c - 1), (r + 1, c), (r + 1, c + 1))
            for r, c in directions:
                if (0 <= r <= self.height - 1) and (0 <= c <= self.width - 1) and self.game_board[r][c] == '':
                    expand_board(r, c)

        if on_flag:
            # plant a flag
            if self.flag > 0 and self.game_board[row][col] == '':
                self.flag -= 1
                self.game_board[row][col] = 'F'
                self.buttons[row][col].configure(image=self.flag_img, state=tkinter.ACTIVE)
                self.flag_label_2.configure(text=f'{self.flag}')
            # cancel a flag
            elif self.game_board[row][col] == 'F':
                self.flag += 1
                self.game_board[row][col] = ''
                self.buttons[row][col].configure(image='', text='', state=tkinter.NORMAL)
                self.flag_label_2.configure(text=f'{self.flag}')
        # game over
        elif self.board[row][col] == '*':
            self.game_clear_over('GAME OVER')
        # not select a mine
        elif self.game_board[row][col] == '':
            expand_board(row, col)

        # game clear
        if self.no_mine == self.width * self.height - self.mine:
            self.game_clear_over('GAME CLEAR')

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
                btn.bind('<Button-1>', lambda event, r=row, c=col: self.on_click(r, c))
                btn.bind('<Button-2>', lambda event, r=row, c=col: self.on_click(r, c, on_flag=True))
                btn.pack(fill=tkinter.BOTH, expand=tkinter.YES)

                self.buttons[row][col] = btn


if __name__ == '__main__':
    start_window = tkinter.Tk()
    start = StartWindow(start_window)
    start.select_level()
    start_window.mainloop()

    game_window = tkinter.Tk()
    game = MineSweeper(game_window, start.level)
    game.play()
    game_window.mainloop()
