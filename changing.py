import tkinter as tk
from tkinter import *
from tkinter import ttk
import ast
from tkinter.messagebox import showinfo
from person import Person


def changing():
    index = 0
    all_person = []
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
                prsn_year = res['year']
                income_one = res['income_one']
                income_two = res['income_two']
                income_three = res['income_three']
                all_person.append(Person(prsn_number, prsn_name, prsn_year, prsn_marriage, income_one, income_two, income_three))

    f.close()

    def change(prsn):
        person = prsn

        # label frame

        # info frame
        info_label = ttk.LabelFrame(person_label, text='مشخصات فردی')
        info_label.grid(column=0, row=0, sticky='NW')
        # number
        ttk.Label(info_label, text='شماره پرسونلی : ').grid(row=0, pady='10')
        person_name = tk.StringVar()
        number = Entry(info_label, textvariable=person_name)
        number.insert(0, person.get_person_number())
        number.grid(column=1, row=0, )

        # name
        ttk.Label(info_label, text='نام و نام خانوادگی : ').grid(row=1, pady='10')
        person_name = tk.StringVar()

        name = Entry(info_label, textvariable=person_name)
        name.insert(0, person.get_name())
        name.grid(column=1, row=1, )

        # marriage
        ttk.Label(info_label, text='وضعیت تعهل : ').grid(row=2, pady='10')

        person_marriage = StringVar(info_label, str(person.get_marriage()))

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
        person_year.set(person.get_semester())
        year = ttk.Entry(info_label, textvariable=person_year)
        year.insert(0, person.get_semester())
        year.grid(column=1, row=3)

        # score frame
        score_label = ttk.LabelFrame(person_label, text='حقوق')
        score_label.grid(column=0, row=1, sticky='NW')

        # income_one
        ttk.Label(score_label, text='درآمد هفته اول : ').grid(row=0, pady='10')
        income_one = tk.IntVar()
        income_one.set(person.get_income_one())
        input_income_one = Entry(score_label, textvariable=income_one)
        input_income_one.insert(0, person.get_income_one())
        input_income_one.grid(column=1, row=0)

        # income_two
        ttk.Label(score_label, text='درآمد هفته دوم : ').grid(row=1, pady='10')
        income_two = tk.IntVar()
        income_two.set(person.get_income_two())
        input_income_two = Entry(score_label, textvariable=income_two)
        input_income_two.insert(0, person.get_income_two())
        input_income_two.grid(column=1, row=1)

        # income_three
        ttk.Label(score_label, text='درآمد هفته سوم : ').grid(row=2, pady='10')
        income_three = tk.IntVar()
        income_three.set(person.get_income_three())
        input_income_three = Entry(score_label, textvariable=income_three)
        input_income_three.insert(0, person.get_income_three())
        input_income_three.grid(column=1, row=2)

        def save_changes():

            newprsn = Person(number.get(), name.get(), year.get(), person_marriage.get(), int(input_income_two.get()),
                            int(input_income_one.get()), int(input_income_three.get()))

            all_person[index] = newprsn

            file = open('dataBase.txt', 'w')

            for i in all_person:
                prsn_number = i.get_person_number()
                prsn_name = i.get_name().encode("utf-8")
                prsn_marriage = str(i.get_marriage()).encode("utf-8")
                prsn_year = i.get_semester()
                income_one = i.get_income_one()
                income_two = i.get_income_two()
                income_three = i.get_income_three()

                person_dict = {'number': prsn_number, 'name': prsn_name, 'year': prsn_year,
                                'marriage': prsn_marriage,
                                'income_one': income_one, 'income_two': income_two, 'income_three': income_three}

                file.write(str(person_dict))
                file.write('\n')
                file.close()
                showinfo(title='ثبت', message='با موقثیت ثبت شد')
                main_change.destroy()

        btn = ttk.Button(person_label, text='ثبت', command=save_changes).grid(column=0, row=3)

    def search_by_number(number):
        global no_res
        no_res = True

        if not number:
            showinfo(title='هشدار', message='مقداری وارد کنید')
        else:

            for prsn in all_person:
                if number == prsn.get_person_number():
                    global index
                    index = (all_person.index(prsn))
                    get_info_label.grid_forget()
                    return change(prsn)
                    no_res = False
            if no_res == True:
                showinfo(title='هشدار', message='نتیجه ای پیدا نشد')

    main_change = tk.Tk()
    main_change.geometry('400x500')
    main_change.resizable(False, False)
    main_change.title('updating')

    person_label = ttk.LabelFrame(main_change, text='ورود اطاعات')
    person_label.grid(column=0, row=0, padx=20, pady=20, sticky='NW')
    get_info_label = ttk.LabelFrame(person_label, )
    get_info_label.grid(column=0, row=0, padx=20, pady=20, sticky='NW')

    numer_label = ttk.Label(get_info_label, text='شماره را وارد کنید').grid(sticky=tk.E)
    number = tk.StringVar()
    my_entery = ttk.Entry(get_info_label, textvariable=number)
    my_entery.grid(sticky=tk.E)
    my_btn = ttk.Button(get_info_label, text='جست و جو', command=lambda: search_by_number(my_entery.get())).grid()

    #

    main_change.mainloop()
