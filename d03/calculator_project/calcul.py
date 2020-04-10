#!/usr/bin/env python3
from tkinter import *
import my_arithmetic

window = Tk()
calc_input = ""

def input_key(value):
    global calc_input
    calc_input += value
    calc_input_text.set(calc_input)
    print(calc_input)

def equal():
    global calc_input
    additions = calc_input.split("+")
    result = 0
    for value in additions:
        result += int(value)
    calc_input = ""
    calc_input_text.set(calc_input)
    result_text.set(result)
    print(result)


Button(window, text=" 0 ", command=lambda: input_key("0")).grid(row=6, column=0)
Button(window, text=" 1 ", command=lambda: input_key("1")).grid(row=5, column=0)
Button(window, text=" 2 ", command=lambda: input_key("2")).grid(row=5, column=1)
Button(window, text=" 3 ", command=lambda: input_key("3")).grid(row=5, column=2)
Button(window, text=" 4 ", command=lambda: input_key("4")).grid(row=4, column=0)
Button(window, text=" 5 ", command=lambda: input_key("5")).grid(row=4, column=1)
Button(window, text=" 6 ", command=lambda: input_key("6")).grid(row=4, column=2)
Button(window, text=" 7 ", command=lambda: input_key("7")).grid(row=3, column=0)
Button(window, text=" 8 ", command=lambda: input_key("8")).grid(row=3, column=1)
Button(window, text=" 9 ", command=lambda: input_key("9")).grid(row=3, column=2)
Button(window, text=" + ", command=lambda: input_key("+")).grid(row=5, column=3)
Button(window, text=" - ", command=lambda: input_key("-")).grid(row=6, column=3)
Button(window, text=" * ", command=lambda: input_key("*")).grid(row=4, column=3)
Button(window, text=" / ", command=lambda: input_key("/")).grid(row=3, column=3)
Button(window, text=" . ", command=lambda: input_key(".")).grid(row=6, column=1)
Button(window, text=" = ", command=lambda: equal()).grid(row=6, column=2)

calc_input_text = StringVar()
Label(window, textvariable=calc_input_text).grid(row=1, column=0)
result_text = StringVar()
Label(window, textvariable=result_text).grid(row=2, column=0)
window.mainloop()