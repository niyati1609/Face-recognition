from tkinter import *
import sqlite3 as sq
from tkinter import messagebox as msg
import scrolling
from PIL import ImageTk,Image
import pyttsx3 as py

root=Tk()
root.resizable(False,False)
root.title('Fruit Management System')
root.geometry('1366x768')
frame=Frame(root,width=1366,height=768)
frame.place(x=0,y=0)

def main(root,frame):
    img=ImageTk.PhotoImage(Image.open('C:/Users/HP/Downloads/586289314-fruit-desktop-wallpaper.jpg'))
    L0=Label(frame,image=img)
    L0.place(x=0,y=0)
    B29=Button(frame,text='USER',font=('times',40),bd=8,bg='green',command=lambda:user(root,frame),width=10,fg='white',relief=RAISED)
    B29.place(x=850,y=180)
    B30=Button(frame,text='ADMIN',command=lambda:adminpage(root,frame),font=('times',40),bd=8,bg='green',width=10,fg='white',relief=RAISED)
    B30.place(x=850,y=500)


    frame.mainloop()
def user(root,frame):
    img15=ImageTk.PhotoImage(Image.open('C:/Users/HP/Downloads/Untitled.png'))
    L49=Label(frame,image=img15)
    L49.place(x=0,y=0)
    L50=Label(frame,text='LOGIN',font=('times',20),bd=4,width=10,fg='black',highlightthickness=0,relief=RAISED)
    L50.place(x=600,y=250)
    L51=Label(frame,text='Username',font=('times',16),bd=4,width=10,bg='white',fg='black',highlightthickness=0,relief=RAISED)
    L51.place(x=460,y=340)
    E35=Entry(frame,bd=4,width=22,font=('times',16))
    E35.place(x=620,y=340)
    L52=Label(frame,text='Password',font=('times',16),bd=4,width=12,bg='white',fg='black',highlightthickness=0,relief=RAISED)
    L52.place(x=450,y=440)
    E36=Entry(frame,bd=4,width=22,font=('times',16))
    E36.place(x=620,y=440)
    B30=Button(frame,text='Log In',command=lambda:(root,frame),font=('times',12),bd=8,bg='white',width=8,fg='black',relief=RAISED)
    B30.place(x=690,y=500)
    frame.mainloop()

def adminpage(root,frame):
    frame.destroy()
    frame=Frame(root,width=1366,height=768)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('C:/Users/HP/Downloads/hd-wallpaper-ivy-wall-207301.jpg'))
    L0=Label(frame,image=img)
    L0.place(x=0,y=0)

    L3=Label(frame,text='ADMIN',font=('times',40),bd=8,bg='LightSalmon4',width=30,fg='white',relief=RAISED)
    L3.place(x=240,y=20)

    img9=ImageTk.PhotoImage(Image.open('C:/Users/HP/Downloads/imageedit_39_6690743420.jpg'))
    L47=Label(frame,image=img9,bd=3,bg='salmon4',relief=RAISED)
    L47.place(x=920,y=140)
    img10=ImageTk.PhotoImage(Image.open('C:/Users/HP/Downloads/imageedit_32_9365276876.jpg'))
    L48=Label(frame,image=img10,bd=3,bg='salmon4',relief=RAISED)
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
    L49=Label(frame,image=img11,bd=3,bg='salmon4',relief=RAISED)
    L49.place(x=800,y=413)

    #L1=Label(frame,text=' PASSWORD ',font=('Helvetica',17,'bold'),width=14,height=1,bd=6,bg='salmon4',fg='white',relief=RAISED)
    #L1.place(x=680,y=485)
    img12=ImageTk.PhotoImage(Image.open('C:/Users/HP/Downloads/download (1).png'))
    L50=Label(frame,image=img12,bd=3,bg='salmon4',relief=RAISED)
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
                     dashboard(root,frame)
           else:
                     msg.showinfo("RETRY","invalid ID or Password")
                     main(root,frame) 
    B2=Button(frame,text='LOGIN',command=lambda:adminlogin(root,frame),font=('Helvetica',17,'bold'),bd=4,bg='salmon4',fg='white')
    B2.place(x=970,y=550)
    B2=Button(frame,text='BACK',command=lambda:main(root,frame),font=('Helvetica',17,'bold'),bd=4,bg='salmon4',fg='white')
    B2.place(x=1111,y=550)
    frame.mainloop()

