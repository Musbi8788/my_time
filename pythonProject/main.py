from calendar import weekday
from datetime import datetime
from  tkinter import *
import time

FONT = "Ticking Timebomb BB"
FOREGROUND = "#024CAA"
BACKGROUND = "#BCF2F6"
# create
def update_time():
    current_time = time.strftime("%H:%M:%S %p")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)


# window
root = Tk()
root.title("Musbi Time")
root.config(padx=200, pady=50, bg=BACKGROUND)

# clock label
clock_label = Label(text="00:00" , background=BACKGROUND,  foreground=FOREGROUND, font=(FONT, 50, "bold"))
clock_label.pack()

day = weekday(2024,10,28)
print(type(day))

# update time
update_time()
root.mainloop()



