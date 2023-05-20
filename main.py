from tkinter import*
from tkinter import ttk
#from tkinter.tix import IMAGETEXT
from PIL import Image,ImageTk


class Face_Recognition_System:
    def __init__(self, root ):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")

        #first img
        img=Image.open(r"D:\python\smart attendence system\images\A.jpg") 
        img=img.resize((500,130), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root, image=self.photoimg1) 
        f_lbl.place(x=500,y=0,width=500, height=130)

        # second image

        img1=Image.open(r"D:\python\smart attendence system\images\B.jpg")
        img1=img1.resize((500,130), Image.ANTIALIAS) 
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root, image=self.photoimg1) 
        f_lbl.place(x=500,y=0,width=500, height=130)

        # third imag

        img2=Image.open(r"D:\python\smart attendence system\images\C.jfif")
        img2=img2.resize((500,130), Image.ANTIALIAS) 
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root, image=self.photoimg2) 
        f_lbl.place(x=1000,y=0,width=550, height=130)