def dashboard(root,frame):

    frame.destroy()
    frame=Frame(root,width=1366,height=768)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('C:/Users/HP/Downloads/pro1.jpg'))
    L2=Label(frame,image=img)
    L2.place(x=0,y=0)

    L4=Label(frame,text='DASHBOARD',font=('times',40),bd=8,bg='red3',width=40,fg='white',relief=RAISED)
    L4.place(x=70,y=50)

    img1=ImageTk.PhotoImage(Image.open('C:/Users/HP/Downloads/imageedit_4_9388960357.png'))
    L34=Label(frame,image=img1)
    L34.place(x=200,y=180)
    B3=Button(frame,text='SALES',command=lambda:sales(root,frame),font=('Helvetica',25,'bold'),width=8,height=1,bd=5,bg='red3',fg='white')
    B3.place(x=180,y=320)

    
    img2=ImageTk.PhotoImage(Image.open('C:/Users/HP/Downloads/imageedit_13_4188337389.jpg'))
    L35=Label(frame,image=img2)
    L35.place(x=430,y=180)
    B4=Button(frame,text='PRODUCTS',command=lambda:products(root,frame),font=('Helvetica',25,'bold'),width=10,height=1,bd=5,bg='red3',fg='white')
    B4.place(x=400,y=320)

    img3=ImageTk.PhotoImage(Image.open('C:/Users/HP/Downloads/imageedit_18_7075703315.jpg'))
    L36=Label(frame,image=img3)
    L36.place(x=700,y=180)
    B5=Button(frame,text='CUSTOMERS',font=('Helvetica',25,'bold'),command=lambda:customers(root,frame),width=11,height=1,bd=5,bg='red3',fg='white')
    B5.place(x=660,y=320)

    img4=ImageTk.PhotoImage(Image.open('C:/Users/HP/Downloads/imageedit_21_6410899844.jpg'))
    L37=Label(frame,image=img4)
    L37.place(x=970,y=180)
    B6=Button(frame,text='SUPPLIERS',font=('Helvetica',25,'bold'),command=lambda:suppliers(root,frame),width=10,height=1,bd=5,bg='red3',fg='white')
    B6.place(x=940,y=320)

    B7=Button(frame,text='LOGOUT',font=('Helvetica',25,'bold'),width=8,height=1,bd=5,bg='red3',fg='white',command=lambda:main(root,frame))
    B7.place(x=570,y=560)
    img5=ImageTk.PhotoImage(Image.open('C:/Users/HP/Downloads/imageedit_22_3740277394.png'))
    L38=Label(frame,image=img5)
    L38.place(x=590,y=420)

    B8=Button(frame,text='Back',command=lambda:adminpage(root,frame),font=('Helvetica',13,'bold'),width=5,bg='red3',fg='white')
    B8.place(x=1230,y=15)

    L5=Label(frame,text='WELCOME  ADMIN',font=('Helvetica',14,'bold'),bg='red3',width=16,fg='white',relief=RAISED)
    L5.place(x=1026,y=18)

    frame.mainloop()
    
