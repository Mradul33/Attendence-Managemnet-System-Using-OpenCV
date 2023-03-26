from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,filedialog,messagebox
from PIL import ImageTk,Image
import cv2
from test4 import savefile
import os


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./asset")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)   
def open():
    global image
    result = messagebox.askquestion("Upload Your Photo", "Press 'YES' to take Photo and 'NO' to Uplaod")
    if result == 'yes':
        camera = cv2.VideoCapture(0)
        check, image = camera.read()
        if check:
            cv2.imshow("Photo Captured", image)
            cv2.imwrite('C:\\Users\\mradu\\Documents\\projct 2\\ImagesAttendance\\temp.jpg', image)
            k = cv2.waitKey(1) & 0xFF
            if k == ord('q'):
                cv2.destroyAllWindows()
        image =Image.open('C:\\Users\\mradu\\Documents\\projct 2\\ImagesAttendance\\temp.jpg')
        root.image = ImageTk.PhotoImage(image)
        button_2.config(image=root.image)
            
    else:
        root.file_name=filedialog.askopenfilename(initialdir="your directory path", title="file uploader",
                                filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
        # takes path that is selected by dialog box
        selected_image =Image.open(root.file_name)
        image = selected_image.save('C:\\Users\\mradu\\Documents\\projct 2\\ImagesAttendance\\temp.jpg')
        # resize image with pillow 
        image = selected_image.resize((300, 210), Image.ANTIALIAS)
        # displays an image
        root.image = ImageTk.PhotoImage(image)
        button_2.config(image=root.image)
def home():
    root.destroy()
    import dashboard

root = Tk()
root.geometry("1407x695")
root.configure(bg = "#F8FAFF")
root.title("Student Form")


canvas = Canvas(
    root,
    bg = "#F8FAFF",
    height = 695,
    width = 1407,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)


canvas.create_text(
    104.54791259765625,
    224.0,
    anchor="nw",
    text="Enrollment No",
    fill="#333333",
    font=("Roboto", 12 * -1)
)

button_HOMEIMG = PhotoImage(
    file=relative_to_assets("HOME2.png"))
button_HOME = Button(
    image=button_HOMEIMG,
    borderwidth=0,
    highlightthickness=0,
    command=home,
    relief="flat"
)
button_HOME.place(
    x=6.0,
    y=7.0,
    width=99.0,
    height=31.0
)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry(form).png"))
entry_bg_1 = canvas.create_image(
    254.59500122070312,
    274.0899963378906,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=101.0,
    y=251.0,
    width=307.19000244140625,
    height=44.17999267578125
)

canvas.create_text(
    448.71783447265625,
    224.0,
    anchor="nw",
    text="Name",
    fill="#333333",
    font=("Roboto", 12 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry(form).png"))
entry_bg_2 = canvas.create_image(
    602.5939483642578,
    274.0918884277344,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_2.place(
    x=449.0,
    y=251.0,
    width=307.1878967285156,
    height=44.18377685546875
)

canvas.create_text(
    104.54791259765625,
    320.2162170410156,
    anchor="nw",
    text="Father Name",
    fill="#333333",
    font=("Roboto", 12 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry(form).png"))
entry_bg_3 = canvas.create_image(
    254.5939483642578,
    370.09189224243164,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_3.place(
    x=101.0,
    y=347.0,
    width=307.1878967285156,
    height=44.18378448486328
)

canvas.create_text(
    448.71783447265625,
    320.2162170410156,
    anchor="nw",
    text="E-Mail",
    fill="#333333",
    font=("Roboto", 12 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry(form).png"))
entry_bg_4 = canvas.create_image(
    602.5939483642578,
    370.09189224243164,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_4.place(
    x=449.0,
    y=347.0,
    width=307.1878967285156,
    height=44.18378448486328
)

canvas.create_text(
    104.54791259765625,
    410.0,
    anchor="nw",
    text="Phone number",
    fill="#333333",
    font=("Roboto", 12 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry(form).png"))
entry_bg_5 = canvas.create_image(
    254.5939483642578,
    462.09189224243164,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_5.place(
    x=101.0,
    y=439.0,
    width=307.1878967285156,
    height=44.18378448486328
)

canvas.create_rectangle(
    101.0,
    525.0,
    746.0,
    525.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    107.0,
    215.0,
    752.0,
    215.0,
    fill="#000000",
    outline="")

canvas.create_text(
    101.0,
    37.0,
    anchor="nw",
    text="Registor\nStudent",
    fill="#42505C",
    font=("Roboto Bold", 54 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    1123.660400390625,
    417.1090393066406,
    image=image_image_1
)

def save():
    
    Enrollment_No = entry_1.get()
    Name= entry_2.get()
    Father_Name = entry_3.get()
    EMail = entry_4.get()
    Contact = entry_5.get()
    
    savefile(Enrollment_No, Name, Father_Name, EMail, Contact)
    x = Name.split()
    old_name=("C:\\Users\\mradu\\Documents\\projct 2\\ImagesAttendance\\temp.jpg")
    new_name=(f"C:\\Users\\mradu\\Documents\\projct 2\\ImagesAttendance\\{x[0]}.jpg")
    os.rename(old_name, new_name)
    root.destroy()
    import dashboard

    


button_image_1 = PhotoImage(
    file=relative_to_assets("registor.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=save,
    relief="flat"
)
button_1.place(
    x=355.0,
    y=540.4375,
    width=149.0,
    height=37.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("upload.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=open,
    relief="flat",
    bg="#F8FAFF"
)
button_2.place(
    x=593.0,
    y=38.0,
    width=127.02083587646484,
    height=127.01998901367188
)
root.resizable(False, False)
root.mainloop()