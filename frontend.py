from tkinter import *
import backend

def get_selected_row(event):
  global selected_tuple
  index = list1.curselection()[0]
  selected_tuple = list1.get(index)
  

def view_command():
  list1.delete(0, END)
  for row in backend.view():
    list1.insert(END, row)

def search_command():
  list1.delete(0, END)
  for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
    list1.insert(END, row)

def add_command():
  backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
  list1.delete(0, END)
  list1.insert(END,(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def update_command():
  pass

def delete_command():
  backend.delete(selected_tuple[0])

def close_command():
  pass

window = Tk()

title = Label(window, text="Title")
title.grid(row=0, column=0)

author = Label(window, text="Author")
author.grid(row=0, column=2)

year = Label(window, text="Year")
year.grid(row=1, column=0)

isbn = Label(window, text="ISBN")
isbn.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

view_button = Button(window, text="View all", width=12, command=view_command)
view_button.grid(row=2, column=3)

search_button = Button(window, text="Search entry", width=12, command=search_command)
search_button.grid(row=3, column=3)

add_button = Button(window, text="Add entry", width=12, command=add_command)
add_button.grid(row=4, column=3)

update_button = Button(window, text="Update Selected", width=12, command=update_command)
update_button.grid(row=5, column=3)

delete_button = Button(window, text="Delete Selected", width=12, command=delete_command)
delete_button.grid(row=6, column=3)

close_button = Button(window, text="Close", width=12, command=close_command)
close_button.grid(row=7, column=3)

window.mainloop()