def sales(root,frame):
    frame.destroy()
    frame=Frame(root,width=1366,height=768,bg='white')
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('C:/Users/HP/Downloads/pro4.jpg'))
    L7=Label(frame,image=img)
    L7.place(x=0,y=0)
    L6=Label(frame,text='SALES ',font=('times',40),bd=8,bg='red3',width=40,fg='white',relief=RAISED)
    L6.place(x=70,y=50)

    B9=Button(frame,text='Back',command=lambda:dashboard(root,frame),font=('Helvetica',13,'bold'),width=5,bg='red3',fg='white')
    B9.place(x=1224,y=17)
  #scrolling table
    conn=sq.connect('database01.db')
    cur=conn.execute('''SELECT * from salestable''' )
    scl=scrolling.Scrolling_Area(frame,width=1200,height=400)
    scl.place(x=70,y=210)
    table=scrolling.Table(scl.innerframe,['Product_Name','Generic_Name','Comapany','Price','Amount','Qty','Profit'],column_minwidths=[170,170,170,170,170,170,170])
    table.pack(expand=True,fill=X)
    table.on_change_data(scl.update_viewport)
    data=[]
    for row in cur:
        column=[]
        data.append(column)
        for r in row:
            column.append(r)
    table.set_data(data)

    #E5=Entry(frame,bd=3,width=60,font=('times',17),bg='old lace') 
    #E5.place(x=70,y=150)
    
    #Search=IntVar()
    #Search.set(2000)
    #Search.set('Search Products')

    #E1=OptionMenu(frame,Search,'Apple','Banana','Orange','Cherry','Mango','Plum','Rasperry',
                  #'Jackfruit','Papaya','Kiwi','Melon','Mandrain','Grape','Strawberry','Peach')
    #E1.config(font=('times',20,'bold'),relief=RAISED,width=43,bg='red3',fg='white',highlightthickness=0)
    #E1.place(x=70,y=150)
    B15=Button(frame,text='+ ADD CONTENT',command=lambda:sales_window(root,frame),font=('Helvetica',16,'bold'),width=20,height=1,bg='red3',fg='white')
    B15.place(x=520,y=150)

    B11=Button(frame,text='LogOut',command=lambda:main(frame,root),font=('Helvetica',13,'bold'),width=8,bg='red3',fg='white')
    B11.place(x=1130,y=17)

    L9=Label(frame,text='WELCOME  ADMIN',font=('Helvetica',14,'bold'),bg='red3',width=16,fg='white',relief=RAISED)
    L9.place(x=928,y=21)
    frame.mainloop()
    
def sales_window(root,frame):
    frame.destroy()
    frame=Frame(root,width=1366,height=768,bg='white')
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('C:/Users/HP/Downloads/art-artist-black-and-white-265047.jpg'))
    L18=Label(frame,image=img)
    L18.place(x=0,y=0)
    
    L19=Label(frame,text='Product Name',font=('times',20),bd=4,width=11,fg='black',highlightthickness=0,relief=RAISED)
    L19.place(x=150,y=200)
    L20=Label(frame,text='Generic Name',font=('times',20),width=11,bd=4,fg='black',highlightthickness=0,relief=RAISED)
    L20.place(x=570,y=200)
    L21=Label(frame,text='Category/Description',font=('times',20),width=23,bd=4,fg='black',highlightthickness=0,relief=RAISED)
    L21.place(x=150,y=300)
    L19=Label(frame, text='Price',font=('times',20),bd=4,width=6,fg='black',highlightthickness=0,relief=RAISED)
    L19.place(x=150,y=400)
    L20=Label(frame,text='Qty.',font=('times',20),bd=4,width=6,fg='black',highlightthickness=0,relief=RAISED)
    L20.place(x=520,y=400)
    L21=Label(frame,text='Amount',font=('times',20),bd=4,width=7,fg='black',highlightthickness=0,relief=RAISED)
    L21.place(x=810,y=400)
    L21=Label(frame,text='Profit',font=('times',20),bd=4,width=6,fg='black',highlightthickness=0,relief=RAISED)
    L21.place(x=470,y=490)
    L22=Label(frame,text='Enter The New Data',font=('times',20,'bold'),bd=9,width=50,height=1,fg='black',highlightthickness=0,relief=RAISED)
    L22.place(x=154,y=95)
    
    E8=Entry(frame,bd=4,width=15,font=('times',20)) 
    E8.place(x=340,y=200)
    E9=Entry(frame,bd=4,width=15,font=('times',20))
    E9.place(x=760,y=200)
    E10=Entry(frame,bd=5,width=30,font=('times',20))
    E10.place(x=530,y=300)
    E11=Entry(frame,bd=4,width=15,font=('times',20))
    E11.place(x=270,y=400)
    E12=Entry(frame,bd=4,width=10,font=('times',20))
    E12.place(x=640,y=400)
    E13=Entry(frame,bd=4,width=10,font=('times',20))
    E13.place(x=940,y=400)
    E34=Entry(frame,bd=4,width=12,font=('times',20))
    E34.place(x=590,y=490)

    B18=Button(frame,text='Save',command=lambda:save1(E8,E9,E10,E11,E12,E13,E34),font=('times',17,'bold'),width=13,fg='black',relief=RAISED)
    B18.place(x=200,y=570)
    B19=Button(frame,text='Back',command=lambda:sales(root,frame),font=('times',17,'bold'),width=13,fg='black',relief=RAISED)
    B19.place(x=490,y=570)
    B27=Button(frame,text='Erase All',command=lambda:clr2(),font=('times',17,'bold'),width=13,fg='black',relief=RAISED)
    B27.place(x=800,y=570)
    frame.mainloop()
