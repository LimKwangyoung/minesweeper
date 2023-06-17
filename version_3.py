from tkinter import *

ROOT_WIDTH, ROOT_HEIGHT = (600, 600)
LEVEL_SET = {'초급': (9, 9, 10), '중급': (16, 16, 40), '고급': (16, 30, 99)}  # (width, height, mine)

width, height, mine = LEVEL_SET['초급']

root = Tk()
root.title('지뢰찾기')
root.geometry(f'{ROOT_WIDTH}x{ROOT_HEIGHT}')
root.resizable(False, False)

# main game frame.
game_frame = Frame(root, width=int(ROOT_WIDTH * 0.8), height=int(ROOT_HEIGHT * 0.8), background='black')
game_frame.pack(pady=30)


def say(event, r, c):
    print(r, c)


# button
# buttons = [[None] * width for _ in range(height)]
for row in range(height):
    for col in range(width):
        btn = Button(game_frame, padx=2, pady=2)
        btn.bind('<Button-1>', lambda event, r=row, c=col: say(event, r, c))
        btn.grid(column=row, row=col)

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