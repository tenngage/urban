import tkinter as tk

def add():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())

    answer_entry.delete(0, "end")
    answer_entry.insert(0, num1 + num2)

def sub():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())

    answer_entry.delete(0, "end")
    answer_entry.insert(0, num1 - num2)

def mul():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())

    answer_entry.delete(0, "end")
    answer_entry.insert(0, num1 * num2)

def div():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())

    answer_entry.delete(0, "end")
    answer_entry.insert(0, num1 / num2)

window = tk.Tk()
window.title("Calculator")
window.geometry("350x350")
window.resizable(False, False)
button_add = tk.Button(window, text="+", height=2, width=2, command=add)
button_add.place(x=80, y=200)
button_sub = tk.Button(window, text="-", height=2, width=2, command=sub)
button_sub.place(x=130, y=200)
button_mul = tk.Button(window, text="*", height=2, width=2, command=mul)
button_mul.place(x=180, y=200)
button_div = tk.Button(window, text="/", height=2, width=2, command=div)
button_div.place(x=230, y=200)
number1_entry = tk.Entry(window, width=28)
number1_entry.place(x=75, y=100)
number2_entry = tk.Entry(window, width=28)
number2_entry.place(x=75, y=150)
answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=75, y=300)
number1 = tk.Label(window, text="Введите первое число: ")
number1.place(x=75, y=75)
number2 = tk.Label(window, text="Введите второе число: ")
number2.place(x=75, y=125)
number3 = tk.Label(window, text="Ответ: ")
number3.place(x=75, y=275)

window.mainloop()