def save1(E8,E9,E10,E11,E12,E13,E34): 
    t1=E8.get() 
    t2=E9.get() 
    t3=E10.get() 
    t4=E11.get() 
    t5=E12.get()  
    t6=E13.get() 
    t7=E34.get() 
    conn=sq.connect('database01.db') 
    conn.execute('''create table if not exists salestable(Product_Name Text,Generic_Name Text,Comapany Text, 
                     Price INTEGER,Amount INTEGER,Qty INEGER,Profit TEXT)''') 
    conn.execute('''insert into salestable values (?,?,?,?,?,?,?)''',(t1,t2,t3,int(t4),int(t5),int(t6),int(t7))) 
    #conn.execute('''delete from salestable where Amount = 5''')
    #conn.execute('''delete from salestable where Amount = 4''')
    #conn.execute('''drop table salestable''') 
    conn.commit()
    conn.close() 
    msg.showinfo('Data','successfully Added!!') 

def clr2():
    sales_window(root,frame)
     
def products(root,frame):
    frame.destroy()
    frame=Frame(root,width=1366,height=768,bg='white')
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('C:/Users/HP/Downloads/pro5.jpg'))
    L8=Label(frame,image=img)
    L8.place(x=0,y=0)
    L9=Label(frame,text='PRODUCTS ',font=('times',40),bd=8,bg='yellow2',width=40,fg='white',relief=RAISED)
    L9.place(x=70,y=50)

    B9=Button(frame,text='Back',command=lambda:dashboard(root,frame),font=('Helvetica',13,'bold'),width=5,bg='yellow2',fg='white')
    B9.place(x=1224,y=17)
#scrolling table
    conn=sq.connect('database02.db')
    cur=conn.execute('''SELECT * from producttable''' )
    scl=scrolling.Scrolling_Area(frame,width=1200,height=400)
    scl.place(x=70,y=210)
    table=scrolling.Table(scl.innerframe,['Fruit_Name','Generic_Name','Category',
                    'Supplier','Date_received','selling_price','Original_Price','Expiry_Date','Qty'],column_minwidths=[170,170,170,170,170,170,170])
    table.pack(expand=True,fill=X)
    table.on_change_data(scl.update_viewport)
    data=[]
    for row in cur:
        column=[]
        data.append(column)
        for r in row:
            column.append(r)
    table.set_data(data)


   # E5=Entry(frame,bd=3,width=60,font=('times',17),bg='old lace') 
    #E5.place(x=70,y=150)
   # Search=IntVar()
   # Search.set(2000)
   # Search.set('Search Products')

    #E2=OptionMenu(frame,Search,'Apple','Banana','Orange','Cherry','Mango','Plum','Rasperry',
     #             'Jackfruit','Papaya','Kiwi','Melon','Mandrain','Grape','Strawberry','Peach')
    #E2.config(font=('Helvetica',20),relief=RAISED,width=40,bg='yellow2',fg='white',highlightthickness=0)
    #E2.place(x=70,y=150)

    B10=Button(frame,text='+ ADD CONTENT',font=('Helvetica',16,'bold'),command=lambda:products_window(root,frame),width=20,height=1,bg='yellow2',fg='white')
    B10.place(x=520,y=150)
    B11=Button(frame,text='LogOut',command=lambda:main(frame,root),font=('Helvetica',13,'bold'),width=8,bg='yellow2',fg='white')
    B11.place(x=1130,y=17)

    L10=Label(frame,text='WELCOME  ADMIN',font=('Helvetica',14,'bold'),bg='yellow2',width=16,fg='white',relief=RAISED)
    L10.place(x=928,y=21)

    frame.mainloop()

