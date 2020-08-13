import cv2
from tkinter import *
from tkinter.filedialog import askopenfile
import numpy as np
import face_recognition
import os
from datetime import datetime


def attendance():
    path = 'ImagesAttendance'
    images = []
    classNames = []
    myList = os.listdir(path)
    print(myList)
    for cls in myList:
        curImg = cv2.imread(f'{path}/{cls}')
        images.append(curImg)
        classNames.append(os.path.splitext(cls)[0])
    print(classNames)

    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    def markAttendance(name):
        with open('Attendance.csv', 'r+') as f:
            myDataList = f.readline()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                dtstring = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtstring}')



    encodeListKnown = findEncodings(images)
    print('encodings complete')

    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            #print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                #print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2-35),(x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                markAttendance(name)

        cv2.imshow('webcam', img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cap.release()


def open_file():
    file = askopenfile(mode='r', filetypes=[('Excel File', '*.csv')])
    if file is not None:
        content = file.read()
        print(content)


root = Tk()

root.geometry("644x480")
root.title("Automatic Attendance System")
root.configure(bg="grey")
root.resizable(0, 0)

# header part
frame = Frame(root, borderwidth=2, bg="black")
frame.grid(row=0, column=0, padx=120, pady=10)

l1 = Label(frame, text="Automatic Attendance System", fg="black", bg="yellow", font="comicsansms 20 bold")
l1.grid(row=0, column=0)



# Body content
f1 = Frame(root, borderwidth=1, bg="black")
f1.grid(row=5, column=0, padx=70, pady=40)

l2 = Label(f1, text="Press Button For Attendance", height=1, width=30, bg="black", fg="white", font="comicsansms 10 bold")
l2.grid(row=0, column=0)
l3 = Label(f1, text="Input Images of students", height=1, width=30, bg="black", fg="white", font="comicsansms 10 bold")
l3.grid(row=1, column=0)
l4 = Label(f1, text="Train Images For Attendance", height=1, width=30, bg="black", fg="white", font="comicsansms 10 bold")
l4.grid(row=2, column=0)
l5 = Label(f1, text="Get Attendance Report", height=1, width=30, bg="black", fg="white", font="comicsansms 10 bold")
l5.grid(row=3, column=0)


b1 = Button(f1, fg="white", bg="blue", height=1, width=30, font="comicsansms 10 bold ", text="Attendance",
            command=attendance)
# b1.pack(side="left",padx=40)
b1.grid(row=0, column=3, pady=20, padx=8)

b2 = Button(f1, fg="white", bg="grey", height=1, width=30, font="comicsansms 10 bold ", text="Input Image")
# b2.pack(side="left",padx=40)
b2.grid(row=1, column=3, pady=20, padx=8)

b3 = Button(f1, fg="white", bg="red", height=1, width=30, font="comicsansms 10 bold ", text="Train Image")
# b3.pack(side="left",padx=40)
b3.grid(row=2, column=3, pady=20, padx=8)

b4 = Button(f1, fg="white", bg="green", height=1, width=30, font="comicsansms 10 bold ", text="Attendance Report",
            command=open_file)
# b4.pack(side="left",padx=40)
b4.grid(row=3, column=3, pady=20, padx=8)
frame1 = Frame(root, borderwidth=0, bg="grey")
frame1.grid(row=7, column=0, padx=120, pady=1)

l10 = Label(frame1, text="@copyright-2020", bg="grey", fg="black", font="comicsansms 10 ")
l10.grid(row=0, column=0)

dev = Frame(root, borderwidth=0, bg="black")
dev.grid(row=8, column=0, padx=70, pady=1)

dev_leb = Label(dev, text="Developers: Shivam Raj, Madhusudan Anand, Abhineet Mishra, Nikita Sanyasi", bg="grey", fg="black", font="comicsansms 10 ")
dev_leb.grid(row=0, column=0)

root.mainloop()
