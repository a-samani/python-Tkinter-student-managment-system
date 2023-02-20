import ast
from person import Person
import matplotlib.pyplot as plt
import numpy as np

import tkinter as tk
from tkinter import ttk


def create_plot():
    axis = {}
    all_persons = []

    #opening the txt file too read data and build students
    f = open('dataBase.txt', 'r')

    data = f.readlines()

    if data == []:
        pass
        # show error message

    else:

        for i in data:
            if i != '\n':
                res = ast.literal_eval(i)
                prsn_number = res['number']
                prsn_name = res['name'].decode("utf-8")
                prsn_marriage = res['marriage'].decode("utf-8")
                prsn_semester = res['year']
                income_one = int(res['income_one'])
                income_two = int(res['income_two'])
                art = int(res['income_three'])
                all_persons.append(Person(prsn_number, prsn_name, prsn_semester, prsn_marriage, income_one, income_two, art))

    f.close()


    # select the semester and average to create the plot
    for prsn in all_persons:
        if prsn.get_semester() in axis.keys():
            axis[prsn.get_semester()] += int(prsn.get_average())
        else:
            axis[prsn.get_semester()] = int(prsn.get_average())

    x = np.array(list(axis.keys()))
    y = np.array(list(axis.values()))
    plt.bar(x, y)
    plt.show()


def plot():
    plot_page = tk.Tk()

    # configure the root window
    plot_page.geometry('300x300')
    plot_page.resizable(False, False)
    plot_page.title('plot')

    ttk.Button(plot_page, text='show plot', command=create_plot).pack()

    plot_page.mainloop()
