import tkinter as tk
import add_or_remove_person_display

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
    
    def make_widgets(self) -> None:
        """make widgets"""
        person = tk.Button(self.win, text='Add or remove person', command=self.add_or_remove_person)
        person.place(relx=0.03, rely=0.03)
    
    def run(self)->None:
        """run the window"""
        self.make_widgets()
        tk.mainloop()

if __name__ == "__main__":
    menu = Menu()
    menu.run()