def products_window(root,frame):
    frame.destroy()
    frame=Frame(root,width=1366,height=768,bg='white')
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('C:/Users/HP/Downloads/color-design-flora-1166644.jpg'))
    L18=Label(frame,image=img)
    L18.place(x=0,y=0)
    
    L19=Label(frame,text='Fruit Name',font=('times',20),bd=4,width=11,fg='black',highlightthickness=0,relief=RAISED)
    L19.place(x=170,y=200)
    L20=Label(frame,text='Generic Name',font=('times',20),width=11,bd=4,fg='black',highlightthickness=0,relief=RAISED)
    L20.place(x=590,y=200)
    L21=Label(frame,text='Category/Description',font=('times',20),width=23,bd=4,fg='black',highlightthickness=0,relief=RAISED)
    L21.place(x=170,y=300)
    L19=Label(frame,text='Supplier',font=('times',20),bd=4,width=8,fg='black',highlightthickness=0,relief=RAISED)
    L19.place(x=350,y=400)
    L20=Label(frame,text='Date Received',font=('times',20),bd=4,width=12,fg='black',highlightthickness=0,relief=RAISED)
    L20.place(x=740,y=400)
    L21=Label(frame,text='Original Price',font=('times',20),bd=4,width=12,fg='black',highlightthickness=0,relief=RAISED)
    L21.place(x=390,y=480)
    
    L22=Label(frame,text='Selling Price',font=('times',20),bd=4,width=12,fg='black',highlightthickness=0,relief=RAISED)
    L22.place(x=790,y=480)
    L23=Label(frame,text='Expiry Date',font=('times',20),bd=4,width=10,fg='black',highlightthickness=0,relief=RAISED)
    L23.place(x=985,y=300)
    L24=Label(frame,text='Qty.',font=('times',20),bd=5,fg='black',highlightthickness=0,relief=RAISED)
    L24.place(x=1020,y=200)
    L25=Label(frame,text='Enter New Product',font=('times',20,'bold'),bd=9,width=70,height=1,fg='black',highlightthickness=0,relief=RAISED)
    L25.place(x=170,y=60)
    L26=Label(frame,text='**Filling all Entry Is Compulsory',font=('times',10,'bold'),bd=9,fg='black',highlightthickness=0,)
    L26.place(x=170,y=150)
    
    E14=Entry(frame,bd=4,width=15,font=('times',20)) 
    E14.place(x=360,y=200)
    E15=Entry(frame,bd=4,width=15,font=('times',20))
    E15.place(x=780,y=200)
    E16=Entry(frame,bd=5,width=30,font=('times',20))
    E16.place(x=540,y=300)
    E17=Entry(frame,bd=4,width=15,font=('times',20))
    E17.place(x=500,y=400)
    E18=Entry(frame,bd=4,width=12,font=('times',20))
    E18.place(x=950,y=400)
    E19=Entry(frame,bd=4,width=12,font=('times',20))
    E19.place(x=600,y=480)
    E20=Entry(frame,bd=4,width=12,font=('times',20))
    E20.place(x=1000,y=480)
    E21=Entry(frame,bd=4,width=8,font=('times',20))
    E21.place(x=1160,y=300)
    E22=Entry(frame,bd=4,width=6,font=('times',20))
    E22.place(x=1090,y=200)

    B18=Button(frame,text='Save',font=('times',17,'bold'),command=lambda:save2(E14,E15,E16,E17,E18,E19,E20,E21,E22),width=13,fg='black',relief=RAISED)
    B18.place(x=370,y=580)
    B19=Button(frame,text='Back',command=lambda:products(root,frame),font=('times',17,'bold'),width=13,fg='black',relief=RAISED)
    B19.place(x=670,y=580)
    B20=Button(frame,text='Erase',command=lambda:clr1(),font=('times',17,'bold'),width=13,fg='black',relief=RAISED)
    B20.place(x=970,y=580)
    frame.mainloop()

def save2(E14,E15,E16,E17,E18,E19,E20,E21,E22):
     t1=E14.get()
     t2=E15.get()
     t3=E16.get()
     t4=E17.get()
     t5=E18.get()
     t6=E19.get()
     t7=E20.get()
     t8=E21.get()
     t9=E22.get()
     conn=sq.connect('database02.db')
     conn.execute('''create table if not exists producttable(Fruit_Name Text,Generic_Name Text,Category Text,
                    Supplier Text,Date_received INTVAR,selling_price INTVAR,Original_Price INTVAR,Expiry_Date INTVAR,Qty INTEGER)''')
     conn.execute('''insert into producttable values (?,?,?,?,?,?,?,?,? )''',(t1,t2,t3,t4,t5,t6,t7,t8,int(t9)))
     #conn.execute('''delete from salestable where Amount = 2''')
     conn.commit()
     conn.close()
     msg.showinfo('Message','successfully Added!!')

