from tkinter import *
from backend import Database

database = Database("books.db")

class Window:

  def __init__(self, window):
    self.window = window

    self.window.wm_title("Bookstore")

    title = Label(window, text="Title")
    title.grid(row=0, column=0)

    author = Label(window, text="Author")
    author.grid(row=0, column=2)

    year = Label(window, text="Year")
    year.grid(row=1, column=0)

    isbn = Label(window, text="ISBN")
    isbn.grid(row=1, column=2)

    self.title_text = StringVar()
    self.e1 = Entry(window, textvariable=self.title_text)
    e1.grid(row=0, column=1)

    self.author_text = StringVar()
    self.e2 = Entry(window, textvariable=self.author_text)
    e2.grid(row=0, column=3)

    self.year_text = StringVar()
    self.e3 = Entry(window, textvariable=self.year_text)
    e3.grid(row=1, column=1)

    self.isbn_text = StringVar()
    self.e4 = Entry(window, textvariable=self.isbn_text)
    e4.grid(row=1, column=3)

    self.list1 = Listbox(window, height=6, width=35)
    self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)

    sb1 = Scrollbar(window)
    sb1.grid(row=2, column=2, rowspan=6)

    self.list1.configure(yscrollcommand=sb1.set)
    sb1.configure(command=self.list1.yview)

    self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

    view_button = Button(window, text="View all", width=12, command=self.view_command)
    view_button.grid(row=2, column=3)

    search_button = Button(window, text="Search entry", width=12, command=self.search_command)
    search_button.grid(row=3, column=3)

    add_button = Button(window, text="Add entry", width=12, command=self.add_command)
    add_button.grid(row=4, column=3)

    update_button = Button(window, text="Update Selected", width=12, command=self.update_command)
    update_button.grid(row=5, column=3)

    delete_button = Button(window, text="Delete Selected", width=12, command=self.delete_command)
    delete_button.grid(row=6, column=3)

    close_button = Button(window, text="Close", width=12, command=window.destroy)
    close_button.grid(row=7, column=3)


  def get_selected_row(self, event):
    index = self.list1.curselection()[0]
    self.selected_tuple = self.list1.get(index)
    self.e1.delete(0, END)
    self.e1.insert(END, self.selected_tuple[1])
    self.e2.delete(0, END)
    self.e2.insert(END, self.selected_tuple[2])
    self.e3.delete(0, END)
    self.e3.insert(END, self.selected_tuple[3])
    self.e4.delete(0, END)
    self.e4.insert(END, self.selected_tuple[4])

  def view_command(self):
    self.list1.delete(0, END)
    for row in database.view():
      self.list1.insert(END, row)

  def search_command(self):
    self.list1.delete(0, END)
    for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
      self.list1.insert(END, row)

  def add_command(self):
    database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
    self.list1.delete(0, END)
    self.list1.insert(END,(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))

  def update_command(self):
    database.update(self.selected_tuple[0], self.title_text.get(), self.author_text.get(), year_text.get(), self.isbn_text.get())

  def delete_command(self):
    database.delete(self.selected_tuple[0])


window = Tk()
Window(window)
window.mainloop()