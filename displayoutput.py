import tkinter as tk
from tkinter import ttk

class DisplayOutput:
    def __init__(self, header: list=[], data: list=[]) -> None:
        """this class is for display the outpus of searches"""
        self.win = tk.Tk()
        self.win.title('Display output')
        #self.win.geometry('500x300')
        self.header = header
        self.data = data

    def make_str(self):
        """all the data should be string so this method make all of them strings"""
        self.mx = 0
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                self.data[i][j] = str(self.data[i][j])

    def make_widgets(self):
        """this methods is for make table and some other stuffs"""
        frame = tk.Frame(self.win)
        frame.pack()

        scrolly = tk.Scrollbar(frame, orient='vertical')
        scrolly.pack(side=tk.RIGHT, fill=tk.Y)

        scrollx = tk.Scrollbar(frame,orient='horizontal')
        scrollx.pack(side= tk.BOTTOM,fill=tk.X)

        tree = ttk.Treeview(frame,yscrollcommand=scrolly.set, xscrollcommand =scrollx.set)
        tree.pack()
        scrolly.config(command=tree.yview)
        scrollx.config(command=tree.xview)

        tree['columns'] = tuple(self.header)
        tree.column("#0", width=0,  stretch=tk.NO)
        tree.heading("#0",text="",anchor=tk.CENTER)
        for i in range(len(self.header)):
            mx = 0
            for j in range(len(self.data)):
                mx = max(mx, len(self.data[j][i]))
            mx = max(mx, len(self.header[i]))
            tree.column(self.header[i],anchor=tk.CENTER, width=mx*9, stretch=tk.NO)
            tree.heading(self.header[i], text=self.header[i],anchor=tk.CENTER)
        for i in range(len(self.data)):
            tree.insert(values=self.data[i],parent='',index='end',iid=i,text='') 
    


        exit_button = tk.Button(self.win, text="Exit", command=self.win.destroy)
        exit_button.pack()

    def run(self):
        """this method run all the other methods in a good way"""
        self.make_str()
        self.make_widgets()
        self.win.mainloop()


if __name__ == "__main__":
    data = [[i*10000000000000000, i*200000000000000000000000, i*30000000000000000000000000000, i*40000000000000000000000] for i in range(100)]
    test = DisplayOutput(["expenses", "place", "person", "date"],data)
    test.run()