from tkinter import *

root = Tk()

root.geometry("644x544")
root.title("Automatic Attendance System")

# header part
frame=Frame(root,borderwidth=2, bg="black")
frame.grid(row=0, column=0,padx=120,pady=10)

l1=Label(frame,text="Automatic Attendance System", fg="black",bg="yellow", font="comicsansms 20 bold")
l1.grid(row=0, column=0)



# Body content
f1=Frame(root,borderwidth=1, bg="white")
f1.grid(row=5, column=0,padx=140,pady=80)

l2=Label(f1,text="Press Button For Attendance",bg="white", font="comicsansms 10 bold")
l2.grid(row=0, column=0)
l3=Label(f1,text="Input Images of students",bg="white", font="comicsansms 10 bold")
l3.grid(row=1, column=0)
l4=Label(f1,text="Train Images For Attendance",bg="white", font="comicsansms 10 bold")
l4.grid(row=2, column=0)
l5=Label(f1,text="Get Attendance Report",bg="white", font="comicsansms 10 bold")
l5.grid(row=3, column=0)


b1 = Button(f1, fg="white", bg="blue", text="Attendance", )
# b1.pack(side="left",padx=40)
b1.grid(row=0, column=3,pady=20,padx=8)

b2 = Button(f1, fg="white", bg="grey", text="Input Image")
# b2.pack(side="left",padx=40)
b2.grid(row=1, column=3,pady=20,padx=8)

b3 = Button(f1, fg="white", bg="red", text="Train Image")
# b3.pack(side="left",padx=40)
b3.grid(row=2, column=3,pady=20,padx=8)

b4 = Button(f1, fg="white", bg="green", text="Attendance Report")
# b4.pack(side="left",padx=40)
b4.grid(row=3, column=3,pady=20,padx=8)

# footer part
frame1=Frame(root,borderwidth=0, bg="black")
frame1.grid(row=7, column=0,padx=120,pady=1)

l10=Label(frame1,text="@copyright-2020", fg="black", font="comicsansms 10 ")
l10.grid(row=0, column=0)

dev=Frame(root,borderwidth=0, bg="black")
dev.grid(row=8, column=0,padx=70,pady=1)

dev_leb=Label(dev,text="Developers: Shivam Raj, Madhusudan Anand, Abhineet Mishra, Nikita Sanyasi", fg="black", font="comicsansms 10 ")
dev_leb.grid(row=0, column=0)

root.mainloop()