def clr1():
    products_window(root,frame)
     
#Fruit_Name Text,Generic_Name Text,Category Text, Supplier Text,Date_received INTVAR,selling_price INTVAR,Original_Price INTVAR,Expiry_Date INTVAR,Qty INTEGER
     #?,?,?,?,?,?,?,?,? )''',(t1,t2,t3,t4,t5,t6,t7,t8,int(t9))
def customers(root,frame):
    frame.destroy()
    frame=Frame(root,width=1366,height=768,bg='white')
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('C:/Users/HP/Downloads/pro3.jpg'))
    L11=Label(frame,image=img)
    L11.place(x=0,y=0)

    L12=Label(frame,text='CUSTOMERS',font=('times',40),bd=8,bg='sienna1',width=40,fg='white',relief=RAISED)
    L12.place(x=70,y=50)

    B12=Button(frame,text='Back',command=lambda:dashboard(root,frame),font=('Helvetica',13,'bold'),width=5,bg='sienna1',fg='white')
    B12.place(x=1224,y=17)

    #Search=IntVar()
    #Search.set(2000)
    #Search.set('Search Products')

    #scrolling table
    conn=sq.connect('database03.db')
    cur=conn.execute('''SELECT * from customertable''' )
    scl=scrolling.Scrolling_Area(frame,width=1800,height=450)
    scl.place(x=70,y=210)
    table=scrolling.Table(scl.innerframe,['Customer_ID','Customer_Name','Note','Address','Contact_number'],column_minwidths=[240,240,240,240,240])
    table.pack(expand=True,fill=X)
    table.on_change_data(scl.update_viewport)
    data=[]
    for row in cur:
        column=[]
        data.append(column)
        for r in row:
            column.append(r)
    table.set_data(data)

    #E6=OptionMenu(frame,Search,'Apple','Banana','Orange','Cherry','Mango','Plum','Rasperry',
    #              'Jackfruit','Papaya','Kiwi','Melon','Mandrain','Grape','Strawberry','Peach')
    #E6.config(font=('Helvetica',20),relief=RAISED,width=40,bg='sienna1',fg='white',highlightthickness=0)
    #E6.place(x=70,y=150)

    B13=Button(frame,text='+ ADD PRODUCT',command=lambda:customer_window(root,frame),font=('Helvetica',16,'bold'),width=20,height=1,bg='sienna1',fg='white')
    B13.place(x=520,y=150)

    B14=Button(frame,text='LogOut',command=lambda:main(frame,root),font=('Helvetica',13,'bold'),width=8,bg='sienna1',fg='white')
    B14.place(x=1130,y=17)

    L13=Label(frame,text='WELCOME  ADMIN',font=('Helvetica',14,'bold'),bg='sienna1',width=16,fg='white',relief=RAISED)
    L13.place(x=928,y=20)
    frame.mainloop()

