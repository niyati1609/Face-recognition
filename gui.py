from tkinter import *
import os
from tkinter import messagebox as msg
from PIL import ImageTk,Image
import pyttsx3 as py
root=Tk()
root.resizable(False,False)
root.title('Face Recognition System')
root.geometry('1366x768')
frame=Frame(root,width=1366,height=768)
frame.place(x=0,y=0)
def main(root,frame):
    img=ImageTk.PhotoImage(Image.open('C:/Users/HP/Desktop/facedet/e852b05abac18b2a42e13fcaee1f0cd5.jpg'))
    L0=Label(frame,image=img)
    L0.place(x=0,y=0)
    L3=Label(frame,text='Welcome To Face Recogntion Panel',font=('times',30),bd=8,bg='Black',width=60,fg='white',relief=RAISED)
    L3.place(x=10,y=40)
    #img1=ImageTk.PhotoImage(Image.open('C:/Users/HP/Desktop/facedet/download.jfif'))
    #L1=Label(frame,image=img1)
    #L1.place(x=22,y=100)
    L77=Label(frame,text='Click the authentication button below!!',font=('times',16),bd=8,bg='Black',width=26,fg='white',relief=FLAT)
    L77.place(x=510,y=580)
    B30=Button(frame,text='Authentication',command=lambda:adminpage(root,frame),font=('times',17),bd=8,bg='black',width=14,fg='white',relief=RAISED)
    B30.place(x=570,y=650)
    frame.mainloop()
def adminpage(root,frame):
    frame.destroy()
    frame=Frame(root,width=1366,height=768)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('C:/Users/HP/Desktop/facedet/Download-Panda-wallpapers-HD.png'))
    L0=Label(frame,image=img)
    L0.place(x=0,y=0)

    L3=Label(frame,text='Welcome To Login Panel',font=('times',40),bd=8,bg='Black',width=46,fg='white',relief=RAISED)
    L3.place(x=10,y=20)

    img9=ImageTk.PhotoImage(Image.open('C:/Users/HP/Downloads/imageedit_39_6690743420.jpg'))
    L47=Label(frame,image=img9,bd=3,bg='Black',relief=RAISED)
    L47.place(x=920,y=140)
    img10=ImageTk.PhotoImage(Image.open('C:/Users/HP/Downloads/imageedit_32_9365276876.jpg'))
    L48=Label(frame,image=img10,bd=3,bg='Black',relief=RAISED)
    L48.place(x=960,y=352)

   

    #L3=Label(frame,bd=8,bg='salmon3',width=80,height=12,relief=RAISED)
    #L3.place(x=660,y=300)

    def userText(event):
        tts=py.init()
        tts.say("Hello admin... Enter user Name")
        tts.runAndWait()
        E3.delete(0,END)
        E3.config(fg="black")
        usercheck=True

    def passText(event):
        tts=py.init()
        tts.say("Enter Password")
        tts.runAndWait()
        E4.delete(0, END)
        E4.config(fg="black",show="*")
        passcheck=True
    a=StringVar()
    b=StringVar()
    usercheck=False
    passcheck=False

    #L=Label(frame,text='USERNAME',font=('Helvetica',17,'bold'),width=16,height=1,bd=6,bg='salmon4',fg='white',relief=RAISED)
    #L.place(x=680,y=420)
    img11=ImageTk.PhotoImage(Image.open('C:/Users/HP/Downloads/images (6).jpg'))
    L49=Label(frame,image=img11,bd=3,bg='black',relief=RAISED)
    L49.place(x=800,y=413)

    #L1=Label(frame,text=' PASSWORD ',font=('Helvetica',17,'bold'),width=14,height=1,bd=6,bg='salmon4',fg='white',relief=RAISED)
    #L1.place(x=680,y=485)
    img12=ImageTk.PhotoImage(Image.open('C:/Users/HP/Downloads/download (1).png'))
    L50=Label(frame,image=img12,bd=3,bg='black',relief=RAISED)
    L50.place(x=802,y=478)
    E3=Entry(frame,bd=11,fg='black',width=26,font=('times',17)) 
    E3.place(x=930,y=420)
    E3.insert(0,"Username")
    E3.config(fg="grey")
    E3.bind("<Button>",userText)


    E4=Entry(frame,textvariable=b,bd=11,width=26,font=('times',17))
    E4.place(x=930,y=485)
    E4.insert(0,"Password")
    E4.config(fg='grey')
    E4.bind("<Button>",passText)

    def showpassword():
        if(check_var.get()):
            E4.config(show="")
        else:
            E4.config(show="*")  

    check_var = IntVar()
    check_show_psw = Checkbutton(frame, text = "Show", variable = check_var, \
                     onvalue = 1, offvalue = 0, height=1, \
                     width = 5, command = showpassword,background='white')
    check_show_psw.place(x=1160, y=499)

    def adminlogin(root,frame):
           LOGIN="admin"
           PASSWORD="admin"
           a=E3.get()
           b=E4.get()
           L1="niyati"
           P1="niyati"

           if LOGIN==a and PASSWORD==b or L1==a and P1==b: 
                     msg.showinfo("LOGIN","Login Successful")
                     new(root,frame)
           else:
                     msg.showinfo("RETRY","invalid ID or Password")
                     main(root,frame) 
    B2=Button(frame,text='LOGIN',command=lambda:adminlogin(root,frame),font=('Helvetica',17,'bold'),bd=4,bg='Black',fg='white')
    B2.place(x=970,y=550)
    B2=Button(frame,text='BACK',command=lambda:main(root,frame),font=('Helvetica',17,'bold'),bd=4,bg='Black',fg='white')
    B2.place(x=1111,y=550)
    frame.mainloop()
