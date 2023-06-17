from tkinter import *

window_width, window_height = (600, 600)


LEVEL_SET = {'초급': (9, 9, 10), '중급': (16, 16, 40), '고급': (16, 30, 99)}  # (width, height, mine)

width, height, mine = LEVEL_SET['고급']

root = Tk()
root.title('지뢰찾기')
root.geometry(f'{window_width}x{window_height}')
# root.resizable(False, False)

# main game frame.
game_frame = Frame(root)
game_frame.pack()

btn_frame = Frame(game_frame)
btn_frame.pack(side='top')

btn = Button(btn_frame, text='12', bd=1, bg='black')
btn.place(width=10, height=10)
# btn_frame = Frame(game_frame, background='black', width=100, height=100)
# btn_frame.pack(side='left')

# for row in range(height):
#     btn_frame = Frame(game_frame, background='black')
#     for col in range(width):
#         btn = Button(btn_frame)
#         btn.place(width=100, height=100)
#     btn_frame.pack()




# flag frame.
# frame2 = Frame()

root.mainloop()