#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    # Python 2.x
    from Tkinter import *
    from ttk import *
    from tkMessageBox import *
except ImportError:
    # Python 3.x
    from tkinter import *
    from tkinter.ttk import *
    from tkinter.messagebox import *

# Ver http://www.python-course.eu/tkinter_dialogs.php

dolar = 3.75

def cotizar(*args):
    try:
        guaranies.set(int(dolares.get())*dolar)
    except ValueError:
        showerror(title='Error', message='Sólo números arábigos, por favor.')
        dolares.set('')

ventana = Tk()
ventana.title("Dólares a Nuevos SolmPeruano")

marco = Frame(ventana, padding="10 10 10 10")
marco.grid(column=0, row=0, sticky=(N, W, E, S))

dolares = StringVar()
guaranies = StringVar()

entrada = Entry(marco, width=7, textvariable=dolares)
entrada.grid(column=2, row=1, sticky=(W, E))

Label(marco, textvariable=guaranies).grid(column=2, row=2, sticky=(W, E))
Button(marco, text="Cotizar", command=cotizar).grid(column=3, row=3, sticky=W)

Label(marco, text="dólares").grid(column=3, row=1, sticky=W)
Label(marco, text="equivale a").grid(column=1, row=2, sticky=E)
Label(marco, text="SOLES PERUANOS").grid(column=3, row=2, sticky=W)

#              1                  2                   3
#   -------------------------------------------------------------
# 1 |                   |     [entrada]     | dólares           |
#   -------------------------------------------------------------
# 2 |        equivale a |    {soles}    | gperuanos        |
#   -------------------------------------------------------------
# 3 |                   |                   | < Cotizar >       |
#   -------------------------------------------------------------

for hijo in marco.winfo_children(): hijo.grid_configure(padx=5, pady=5)

entrada.focus()

ventana.bind('<Return>', cotizar)
ventana.bind('<Escape>', lambda x: ventana.destroy())

ventana.mainloop()