def customer_window(root,frame):
    frame.destroy()
    frame=Frame(root,width=1366,height=768,bg='white')
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('C:/Users/HP/Downloads/art-artist-black-and-white-265047.jpg'))
    L27=Label(frame,image=img)
    L27.place(x=0,y=0)
    L28=Label(frame,text='Customer ID',font=('times',20),bd=4,width=11,fg='black',highlightthickness=0,relief=RAISED)
    L28.place(x=150,y=200)
    L29=Label(frame,text='Customer Name',font=('times',20),width=12,bd=4,fg='black',highlightthickness=0,relief=RAISED)
    L29.place(x=570,y=200)
    L30=Label(frame,text='Note',font=('times',20),width=11,bd=4,fg='black',highlightthickness=0,relief=RAISED)
    L30.place(x=150,y=300)
    L31=Label(frame,text='Address',font=('times',20),bd=4,width=11,fg='black',highlightthickness=0,relief=RAISED)
    L31.place(x=150,y=400)
    L32=Label(frame,text='Contact Number',font=('times',20),bd=4,width=13,fg='black',highlightthickness=0,relief=RAISED)
    L32.place(x=150,y=480)
    L33=Label(frame,text='Enter The New Data',font=('times',20,'bold'),bd=9,width=50,height=1,fg='black',highlightthickness=0,relief=RAISED)
    L33.place(x=154,y=95)

    E23=Entry(frame,bd=4,width=15,font=('times',20)) 
    E23.place(x=340,y=200)
    E24=Entry(frame,bd=4,width=15,font=('times',20))
    E24.place(x=770,y=200)
    E25=Entry(frame,bd=5,width=45,font=('times',20))
    E25.place(x=340,y=300)
    E26=Entry(frame,bd=4,width=45,font=('times',20))
    E26.place(x=340,y=400)
    E27=Entry(frame,bd=4,width=17,font=('times',20))
    E27.place(x=370,y=480)

    B21=Button(frame,text='Save',command=lambda:save3(E23,E24,E25,E26,E27), font=('times',17,'bold'),width=13,fg='black',relief=RAISED)
    B21.place(x=250,y=550)
    B22=Button(frame,text='Back',command=lambda:customers(root,frame),font=('times',17,'bold'),width=13,fg='black',relief=RAISED)
    B22.place(x=550,y=550)
    B23=Button(frame,text='Erase',command=lambda:clr(),font=('times',17,'bold'),width=13,fg='black',relief=RAISED)
    B23.place(x=850,y=550)
    frame.mainloop()

def save3(E23,E24,E25,E26,E27):
     t1=E23.get()
     t2=E24.get()
     t3=E25.get()
     t4=E26.get()
     t5=E27.get()
     conn=sq.connect('database03.db')
     conn.execute('''create table if not exists customertable(Customer_ID INTVAR PRIMARY KEY,Customer_Name Text NOT NULL,Note Text,
                    Address INTVAR,Contact_number INTEGER)''')
     conn.execute('''insert into customertable values (?,?,?,?,? )''',(t1,t2,t3,t4,int(t5)))
     #conn.execute('''delete from salestable where Amount = 2''')
     conn.commit()
     conn.close()
     msg.showinfo('Message','successfully Added!!')

def clr():
    customer_window(root,frame)

def suppliers(root,frame):
    frame.destroy()
    frame=Frame(root,width=1366,height=768,bg='white')
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('C:/Users/HP/Downloads/pro33.jpg'))
    L14=Label(frame,image=img)
    L14.place(x=0,y=0)
    L15=Label(frame,text='SUPPLIERS',font=('times',40),bd=8,bg='hot pink',width=40,fg='white',relief=RAISED)
    L15.place(x=70,y=50)
    
    B12=Button(frame,text='Back',command=lambda:dashboard(root,frame),font=('Helvetica',13,'bold'),width=5,bg='hot pink',fg='white')
    B12.place(x=1224,y=17)
    
   # Search=IntVar()
    #Search.set(2000)
    #Search.set('Search Products')

   #scrolling table
    conn=sq.connect('database04.db')
    cur=conn.execute('''SELECT * from suppliertable''' )
    scl=scrolling.Scrolling_Area(frame,width=1800,height=450)
    scl.place(x=70,y=210)
    table=scrolling.Table(scl.innerframe,['Supplier_Name','Supplier_ID','Address','Contact_person','Contact_number','Fruit_supplying'],column_minwidths=[200,200,200,200,200,200])
    table.pack(expand=True,fill=X)
    table.on_change_data(scl.update_viewport)
    data=[]
    for row in cur:
        column=[]
        data.append(column)
        for r in row:
            column.append(r)
    table.set_data(data)

    #E7=OptionMenu(frame,Search,'Apple','Banana','Orange','Cherry','Mango','Plum','Rasperry',
     #             'Jackfruit','Papaya','Kiwi','Melon','Mandrain','Grape','Strawberry','Peach')
    #E7.config(font=('Helvetica',20),relief=RAISED,width=40,bg='hot pink',fg='white',highlightthickness=0)
    #E7.place(x=70,y=150)

    B17=Button(frame,text='+ ADD PRODUCT',command=lambda:supplier_window(root,frame),font=('Helvetica',16,'bold'),width=20,height=1,bg='hot pink',fg='white')
    B17.place(x=520,y=150)

    B14=Button(frame,text='LogOut',command=lambda:main(frame,root),font=('Helvetica',13,'bold'),width=8,bg='hot pink',fg='white')
    B14.place(x=1130,y=17)

    L16=Label(frame,text='WELCOME  ADMIN',font=('Helvetica',14,'bold'),bg='hot pink',width=16,fg='white',relief=RAISED)
    L16.place(x=928,y=20)
    frame.mainloop()
