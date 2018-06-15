#!/usr/bin/python

from tkinter import *
from tkinter import ttk


main = Tk()
main.title('Form Filler 5000')
main.geometry('500x800')


# gives weight to the cells in the grid
rows = 0
while rows < 85:
    s = ttk.Style()
    s.theme_use('classic')
    main.rowconfigure(rows, weight=1)
    main.columnconfigure(rows, weight=1)
    rows += 1

# Defines and places the notebook widget
nb = ttk.Notebook(main)
nb.grid(row=0, column=0, columnspan=85, rowspan=85, sticky='NESW')

# Adds tab 1 of the notebook
page1 = ttk.Frame(nb)
nb.add(page1, text='Submit Request')

# Adds tab 2 of the notebook
page2 = ttk.Frame(nb)
nb.add(page2, text='Fix Details')


# Adds tab 2 of the notebook
page3 = ttk.Frame(nb)
nb.add(page3, text='Guide')

main.mainloop()
