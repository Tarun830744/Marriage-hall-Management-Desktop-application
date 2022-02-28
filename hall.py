from tkinter import *
from PIL  import Image,ImageTk
from tkinter import ttk ,messagebox
import Marriage_Hall_Management
import halladd
import customer
import bookinghall
import payment
import report
import pymongo

class hallmanagement:
    def __init__(self,root):
        self.root= root
        self.root.title("Hall Management System")
        self.root.geometry("1550x795+0+0")
        self.root.state("zoomed")
        self.root.resizable(width=False, height=False)
        #self.root.wn_iconbitmap("city-hall.png")

        self.total_customer = StringVar()
        self.total_booking = StringVar()
        self.total_hall = StringVar()
        
        icon = Image.open("images/city-hall.png")
        self.icon = ImageTk.PhotoImage(icon)
        self.root.iconphoto(FALSE,self.icon)

    #======================logo=============================
        img1 =Image.open("images/logo3.png")
        img1 = img1.resize((230,100),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(self.root,image =self.photoimg1)
        lblimg1.place(x=0,y=0,width =232,height=100)

    #==========================footer======================
        lbl_title = Label(self.root,font =("times new roman",20,"bold"),bg = "black",fg ="gold")
        lbl_title.place(x=1,y=802,width =1550,height =40)

    #====================title=============================
        lbl_title = Label(self.root,text ="Marriage Hall Management",font =("Algerian",40,"bold"),bg = "black",fg ="gold")
        lbl_title.place(x=230,y=0,width =1305,height =100)

   #=======================main frame==========================
        main_frame =Frame(self.root)
        main_frame.place(x=0,y=100,width=1530,height=700)

    #========================menu===========================
        menu_btn = Button(main_frame ,text ="HOME",command = self.home,font =("times new roman",20,"bold"),bg = "black",fg ="gold",bd =2,relief=RIDGE,activeforeground="gold",activebackground="black")
        menu_btn.place(x=0,y=8,width =230)

    #==================CST btn=========================
        cust_btn =Button(main_frame,text = "CUSTOMER",command = self.cust,font =("times new roman",20,"bold"),bg = "black",fg ="gold",bd =2,relief=RIDGE,activeforeground="gold",activebackground="black")
        cust_btn.place(x=0,y=65,width=230)

    #==================book btn===========================
        book_btn =Button(main_frame,text = "BOOKING",command = self.book,font =("times new roman",20,"bold"),bg = "black",fg ="gold",bd =2,relief=RIDGE,activeforeground="gold",activebackground="black")
        book_btn.place(x=0,y=122,width=230)

    #==================payment btn=============================
        payment_btn =Button(main_frame,text = "PAYMENT",command = self.payment,font =("times new roman",20,"bold"),bg = "black",fg ="gold",bd =2,relief=RIDGE,activeforeground="gold",activebackground="black")
        payment_btn.place(x=0,y=179,width=230)

    #====================hall btn========================
        hall_btn =Button(main_frame,text = "HALL MANAGE",command = self.hall_add,font =("times new roman",20,"bold"),bg = "black",fg ="gold",bd =2,relief=RIDGE,activeforeground="gold",activebackground="black")
        hall_btn.place(x=0,y=236,width=230)

    #====================report btn========================
        report_btn =Button(main_frame,text = "REPORT",command =self.report,font =("times new roman",20,"bold"),bg = "black",fg ="gold",bd =2,relief=RIDGE,activeforeground="gold",activebackground="black")
        report_btn.place(x=0,y=293,width=230)

    #====================logout btn========================
        logout_btn =Button(main_frame,text = "LOGOUT",command =self.logout,font =("times new roman",20,"bold"),bg = "black",fg ="gold",bd =2,relief=RIDGE,activeforeground="gold",activebackground="black")
        logout_btn.place(x=0,y=350,width=230)

    #===================frame image============================
        img2 =Image.open("images/hotel1.jpg")
        img2 = img2.resize((1300,700),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        fmimg2 = Label(main_frame,image =self.photoimg2,bd =2)
        fmimg2.place(x=240,y=8,width =1300,height=700)

    #=======================Total==========================
        frame1 = Frame(self.root,bg ="black")
        frame1.place(x = 400,y = 550,width=200,height=200)

        frame2 = Frame(self.root,bg ="black")
        frame2.place(x = 800,y = 550,width=200,height=200)

        frame3 = Frame(self.root,bg ="black")
        frame3.place(x = 1200,y = 550,width=200,height=200)

        lbl1 = Label(frame1,text ="Total Customer",font =("times new roman",20,"bold"),fg ="gold",bg="Black")
        lbl1.place(x =7 ,y =15)

        lbl2 = Label(frame2,text ="Total Booking",font =("times new roman",20,"bold"),fg ="gold",bg="Black")
        lbl2.place(x =15 ,y =15)

        lbl3 = Label(frame3,text ="Total Hall",font =("times new roman",20,"bold"),fg ="gold",bg="Black")
        lbl3.place(x =40 ,y =15)

        entry_lbl1 =Entry(frame1,textvariable=self.total_customer,width=5,font =("times new roman",22,"bold"),state = "readonly",bd =0,readonlybackground="black",fg ="white",justify='center')
        entry_lbl1.place(x = 60, y =65)
        self.total_customer.set(0)

        entry_lbl2 =Entry(frame2,textvariable=self.total_booking,width=5,font =("times new roman",22,"bold"),state = "readonly",bd = 0,readonlybackground="black",fg ="white",justify='center')
        entry_lbl2.place(x = 60, y =65)
        self.total_booking.set(0)

        entry_lbl3 =Entry(frame3,textvariable=self.total_hall,width=5,font =("times new roman",22,"bold"),state = "readonly",bd = 0,readonlybackground="black",fg ="white",justify='center')
        entry_lbl3.place(x = 60, y =65)
        self.total_hall.set(0)

        btnlbl1 = Button(frame1,text="REFRESH",command = self.totalcustomer,font =("times new roman",14,"bold"),bg = "red",fg="black",activeforeground="black",activebackground="red")
        btnlbl1.place(x = 40, y=120,width=120)

        btnlbl2 = Button(frame2,text="REFRESH",command = self.totalbooking,font =("times new roman",14,"bold"),bg = "red",fg="black",activeforeground="black",activebackground="red")
        btnlbl2.place(x = 40, y=120,width=120)

        btnlbl3 = Button(frame3,text="REFRESH",command = self.totalhall,font =("times new roman",14,"bold"),bg = "red",fg="black",activeforeground="black",activebackground="red")
        btnlbl3.place(x = 40, y=120,width=120)

    #=================================contact details=====================================================
        frame4 = Frame(self.root,bg="black")
        frame4.place(x = 1,y = 507,width=230,height=290)

        lbl1 = Label(frame4,text ="CREATED BY",font =("times new roman",20,"bold"),fg ="red",bg="Black")
        lbl1.place(x =20 ,y =0)

        lbl2 = Label(frame4,text ="●Meghanshu Kumrawat",font =("times new roman",16,"bold"),fg ="white",bg="Black")
        lbl2.place(x =7 ,y =35)

        lbl3 = Label(frame4,text ="●Purnesh Kumrawat",font =("times new roman",16,"bold"),fg ="white",bg="Black")
        lbl3.place(x =7 ,y =65)

        lbl4 = Label(frame4,text ="●Raj Choudhary",font =("times new roman",16,"bold"),fg ="white",bg="Black")
        lbl4.place(x =7 ,y =95)

        lbl5 = Label(frame4,text ="●Tarun Choudhary",font =("times new roman",16,"bold"),fg ="white",bg="Black")
        lbl5.place(x =7 ,y =125)

        lbl6 = Label(frame4,text ="CONTACT INFO",font =("times new roman",20,"bold"),fg ="red",bg="Black")
        lbl6.place(x =7 ,y =155)

        lbl7 = Label(frame4,text ="EMAIL",font =("times new roman",16,"bold"),fg ="yellow",bg="Black")
        lbl7.place(x =70 ,y =185)

        lbl8 = Label(frame4,text ="tarunchoudhary.744@gmail.com",font =("times new roman",12,"bold"),fg ="white",bg="Black")
        lbl8.place(x =5 ,y =215)

        lbl9 = Label(frame4,text ="MOBILE NO",font =("times new roman",16,"bold"),fg ="yellow",bg="Black")
        lbl9.place(x =50 ,y =240)

        lbl10 = Label(frame4,text ="7440744369",font =("times new roman",14,"bold"),fg ="white",bg="Black")
        lbl10.place(x =60 ,y =265)

        self.totalcustomer()
        self.totalbooking()
        self.totalhall()

    def cust(self):
        self.new_window_cust = Toplevel(self.root)
        self.obj = customer.cust_win(self.new_window_cust)

    def book(self):
        self.new_window_book = Toplevel(self.root)
        self.obj = bookinghall.booking_win(self.new_window_book)

    def payment(self):
        self.new_window_payment = Toplevel(self.root)
        self.obj = payment.payment_win(self.new_window_payment)

    def hall_add(self):
        self.new_window_hall_add = Toplevel(self.root)
        self.obj = halladd.hall_win(self.new_window_hall_add)

    def report(self):
        self.new_window_report = Toplevel(self.root)
        self.obj = report.report_win(self.new_window_report)

    def logout(self):
        self.root.destroy()
        Marriage_Hall_Management.main()
    
    def home(self):
        self.root.destroy()
        Marriage_Hall_Management.hall_run()

    def totalcustomer(self):
        client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
        db = client["application"]
        col = db["Customer"]
        query = {"_id":0}
        count = 0
        for i in col.find({},query):
            rows =i
            count = count+1
        self.total_customer.set(count)

    def totalbooking(self):
        client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
        db = client["application"]
        col = db["Booking Details"]
        query = {"_id":0}
        count = 0
        for i in col.find({},query):
            rows =i
            count = count+1
        self.total_booking.set(count)

    def totalhall(self):
        client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
        db = client["application"]
        col = db["Hall Manage"]
        query = {"_id":0}
        count = 0
        for i in col.find({},query):
            rows =i
            count = count+1
        self.total_hall.set(count)

