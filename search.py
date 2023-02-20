import ast
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from person import Person


def search():
    all_persons = []
    f = open('dataBase.txt', 'r')


    # open the txt file and read data from it to make persons
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
                all_persons.append(Person(prsn_number, prsn_name, prsn_year, prsn_marriage, income_one, income_two, income_three))

    f.close()

    # create tk page
    search = tk.Tk()
    search.geometry('1200x720')
    search.resizable(False, False)
    search.title('search')


# function to searcg by number
    def search_by_number(number):
        global no_res
        no_res = True
        found = []
        if not number:
            showinfo(title='هشدار', message='عددی وارد کنید')
        else:

            for prsn in all_persons:
                if number in prsn.get_person_number():
                    found.append(prsn)

                    no_res = False
            if no_res == True:
                showinfo(title='هشدار', message='نتیجه ای پیدا نشد')
            else:
                for prsn in found:
                    frame = ttk.Frame(result_label)
                    frame['borderwidth'] = 20
                    frame.pack(anchor=tk.E)
                    res = str(
                        ' شماره :' + prsn.get_person_number()) + '\t' + 'نام :' + prsn.get_name() + '\t' + 'سال کارکرد :' + str(
                        prsn.get_semester()) + '\t' + 'تعهل :' + prsn.get_marriage() + '\t' + 'معدل :' + str(
                        prsn.get_average()) + '\t' + 'درآمد هفته اول :' + str(
                        prsn.get_income_one()) + '\t' + 'درآمد هفته دوم :' + str(prsn.get_income_two()) + '\t' + 'درآمد هفته سوم :' + str(
                        prsn.get_income_three())
                    ttk.Label(frame, text=res).pack(anchor=tk.E)
#function to searcg by name
    def search_by_name(name):
        global no_res
        no_res = True
        found = []
        if not name:
            showinfo(title='هشدار', message='نامی وارد کنید')
        else:
            for prsn in all_persons:
                if name in prsn.get_name():
                    found.append(prsn)

                    no_res = False
            if no_res == True:
                showinfo(title='هشدار', message='نتیجه ای پیدا نشد')
            else:
                for prsn in found:
                    frame = ttk.Frame(result_label)
                    frame['borderwidth'] = 20
                    frame.pack(anchor=tk.E)
                    res = str(
                        ' شماره :' + prsn.get_person_number()) + '\t' + 'نام :' + prsn.get_name() + '\t' + 'سال کارکرد :' + str(
                        prsn.get_semester()) + '\t' + 'تعهل :' + prsn.get_marriage() + '\t' + 'معدل :' + str(
                        prsn.get_average()) + '\t' + 'درآمد هفته اول :' + str(
                        prsn.get_income_one()) + '\t' + 'درآمد هفته دوم :' + str(prsn.get_income_two()) + '\t' + 'درآمد هفته سوم :' + str(
                        prsn.get_income_three())
                    ttk.Label(frame, text=res).pack(anchor=tk.E)

    # label frame

    # showing the result

    search_label = ttk.LabelFrame(search, text='ورود اطاعات')
    search.geometry('1200x720')
    search_label.pack(fill='x')

    number_label = ttk.LabelFrame(search_label, text='بر اساس شماره')
    number_label.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True, )
    ttk.Label(number_label, text='شماره را وارد کنید').pack(anchor=tk.E)
    number = tk.StringVar()
    inputnumber = ttk.Entry(number_label, textvariable=number)
    inputnumber.pack(anchor=tk.E)
    ttk.Button(number_label, text='جست و جو', command=lambda: search_by_number(inputnumber.get())).pack()

    name_label = ttk.LabelFrame(search_label, text='بر اساس نام')
    name_label.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True, )
    ttk.Label(name_label, text='نام را وارد کنید').pack(anchor=tk.E)
    name = tk.StringVar()
    inputname =ttk.Entry(name_label, textvariable=name)
    inputname.pack(anchor=tk.E)
    ttk.Button(name_label, text='جست و جو', command=lambda: search_by_name(inputname.get())).pack()
    result_label = ttk.LabelFrame(search_label, text='نتیجه')
    result_label.pack(anchor=tk.E)

    search.mainloop()
