import tkinter as tk
from tkcalendar import DateEntry
import add_or_remove_payment_method
import add_or_remove_place
import add_or_remove_person_display
from tkinter import messagebox
import search_date
import search_persons
import search_place
import search_payment_methods
import variable
import search_expense
import displayoutput

class AddRemoveExpense:
    def __init__(self) -> None:
        """this class make and manage add or remove expense window"""
        self.win = tk.Tk()
        self.win.title('add or remove expense')
        self.win.geometry('400x500')
    
    def read_text(self) -> list:
        """read all widgets as string and return as a list """
        inp = []
        inp.append(self.amount.get("1.0",'end-1c'))
        inp.append(self.place.get("1.0",'end-1c'))
        inp.append(self.date.get())
        inp.append(self.explantion.get("1.0",'end-1c'))
        inp.append(self.person.get("1.0",'end-1c'))
        inp.append(self.payment_method.get("1.0",'end-1c'))
        inp.append(self.discount.get("1.0",'end-1c'))
        inp.append(self.amount_from.get("1.0",'end-1c'))
        inp.append(self.amount_to.get("1.0",'end-1c'))
        inp.append(self.date_from.get())
        inp.append(self.date_to.get())
        inp.append(self.discount_from.get("1.0",'end-1c'))
        inp.append(self.discount_to.get("1.0",'end-1c'))
        return inp

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

    def data_filter(self) -> list:
        """check if data are correct  and return which text are filled """
        data = self.read_text()
        flag = [0 for i in range(13)]
        for i in range(len(data)):
            if data[i] != '':
                flag[i] = 1
        
        if flag[0] and not data[0].isdigit():
            messagebox.showerror('amount Error', 'amount is not intiger')
            return [],[]
        
        if flag[1]:
            sch = search_place.SearchPlace()
            sch.by_name(data[1])
            out = sch.run()
            if len(out) == 0:
                messagebox.showerror('place Error', 'there is not such a place')
                return [],[]
            else:
                data[1] = out[0]
        
        if flag[2]:
            try:
                data[2] = self.translate_time(data[2])
            except:
                messagebox.showerror('date Error', 'the date is not correct')
                return [],[]
        
        if flag[4]:
            sch = search_persons.SearchPerson()
            sch.by_name(data[4])
            out = sch.run()
            if len(out) == 0:
                messagebox.showerror('person Error', 'there is not such a person')
                return [],[]
            else:
                data[4] = out[0]

        if flag[5]:
            sch = search_payment_methods.SearchPaymentMethod()
            sch.by_name(data[5])
            out = sch.run()
            if len(out) == 0:
                messagebox.showerror('payment method Error', 'there is not such a payment method')
                return [],[]
            else:
                data[5] = out[0]
        
        if flag[6] and not data[6].isdigit():
            messagebox.showerror('discount Error', 'discount is not intiger')
            return [],[]
        
        if flag[7] and not data[7].isdigit():
            messagebox.showerror('amount Error', 'amount is not intiger')
            return [],[]

        if flag[8] and not data[8].isdigit():
            messagebox.showerror('amount Error', 'amount is not intiger')
            return [],[]

        if flag[9]:
            try:
                data[9] = self.translate_time(data[9])
            except:
                messagebox.showerror('date Error', 'the date is not correct')
                return [],[]
        
        if flag[10]:
            try:
                data[10] = self.translate_time(data[10])
            except:
                messagebox.showerror('date Error', 'the date is not correct')
                return [],[]
        
        if flag[11] and not data[11].isdigit():
            messagebox.showerror('discount Error', 'discount is not intiger')
            return [],[]

        if flag[12] and not data[12].isdigit():
            messagebox.showerror('discount Error', 'discount is not intiger')
            return [],[]

        return data, flag
    
    def reset(self) -> None:
        """clean all data from widgets """
        self.amount.delete("1.0",'end-1c')
        self.place.delete("1.0",'end-1c')
        self.date._set_text(self.date._date.strftime(''))
        self.explantion.delete("1.0",'end-1c')
        self.person.delete("1.0",'end-1c')
        self.payment_method.delete("1.0",'end-1c')
        self.discount.delete("1.0",'end-1c')
        self.amount_to.delete("1.0",'end-1c')
        self.amount_from.delete("1.0",'end-1c')
        self.date_to._set_text(self.date_to._date.strftime(''))
        self.date_from._set_text(self.date_from._date.strftime(''))
        self.discount_from.delete("1.0",'end-1c')
        self.discount_to.delete("1.0",'end-1c')

    def add_button(self)->None:
        """this method runs when you push the add button"""
        data, flag = self.data_filter()
        if len(flag) == 0:
            self.reset()
            return

        if flag[0]+flag[1]+flag[2] + flag[3]+ flag[4]+ flag[5]+ flag[6] != 7:
            messagebox.showerror('empty input', 'please fill Entries')
            self.reset()
            return

        expense = variable.Expense(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
        expense.add_to_database()
        self.reset()

    def remove_button(self) -> None:
        """this method runs when client push remove button"""
        for i in self.search():
            i.remove_from_database()

    def search(self):
        """search for data in objects and make their objects"""
        data, flag = self.data_filter()
        if len(flag) == 0:
            self.reset()
            return
        
        sch = search_expense.SearchExpense()
        if flag[0]:
            sch.by_amount(data[0], data[0])
        if flag[1]:
            sch.by_place([data[1]])
        
        if flag[2]:
            sch.by_date([data[2]])

        if flag[4]:
            sch.by_person([data[4]])
        
        if flag[5]:
            sch.by_payment_method([data[5]])
        
        if flag[6]:
            sch.by_discount(data[6], data[6])

        if flag[7] and flag[8]:
            sch.by_amount(data[7], data[8])
        elif flag[7]:
            sch.by_amount(data[7])
        elif flag[8]:
            sch.by_amount(amount_up=data[8])

        if flag[9] and flag[10]:
            days = search_date.SearchDate()
            days.by_date(data[9], data[10])
            days = days.run()
            sch.by_date(days)

        elif flag[9]:
            days = search_date.SearchDate()
            days.by_date(date_down=data[9])
            days = days.run()
            sch.by_date(days)

        elif flag[10]:
            days = search_date.SearchDate()
            days.by_date(date_up=data[10])
            days = days.run()
            sch.by_date(days)

        if flag[11] and flag[12]:
            sch.by_discount(data[11], data[12])
        elif flag[11]:
            sch.by_discount(discount_down=data[11])
        elif flag[12]:
            sch.by_discount(discount_up=data[12])
        
        return sch.run()

    def show_button(self) -> None:
        """this method run when client push show button"""
        header = ["amount", 'place', 'date', 'explanation', "person", "payment method", "discount"]
        data = []
        i: variable.Expense
        for i in self.search():
            data.append([i.amount, i.place.name, i.date.show(), i.explanation, i.person.name, i.payment_method.name, i.discount])

        displayoutput.DisplayOutput(header, data).run()
        self.reset()

    def add_or_remove_place(self) -> None:
        """open add or remove window of chaing place"""
        place = add_or_remove_place.PlaceAddRemove()
        place.run()

    def add_or_remove_payment_method(self) -> None:
        """open add or remove payment method window """
        payment = add_or_remove_payment_method.PaymentMethodAddRemove()
        payment.run()

    def add_or_remove_person(self):
        """this methods works when you push the add or remove person button"""
        person = add_or_remove_person_display.PersonAddRemove()
        person.run()

    def make_widgets(self) -> None:
        """make all widgets and fixed them"""
        x = 0.2
        y = 0.06
        down = 0.082

        # labels
        tk.Label(self.win, text='amount: ').place(relx=x, rely=y, anchor = 'center')
        tk.Label(self.win, text='place: ').place(relx=x, rely=y+down, anchor = 'center')
        tk.Label(self.win, text='date: ').place(relx=x, rely=y+down*2, anchor = 'center')
        tk.Label(self.win, text='explantions: ').place(relx=x, rely=y+down*3, anchor = 'center')
        tk.Label(self.win, text='person: ').place(relx=x, rely=y+down*4, anchor = 'center')
        tk.Label(self.win, text='payment method: ').place(relx=x, rely=y+down*5, anchor = 'center')
        tk.Label(self.win, text='discount: ').place(relx=x, rely=y+down*6, anchor = 'center')
        tk.Label(self.win, text='amount(search):').place(relx=x, rely=y+down*7, anchor = 'center')
        tk.Label(self.win, text='date(search): ').place(relx=x, rely=y+down*8, anchor = 'center')
        tk.Label(self.win, text='discount(search): ').place(relx=x, rely=y+down*9, anchor = 'center')

        # buttons 
        person_ = tk.Button(self.win, text='check/update', command=self.add_or_remove_person,height=1,width=12) 
        place_ = tk.Button(self.win, text='check/update', command=self.add_or_remove_place,height=1,width=12) 
        payment_ = tk.Button(self.win, text='check/update', command=self.add_or_remove_payment_method,height=1,width=12) 

        add_ = tk.Button(self.win, text='Add', command=self.add_button) 
        remove_ = tk.Button(self.win, text='Remove', command=self.remove_button) 
        show_ = tk.Button(self.win, text='Show', command=self.show_button) 
        exit_ = tk.Button(self.win, text='Exit', command=self.win.destroy) 

        x = 0.7
        place_.place(relx=x, rely=y+down, anchor = 'w')
        person_.place(relx=x, rely=y+down*4, anchor = 'w')
        payment_.place(relx=x, rely=y+down*5, anchor = 'w')

        x = 0.19
        add_.place(relx=x+0.055, rely=y+down*10)
        remove_.place(relx=0.155+x, rely=y+down*10)
        show_.place(relx=0.315+x, rely=y+down*10)
        exit_.place(relx=0.435+x, rely=y+down*10)

        # Entries 
        x = x = 0.4
        self.amount = tk.Text(self.win,height=1,width=25)
        self.amount.place(relx=x, rely=y, anchor = 'w')

        self.place = tk.Text(self.win,height=1,width=12)
        self.place.place(relx=x, rely=y+down, anchor = 'w')

        self.date=DateEntry(self.win,selectmode='day',height=1,width=30, date_pattern='yyyy/mm/dd')
        self.date.configure(validate='none')
        self.date._set_text(self.date._date.strftime(''))
        self.date.place(relx=x, rely=y+down*2, anchor = 'w')

        self.explantion = tk.Text(self.win,height=1,width=25)
        self.explantion.place(relx=x, rely=y+down*3, anchor = 'w')        

        self.person = tk.Text(self.win,height=1,width=12)
        self.person.place(relx=x, rely=y+down*4, anchor = 'w')
    
        self.payment_method = tk.Text(self.win,height=1,width=12)
        self.payment_method.place(relx=x, rely=y+down*5, anchor = 'w')

        self.discount = tk.Text(self.win,height=1,width=25)
        self.discount.place(relx=x, rely=y+down*6, anchor = 'w')
  
        self.amount_from = tk.Text(self.win,height=1,width=8)
        self.amount_from.place(relx=x, rely=y+down*7, anchor = 'w')
        tk.Label(self.win, text='to: ').place(relx=x+0.25, rely=y+down*7, anchor = 'center')
        self.amount_to = tk.Text(self.win,height=1,width=8)
        self.amount_to.place(relx=x+0.335, rely=y+down*7, anchor = 'w')

        self.date_from=DateEntry(self.win,selectmode='day',height=1,width=10, date_pattern='yyyy/mm/dd')
        self.date_from.configure(validate='none')
        self.date_from._set_text(self.date_from._date.strftime(''))
        self.date_from.place(relx=x, rely=y+down*8, anchor = 'w')

        tk.Label(self.win, text='to: ').place(relx=x+0.25, rely=y+down*8, anchor = 'center')
        
        self.date_to=DateEntry(self.win,selectmode='day',height=1,width=10, date_pattern='yyyy/mm/dd')
        self.date_to.configure(validate='none')
        self.date_to._set_text(self.date_to._date.strftime(''))
        self.date_to.place(relx=x+0.335, rely=y+down*8, anchor = 'w')


        self.discount_from = tk.Text(self.win,height=1,width=8)
        self.discount_from.place(relx=x, rely=y+down*9, anchor = 'w')
        tk.Label(self.win, text='to: ').place(relx=x+0.25, rely=y+down*9, anchor = 'center')
        self.discount_to = tk.Text(self.win,height=1,width=8)
        self.discount_to.place(relx=x+0.335, rely=y+down*9, anchor = 'w')

    def run(self)->None:
        """run the window"""
        self.make_widgets()
        tk.mainloop()
