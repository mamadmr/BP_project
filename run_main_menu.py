import tkinter as tk
import add_or_remove_person_display
import add_or_remove_place
import add_or_remove_payment_method
import add_or_remove_expense
import show_diagram_person

class Menu:
    def __init__(self) -> None:
        """this class makes the main menu"""
        self.win = tk.Tk()
        self.win.title('main.menu')
        self.win.geometry('300x160')
    
    def add_or_remove_person(self):
        """this methods works when you push the add or remove person button"""
        person = add_or_remove_person_display.PersonAddRemove()
        person.run()
    
    def add_or_remove_place(self):
        place = add_or_remove_place.PlaceAddRemove()
        place.run()

    def add_or_remove_payment_method(self):
        payment = add_or_remove_payment_method.PaymentMethodAddRemove()
        payment.run()

    def add_or_remove_expense(self):
        expense = add_or_remove_expense.AddRemoveExpense()
        expense.run()

    def dig_person(self):
        show_diagram_person.PersonShow().run()

    def make_widgets(self) -> None:
        """make widgets"""
        person = tk.Button(self.win, text='Add or remove person', command=self.add_or_remove_person, height=1,width=18)
        person.place(relx=0.03, rely=0.03)

        person = tk.Button(self.win, text='Add or remove place', command=self.add_or_remove_place, height=1,width=18)
        person.place(relx=0.03, rely=0.23)

        payment = tk.Button(self.win, text='Add or remove payment', command=self.add_or_remove_payment_method, height=1,width=18)
        payment.place(relx=0.03, rely=0.43)
    
        payment = tk.Button(self.win, text='Add or remove expense', command=self.add_or_remove_expense, height=1,width=18)
        payment.place(relx=0.03, rely=0.63)

        diagram_person = tk.Button(self.win, text='persons diagram', command=self.dig_person, height=1,width=18)
        diagram_person.place(relx=0.52, rely=0.03)
        
    def run(self)->None:
        """run the window"""
        self.make_widgets()
        tk.mainloop()

if __name__ == "__main__":
    menu = Menu()
    menu.run()