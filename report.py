from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import pymongo
import random
from tkinter import  messagebox
from tkcalendar import DateEntry


class report_win:
    def __init__(self,root):
        self.root= root
        self.root.title("Report")
        self.root.geometry("1300x663+233+130")
        self.root.resizable(width=False, height=False)

        self.var_third_entry = StringVar()

        icon = Image.open("images/city-hall.png")
        self.icon = ImageTk.PhotoImage(icon)
        self.root.iconphoto(FALSE,self.icon)
    #==========================logo========================
        img1 =Image.open("images/logo3.png")
        img1 = img1.resize((100,50),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(self.root,image =self.photoimg1)
        lblimg1.place(x=0,y=0,width =100,height=50)



    #==========================title fo report======================
        lbl_title = Label(self.root,text ="Report",font =("times new roman",20,"bold"),bg = "black",fg ="gold")
        lbl_title.place(x=100,y=0,width =1195,height =50)

    #==============================tabel frame===========================
        frame_tabel = LabelFrame(self.root,font =("times new roman",18,"bold"),bd= 5 ,relief = RIDGE)
        frame_tabel.place(x=3,y=105,width= 1290, height =555)


    #============================searching combo===============================
        self.category =["Select","Customer Details","Booking Details","Hall Available Details","Hall Details","Payment Details"]
        self.customer_details =["Select","Customer No","Email","Pincode"]
        self.booking_details=["Select","Booking ID","Customer No","Booking Date","Hall Name"]
        self.hall_details =["Select","Hall Name","Hall Limit"]
        self.payment_details =["Select","Booking ID","Customer No","Booking Date"]

        lblsearch = Label(self.root,text ="Search By :",font =("times new roman",16,"bold"),fg="black")
        lblsearch.place(x =3 ,y =60)

        self.combo_first = ttk.Combobox(self.root,value=self.category,font =("times new roman",16),width = 18,state ="readonly")
        self.combo_first.current(0)
        self.combo_first.place(x = 110,y=62)
        self.combo_first.bind("<<ComboboxSelected>>",self.categories)

        self.combo_second = ttk.Combobox(self.root,value =[""],font =("times new roman",16),width = 18,state ="readonly")
        self.combo_second.current(0)
        self.combo_second.place(x = 440,y=62)
        self.combo_second.bind("<<ComboboxSelected>>",self.booking_date)

        third =ttk.Entry(self.root,textvariable =self.var_third_entry,width=18,font =("times new roman",16))
        third.place(x = 770,y = 62)

        btnsearch= Button(self.root,text="SEARCH",command =self.search,width =9,font =("times new roman",12,"bold"),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btnsearch.place(x = 980,y =60)

        btnsearch= Button(self.root,text="SHOW ALL",command = self.showall,width =10,font =("times new roman",12,"bold"),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btnsearch.place(x = 1080,y =60)

        btnsearch= Button(self.root,text="RESET",command = self.reset,width =9,font =("times new roman",12,"bold"),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btnsearch.place(x = 1190,y =60)


    def combo(self):
        lbldate = Label(self.root,text ="           ",font =("times new roman",16,"bold"),fg="black")
        lbldate.place(x =370 ,y =60)

        lbltime = Label(self.root,text ="           ",font =("times new roman",16,"bold"),fg="black")
        lbltime.place(x =700 ,y =60)

        self.combo_second = ttk.Combobox(self.root,font =("times new roman",16),width = 18,state ="readonly")
        self.combo_second.place(x = 440,y=62)
        self.combo_second.bind("<<ComboboxSelected>>",self.booking_date)


        third =ttk.Entry(self.root,textvariable =self.var_third_entry,width=18,font =("times new roman",16))
        third.place(x = 770,y = 62)

    def labelprint(self):
        lbldate = Label(self.root,text ="Date :",font =("times new roman",16,"bold"),fg="black")
        lbldate.place(x =370 ,y =60)

        lbltime = Label(self.root,text ="Time :",font =("times new roman",16,"bold"),fg="black")
        lbltime.place(x =700 ,y =60)

    def reset(self):
        self.destroy_tabel()
        self.combo_first.set("Select")
        self.combo()

    def destroy_tabel(self):
        if self.combo_first.get()=="Customer Details":
            self.cust_details_tabel.destroy()
        if self.combo_first.get()=="Booking Details":
            self.booking_details_tabel.destroy()
        if self.combo_first.get()=="Hall Available Details":
            self.available_details_tabel.destroy()
        if self.combo_first.get()=="Payment Details":
            self.payment_details_tabel.destroy()
        if self.combo_first.get()=="Hall Details":
            self.hall_details_tabel.destroy()

    def categories(self,event =""):
        if self.combo_first.get()=="Customer Details":
            self.combo()
            self.combo_second.config(value = self.customer_details)
            self.combo_second.current(0)

        if self.combo_first.get()=="Booking Details":
            self.combo()
            self.combo_second.config(value = self.booking_details)
            self.combo_second.current(0)

        if self.combo_first.get()=="Hall Available Details":
            self.labelprint()

            self.co_date=DateEntry(self.root,width=18,selectmode ='day',font =("times new roman",16))
            self.co_date.place(x = 440,y = 62)
            self.co_date.bind("<<ComboboxSelected>>",self.categories)

            self.combo_time = ttk.Combobox(self.root,font =("times new roman",16),width = 19,state ="readonly")
            self.combo_time["value"]=("Select","Day","Night","Full Day")
            self.combo_time.current(0)
            self.combo_time.place(x = 770,y=62,width =204)

        if self.combo_first.get()=="Hall Details":
            self.combo()
            self.combo_second.config(value = self.hall_details)
            self.combo_second.current(0)

        if self.combo_first.get()=="Payment Details":
            self.combo()
            self.combo_second.config(value = self.payment_details)
            self.combo_second.current(0)

    def booking_date(self,event=""):
        if self.combo_second.get() == "Booking Date":
            self.date=DateEntry(self.root,width=19,selectmode ='day',font =("times new roman",16))
            self.date.place(x = 770,y = 62,width=204)
            self.date.bind("<<ComboboxSelected>>",self.booking_date)

        if self.combo_second.get()=="Customer No":
            third =ttk.Entry(self.root,textvariable =self.var_third_entry,width=18,font =("times new roman",16))
            third.place(x = 770,y = 62)

        if self.combo_second.get()=="Hall Name":
            third =ttk.Entry(self.root,textvariable =self.var_third_entry,width=18,font =("times new roman",16))
            third.place(x = 770,y = 62)

        if self.combo_second.get()=="Booking ID":
            third =ttk.Entry(self.root,textvariable =self.var_third_entry,width=18,font =("times new roman",16))
            third.place(x = 770,y = 62)


#========================================customer detial================================================================
    def customer_tabel(self):
            show_frame =Frame(self.root,bd =2,relief =RIDGE)
            show_frame.place(x=8,y=112,width=1280,height=543)

            scroll_x = ttk.Scrollbar(show_frame,orient=HORIZONTAL)
            scroll_y = ttk.Scrollbar(show_frame,orient=VERTICAL)

            self.cust_details_tabel=ttk.Treeview(show_frame,column=("Ref","Cname","Fname","Gender","Mobile","Email","Nat","Id Proof","Id Number","Address","Pincode"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)

            scroll_x.config(command=self.cust_details_tabel.xview)
            scroll_y.config(command=self.cust_details_tabel.yview)

            self.cust_details_tabel.heading("Ref",text="Reference No")
            self.cust_details_tabel.heading("Cname",text="Customer Name")
            self.cust_details_tabel.heading("Fname",text="Father Name")
            self.cust_details_tabel.heading("Gender",text="Gender")
            self.cust_details_tabel.heading("Mobile",text="Mobile No")
            self.cust_details_tabel.heading("Email",text="Email")
            self.cust_details_tabel.heading("Nat",text="Nationality")
            self.cust_details_tabel.heading("Id Proof",text="Id Proof")
            self.cust_details_tabel.heading("Id Number",text="Id Number")
            self.cust_details_tabel.heading("Address",text="Address")
            self.cust_details_tabel.heading("Pincode",text="Pincode")

            self.cust_details_tabel["show"] ="headings"

            self.cust_details_tabel.column("Ref",width=100,anchor= CENTER)
            self.cust_details_tabel.column("Cname",width=100,anchor=CENTER)
            self.cust_details_tabel.column("Fname",width=100,anchor= CENTER)
            self.cust_details_tabel.column("Gender",width=100,anchor= CENTER)
            self.cust_details_tabel.column("Mobile",width=100,anchor= CENTER)
            self.cust_details_tabel.column("Email",width=100,anchor= CENTER)
            self.cust_details_tabel.column("Nat",width=100,anchor= CENTER)
            self.cust_details_tabel.column("Id Proof",width=100,anchor= CENTER)
            self.cust_details_tabel.column("Id Number",width=100,anchor= CENTER)
            self.cust_details_tabel.column("Address",width=100,anchor= CENTER)
            self.cust_details_tabel.column("Pincode",width=100,anchor= CENTER)
            self.cust_details_tabel.pack(fill=BOTH,expand=1)

    def customer_search(self):
        if self.combo_second.get()=="Select":
            messagebox.showerror("Error","Select Something",parent = self.root)
        elif self.combo_second.get()=="":
            messagebox.showerror("Error","Enter the text field",parent = self.root)
        else:
            client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
            db = client["application"]
            col = db["Customer"]
            if self.combo_second.get()=="Customer No":
                query1 = {"mobile":self.var_third_entry.get()}
                for i in col.find(query1):
                    rows =i
                    if len(rows)!=0:
                        self.cust_details_tabel.delete(*self.cust_details_tabel.get_children())
                        t = tuple(rows.values())
                        self.cust_details_tabel.insert("",END,values =t[1:12])
                        self.combo_second.set("Select")
                        self.var_third_entry.set("")
                        break
                else:
                    messagebox.showerror("Error","This number is not register",parent = self.root)
                    self.combo_second.set("Select")
                    self.var_third_entry.set("")

            if self.combo_second.get()=="Email":
                query1 = {"email":self.var_third_entry.get()}
                for i in col.find(query1):
                    rows =i
                    if len(rows)!=0:
                        self.cust_details_tabel.delete(*self.cust_details_tabel.get_children())
                        t = tuple(rows.values())
                        self.cust_details_tabel.insert("",END,values =t[1:12])
                        self.combo_second.set("Select")
                        self.var_third_entry.set("")
                        break
                else:
                    messagebox.showerror("Error","This email is not register",parent = self.root)
                    self.combo_second.set("Select")
                    self.var_third_entry.set("")


            if self.combo_second.get()=="Pincode":
                query1 = {"pincode":self.var_third_entry.get()}
                for i in col.find(query1):
                    rows =i
                    if len(rows)!=0:
                        self.cust_details_tabel.delete(*self.cust_details_tabel.get_children())
                        t = tuple(rows.values())
                        self.cust_details_tabel.insert("",END,values =t[1:12])
                        self.combo_second.set("Select")
                        self.var_third_entry.set("")
                        break
                else:
                    messagebox.showerror("Error","This pincode have no customer",parent = self.root)
                    self.combo_second.set("Select")
                    self.var_third_entry.set("")

    def cust_showall(self):
        self.cust_details_tabel.delete(*self.cust_details_tabel.get_children())
        client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
        db = client["application"]
        col = db["Customer"]
        query = {"_id":0}
        for i in col.find({},query):
            rows =i
            if len(rows)!=0:
                t = tuple(rows.values())
                self.cust_details_tabel.insert("",END,values =t)

#=============================================Booking tabel=====================================================================
    def booking_tabel(self):
        show_frame =Frame(self.root,bd =2,relief =RIDGE)
        show_frame.place(x=8,y=112,width=1280,height=543)

        scroll_x = ttk.Scrollbar(show_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(show_frame,orient=VERTICAL)

        self.booking_details_tabel=ttk.Treeview(show_frame,column=("Customer No","Customer Name","Booking ID","Booking Date","Time","Hall Name","Hall Limit","Hall Price","Cooling Type"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.booking_details_tabel.xview)
        scroll_y.config(command=self.booking_details_tabel.yview)

        self.booking_details_tabel.heading("Customer No",text="Customer No")
        self.booking_details_tabel.heading("Customer Name",text="Customer Name")
        self.booking_details_tabel.heading("Booking ID",text="Booking ID")
        self.booking_details_tabel.heading("Booking Date",text="Booking Date")
        self.booking_details_tabel.heading("Time",text="Time")
        self.booking_details_tabel.heading("Hall Name",text="Hall Name")
        self.booking_details_tabel.heading("Hall Limit",text="Hall Limit")
        self.booking_details_tabel.heading("Hall Price",text="Hall Price")
        self.booking_details_tabel.heading("Cooling Type",text="Cooling Type")

        self.booking_details_tabel["show"] ="headings"
        self.booking_details_tabel.column("Customer No",width=100,anchor=CENTER)
        self.booking_details_tabel.column("Customer Name",width=100,anchor= CENTER)
        self.booking_details_tabel.column("Booking ID",width=100,anchor= CENTER)
        self.booking_details_tabel.column("Booking Date",width=100,anchor= CENTER)
        self.booking_details_tabel.column("Time",width=100,anchor=CENTER)
        self.booking_details_tabel.column("Hall Name",width=100,anchor=CENTER)
        self.booking_details_tabel.column("Hall Limit",width=100,anchor= CENTER)
        self.booking_details_tabel.column("Hall Price",width=100,anchor= CENTER)
        self.booking_details_tabel.column("Cooling Type",width=100,anchor=CENTER)

        self.booking_details_tabel.pack(fill=BOTH,expand=1)

    def booking_search(self):
        if self.combo_second.get()=="Select":
            messagebox.showerror("Error","Select Something",self.root)
        elif self.combo_second.get()=="":
            messagebox.showerror("Error","Enter the text field",self.root)
        else:
            client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
            db = client["application"]
            col = db["Booking Details"]
            if self.combo_second.get()=="Customer No":
                query1 = {"Customer No":self.var_third_entry.get()}
                for i in col.find(query1):
                    rows =i
                    if len(rows)!=0:
                        self.booking_details_tabel.delete(*self.booking_details_tabel.get_children())
                        t = tuple(rows.values())
                        self.booking_details_tabel.insert("",END,values =t[1:9])
                        self.combo_second.set("Select")
                        self.var_third_entry.set("")
                        break
                else:
                    messagebox.showerror("Error","This number has no booking",self.root)
                    self.combo_second.set("Select")
                    self.var_third_entry.set("")

            if self.combo_second.get()=="Booking ID":
                query = {"Booking ID":self.var_third_entry.get()}
                for i in col.find(query):
                    rows =i
                    if len(rows)!=0:
                        self.booking_details_tabel.delete(*self.booking_details_tabel.get_children())
                        t = tuple(rows.values())
                        self.booking_details_tabel.insert("",END,values =t[1:9])
                        self.combo_second.set("Select")
                        self.var_third_entry.set("")
                        break
                    else:
                        messagebox.showerror("Error","This ID Has No Booking",self.root)
                        self.combo_second.set("Select")
                        self.var_third_entry.set("")

            if self.combo_second.get()=="Booking Date":
                query = {"Booking Date":self.date.get()}
                for i in col.find(query):
                    rows =i
                    if len(rows)!=0:
                        self.booking_details_tabel.delete(*self.booking_details_tabel.get_children())
                        t = tuple(rows.values())
                        self.booking_details_tabel.insert("",END,values =t[1:9])
                        self.combo_second.set("Select")
                        third =ttk.Entry(self.root,textvariable =self.var_third_entry,width=22,font =("times new roman",16))
                        third.place(x = 770,y = 62)
                        break
                else:
                    messagebox.showerror("Error","This Date has No Booking",parent = self.root)
                    self.combo_second.set("Select")
                    third =ttk.Entry(self.root,textvariable =self.var_third_entry,width=22,font =("times new roman",16))
                    third.place(x = 770,y = 62)


            if self.combo_second.get()=="Hall Name":
                query = {"Hall Name":self.var_third_entry.get()}
                for i in col.find(query):
                    rows =i
                    if len(rows)!=0:
                        self.booking_details_tabel.delete(*self.booking_details_tabel.get_children())
                        t = tuple(rows.values())
                        self.booking_details_tabel.insert("",END,values =t[1:9])
                        self.combo_second.set("Select")
                        self.var_third_entry.set("")
                        break
                    else:
                        messagebox.showerror("Error","This Hall is not booked",parent = self.root)
                        self.combo_second.set("Select")
                        self.var_third_entry.set("")

    def book_showall(self):
        self.booking_details_tabel.delete(*self.booking_details_tabel.get_children())
        client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
        db = client["application"]
        col = db["Booking Details"]
        query = {"_id":0}
        for i in col.find({},query):
            rows =i
            if len(rows)!=0:
                t = tuple(rows.values())
                self.booking_details_tabel.insert("",END,values =t)

#======================================Payment tabel==============================================================
    def payment_tabel(self):
        show_frame =Frame(self.root,bd =2,relief =RIDGE)
        show_frame.place(x=8,y=112,width=1280,height=543)

        scroll_x = ttk.Scrollbar(show_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(show_frame,orient=VERTICAL)

        self.payment_details_tabel=ttk.Treeview(show_frame,column=("Booking ID","Customer No","Customer Name","Booking Date","Time","Hall Name","Hall Limit","Cooling Type","Hall Price","Cooling Price","GST","Total Amount","Paid Amount","Due Amount"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.payment_details_tabel.xview)
        scroll_y.config(command=self.payment_details_tabel.yview)

        self.payment_details_tabel.heading("Booking ID",text="Booking ID")
        self.payment_details_tabel.heading("Customer No",text="Customer No")       
        self.payment_details_tabel.heading("Customer Name",text="Customer Name")
        self.payment_details_tabel.heading("Booking Date",text="Booking Date")
        self.payment_details_tabel.heading("Time",text="Time")
        self.payment_details_tabel.heading("Hall Name",text="Hall Name")
        self.payment_details_tabel.heading("Hall Limit",text="Hall Limit")
        self.payment_details_tabel.heading("Cooling Type",text="Cooling Type")
        self.payment_details_tabel.heading("Hall Price",text="Hall Price")
        self.payment_details_tabel.heading("Cooling Price",text="Cooling Price")
        self.payment_details_tabel.heading("GST",text="GST")
        self.payment_details_tabel.heading("Total Amount",text="Total Amount")
        self.payment_details_tabel.heading("Paid Amount",text="Paid Amount")
        self.payment_details_tabel.heading("Due Amount",text="Due Amount")

        self.payment_details_tabel["show"] ="headings"
        self.payment_details_tabel.column("Booking ID",width=100,anchor= CENTER)
        self.payment_details_tabel.column("Customer No",width=100,anchor=CENTER)
        self.payment_details_tabel.column("Customer Name",width=100,anchor= CENTER)
        self.payment_details_tabel.column("Booking Date",width=100,anchor= CENTER)
        self.payment_details_tabel.column("Time",width=100,anchor=CENTER)
        self.payment_details_tabel.column("Hall Name",width=100,anchor=CENTER)
        self.payment_details_tabel.column("Hall Limit",width=100,anchor= CENTER)
        self.payment_details_tabel.column("Cooling Type",width=100,anchor=CENTER)
        self.payment_details_tabel.column("Hall Price",width=100,anchor= CENTER)
        self.payment_details_tabel.column("Cooling Price",width=100,anchor=CENTER)
        self.payment_details_tabel.column("GST",width=100,anchor=CENTER)
        self.payment_details_tabel.column("Total Amount",width=100,anchor= CENTER)
        self.payment_details_tabel.column("Paid Amount",width=100,anchor=CENTER)
        self.payment_details_tabel.column("Due Amount",width=100,anchor= CENTER)

        self.payment_details_tabel.pack(fill=BOTH,expand=1)

    def payment_search(self):
        if self.combo_second.get()=="Select":
            messagebox.showerror("Error","Select Something",parent = self.root)
        elif self.combo_second.get()=="":
            messagebox.showerror("Error","Enter the text field",parent = self.root)
        else:
            client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
            db = client["application"]
            col = db["Payment Details"]
            if self.combo_second.get()=="Customer No":
                query1 = {"Customer No":self.var_third_entry.get()}
                for i in col.find(query1):
                    rows =i
                    if len(rows)!=0:
                        self.payment_details_tabel.delete(*self.payment_details_tabel.get_children())
                        t = tuple(rows.values())
                        self.payment_details_tabel.insert("",END,values =t[1:9])
                        self.combo_second.set("Select")
                        self.var_third_entry.set("")
                        break
                else:
                    messagebox.showerror("Error","This number has no payment",parent = self.root)
                    self.combo_second.set("Select")
                    self.var_third_entry.set("")

            if self.combo_second.get()=="Booking ID":
                query = {"Booking ID":self.var_third_entry.get()}
                for i in col.find(query):
                    rows =i
                    if len(rows)!=0:
                        self.payment_details_tabel.delete(*self.payment_details_tabel.get_children())
                        t = tuple(rows.values())
                        self.payment_details_tabel.insert("",END,values =t[1:9])
                        self.combo_second.set("Select")
                        self.var_third_entry.set("")
                        break
                    else:
                        messagebox.showerror("Error","This ID Has No Booking",parent = self.root)
                        self.combo_second.set("Select")
                        self.var_third_entry.set("")

            if self.combo_second.get()=="Booking Date":
                query = {"Booking Date":self.date.get()}
                for i in col.find(query):
                    rows =i
                    if len(rows)!=0:
                        self.payment_details_tabel.delete(*self.payment_details_tabel.get_children())
                        t = tuple(rows.values())
                        self.payment_details_tabel.insert("",END,values =t[1:9])
                        self.combo_second.set("Select")
                        third =ttk.Entry(self.root,textvariable =self.var_third_entry,width=22,font =("times new roman",16))
                        third.place(x = 770,y = 62)
                        break
                else:
                    messagebox.showerror("Error","This Date has No Booking",parent= self.root)
                    self.combo_second.set("Select")
                    third =ttk.Entry(self.root,textvariable =self.var_third_entry,width=22,font =("times new roman",16))
                    third.place(x = 770,y = 62)

    def pay_showall(self):
        self.payment_details_tabel.delete(*self.payment_details_tabel.get_children())
        client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
        db = client["application"]
        col = db["Payment Details"]
        query = {"_id":0}
        for i in col.find({},query):
            rows =i
            if len(rows)!=0:
                t = tuple(rows.values())
                self.payment_details_tabel.insert("",END,values =t)

#=========================================================hall add==========================================================

    def halladd_tabel(self):
        show_frame =Frame(self.root,bd =2,relief =RIDGE)
        show_frame.place(x=8,y=112,width=1280,height=543)


        scroll_x = ttk.Scrollbar(show_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(show_frame,orient=VERTICAL)

        self.hall_details_tabel=ttk.Treeview(show_frame,column=("Hall Name","Hall Limit","Hall Price"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.hall_details_tabel.xview)
        scroll_y.config(command=self.hall_details_tabel.yview)

        self.hall_details_tabel.heading("Hall Name",text="Hall Name")
        self.hall_details_tabel.heading("Hall Limit",text="Hall Limit")
        self.hall_details_tabel.heading("Hall Price",text="Hall Price")

        self.hall_details_tabel["show"] ="headings"

        self.hall_details_tabel.column("Hall Name",width=100,anchor=CENTER)
        self.hall_details_tabel.column("Hall Limit",width=100,anchor= CENTER)
        self.hall_details_tabel.column("Hall Price",width=100,anchor= CENTER)

        self.hall_details_tabel.pack(fill=BOTH,expand=1)

    def halladd_search(self):
        if self.combo_second.get()=="Select":
            messagebox.showerror("Error","Select Something",parent = self.root)
        elif self.combo_second.get()=="":
            messagebox.showerror("Error","Enter the text field",parent= self.root)
        else:
            client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
            db = client["application"]
            col = db["Hall Manage"]
            query = {self.combo_second.get():self.var_third_entry.get()}
            for i in col.find(query):
                rows =i
                if len(rows)!=0:
                    self.hall_details_tabel.delete(*self.hall_details_tabel.get_children())
                    t = tuple(rows.values())
                    self.hall_details_tabel.insert("",END,values =t[1:4])
                    self.combo_second.set("Select")
                    self.var_third_entry.set("")

    def halladd_showall(self):
        self.hall_details_tabel.delete(*self.hall_details_tabel.get_children())
        client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
        db = client["application"]
        col = db["Hall Manage"]
        query = {"_id":0}
        for i in col.find({},query):
            rows =i
            if len(rows)!=0:
                t = tuple(rows.values())
                self.hall_details_tabel.insert("",END,values =t)


#====================================================hall available========================================================================

    def hallavailabel_tabel(self):
        show_frame =Frame(self.root,bd =2,relief =RIDGE)
        show_frame.place(x=8,y=112,width=1280,height=543)

        scroll_x = ttk.Scrollbar(show_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(show_frame,orient=VERTICAL)

        self.available_details_tabel=ttk.Treeview(show_frame,column=("Hall Name","Hall Limit","Hall Price"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.available_details_tabel.xview)
        scroll_y.config(command=self.available_details_tabel.yview)

        self.available_details_tabel.heading("Hall Name",text="Hall Name")
        self.available_details_tabel.heading("Hall Limit",text="Hall Limit")
        self.available_details_tabel.heading("Hall Price",text="Hall Price")
        self.available_details_tabel["show"] ="headings"

        self.available_details_tabel.column("Hall Name",width=100,anchor=CENTER)
        self.available_details_tabel.column("Hall Limit",width=100,anchor= CENTER)
        self.available_details_tabel.column("Hall Price",width=100,anchor= CENTER)

        self.available_details_tabel.pack(fill=BOTH,expand=1)

    def bookingcheck_search(self):
        self.available_details_tabel.delete(*self.available_details_tabel.get_children())
        if self.combo_time.get()== "Select":
            messagebox.showerror("Error","Please Select Time",parent = self.root)
        else:
            client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
            db = client["application"]
            col1 = db["Booking Details"]
            col2 = db["Hall Manage"]
            query1 ={"Booking Date":self.co_date.get(),"Time":self.combo_time.get()}
            l = []
            l1 =[]
            D ={"Time":"Fullday"}
            if query1["Time"] == D["Time"]:
                for i in col1.find({"$and": [{"Booking Date":self.co_date.get()},{"Time":{"$in":["Day","Night","Fullday"]}}]}):
                    row2 = list(i.values())
                    l1.append(row2[6])
                for i in col2.find({"Hall Name" : {"$nin":l1}}):
                    row = i
                    l2 = list(row.values())
                    price = 2*int(l2[3])
                    list1 = list(row.values())
                    list1[3]=price
                    self.available_details_tabel.insert("",END,values =list1[1:4])

            else:
                for i in col1.find({"$and": [{"Booking Date":self.co_date.get()},{"Time":{"$in":["Day","Night","Fullday"]}}]}):
                    row1 = list(i.values())
                    l.append(row1[6])
                for i in col2.find({"Hall Name" : {"$nin":l}}):
                    row = i
                    t = tuple(row.values())
                    self.available_details_tabel.insert("",END,values =t[1:4])



#=====================================search button command=======================================================
    def search(self):
        if self.combo_first.get()=="Customer Details":
            self.customer_tabel()
            self.customer_search()

        if self.combo_first.get()=="Booking Details":
            self.booking_tabel()
            self.booking_search()

        if self.combo_first.get()=="Payment Details":
            self.payment_tabel()
            self.payment_search()

        if self.combo_first.get()=="Hall Available Details":
            self.hallavailabel_tabel()
            self.bookingcheck_search()

        if self.combo_first.get()=="Hall Details":
            self.halladd_tabel()
            self.halladd_search()

        if self.combo_first.get()=="Select":
            messagebox.showerror("Error","Select Something")


#======================================showall button command================================================

    def showall(self):
        if self.combo_first.get()=="Customer Details":
            self.customer_tabel()
            self.cust_showall()

        if self.combo_first.get()=="Booking Details":
            self.booking_tabel()
            self.book_showall()

        if self.combo_first.get()=="Payment Details":
            self.payment_tabel()
            self.pay_showall()

        if self.combo_first.get()=="Hall Details":
            self.halladd_tabel()
            self.halladd_showall()

        if self.combo_first.get()=="Hall Available Details":
            messagebox.showinfo("Info","For Hall Availablity use search button")

        if self.combo_first.get()=="Select":
            messagebox.showerror("Error","Select Something")


