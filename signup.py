import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo


def signup():
    def save_person():

        student = {'number': number.get(), 'name': name.get().encode("utf-8"),
                   'marriage': str(person_marriage.get()).encode("utf-8"),
                   'yaer': str(year.get()), 'income_one': int(income_one.get()), 'income_two': int(income_two.get()), 'income_three': int(income_three.get())}

        return student

    def save_info():

        details = save_person()
        if '' in details.values():
            showinfo(title='ناقص',message='لطفا تمامی موارد را نکمیل کنید')
        else:
            with open('dataBase.txt', 'a') as convert_file:
                convert_file.write(str(details))
                convert_file.write('\n')
            showinfo(title='ثبت', message='با موقثیت ثبت شد')
            signup_page.destroy()




    signup_page = tk.Tk()
    signup_page.geometry('400x500')
    signup_page.resizable(False, False)
    signup_page.title('person Management')

    # label frame
    person_label = ttk.LabelFrame(signup_page, text='ورود اطاعات')
    person_label.grid(column=0, row=0, padx=20, pady=20, sticky='NW')

    # info frame
    info_label = ttk.LabelFrame(person_label, text='مشخصات فردی')
    info_label.grid(column=0, row=0, sticky='NW')
    # student number
    ttk.Label(info_label, text='شماره پرسونلی : ').grid(row=0, pady='10')
    person_number = tk.StringVar()
    number = Entry(info_label, textvariable=person_number)
    number.grid(column=1, row=0, )

    # name
    ttk.Label(info_label, text='نام و نام خانوادگی : ').grid(row=1, pady='10')
    person_name = StringVar()
    name = Entry(info_label, textvariable=person_name)
    name.grid(column=1, row=1, )

    # marriage
    ttk.Label(info_label, text='وضعیت تعهل : ').grid(row=2, pady='10')

    person_marriage = StringVar(info_label, "1")

    # Dictionary to create multiple buttons
    values = {"مجرد": "1",
              "متعهل": "2",
              }

    for (text, value) in values.items():
        Radiobutton(info_label, text=text, variable=person_marriage,
                    value=text).grid(row=2, column=int(value))

    # year
    ttk.Label(info_label, text='سال کارکرد : ').grid(row=3, pady='10')
    person_year = tk.StringVar()
    year = Entry(info_label, textvariable=person_year)
    year.grid(column=1, row=3)

    # score frame
    score_label = ttk.LabelFrame(person_label, text='حقوق')
    score_label.grid(column=0, row=1, sticky='NW')

    # income_one
    ttk.Label(score_label, text='درآمد هفته اول : ').grid(row=0, pady='10')
    income_one = tk.StringVar()
    income_one = Entry(score_label, textvariable=income_one)
    income_one.grid(column=1, row=0)

    # income_two
    ttk.Label(score_label, text='درآمد هفته دوم : ').grid(row=1, pady='10')
    income_two = tk.IntVar()
    income_two = Entry(score_label, textvariable=income_two)
    income_two.grid(column=1, row=1)

    # income_three
    ttk.Label(score_label, text='درآمد هفته سوم : ').grid(row=2, pady='10')
    income_three = tk.IntVar()
    income_three = Entry(score_label, textvariable=income_three)
    income_three.grid(column=1, row=2)

    ttk.Button(person_label, text='ثبت', command=save_info).grid(column=0, row=3)

    signup_page.mainloop()
