from tkinter import *
import tkinter.ttk as ttk
import csv
from pathlib import Path

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



root = Tk()
root.title("Python - Import CSV File To Tkinter Table")
width = 500
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)


TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("Name", "Time", "Date"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('Name', text="Name", anchor=W)
tree.heading('Time', text="Time", anchor=W)
tree.heading('Date', text="Date", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=200)
tree.column('#2', stretch=NO, minwidth=0, width=200)
tree.column('#3', stretch=NO, minwidth=0, width=300)
tree.pack()

with open('C:\\Users\\mradu\\Documents\\projct 2\\Attendance\\sci\\2022-05-09.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        Name = row['Name']
        Time = row['Time']
        Date = row['Date']
        tree.insert("", 0, values=(Name, Time, Date))

if __name__ == '__main__':
    root.mainloop()