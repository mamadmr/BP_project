import tkinter as tk
from tkcalendar import DateEntry
import add_or_remove_payment_method
import add_or_remove_place
import add_or_remove_person_display

class AddRemoveExpense:
    def __init__(self) -> None:
        self.win = tk.Tk()
        self.win.title('add or remove expense')
        self.win.geometry('400x500')

    def add_button(self)->None:
        """this method runs when you push the add button"""
        pass

    def remove_button(self) -> None:
        """this method runs when client push remove button"""
        pass

    def show_button(self) -> None:
        """this method run when client push show button"""
        pass
    
    def add_or_remove_place(self):
        place = add_or_remove_place.PlaceAddRemove()
        place.run()

    def add_or_remove_payment_method(self):
        payment = add_or_remove_payment_method.PaymentMethodAddRemove()
        payment.run()

    def add_or_remove_person(self):
        """this methods works when you push the add or remove person button"""
        person = add_or_remove_person_display.PersonAddRemove()
        person.run()

    def make_widgets(self) -> None:
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

        self.date=DateEntry(self.win,selectmode='day',height=1,width=30)
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

        self.date_from=DateEntry(self.win,selectmode='day',height=1,width=8)
        self.date_from.place(relx=x, rely=y+down*8, anchor = 'w')
        tk.Label(self.win, text='to: ').place(relx=x+0.25, rely=y+down*8, anchor = 'center')
        self.date_to=DateEntry(self.win,selectmode='day',height=1,width=8)
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
