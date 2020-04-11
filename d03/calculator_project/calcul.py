#!/usr/bin/env python3
from tkinter import *
import my_arithmetic
import re

window = Tk()
calc_input = ""

def input_key(value):
    global calc_input
    calc_input += value
    calc_input_text.set(calc_input)
    print(calc_input)

def clear():
    global calc_input
    calc_input = ""
    calc_input_text.set(calc_input)
    print(calc_input)

def merger(to_merge, formated, pos):
    print("merging", formated, "with", to_merge,"on position", pos-1)
    formated.pop(pos+1)
    formated.pop(pos)
    formated[pos-1] = to_merge
    return formated

def paranthese_merger(para_result, formated, start, end):
    while end > start:
        formated.pop(end)
        end-=1
    formated[start] = para_result[0]
    return formated

def get_multiply(formated, pos):
    nbrs = [formated[pos-1], formated[pos+1]]
    print("numbers to multiply :",nbrs)
    op = my_arithmetic.multiply(nbrs)
    to_merge = str(op)
    print("result added to a list to be concatenated to trimmed original list :", to_merge)
    merged = merger(to_merge, formated, pos)
    print("concatenated the two list, here it is before sending it back to priority", merged)
    return merged

def get_division(formated, pos):
    nbrs = [formated[pos-1], formated[pos+1]]
    print("numbers to divide :",nbrs)
    op = my_arithmetic.division(nbrs)
    to_merge = str(op)
    print("result added to a list to be concatenated to trimmed original list :", to_merge)
    merged = merger(to_merge, formated, pos)
    print("concatenated the two list, here it is before sending it back to priority", merged)
    return merged

def get_addition(formated, pos):
    nbrs = [formated[pos-1], formated[pos+1]]
    print("numbers to add :",nbrs)
    op = my_arithmetic.add(nbrs)
    to_merge = str(op)
    print("result added to a list to be concatenated to trimmed original list :", to_merge)
    merged = merger(to_merge, formated, pos)
    print("concatenated the two list, here it is before sending it back to priority", merged)
    return merged

def get_substraction(formated, pos):
    nbrs = [formated[pos-1], formated[pos+1]]
    print("numbers to substract :",nbrs)
    op = my_arithmetic.subtract(nbrs)
    to_merge = str(op)
    print("result added to a list to be concatenated to trimmed original list :", to_merge)
    merged = merger(to_merge, formated, pos)
    print("concatenated the two list, here it is before sending it back to priority", merged)
    return merged

def listRightIndex(alist, value):
    return len(alist) - alist[-1::-1].index(value) -1

def priority(formated):
    print("priority received this list :", formated)
    if "(" in formated and ")" in formated:
        start = formated.index("(")
        print("start at", formated[start], "index is", start)
        end = listRightIndex(formated, ")")
        print("end at", formated[end], "index is", end)
        print("getting this list from the paranthese",formated[start+1:end])
        in_para = formated[start+1:end]
        para_result = priority(in_para)
        formated = paranthese_merger(para_result, formated, start, end)
        print("after paranthese_merger formated looks like", formated)
    if "*" in formated and "/" in formated:
        pos_multi = formated.index("*")
        pos_div = formated.index("/")
        if pos_div > pos_multi: # multiplication is first
            print("going to multiply this", formated,"with the element on position", pos_multi)
            merged = get_multiply(formated, pos_multi)
            print("in second if of priority, did a multi, result is :",merged)
            formated = priority(merged)    
        else: #division is first
            print("going to divide this", formated,"with the element on position", pos_div)
            merged = get_division(formated, pos_div)
            print("in first else of priority, did a division, result is :",merged)
            formated = priority(merged)
    if "*" in formated:
        pos_multi = formated.index("*")
        print("going to multiply this", formated,"with the element on position", pos_multi)
        merged = get_multiply(formated, pos_multi)
        print("in third if of priority, did a multi, result is :",merged)
        formated = priority(merged)
    if "/" in formated:
        pos_div = formated.index("/")
        print("going to divide this", formated,"with the element on position", pos_div)
        merged = get_division(formated, pos_div)
        print("in fourth if of priority, did a division, result is :",merged)
        formated = priority(merged)
    if "*" in formated and "/" in formated:
        pos_add = formated.index("+")
        pos_sub = formated.index("-")
        if pos_sub > pos_add: # addition is first
            print("going to add this", formated,"with the element on position", pos_add)
            merged = get_addition(formated, pos_add)
            print("in second if of priority, did a addition, result is :",merged)
            formated = priority(merged)    
        else: #substraction is first
            print("going to substract this", formated,"with the element on position", pos_sub)
            merged = get_substraction(formated, pos_sub)
            print("in first else of priority, did a substraction, result is :",merged)
            formated = priority(merged)
    if "+" in formated:
        pos_add = formated.index("+")
        print("going to add this", formated,"with the element on position", pos_add)
        merged = get_addition(formated, pos_add)
        print("in second if of priority, did a addition, result is :",merged)
        formated = priority(merged) 
    if "-" in formated:
        pos_sub = formated.index("-")
        print("going to substract this", formated,"with the element on position", pos_sub)
        merged = get_substraction(formated, pos_sub)
        print("in first else of priority, did a substraction, result is :",merged)
        formated = priority(merged)
    result = formated   
    return result

