import tkinter
from tkinter import *

ROOT_WIDTH, ROOT_HEIGHT = (600, 600)
LEVEL_SET = {'초급': (9, 9, 10), '중급': (16, 16, 40), '고급': (16, 30, 99)}  # (width, height, mine)

width, height, mine = LEVEL_SET['초급']

root = Tk()
root.title('지뢰찾기')
root.geometry(f'{ROOT_WIDTH}x{ROOT_HEIGHT}')
root.resizable(False, False)

# main game frame.
game_frame = Frame(root, width=int(ROOT_WIDTH * 0.8), height=int(ROOT_HEIGHT * 0.8))
game_frame.pack(pady=30)


def say(event, r, c):
    print(r, c)


# button
# buttons = [[None] * width for _ in range(height)]
# for row in range(height):
#     for col in range(width):
btn_frame = tkinter.Frame(game_frame, background='black', width=100, height=100, padx=0, pady=0, relief='sunken', bd=1)
btn_frame.pack_propagate(0)
btn_frame.pack()
btn_frame_1 = tkinter.Frame(game_frame, background='black', width=100, height=100)
btn_frame_1.pack()
btn = tkinter.Button(btn_frame)
btn.pack(fill=tkinter.BOTH, expand=tkinter.YES)
# btn.bind('<Button-1>', lambda event, r=0, c=0: say(event, r, c))

# btn_2 = Button(game_frame)
# btn_2.place(x=10 + 90, y=10, width=100, height=100)

        # buttons[row][col] = btn

# for row in range(height):
#     btn_frame = Frame(game_frame, background='black')
#     for col in range(width):
#         btn = Button(btn_frame)
#         btn.place(width=100, height=100)
#     btn_frame.pack()




# flag frame.
# frame2 = Frame()

root.mainloop()