def supplier_window(root,frame):
    frame.destroy()
    frame=Frame(root,width=1366,height=768,bg='white')
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('C:/Users/HP/Downloads/art-artistic-background-1831234.jpg'))
    L39=Label(frame,image=img)
    L39.place(x=0,y=0)
    
    L40=Label(frame,text='Supplier Name',font=('times',20,'bold'),bd=4,width=12,fg='white',bg='hot pink',highlightthickness=0,relief=RAISED)
    L40.place(x=150,y=200)
    L41=Label(frame,text='Supplier ID',font=('times',20,'bold'),width=12,bd=4,fg='white',bg='hot pink',highlightthickness=0,relief=RAISED)
    L41.place(x=660,y=200)
    L42=Label(frame,text='Address',font=('times',20,'bold'),width=10,bd=4,fg='white',highlightthickness=0,bg='hot pink',relief=RAISED)
    L42.place(x=150,y=300)
    L43=Label(frame,text='Contact Person',font=('times',20,'bold'),bd=4,width=12,bg='hot pink',fg='white',highlightthickness=0,relief=RAISED)
    L43.place(x=150,y=400)
    L44=Label(frame,text='Contact No.',font=('times',20,'bold'),bd=4,width=12,bg='hot pink',fg='white',highlightthickness=0,relief=RAISED)
    L44.place(x=650,y=400)
    L45=Label(frame,text='Fruit Supplying',font=('times',20,'bold'),bd=4,width=13,bg='hot pink',fg='white',highlightthickness=0,relief=RAISED)
    L45.place(x=410,y=480)
    L46=Label(frame,text='Enter The Supplier Data',font=('times',22,'bold'),bg='hot pink',bd=12,width=50,height=1,fg='white',highlightthickness=0,relief=RAISED)
    L46.place(x=210,y=95)
    
    E28=Entry(frame,bd=4,width=17,font=('times',20)) 
    E28.place(x=370,y=200)
    E29=Entry(frame,bd=4,width=17,font=('times',20))
    E29.place(x=880,y=200)
    E30=Entry(frame,bd=5,width=50,font=('times',20))
    E30.place(x=350,y=300)
    E31=Entry(frame,bd=4,width=17,font=('times',20))
    E31.place(x=370,y=400)
    E32=Entry(frame,bd=4,width=17,font=('times',20))
    E32.place(x=870,y=400)
    E33=Entry(frame,bd=4,width=17,font=('times',20))
    E33.place(x=650,y=480)

    B24=Button(frame,text='Save',font=('times',17,'bold'),width=12,fg='white',command=lambda:save4(E28,E29,E30,E31,E32,E33),bg='hot pink',relief=RAISED)
    B24.place(x=220,y=570)
    B25=Button(frame,text='Back',command=lambda:suppliers(root,frame),bg='hot pink',font=('times',17,'bold'),width=12,fg='white',relief=RAISED)
    B25.place(x=530,y=570)
    B26=Button(frame,text='Erase All',font=('times',17,'bold'),command=lambda:clear(),width=12,fg='white',bg='hot pink',relief=RAISED)
    B26.place(x=830,y=570)
    frame.mainloop()

def save4(E28,E29,E30,E31,E32,E33):
     t1=E28.get()
     t2=E29.get()
     t3=E30.get()
     t4=E31.get()
     t5=E32.get()
     t6=E33.get()
     conn=sq.connect('database04.db')
     conn.execute('''create table if not exists suppliertable(Supplier_Name Text,Supplier_ID INTVAR PRIMARY KEY,Address INTVAR NOT NULL,Contact_person Text,
                    Contact_number INTVAR,Fruit_supplying INTVAR)''')
     conn.execute('''insert into suppliertable values (?,?,?,?,?,? )''',(t1,t2,t3,t4,t5,t6))
     #conn.execute('''delete from salestable where Amount = 2''')
     conn.commit()
     conn.close()
     msg.showinfo('Message','successfully Added!!')
def clear():
    supplier_window(root,frame)

main(root,frame)
