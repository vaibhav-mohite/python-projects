from tkinter import *
import backend


def get_selected_row(event):
    try:
        global selected_tuple
        global sr_no
        index = lb.curselection()[0]
        selected_tuple = lb.get(index)
        sr_no = selected_tuple[0]
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass


def view_command():
    lb.delete(0, END)
    for i in backend.view():
        lb.insert(END, i)


def search_command():
    lb.delete(0, END)
    for i in backend.search(UID_text.get(), title_text.get(), author_text.get(), publication_text.get()):
        lb.insert(END, i)


def add_command():
    backend.insert(UID_text.get(), title_text.get(), author_text.get(), publication_text.get())
    lb.delete(0, END)
    lb.insert(END, (UID_text.get(), title_text.get(), author_text.get(), publication_text.get()))


def delete_command():
    backend.delete(sr_no)


def update_command():
    backend.update(selected_tuple[0], UID_text.get(), title_text.get(), author_text.get(), publication_text.get())


window = Tk()  # Creating a Window

window.title("Book Management App")  # App Header

# LABEL WIDGETS

l1 = Label(window, text="ID", width=10)
l1.grid(row=0, column=0, padx=5, pady=5, ipady=5)

l2 = Label(window, text="Title", width=10)
l2.grid(row=0, column=3, padx=5, pady=5, ipady=5)

l3 = Label(window, text="Author", width=10)
l3.grid(row=1, column=0, padx=5, pady=5, ipady=5)

l4 = Label(window, text="Publication", width=10)
l4.grid(row=1, column=3, padx=5, pady=5, ipady=5)

# ENTRY WIDGETS

UID_text = StringVar()
e1 = Entry(window, textvariable=UID_text, width=25)
e1.grid(row=0, column=1, columnspan=2)

title_text = StringVar()
e2 = Entry(window, textvariable=title_text, width=20)
e2.grid(row=0, column=4, columnspan=2, padx=(0, 30))

author_text = StringVar()
e3 = Entry(window, textvariable=author_text, width=25)
e3.grid(row=1, column=1, columnspan=2)

publication_text = StringVar()
e4 = Entry(window, textvariable=publication_text, width=20)
e4.grid(row=1, column=4, columnspan=2, padx=(0, 30))

# BUTTON WIDGETS

b1 = Button(window, text="View All", width=12, command=view_command)
b1.grid(row=3, column=5, padx=(0, 20), pady=(0, 10), ipady=5)

b2 = Button(window, text="Search", width=12, command=search_command)
b2.grid(row=4, column=5, padx=(0, 20), pady=(0, 10), ipady=5)

b3 = Button(window, text="Add Entry", width=12, command=add_command)
b3.grid(row=5, column=5, padx=(0, 20), pady=(0, 10), ipady=5)

b4 = Button(window, text="Update", width=12, command=update_command)
b4.grid(row=6, column=5, padx=(0, 20), pady=(0, 10), ipady=5)

b5 = Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=7, column=5, padx=(0, 20), pady=(0, 10), ipady=5)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=8, column=5, padx=(0, 20), pady=(0, 15), ipady=5)

# LISTBOX WIDGET
lb = Listbox(window, height=15, width=60)
lb.grid(row=3, column=0, rowspan=6, columnspan=4, padx=15, pady=(0, 15))

sb = Scrollbar(window)  # Creating Scrollbar
sb.grid(row=3, column=4, rowspan=10)

lb.configure(yscrollcommand=sb.set)
sb.configure(command=lb.yview)

lb.bind('<<ListboxSelect>>', get_selected_row)  # Bind connects Selected row with Buttons

window.mainloop()
