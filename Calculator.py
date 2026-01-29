from tkinter import *

expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def lbc():
    global expression
    expression += '('
    equation.set(expression)

def equal():
    global expression
    try:
        total = eval(expression)
        equation.set(total)
        expression = str(total)
    except:
        equation.set('Nonsense! Olodo!!!')
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

def inverse():
    global expression
    try:
        value = eval(expression)
        inv = 1 / value
        equation.set(inv)
        expression = str(inv)
    except:
        equation.set('Nonsense! Olodo!!!')
        expression = ""

def square():
    global expression
    try:
        value = eval(expression)
        rt = value ** 0.5
        equation.set(rt)
        expression = str(rt)
    except:
        equation.set('Nonsense! Olodo!!!')
        expression = ""

root = Tk()
root.title("Calculator")
root.geometry('320x500')
root.configure(background='black')

equation = StringVar()
expression_field = Entry(
    root,
    textvariable=equation,
    bg='black',
    fg='white',
    font="Cambria_Math 15 bold",
    justify='right'
)
expression_field.grid(columnspan=20, ipadx=45, ipady=65)

btn = dict(width=10, height=3, fg='white', bg='black', font="Comic_Sans_MS 9 bold")

Button(root, text='1', command=lambda: press(1), **btn).grid(row=26, column=0)
Button(root, text='2', command=lambda: press(2), **btn).grid(row=26, column=1)
Button(root, text='3', command=lambda: press(3), **btn).grid(row=26, column=2)

Button(root, text='4', command=lambda: press(4), **btn).grid(row=25, column=0)
Button(root, text='5', command=lambda: press(5), **btn).grid(row=25, column=1)
Button(root, text='6', command=lambda: press(6), **btn).grid(row=25, column=2)

Button(root, text='7', command=lambda: press(7), **btn).grid(row=24, column=0)
Button(root, text='8', command=lambda: press(8), **btn).grid(row=24, column=1)
Button(root, text='9', command=lambda: press(9), **btn).grid(row=24, column=2)

Button(root, text='0', command=lambda: press(0), **btn).grid(row=27, column=1)
Button(root, text='.', command=lambda: press('.'), **btn).grid(row=27, column=0)
Button(root, text='+/-', command=lambda: press('-'), **btn).grid(row=27, column=2)

Button(root, text='=', command=equal, **btn).grid(row=27, column=3)
Button(root, text='+', command=lambda: press('+'), **btn).grid(row=26, column=3)
Button(root, text='-', command=lambda: press('-'), **btn).grid(row=25, column=3)
Button(root, text='/', command=lambda: press('/'), **btn).grid(row=24, column=3)
Button(root, text='x', command=lambda: press('*'), **btn).grid(row=23, column=3)

Button(root, text='√x', command=square, **btn).grid(row=23, column=0)
Button(root, text='x^y', command=lambda: press('**'), **btn).grid(row=23, column=1)
Button(root, text='1/x', command=inverse, **btn).grid(row=23, column=2)

Button(root, text='clear', command=clear, **btn).grid(row=22, column=3)
Button(root, text='mod', command=lambda: press('%'), **btn).grid(row=22, column=0)
Button(root, text='(', command=lbc, **btn).grid(row=22, column=1)
Button(root, text=')', command=lambda: press(')'), **btn).grid(row=22, column=2)

root.mainloop()
