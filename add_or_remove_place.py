import tkinter as tk
from tkinter import messagebox
import variable
import database_maker
import displayoutput
import search_place

class PlaceAddRemove:
    def __init__(self) -> None:
        """this class works with places table in dataset search remove and delete """
        self.win = tk.Tk()
        self.win.title('add or remove place')
        self.win.geometry('300x160')

    def data_filter(self) -> list:
        """check if data are correct  and return which text are filled """
        data = self.read_text()
        flag = [0, 0, 0, 0, 0]
        for i in range(len(data)):
            if data[i] != '':
                flag[i] = 1

        if flag[1] and not data[1].isdigit():
            messagebox.showerror('distance Error', 'distance is not intiger')
            return []

        if flag[3] and not data[3].isdigit():
            messagebox.showerror('distance Error', 'from distance is not intiger')
            return []

        if flag[4] and not data[4].isdigit():
            messagebox.showerror('distance Error', 'to distance is not intiger')
            return []
    
        return flag

    def add_button(self)->None:
        """this method runs when you push the add button"""
        flag = self.data_filter()
        if len(flag) == 0:
            self.reset()
            return
        data = self.read_text()
        if flag[0]+flag[1]+flag[2] != 3:
            messagebox.showerror('empty input', 'please write name distance and address')
            self.reset()
            return

        person = variable.Place(data[0], data[1], data[2])
        person.add_to_database()
        self.reset()

    def search(self) -> list:
        """return the objects that satisfied in conditions"""
        flag = self.data_filter()
        if len(flag) == 0:
            self.reset()
            return
        data = self.read_text()

        sch_p = search_place.SearchPlace()
        if flag[0]:
            sch_p.by_name(data[0])
        if flag[1]:
            sch_p.by_distance(int(data[1]), int(data[1]))
        if flag[3] and flag[4]:
            sch_p.by_distance(int(data[3]), int(data[4]))
        elif flag[3]:
            sch_p.by_distance(distance_down=int(data[3]))
        elif flag[4]:
            sch_p.by_distance(distance_up=int(data[4]))
        
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
            data.append([i.name, i.distance, i.address])
        show = displayoutput.DisplayOutput(["name" , 'distance', "address"], data)
        self.reset()
        show.run()

    def make_widgets(self) -> None:
        """make widgets"""
        y = 0.065
        # name
        tk.Label(self.win, text='name: ').place(relx=0.15, rely=0.06, anchor = 'center')
        self.name = tk.Text(self.win,height=1,width=25)
        self.name.place(relx=0.63, rely=0.062, anchor = 'center')

        # distance
        tk.Label(self.win, text='distance: ').place(relx=0.15, rely=0.16+y, anchor = 'center')
        self.distance = tk.Text(self.win,height=1,width=25)
        self.distance.place(relx=0.63, rely=0.162+y, anchor = 'center')

        # address
        tk.Label(self.win, text='address: ').place(relx=0.15, rely=0.26+y+y, anchor = 'center')
        self.address = tk.Text(self.win,height=1,width=25)
        self.address.place(relx=0.63, rely=0.262+y+y, anchor = 'center')

        # distance from ___ to ___
        tk.Label(self.win, text='distance:                   from').place(relx=0.27, rely=0.36+y+y+y, anchor = 'center')
        tk.Label(self.win, text='to').place(relx=0.72, rely=0.36+y+y+y, anchor = 'center')

        self.distance_from = tk.Text(self.win,height=1,width=5)
        self.distance_to = tk.Text(self.win,height=1,width=5)
        self.distance_from.place(relx=0.6, rely=0.362+y+y+y, anchor = 'center')
        self.distance_to.place(relx=0.84, rely=0.362+y+y+y, anchor = 'center')

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
        self.distance.delete("1.0",'end-1c')
        self.address.delete("1.0",'end-1c')
        self.distance_from.delete("1.0",'end-1c')
        self.distance_to.delete("1.0",'end-1c')

    def read_text(self) -> list:
        """read all texts and return them as a list"""
        inp = []
        inp.append(self.name.get("1.0",'end-1c'))
        inp.append(self.distance.get("1.0",'end-1c'))
        inp.append(self.address.get("1.0",'end-1c'))
        inp.append(self.distance_from.get("1.0",'end-1c'))
        inp.append(self.distance_to.get("1.0",'end-1c'))
        return inp

    def run(self)->None:
        """run the window"""
        self.make_widgets()
        tk.mainloop()

if __name__ == "__main__":
    database_maker.run()
    per = PlaceAddRemove()
    per.run()