def new(root,frame):
 def function1():
    os.system(" py datasetcreator.py")
 def function2():
    os.system("py trainner.py")
 def function3():
    os.system("py final.py")
 def function4():
    root.destroy()
 root.resizable(False,False)
 root.title('Face Recognition System')
 root.geometry('1366x768')
 frame=Frame(root,width=1366,height=768)
 frame.place(x=0,y=0)
 img34=ImageTk.PhotoImage(Image.open('C:/Users/HP/Desktop/facedet/download.jfif'))
 L05=Label(frame,image=img34)
 L05.place(x=250,y=15)
 img33=ImageTk.PhotoImage(Image.open('C:/Users/HP/Desktop/facedet/logo.png'))
 L04=Label(frame,image=img33)
 L04.place(x=570,y=12)
 img35=ImageTk.PhotoImage(Image.open('C:/Users/HP/Desktop/facedet/download.jfif'))
 L06=Label(frame,image=img34)
 L06.place(x=900,y=15)
 L78=Label(frame,text='Face Recognition Panel',font=('times',24),bd=8,bg='Black',width=73,fg='white',relief=RAISED)
 L78.place(x=10,y=270)
 B300=Button(frame,text='Create Dataset',command=lambda:function1(),font=('times',20),bd=8,bg='black',width=50,fg='white',relief=RAISED)
 B300.place(x=270,y=340)
 B301=Button(frame,text='Train Dataset',command=lambda:function2(),font=('times',20),bd=8,bg='black',width=50,fg='white',relief=RAISED)
 B301.place(x=270,y=440)
 B302=Button(frame,text='Recognize',command=lambda:function3(),font=('times',20),bd=8,bg='black',width=50,fg='white',relief=RAISED)
 B302.place(x=270,y=540)
 B303=Button(frame,text='Exit',command=lambda:function4(),font=('times',20),bd=8,bg='black',width=50,fg='white',relief=RAISED)
 B303.place(x=270,y=640)
 #Button(root,text=" Create Dataset",image=a,compound = LEFT,font=("times new roman",25),bg="white",fg='black',command=function1).grid(row=3,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
 #Button(root,text=" Train Dataset",image=a,compound = LEFT,font=("times new roman",25),bg="white",fg='black',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
 #Button(root,text=" Recognize",image=a,compound = LEFT,font=("times new roman",25),bg="white",fg="black",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
 #Button(root,text="EXIT",font=("times",30,),bg="red",fg="white",command=function4).grid(row=6,sticky=N+E+W+S,padx=5,pady=5)
 frame.mainloop()


    
main(root,frame)
