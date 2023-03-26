import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import pandas as pd
import os.path
from tkinter import *
from tkinter import ttk,messagebox
# import threading

# loadcheck =0
# def load():
#     global loadcheck
#     root = Tk()
#     root.attributes('-fullscreen', 'True','-transparentcolor', '#1f1f1f')
#     frameCnt = 12
#     frames = [PhotoImage(file="C:\\Users\\mradu\\Documents\\projct 2\\load.gif",format = 'gif -index %i' %(i)) for i in range(frameCnt)]

#     def update(ind):

#         frame = frames[ind]
#         ind += 1
#         if ind == frameCnt:
#             ind = 0
#         label.configure(image=frame)
#         if loadcheck==1:
#             root.destroy()
#         root.after(100, update, ind)
#     label = Label(root,bg="#1f1f1f")
#     label.pack(side="top", expand=True, fill="both")
#     root.after(0, update, 0)
#     root.mainloop()

# t1=threading.Thread(target=load).start()
path = 'C://Users//mradu//Documents//projct 2//ImagesAttendance'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def findEncodings(images):
    encodeList = []
    for img in images:
     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
     encode = face_recognition.face_encodings(img)[0]
     encodeList.append(encode)
    return encodeList

def addsub(name):
    path = ('C://Users//mradu//Documents//projct 2//Attendance//'+sub)

    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully Added %s " % path)


def markAttendance(name,sub):
    now = datetime.now()
    tString = now.strftime('%H:%M:%S')
    dString = datetime.today()
    d1 = dString.strftime("%Y-%m-%d")

    path = ('C://Users//mradu//Documents//projct 2//Attendance//'+sub)
    filename=("C://Users//mradu//Documents//projct 2//Attendance//"+ sub +"//"+ d1 +".csv")
    answ=os.path.exists(filename)
    print(answ)
    if (answ):
        pass
    else:
        with open(filename, "w") as f1:
         f1.writelines("Name,Time,Date\n")
         print("5")
    df = pd.read_csv(filename)
    print(df.empty)
    if df.empty:
        with open(filename, "a") as f:
            f.writelines(f'{name},{tString},{d1}\n')
        print(df.empty)
    elif not df.empty:
        for ind in df.index:
            print("3")
            name2 = list(df['Name'])
            for subdir, dirs, files in os.walk(path):
                print("2")
                for file in files:
                    df = pd.read_csv(filename)
                    d2 = file.rsplit('.', 1)[0]
                    if d2==d1:
                        print("1")
                        name2 = list(df['Name'])
                        if name not in name2:
                            with open(filename, "a") as f:
                                f.writelines(f'\n{name},{tString},{d1}')
                            
                    else :
                        print("Your Attandance for today is already taken")
encodeListKnown = findEncodings(images)
print('Encoding Complete')
# loadcheck=1
def Attendance(i):
    
        #print('''#############Welcome To Attendance System###################\n* Registor New Sub\n* Take Attendance\n* Registor new student\n* Press "Q" to quit\n''')
        #i = int(input("Enter your option\n"))

        if i == 1:
            win= Tk()
            win.geometry("550x250")
            label=Label(win, text="Enter The Name Of Subject", font=("calibri 16 bold"))
            label.pack()
            sub= Entry(win, width= 20)
            sub.focus_set()
            sub.pack()
            subject=sub.get()
            ttk.Button(win, text= "Submit",width= 20, command= addsub(subject)).pack(pady=20)
            win.mainloop()
        elif i == 2:
            sub="none"
            #Create an instance of Tkinter frame
            win= Tk()

            #Set the geometry of Tkinter frame
            win.geometry("550x250")
            win.grab_set()
            def passSub():
                print(entry.get())
                takeAttendance(entry.get())
            def takeAttendance(sub):

                cap = cv2.VideoCapture(0)
                while True:
                    success, img = cap.read()
                    # img = captureScreen()
                    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
                    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

                    facesCurFrame = face_recognition.face_locations(imgS)
                    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

                    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                        # print(faceDis)
                        matchIndex = np.argmin(faceDis)

                        if matches[matchIndex]:
                            name = classNames[matchIndex].upper()
                            y1, x2, y2, x1 = faceLoc
                            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                            markAttendance(name,sub)

                    cv2.imshow('Webcam', img)
                    k = cv2.waitKey(1) & 0xFF
                    # press 'q' to exit
                    if k == ord('q'):
                        cv2.destroyAllWindows()
                        break
            #Initialize a Label to display the User Input
            label=Label(win, text="Enter The Subject", font=("calibri 16 bold"))
            label.pack()

            #Create an Entry widget to accept User Input
            entry= Entry(win, width= 20)
            entry.focus_set()
            entry.pack()

            #Create a Button to validate Entry Widget
            ttk.Button(win, text= "Submit",width= 20, command= passSub).pack(pady=20)
            win.mainloop()
        elif i==3:
            name="none"
            win= Tk()

            #Set the geometry of Tkinter frame
            win.geometry("550x250")
            def passSub():
                print(entry.get())
                sayCheese(entry.get())
            def sayCheese(name):
                camera = cv2.VideoCapture(0)
                check, frame = camera.read()
                cv2.imwrite("ImagesAttendance/" + name + ".jpg", frame)
            #Initialize a Label to display the User Input
            label=Label(win, text="Write The Name", font=("calibri 16 bold"))
            label.pack()

            #Create an Entry widget to accept User Input
            entry= Entry(win, width= 20)
            entry.focus_set()
            entry.pack()

            #Create a Button to validate Entry Widget
            ttk.Button(win, text= "Submit",width= 20, command= passSub).pack(pady=20)
            win.mainloop()