def check_for_neg_nbr(formated):
    print("in check_for_neg_nbr received", formated)
    if "-" not in formated:
        return formated
    if formated[0] == "-":
        formated.pop(0)
        formated[0]= "-"+formated[0]
    pos = formated.index("-")
    if formated[pos+1] == "-":
        formated[pos+1] = formated[pos+1]+formated[pos+2]
        formated.pop(pos+2)
        formated = check_for_neg_nbr(formated)
    check_against = ["(","+", "*", "/"]
    if formated[pos-1] in check_against:
        formated.pop(pos)
        formated[pos] ="-"+formated[pos]
        formated = check_for_neg_nbr(formated)
    return formated

def formater(to_format):
    formated = re.split('(\W)', to_format)
    print("input formated ->",formated)
    formated[:] = [x for x in formated if x != ""]
    print("input formated and got rid of empty elements ->",formated)
    if "-" in formated:
        formated = check_for_neg_nbr(formated)
    if len(formated)%2 == 0:
        result = "ERROR"
    elif "(" in formated and ")" not in formated:
        result = "ERROR"
    elif ")" in formated and "(" not in formated:
        result = "ERROR"
    else:
        result = priority(formated)
    return result

def equal(*input):
    global calc_input
    result = 0

    result = formater(calc_input)
    if isinstance(result, list):
        result[:] = [x for x in result if x != "(" and x != ")"]  
    calc_input = ""
    calc_input_text.set(calc_input)
    result_text.set(result)
    print(result)

btn_params = {
    'padx': 16,
    'pady': 1,
    'bd': 4,
    'fg': 'white',
    'bg': '#666666',
    'font': ('arial', 18),
    'width': 2,
    'height': 2,
    'relief': 'flat',
    'activebackground': "#666666"
}
display_params = {
    'font' : ('arial', 36),
    'relief' :'flat',
    'bg' : '#666666', 
    'fg' : 'white', 
    'width' : 10, 
    'bd' : 4, 
    'justify' : 'right'
}
equal_params = {
    'padx': 16,
    'pady': 1,
    'bd': 5,
    'fg': 'white',
    'bg': '#9e5644',
    'font': ('arial', 18),
    'width': 7,
    'height': 2,
    'relief': 'flat',
    'activebackground': "#ff9980"
}


Button(window, **btn_params, text=" 0 ", command=lambda: input_key("0")).grid(row=7, column=0)
Button(window, **btn_params, text=" 1 ", command=lambda: input_key("1")).grid(row=6, column=0)
Button(window, **btn_params, text=" 2 ", command=lambda: input_key("2")).grid(row=6, column=1)
Button(window, **btn_params, text=" 3 ", command=lambda: input_key("3")).grid(row=6, column=2)
Button(window, **btn_params, text=" 4 ", command=lambda: input_key("4")).grid(row=5, column=0)
Button(window, **btn_params, text=" 5 ", command=lambda: input_key("5")).grid(row=5, column=1)
Button(window, **btn_params, text=" 6 ", command=lambda: input_key("6")).grid(row=5, column=2)
Button(window, **btn_params, text=" 7 ", command=lambda: input_key("7")).grid(row=4, column=0)
Button(window, **btn_params, text=" 8 ", command=lambda: input_key("8")).grid(row=4, column=1)
Button(window, **btn_params, text=" 9 ", command=lambda: input_key("9")).grid(row=4, column=2)
Button(window, **btn_params, text=" - ", command=lambda: input_key("-")).grid(row=6, column=3)
Button(window, **btn_params, text=" + ", command=lambda: input_key("+")).grid(row=5, column=3)
Button(window, **btn_params, text=" * ", command=lambda: input_key("*")).grid(row=4, column=3)
Button(window, **btn_params, text=" / ", command=lambda: input_key("/")).grid(row=3, column=3)
Button(window, **btn_params, text=" . ", command=lambda: input_key(".")).grid(row=7, column=1)
Button(window, **equal_params, text=" = ", command=lambda: equal()).grid(row=7, column=2, columnspan=2)
Button(window, **btn_params, text=" ( ", command=lambda: input_key("(")).grid(row=3, column=0)
Button(window, **btn_params, text=" ) ", command=lambda: input_key(")")).grid(row=3, column=1)
Button(window, **btn_params, text=" C ", command=lambda: clear()).grid(row=3, column=2)

calc_input_text = StringVar()
Label(window, **display_params, textvariable=calc_input_text).grid(row=1, columnspan=4)
result_text = StringVar()
Label(window, **display_params, textvariable=result_text).grid(row=2, columnspan=4)
window.resizable(False, False)
window.mainloop()