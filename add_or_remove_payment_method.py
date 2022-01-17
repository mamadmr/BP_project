import tkinter as tk
from tkinter import messagebox
import variable
import displayoutput
import search_payment_methods

class PaymentMethodAddRemove:
    def __init__(self) -> None:
        """this class works with payment methods table in dataset search remove and delete """
        self.win = tk.Tk()
        self.win.title('add or remove payment method')
        self.win.geometry('300x160')

    def data_filter(self) -> list:
        """check if data are correct  and return which text are filled """
        data = self.read_text()
        flag = [0, 0, 0, 0, 0]
        for i in range(len(data)):
            if data[i] != '':
                flag[i] = 1

        if flag[1] and not data[1].isdigit():
            messagebox.showerror('number Error', 'number is not intiger')
            return []
    
        return flag

    def add_button(self)->None:
        """this method runs when you push the add button"""
        flag = self.data_filter()
        if len(flag) == 0:
            self.reset()
            return
        data = self.read_text()
        if flag[0]+flag[1] != 2:
            messagebox.showerror('empty input', 'please write name and number')
            self.reset()
            return

        person = variable.PaymentMethod(data[0], data[1])
        person.add_to_database()
        self.reset()

    def search(self) -> list:
        """return the objects that satisfied in conditions"""
        flag = self.data_filter()
        if len(flag) == 0:
            self.reset()
            return
        data = self.read_text()

        sch_p = search_payment_methods.SearchPaymentMethod()
        if flag[0]:
            sch_p.by_name(data[0])
        if flag[1]:
            sch_p.by_number(int(data[1]))
        
        return sch_p.run()

    def remove_button(self) -> None:
        """this method runs when client push remove button"""
        for i in self.search():
            i.remove_from_database()
        self.reset()
    
    def show_button(self) -> None:
        """this method run when client push show button"""
        data = []
        for i in self.search():
            data.append([i.name, i.number])
        show = displayoutput.DisplayOutput(["name" , 'number'], data)
        self.reset()
        show.run()

    def make_widgets(self) -> None:
        """make widgets"""
        y = 0.065
        # name
        tk.Label(self.win, text='name: ').place(relx=0.15, rely=0.06, anchor = 'center')
        self.name = tk.Text(self.win,height=1,width=25)
        self.name.place(relx=0.63, rely=0.062, anchor = 'center')

        # number
        tk.Label(self.win, text='number: ').place(relx=0.15, rely=0.16+y, anchor = 'center')
        self.number = tk.Text(self.win,height=1,width=25)
        self.number.place(relx=0.63, rely=0.162+y, anchor = 'center')

        # buttons add - show - remove - exit
        add_ = tk.Button(self.win, text='Add', command=self.add_button) 
        remove_ = tk.Button(self.win, text='Remove', command=self.remove_button) 
        show_ = tk.Button(self.win, text='Show', command=self.show_button) 
        exit_ = tk.Button(self.win, text='Exit', command=self.win.destroy) 

        x = 0.05
        add_.place(relx=0.18+x, rely=0.45+y+y+y+y)
        remove_.place(relx=0.3+x, rely=0.45+y+y+y+y)
        show_.place(relx=0.49+x, rely=0.45+y+y+y+y)
        exit_.place(relx=0.63+x, rely=0.45+y+y+y+y)

    def reset(self) ->None:
        """clean all the texts"""
        self.name.delete("1.0",'end-1c')
        self.number.delete("1.0",'end-1c')

    def read_text(self) -> list:
        """read all texts and return them as a list"""
        inp = []
        inp.append(self.name.get("1.0",'end-1c'))
        inp.append(self.number.get("1.0",'end-1c'))
        return inp

    def run(self)->None:
        """run the window"""
        self.make_widgets()
        tk.mainloop()
