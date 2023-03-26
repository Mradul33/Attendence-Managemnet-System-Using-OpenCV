from pathlib import Path

# from tkinter import *
from tkinter import *
import tkinter.ttk as ttk
import csv
from ttkwidgets import Calendar
import os

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./asset")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def studentList():
    TableMargin = Frame(window)
    button1=Button(TableMargin, text="Quit",relief=FLAT,bg="#3A7FF6", command=lambda: TableMargin.destroy()).pack()
    #button1=Button(TableMargin, text="Quit", command=TableMargin.pack_forget()).pack()
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Enrollment_No","Name","Father_Name","EMail","Contact"), height=1000,
                        selectmode="extended", yscrollcommand=scrollbary.set,padding=10)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    tree.heading('Enrollment_No', text="Enrollment_No", anchor=W)
    tree.heading('Name', text="Name", anchor=W)
    tree.heading('Father_Name', text="Father_Name", anchor=W)
    tree.heading('EMail', text="EMail", anchor=W)
    tree.heading('Contact', text="Contact", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=150)
    tree.column('#2', stretch=NO, minwidth=0, width=150)
    tree.column('#3', stretch=NO, minwidth=0, width=150)
    tree.column('#4', stretch=NO, minwidth=0, width=150)
    tree.column('#5', stretch=NO, minwidth=0, width=150)
    tree.pack()
    path = ("C:\\Users\\mradu\\Documents\\projct 2\\StudentList\\StudentList.csv")
    with open(path,) as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            Enrollment_No = row['Enrollment_No']
            Name = row['Name']
            Father_Name = row["Father_Name"]
            EMail = row['EMail']
            Contact = row['Contact']
            tree.insert("", 0, values=(Enrollment_No,Name,Father_Name,EMail,Contact))
    #TableMargin.after(3000,lambda: TableMargin.pack_forget())
    TableMargin.pack(side="top", expand=True, fill="both")



def index():

    # Create transparent window
    # window.attributes('-alpha',0.5)
    root = Toplevel(window)
    root.title("Select a date")
    root.grab_set()
    # Calendar changed with ttk widget
    calendar = Calendar(root, year=2022, month=5, selectforeground='white',
                        selectbackground='#3A7FF6')
    calendar.pack()
    width = 500
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    def get_date():
        sel = calendar.selection
        date = (sel.strftime("%Y-%m-%d"))
        print(date)
        if date != 0:
            #table is here
            root = Tk()
            root.title(date)
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
            tree = ttk.Treeview(TableMargin, columns=("Name", "Time", "Date"), height=400,
                                selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
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
            path = (
                f"C:\\Users\\mradu\\Documents\\projct 2\\Attendance\\sci\\{date}.csv")
            print(path)
            with open(path,) as f:
                reader = csv.DictReader(f, delimiter=',')
                for row in reader:
                    Name = row['Name']
                    Time = row['Time']
                    Date = row['Date']
                    tree.insert("", 0, values=(Name, Time, Date))
            root.mainloop()
    button = Button(root, text="Select the Date", command=get_date)
    button.pack(pady=20)
    root.mainloop()
    root.grab_release()


def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):

    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)


def addStu():
    i = 3
    attendance.Attendance(i)


def takeAttendance():
    i = 2
    attendance.Attendance(i)


def logout():
    window.destroy()
    import login

def refresh():
    pass
# ui start from here
window = Tk()

window.geometry("1407x695")
window.configure(bg="#F1F1F1")


canvas = Canvas(
    window,
    bg="#F1F1F1",
    height=695,
    width=1407,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Home clicked"),
    relief="flat"
)
button_1.place(
    x=336.0,
    y=87.0,
    width=197.0,
    height=34.0
)

canvas.create_text(
    336.0,
    34.0,
    anchor="nw",
    text="Dashboard",
    fill="#3A7FF6",
    font=("Montserrat Bold", 36 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=takeAttendance,
    relief="flat"
)
button_2.place(
    x=703.0,
    y=198.0,
    width=300.0,
    height=226.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=addStu,
    relief="flat"
)
button_3.place(
    x=324.0,
    y=198.0,
    width=300.0,
    height=226.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=index,
    relief="flat"
)
button_4.place(
    x=1082.0,
    y=198.0,
    width=300.0,
    height=226.0
)
#progress in attendance

# getting list of students
path = 'C://Users//mradu//Documents//projct 2//ImagesAttendance'
images = []
classNames = []
myList = os.listdir(path)
for cl in myList:
    classNames.append(os.path.splitext(cl)[0])
stLen = len(classNames)
canvas.create_text(
    1178.0,
    123.0,
    anchor="nw",
    text=stLen,
    fill="#000000",
    font=("Montserrat Regular", 32 * -1)
)

canvas.create_text(
    1174.722900390625,
    94.546142578125,
    anchor="nw",
    text="Total Students Registred",
    fill="#000000",
    font=("Montserrat Regular", 14 * -1)
)

my_rectangle = round_rectangle(
    324.0,
    454.0,
    1382.0,
    676.0,
    radius=19,
    fill="#FFFFFF")

canvas.create_rectangle(
    0.0,
    0.0,
    62.0,
    695.0,
    fill="#3A7FF6",
    outline="")

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=logout,
    relief="flat"
)
button_5.place(
    x=13.0,
    y=651.0,
    width=25.0,
    height=25.0
)

canvas.create_rectangle(
    62.0,
    0.0,
    295.0,
    695.0,
    fill="#FFFFFF",
    outline="")

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=69.0,
    y=113.0,
    width=137.0,
    height=30.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=studentList,
    relief="flat"
)
button_7.place(
    x=69.0,
    y=71.0,
    width=137.0,
    height=30.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=refresh,
    relief="flat"
)
button_8.place(
    x=69.0,
    y=29.0,
    width=137.0,
    height=30.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=15.0,
    y=29.0,
    width=31.0,
    height=26.0

)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=13.0,
    y=77.0,
    width=31.0,
    height=26.0

)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
)
button_11.place(
    x=1269.0,
    y=39.0,
    width=113.0,
    height=34.0
)

my_rectangle2 = round_rectangle(
    689.0,
    69.0,
    927.0,
    123.0,
    radius=19,
    fill="#FFFFFF")


canvas.create_text(
    735.0,
    87.0,
    anchor="nw",
    text="19.12.2020 - 25.12.2020",
    fill="#343A40",
    font=("Roboto Regular", 12 * -1)
)
window.resizable(False, False)
window.mainloop()
