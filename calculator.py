import tkinter as tk

root_width, root_height = 350, 500

root = tk.Tk()
root.title('Calculator')
root.geometry(f'{root_width}x{root_height}')

frame_1 = tk.Frame(root, width=root_width, height=70)
frame_1.pack(pady=40)  # 상하로 패딩.

frame_2 = tk.Frame(root, width=root_width, height=1000)
frame_2.pack(padx=10, pady=10)  # 상하좌우로 패딩.

calculation_entry = tk.Entry(frame_1, width=30)  # width의 단위는 픽셀이 아닌 글자 수.
calculation_entry.pack()
calculation_entry.insert(0, '0')

math = ''
f_num = int()


def button_clicked(num):
    current = calculation_entry.get()  # get(): Entry의 텍스트를 반환.
    calculation_entry.delete(0, tk.END  e)  # delete(start_index, end_index): start_index부터 end_index까지 삭제.
    calculation_entry.insert(0, str(current) + str(num))  # insert(index, string): index 위치에 string 추가.


def button_clear():
    calculation_entry.delete(0, tk.END)


def button_add():
    global math, f_num

    num_1 = calculation_entry.get()
    math = 'addition'
    f_num = int(num_1)
    calculation_entry.delete(0, tk.END)


def button_sub():
    global math, f_num

    num_1 = calculation_entry.get()
    math = 'subtraction'
    f_num = int(num_1)
    calculation_entry.delete(0, tk.END)


def button_mul():
    global math, f_num

    num_1 = calculation_entry.get()
    math = 'multiplication'
    f_num = int(num_1)
    calculation_entry.delete(0, tk.END)


def button_div():
    global math, f_num

    num_1 = calculation_entry.get()
    math = 'division'
    f_num = int(num_1)
    calculation_entry.delete(0, tk.END)


def button_equal():
    global f_num

    num_2 = calculation_entry.get()
    calculation_entry.delete(0, tk.END)

    if math == 'addition':
        calculation_entry.insert(0, str(f_num + int(num_2)))
    elif math == 'subtraction':
        calculation_entry.insert(0, str(f_num - int(num_2)))
    elif math == 'multiplication':
        calculation_entry.insert(0, str(f_num * int(num_2)))
    elif math == 'division':
        calculation_entry.insert(0, str(f_num / int(num_2)))


btn7 = tk.Button(frame_2, text='7', padx=10, pady=10, command=lambda: button_clicked(7))  # 입력값이 있으므로 lambda 사용.
btn7.grid(column=0, row=0)

btn8 = tk.Button(frame_2, text='8', padx=15, pady=10, command=lambda: button_clicked(8))
btn8.grid(column=1, row=0, padx=5, pady=5)

btn9 = tk.Button(frame_2, text='9', padx=15, pady=10, command=lambda: button_clicked(9))
btn9.grid(column=2, row=0, padx=5, pady=5)

btn4 = tk.Button(frame_2, text='4', padx=15, pady=10, command=lambda: button_clicked(4))
btn4.grid(column=0, row=1, padx=5, pady=5)

btn5 = tk.Button(frame_2, text='5', padx=15, pady=10, command=lambda: button_clicked(5))
btn5.grid(column=1, row=1, padx=5, pady=5)

btn6 = tk.Button(frame_2, text='6', padx=15, pady=10, command=lambda: button_clicked(6))
btn6.grid(column=2, row=1, padx=5, pady=5)

btn1 = tk.Button(frame_2, text='1', padx=15, pady=10, command=lambda: button_clicked(1))
btn1.grid(column=0, row=2, padx=5, pady=5)

btn2 = tk.Button(frame_2, text='2', padx=15, pady=10, command=lambda: button_clicked(2))
btn2.grid(column=1, row=2, padx=5, pady=5)

btn3 = tk.Button(frame_2, text='3', padx=15, pady=10, command=lambda: button_clicked(3))
btn3.grid(column=2, row=2, padx=5, pady=5)

btn_pm = tk.Button(frame_2, text='+/-', padx=5, pady=10, command=lambda: button_clicked('-'))
btn_pm.grid(column=0, row=3, padx=5, pady=5)

btn0 = tk.Button(frame_2, text='0', padx=15, pady=10, command=lambda: button_clicked(0))
btn0.grid(column=1, row=3, padx=5, pady=5)

btn_p = tk.Button(frame_2, text='.', padx=15, pady=10, command=lambda: button_clicked('.'))
btn_p.grid(column=2, row=3, padx=5, pady=5)

btn_mul = tk.Button(frame_2,text='X', padx=15, pady=10, command=button_mul, bg='orange')  # 입력값이 필요 없으므로 lambda 사용하지 않고 함수명만 입력.
btn_mul.grid(column=3, row=0, padx=5, pady=5)

btn_sub = tk.Button(frame_2,text='-', padx=15, pady=10, command=button_sub, bg='orange')
btn_sub.grid(column=3, row=1, padx=5, pady=5)

btn_add = tk.Button(frame_2, text='+', padx=15, pady=10, command=button_add, bg='orange')
btn_add.grid(column=3, row=2, padx=5, pady=5)

btn_div = tk.Button(frame_2, text='/', padx=15, pady=10, command=button_div, bg='orange')
btn_div.grid(column=3, row=3, padx=5, pady=5)

btn_c = tk.Button(frame_2, text='C', padx=15, pady=10, command=button_clear, bg='orange')
btn_c.grid(column=2, row=4, padx=5, pady=5)

btn_res = tk.Button(frame_2, text='=', padx=15, pady=10, command=button_equal, bg='orange')
btn_res.grid(column=3, row=4, padx=5, pady=5)

# btn3 = tk.Button(root, text='9')

root.mainloop()
