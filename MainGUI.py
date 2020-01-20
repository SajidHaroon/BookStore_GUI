import tkinter as tk
from tkinter import * #Import all
#:::Importing backend file n functions and merging it here with the gui buttons
#----------------------------------------------------------------
from backend import Database

database=Database("books.db")     # Making an object of that class
                                  # Filepath as arg, changed as db in __init__ function
  

def get_selected_row(event):             # 'event'-A special paratmeter, hold info abt an event. Function returns a tuple
    try:                                    #Added later. to avoid index error while clicking blank list screen
        global seleted_tuple                 # Making a global variable which will be used in 'delete_command' funciton
        index=list1.curselection()[0]        # Item 0 of tuple which is ID #
        seleted_tuple=list1.get(index)       # Value of this will be a tuple with values of the rows
        e1.delete(0,END)                     # Now to show the selecte items in view or highlighted in fields of GUI
        e1.insert(END,seleted_tuple[1])      # Like in tuple Title[1], Author[2], Year[3], Isbn[4]
        e2.delete(0,END)                     # An example (1, 'The book', 'Jack', 1924, 353384890)
        e2.insert(END,seleted_tuple[3])
        e3.delete(0,END)
        e3.insert(END,seleted_tuple[2])
        e4.delete(0,END)
        e4.insert(END,seleted_tuple[4])
        #print(seleted_tuple)                 #For testing only.Just prints the row selected in powershell
    except IndexError:
        pass

def view_command():                           # Iteriting through all entries and displaying
    list1.delete(0,END)                       #From index 0 till end-Clear the entries ahead of viewing 
    for row in database.view(): 
        list1.insert(END,row)                 #End shows that evey entry is stored in new line

def search_command(): 
    list1.delete(0,END) 
    for row in database.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)                 # .get() is used above as all these text variables are 
                                              # declared as plain strings
                                              # Also Search function in backend takes arguments

def add_command():
    database.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
                                              # But these changes only visible once view all button is pressed.However, in order to see
                                              # immediately if the entry was successfull add following
    list1.delete(0,END)                       #Make sure the list is empty
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())) # Put() around to make it a single value otherwise it will appear each entry each line 
                                             # ^ Display all data user has entrered

def delete_command():
    database.delete(seleted_tuple[0])

def update_command():
    database.update(seleted_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
                                             # ^^ The above function takes id as selected tuple and then expects editing in user defined data as Strings .get()

window=tk.Tk()

window.wm_title("BookStore")                 # Give GUI a title

#Take the 
l1=Label(window,text="Title")
l1.grid(row=0, column=0)

l1=Label(window,text="Year")
l1.grid(row=1, column=0)

l1=Label(window,text="Author")
l1.grid(row=0, column=2)

l1=Label(window,text="ISBN")
l1.grid(row=1, column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text )
e1.grid(row=0,column=1)

year_text=StringVar()
e2=Entry(window,textvariable=year_text )
e2.grid(row=1,column=1)

author_text=StringVar()
e3=Entry(window,textvariable=author_text )
e3.grid(row=0,column=3)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text )
e4.grid(row=1,column=3)

list1=Listbox(window, height=6, width=35)
list1.grid(row=2,column=0, rowspan=6, columnspan=2)

#we first creat a scroll bar and then attach it to Listbox

sb1=Scrollbar(window)
sb1.grid(row=2,column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set) #Vertical scrollbar on y axis
sb1.configure(command=list1.yview) #Scrollbar on y axis with the list

list1.bind('<<ListboxSelect>>',get_selected_row)
# We need the above binding for select and delete row. Item select and delete is an event.
# For that event, wee a need function, defined in the begining. When 'get_selected_row' is passed to 
# the bind method, it expects the function to have this paratmeter

#b1=Button(window, text="View all", width=12)
b1=Button(window, text="View all", width=12, command=view_command) # Python wrapper fucntion(Backend imported function)
b1.grid(row=2, column=3)

b2=Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3=Button(window, text="Add Entry" ,width=12, command=add_command)
b3.grid(row=4, column=3)

b4=Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5, column=3)

b5=Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6=Button(window, text="Close" ,width=12, command=window.destroy) # By closing button, simply close the GUI
b6.grid(row=7, column=3)

window.mainloop()
