import matplotlib.pyplot as plt
import tkinter as tk
from tkcalendar import DateEntry
import variable
import search_date
from tkinter import messagebox
import search_expense

class PaymentMethodShow:
    def __init__(self) -> None:
        """this class shows a diagram for person in period of time"""
        self.win = tk.Tk()
        self.win.title('show diagram')
        self.win.geometry('300x70')

    def translate_time(self, date) -> variable.Date:
        """check if the date exist if not make it and return date object"""
        year, month, day = date.split('/')
        year, month, day = int(year), int(month), int(day)
        date = variable.Date(year, month, day)
        sch = search_date.SearchDate()
        sch.by_date(date, date)
        temp = sch.run()
        if len(temp) == 0:
            date.add_to_database()
            return date
        return temp[0]
    
    def read_text(self) -> list:
        """read all tests and return list of them"""
        inp = []
        inp.append(self.date_from.get())
        inp.append(self.date_to.get())
        return inp
    
    def reset(self) -> None:
        """clean all Texts"""
        self.date_to._set_text(self.date_to._date.strftime(''))
        self.date_from._set_text(self.date_from._date.strftime(''))

    def data_filter(self) -> list:
        """check if data are correct  and return which text are filled """
        data = self.read_text()
        flag = [0 for _ in range(2)]
        for i in range(len(data)):
            if data[i] != '':
                flag[i] = 1

        if flag[0]:
            try:
                data[0] = self.translate_time(data[0])
            except:
                messagebox.showerror('date Error', 'the date is not correct')
                return [],[]
        
        if flag[1]:
            try:
                data[1] = self.translate_time(data[1])
            except:
                messagebox.showerror('date Error', 'the date is not correct')
                return [],[]

        return data, flag

    def search(self) -> list:
        """return expenses that are in the time period"""
        data, flag = self.data_filter()

        if flag[0] and flag[1]:
            days = search_date.SearchDate()
            days.by_date(data[0], data[1])
            days = days.run()

        elif flag[0]:
            days = search_date.SearchDate()
            days.by_date(date_down=data[0])
            days = days.run()

        elif flag[1]:
            days = search_date.SearchDate()
            days.by_date(date_up=data[1])
            days = days.run()

        sch = search_expense.SearchExpense()
        sch.by_date(days)

        return sch.run()

    def show_button(self) -> None:
        """work when client push show button"""
        payments = dict()
        for i in self.search():
            i: variable.Expense
            payment = i.payment_method.name
            if payment not in payments:
                payments[payment] = i.amount
            else:
                payments[payment] += i.amount
        self.reset()
        plt.bar(payments.keys(), payments.values())
        plt.show()

                
    def make_widgets(self) -> None:
        """make widgets"""
        x = 0.14
        y = 0.18
        self.date_from=DateEntry(self.win,selectmode='day',height=1,width=10, date_pattern='yyyy/mm/dd')
        self.date_from.configure(validate='none')
        self.date_from._set_text(self.date_from._date.strftime(''))
        self.date_from.place(relx=x, rely=y, anchor = 'w')

        tk.Label(self.win, text='to: ').place(relx=x+0.375, rely=y, anchor = 'center')
        
        self.date_to=DateEntry(self.win,selectmode='day',height=1,width=10, date_pattern='yyyy/mm/dd')
        self.date_to.configure(validate='none')
        self.date_to._set_text(self.date_to._date.strftime(''))
        self.date_to.place(relx=x+0.45, rely=y, anchor = 'w')

        exit_ = tk.Button(self.win, text='Exit', command=self.win.destroy) 
        show_ = tk.Button(self.win, text='Show', command=self.show_button) 

        show_.place(relx=0.5, rely=0.5)
        exit_.place(relx=0.4, rely=0.5)

    def run(self)->None:
        """run the window"""
        self.make_widgets()  
        tk.mainloop()


if __name__ == "__main__":
    dig = PaymentMethodShow()
    dig.run()
