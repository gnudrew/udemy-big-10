from tkinter import *
from backend import Database

class GUI:
    def get_selected_row(event):
        global selected_tuple
        index=self.list1.curselection()[0]
        selected_tuple=self.list1.get(index)
        self.e1.delete(0,END)
        self.e1.insert(END,selected_tuple[1])
        self.e2.delete(0,END)
        self.e2.insert(END,selected_tuple[2])
        self.e3.delete(0,END)
        self.e3.insert(END,selected_tuple[3])
        self.e4.delete(0,END)
        self.e4.insert(END,selected_tuple[4])

    def view_command():
        self.list1.delete(0,END)
        for row in database.view():
            self.list1.insert(END,row)

    def search_command():
        self.list1.delete(0,END)
        for row in database.search(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()):
            self.list1.insert(END,row)

    def add_command():
        database.insert(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
        self.list1.delete(0,END)
        self.list1.insert(END,(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()))

    def delete_command():
        database.delete(selected_tuple[0])

    def update_command():
        database.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

    def __init__(self, name):
        self.name = name
        self.window=Tk()
        self.window.wm_title(self.name)

        self.l1=Label(self.window,text="Title")
        self.l1.grid(row=0,column=0)

        self.l2=Label(self.window,text="Author")
        self.l2.grid(row=0,column=2)

        self.l3=Label(self.window,text="Year")
        self.l3.grid(row=1,column=0)

        self.l4=Label(self.window,text="ISBN")
        self.l4.grid(row=1,column=2)

        self.title_text=StringVar()
        self.e1=Entry(self.window,textvariable=self.title_text)
        self.e1.grid(row=0,column=1)

        self.author_text=StringVar()
        self.e2=Entry(self.window,textvariable=self.author_text)
        self.e2.grid(row=0,column=3)

        self.year_text=StringVar()
        self.e3=Entry(self.window,textvariable=self.year_text)
        self.e3.grid(row=1,column=1)

        self.isbn_text=StringVar()
        self.e4=Entry(self.window,textvariable=self.isbn_text)
        self.e4.grid(row=1,column=3)

        self.list1=Listbox(self.window, height=6,width=35)
        self.list1.grid(row=2,column=0,rowspan=6,columnspan=2)

        self.sb1=Scrollbar(self.window)
        self.sb1.grid(row=2,column=2,rowspan=6)

        self.list1.configure(yscrollcommand=sb1.set)
        self.sb1.configure(command=list1.yview)

        self.list1.bind('<<ListboxSelect>>',get_selected_row)

        self.b1=Button(self.window,text="View all", width=12,command=view_command)
        self.b1.grid(row=2,column=3)

        self.b2=Button(self.window,text="Search entry", width=12,command=search_command)
        self.b2.grid(row=3,column=3)

        self.b3=Button(self.window,text="Add entry", width=12,command=add_command)
        self.b3.grid(row=4,column=3)

        self.b4=Button(self.window,text="Update selected", width=12,command=update_command)
        self.b4.grid(row=5,column=3)

        self.b5=Button(self.window,text="Delete selected", width=12,command=delete_command)
        self.b5.grid(row=6,column=3)

        self.b6=Button(self.window,text="Close", width=12,command=self.window.destroy)
        self.b6.grid(row=7,column=3)

        self.window.mainloop()

database=Database("books.db")
