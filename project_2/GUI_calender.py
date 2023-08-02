# These lines import necessary modules:tkinter for GUI,tkcalendar for calendar width,datetime for date update
from tkinter import *          
from tkcalendar import*
from datetime import datetime

# Tk instance named root is created:we can add title,change bg colorand change dimensions
root = Tk()
root.title("CALENDAR")
root.geometry('252x300')
root.configure(bg="lightblue")

# This creates an instance of the Calendar with right date and years
cal=Calendar(root,setmode="day",date_pattern="d/m/yy")
cal.pack(pady=2) 

# function is called when the "Select Date" button is clicked right date,day,and year with bold letter 
def get_date():
    selected_date = cal.get_date()
    date_name = datetime.strptime(selected_date,"%d/%m/%y")
    date_name_uniq = date_name.strftime("Selected Date: %d %B %Y")
    my_label.config(text= date_name_uniq,font=("Helvetica", 12, "bold"))

    # my_label.config(text="Selected Date:" + selected_date,font=("Helvetica", 12, "bold"))

# A Label widget named my_label is created with light blue background 
my_label=Label(root,background="lightblue")
my_label.pack(pady=10)

# button named btm with the label "Select Date" is created. It has background and white text color. 
btm=Button(root, text = 'Select Date',  background = "green", fg = "white",command = get_date)
btm.pack(side = 'top')  
btm.pack(pady=5) 

# This line starts the main event loop of the GUI.It keeps the code running to until the main window is closed.
root.mainloop()



