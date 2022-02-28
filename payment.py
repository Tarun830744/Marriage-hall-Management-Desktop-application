from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import pymongo
import random ,os
from tkinter import  messagebox
from tkcalendar import DateEntry
import tempfile

class payment_win:
    def __init__(self,root):
        self.root= root
        self.root.title("Payment Details")
        self.root.geometry("1300x663+233+130")
        self.root.resizable(width=False, height=False)

        icon = Image.open("images/city-hall.png")
        self.icon = ImageTk.PhotoImage(icon)
        self.root.iconphoto(FALSE,self.icon)
        
    #==========================logo========================
        img1 =Image.open("images/logo3.png")
        img1 = img1.resize((100,50),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(self.root,image =self.photoimg1)
        lblimg1.place(x=0,y=0,width =100,height=50)
    



        self.var_customerno = StringVar()
        self.var_bookingid = StringVar()
        self.var_custname = StringVar()
        self.var_bookdate = StringVar()
        self.var_time = StringVar()
        self.var_hall_name = StringVar()
        self.var_hall_limit = StringVar()
        self.var_hall_price = StringVar()
        self.var_coolingtype = StringVar()
        self.var_coolingprice = StringVar()
        self.var_gst = StringVar()
        self.var_totalamount = StringVar()
        self.var_paidamount = StringVar()
        self.var_dueamount = StringVar()

    #==========================title======================
        lbl_title = Label(self.root,text ="Payment",font =("times new roman",20,"bold"),bg = "black",fg ="gold")
        lbl_title.place(x=100,y=0,width =1195,height =50)


    #==========================label frame====================
        label_framleft = LabelFrame(self.root,text ="Payment",font =("times new roman",18,"bold"),bd= 5 ,relief = RIDGE)
        label_framleft.place(x=5,y=60,width= 660,height =340)

    #==========================custref============================
        lblcust_ref = Label(label_framleft,text ="Booking ID :",font =("times new roman",13),padx=6,pady=6)
        lblcust_ref.grid(row=0,column=0,sticky=W)

        entry_ref =ttk.Entry(label_framleft,textvariable=self.var_bookingid,width=12,font =("times new roman",13))
        entry_ref.grid(row =0,column =1,sticky=W)

    #==================================Checkbtn======================================
        btncheck = Button(label_framleft,text="CHECK",command = self.check,font =("times new roman",10,"bold"),bg = "gold",fg="black",activeforeground="black",activebackground="gold",width =10)
        btncheck.place(x = 255, y=4,width=60)

     #=============================Custiomer no=============================
        lblcust_mobile = Label(label_framleft,text ="Customer No :",font =("times new roman",13),padx=6,pady=6)
        lblcust_mobile.grid(row=1,column=0,sticky=W)

        entry_mobile =ttk.Entry(label_framleft,textvariable=self.var_customerno,width=20,font =("times new roman",13),state="readonly")
        entry_mobile.grid(row =1,column =1,sticky = W)

    #===========================custname===========================
        lblcust_name = Label(label_framleft,text ="Customer Name :",font =("times new roman",13),padx=6,pady=6)
        lblcust_name.grid(row=2,column=0,sticky=W)

        entry_name =ttk.Entry(label_framleft,textvariable=self.var_custname,width=20,font =("times new roman",13),state ="readonly")
        entry_name.grid(row =2,column =1,sticky=W)

    #=============================Booking Date ==============================
        lbl_book_date = Label(label_framleft,text ="Booking Date :",font =("times new roman",13),padx=6,pady=6)
        lbl_book_date.grid(row=3,column=0,sticky=W)

        entry_book_date = ttk.Entry(label_framleft,textvariable = self.var_bookdate,width = 20,font =("times new roman",13),state = "readonly")
        entry_book_date.grid(row =3,column =1 ,sticky =W)
    
    #=============================Book time===============================
        lbl_time = Label(label_framleft,text ="Time :",font =("times new roman",13),padx=6,pady=6)
        lbl_time.grid(row=4,column=0,sticky=W)

        entry_book_time = ttk.Entry(label_framleft,textvariable = self.var_time,width = 20,font =("times new roman",13),state = "readonly")
        entry_book_time.grid(row =4,column =1 ,sticky =W)


    #==========================Hall Name==========================================
        lblhall_name = Label(label_framleft,text ="Hall Name:",font =("times new roman",13),padx=6,pady=6)
        lblhall_name.grid(row=5,column=0,sticky=W)

        entry_hall_name =ttk.Entry(label_framleft,textvariable=self.var_hall_name,width=20,font =("times new roman",13),state = "readonly")
        entry_hall_name.grid(row =5,column =1,sticky=W)

    #==========================Hall limit===========================================
        lblhall_limit = Label(label_framleft,text ="Hall limit:",font =("times new roman",13),padx=6,pady=6)
        lblhall_limit.grid(row=6,column=0,sticky=W)

        entry_hall_limit =ttk.Entry(label_framleft,textvariable=self.var_hall_limit,width=20,font =("times new roman",13),state = "readonly")
        entry_hall_limit.grid(row =6,column =1,sticky=W)



    #======================= Cooling Type ===========================================
        lbl_cooling = Label(label_framleft,text ="Cooling Type:",font =("times new roman",13),padx=6,pady=6)
        lbl_cooling.grid(row=0,column=3)

        entry_cooling =ttk.Entry(label_framleft,textvariable=self.var_coolingtype,width=20,font =("times new roman",13),state = "readonly")
        entry_cooling.grid(row =0,column =4)
    
    #==============================Hall Price=====================================
        lblhall_limit = Label(label_framleft,text ="Hall Price:",font =("times new roman",13),padx=6,pady=6)
        lblhall_limit.grid(row=1,column=3)

        entry_hall_limit =ttk.Entry(label_framleft,textvariable=self.var_hall_price,width=20,font =("times new roman",13),state = "readonly")
        entry_hall_limit.grid(row =1,column =4)

    
    #========================Cooling Charges ===========================================
        lbl_cooling_price = Label(label_framleft,text ="Cooling Charges:",font =("times new roman",13),padx=6,pady=6)
        lbl_cooling_price.grid(row=2,column=3)

        entry_cooling_price =ttk.Entry(label_framleft,textvariable=self.var_coolingprice,width=20,font =("times new roman",13),state = "readonly")
        entry_cooling_price.grid(row =2,column =4)

    #========================GST ===========================================
        lbl_GST = Label(label_framleft,text ="GST:",font =("times new roman",13),padx=6,pady=6)
        lbl_GST.grid(row=3,column=3)

        entry_GST =ttk.Entry(label_framleft,textvariable=self.var_gst,width=20,font =("times new roman",13),state = "readonly")
        entry_GST.grid(row =3,column =4)

    #=============================Total Amount==============================================
        lbl_total_amount = Label(label_framleft,text ="Total Amount:",font =("times new roman",13),padx=6,pady=6)
        lbl_total_amount.grid(row=4,column=3)

        entry_total_amount =ttk.Entry(label_framleft,textvariable=self.var_totalamount,width=20,font =("times new roman",13),state = "readonly")
        entry_total_amount.grid(row =4,column =4)
    
    #=======================Paid Amount===========================================
        lbl_paid_amount = Label(label_framleft,text ="Paid Amount:",font =("times new roman",13),padx=6,pady=6)
        lbl_paid_amount.grid(row=5,column=3)

        entry_paid_amount =ttk.Entry(label_framleft,textvariable=self.var_paidamount,width=20,font =("times new roman",13))
        entry_paid_amount.grid(row =5,column =4)

    #========================Due Amount===========================================
        lbl_due_amount = Label(label_framleft,text ="Due Amount:",font =("times new roman",13),padx=6,pady=6)
        lbl_due_amount.grid(row=6,column=3)

        entry_due_amount =ttk.Entry(label_framleft,textvariable=self.var_dueamount,width=20,font =("times new roman",13),state = "readonly")
        entry_due_amount.grid(row =6,column =4)

    #================================Btn===============================
        btnadd = Button(label_framleft,text="PAYMENT",command = self.payment,font =("times new roman",14,"bold"),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btnadd.place(x = 40, y=255,width=120)

        btnupdate = Button(label_framleft,text="UPDATE",command = self.update,font =("times new roman",14,"bold"),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btnupdate.place(x = 200, y=255,width=120)

        btndelete= Button(label_framleft,text="DELETE",command = self.delete,font =("times new roman",14,"bold"),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btndelete.place(x = 360, y=255,width=120)

        btnreset = Button(label_framleft,text="RESET",command = self.reset,font =("times new roman",14,"bold"),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btnreset.place(x = 520, y=255,width=120)
    
    #=================================Search for bill===============================
        self.search_bill = StringVar()
        lblsearch = Label(self.root,text ="Booking ID :",font =("times new roman",14,"bold"),fg ="black")
        lblsearch.place(x = 677 ,y =70 )

        entry_search_bill=ttk.Entry(self.root,width=20,textvariable = self.search_bill,font =("times new roman",14))
        entry_search_bill.place(x = 790,y =70)

        btnsearch_bill= Button(self.root,text="SEARCH",command = self.find_bill,width =10,font =("times new roman",12,"bold"),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btnsearch_bill.place(x = 990,y =68, width = 120)


    #=======================================Bill ====================================
        frame_bill = LabelFrame(self.root,bd= 5 ,relief = RIDGE)
        frame_bill.place(x=675,y=100,width= 610, height =480)

        scroll1_y = ttk.Scrollbar(frame_bill,orient=VERTICAL)
        self.textarea = Text(frame_bill,yscrollcommand=scroll1_y.set,bg = "white",fg = "black",font =("times new roman",12))
        scroll1_y.pack(side=RIGHT,fill = Y)

        scroll1_y.config(command=self.textarea.yview)

        self.textarea.pack(fill = BOTH ,expand = 1)


    #======================================BTn for bill=====================================
        btnsave = Button(self.root,text="SAVE",command = self.save_bill,font =("times new roman",16,"bold"),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btnsave.place(x = 687, y=600,width=150)

        btnprint = Button(self.root,text="PRINT",command = self.print_bill,font =("times new roman",16,"bold"),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btnprint.place(x = 887, y=600,width=150)

        btnclear = Button(self.root,text="CLEAR",command=self.clear,font =("times new roman",16,"bold"),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btnclear.place(x = 1087, y=600,width=150)
    


    #===========================================Payment tabel ================================================
        frame_tabel1 = LabelFrame(self.root,text ="Payment details",font =("times new roman",18,"bold"),bd= 5 ,relief = RIDGE)
        frame_tabel1.place(x=5,y=400,width= 660, height =255)

        self.search_var = StringVar()
        lblsearch = Label(frame_tabel1,text ="Search By:",font =("times new roman",14,"bold"),fg ="black")
        lblsearch.grid(row=0,column=0,sticky=W,padx=2)

        combo_search = ttk.Combobox(frame_tabel1,font =("times new roman",14),textvariable = self.search_var,width = 17,state ="readonly")
        combo_search["value"]=("Select","Customer No","Booking ID","Hall Name")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search = StringVar()
        entry_search=ttk.Entry(frame_tabel1,width=17,textvariable = self.txt_search,font =("times new roman",14))
        entry_search.grid(row =0,column =2,padx=2)

        btnsearch= Button(frame_tabel1,text="SEARCH",command=self.search,width =10,font =("times new roman",12,"bold"),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btnsearch.grid(row =0,column =3,padx=2)

        btnshowall = Button(frame_tabel1,text="SHOW ALL",command=self.fetch_deta,width =10,font =("times new roman",12,"bold"),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btnshowall.grid(row =0,column =4,padx=2)

     #============================show payment tabel data  =======================
        show_frame =Frame(frame_tabel1,bd =2,relief =RIDGE)
        show_frame.place(x=5,y=35,width=640,height=190)

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
        self.payment_details_tabel.bind("<ButtonRelease-1>",self.cursor)

        self.welcome()
        
    #===================================Check============================
    def check(self):
        if self.var_bookingid.get()=="":
            messagebox.showerror("Error","Please Enter Booking ID",parent =self.root)
        else:
            client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
            db = client["application"]
            col = db["Booking Details"]
            query = {"Booking ID":self.var_bookingid.get()}
            for i in col.find(query):
                rows =i
                list1 = list(rows.values())

                self.var_customerno.set(list1[1])
                self.var_custname.set(list1[2])
                self.var_bookdate.set(list1[4])
                self.var_time.set(list1[5])
                self.var_hall_name.set(list1[6])
                self.var_hall_limit.set(list1[7])
                self.var_hall_price.set(list1[8])
                self.var_coolingtype.set(list1[9])
                self.calculation()
                messagebox.showinfo("Info","Valid Customer",parent = self.root)
                break
            else:
                self.var_customerno.set("")
                self.var_custname.set("")
                self.var_bookdate.set("")
                self.var_time.set("")
                self.var_hall_name.set("")
                self.var_hall_limit.set("")
                self.var_hall_price.set("")
                self.var_coolingtype.set("")
                self.var_coolingprice.set("")
                self.var_gst.set("")
                self.var_totalamount.set("")
                self.var_paidamount.set("")
                self.var_dueamount.set("")
                messagebox.showerror("Error","Please Enter Valid Booking id",parent = self.root)

    #===============================Calculation===============================

    def calculation(self):
        client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
        db = client["application"]
        col = db["Booking Details"]
        query = {"Booking ID":self.var_bookingid.get()}
        for i in col.find(query):
            rows =i
            list1 = list(rows.values())
            day =list1[5]
            print(day)
            hall = float(list1[8])
            cool = list1[9]
            if cool == "AC":
                if day == "Fullday":
                    gst = (20000+hall)*0.180
                    total = 20000+hall+gst
                    self.var_coolingprice.set("20000")
                    self.var_gst.set(gst)
                    self.var_totalamount.set(total)
                else:
                    gst = (10000+hall)*0.180
                    total = 10000+hall+gst
                    self.var_coolingprice.set("10000")
                    self.var_gst.set(gst)
                    self.var_totalamount.set(total)

            else:
                if day == "Fullday":
                    gst = (4000+hall)*0.180
                    total = 4000+hall+gst
                    self.var_coolingprice.set("4000")
                    self.var_gst.set(gst)
                    self.var_totalamount.set(total)
                else:
                    gst = (2000+hall)*0.180
                    total = 2000+hall+gst
                    self.var_coolingprice.set("2000")
                    self.var_gst.set(gst)
                    self.var_totalamount.set(total)

    def dueamount(self):
        paid = float(self.var_paidamount.get())
        total = float(self.var_totalamount.get())
        due = total - paid
        self.var_dueamount.set(due)


    #================================add data in booking tabel===============================
    def payment(self):
        if self.var_hall_name.get()=="" or self.var_hall_limit.get()=="" or self.var_custname.get()=="" or self.var_coolingtype.get()=="Select"or self.var_paidamount.get()=="":
            messagebox.showerror("Error","All Fields Required",parent=self.root)
        else:
            client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
            db = client["application"]
            col = db["Payment Details"]
            query = {"Hall Name":self.var_hall_name.get(),"Customer No":self.var_customerno.get(),"Time":self.var_time.get(),"Booking Date":self.var_bookdate.get(),"Booking ID":self.var_bookingid.get()}
            for i in col.find(query):
                messagebox.showerror("Error","Payment already exist",parent=self.root)
                break
            else:
                self.dueamount()
                try:
                    record = {"Booking ID":self.var_bookingid.get(),"Customer No":self.var_customerno.get(),"Customer Name":self.var_custname.get(),"Booking Date":self.var_bookdate.get(),"Time":self.var_time.get(),"Hall Name":self.var_hall_name.get(),"Hall Limit":self.var_hall_limit.get(),"Cooling Type":self.var_coolingtype.get(),"Hall Price":self.var_hall_price.get(),"Cooling Price":self.var_coolingprice.get(),"GST":self.var_gst.get(),"Total Amount":self.var_totalamount.get(),"Paid Amount":self.var_paidamount.get(),"Due Amount":self.var_dueamount.get()}
                    col.insert_one(record)
                    self.welcome()
                    self.fetch_deta()
                    messagebox.showinfo("Success", "Payment Successfully",parent=self.root)
                    #self.reset()
                except Exception as e:
                    messagebox.showwarning("Warning","Some thing went wrong",parent=self.root)

    #===============================fetch and insert data in booking table==============================================
    def fetch_deta(self):
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

    #================================cursor for update or delete=======================================
    def cursor(self,event = ""):
        cursor_row = self.payment_details_tabel.focus()
        contain = self.payment_details_tabel.item(cursor_row)
        row = contain["values"]
        self.var_bookingid.set(row[0])
        self.var_customerno.set(row[1])
        self.var_custname.set(row[2])
        self.var_bookdate.set(row[3])
        self.var_time.set(row[4])
        self.var_hall_name.set(row[5])
        self.var_hall_limit.set(row[6])
        self.var_coolingtype.set(row[7])
        self.var_hall_price.set(row[8])
        self.var_coolingprice.set(row[9])
        self.var_gst.set(row[10])
        self.var_totalamount.set(row[11])
        self.var_paidamount.set(row[12])
        self.var_dueamount.set(row[13])

    #================================update btn==================================
    def update(self):
        if self.var_customerno.get()=="" or self.var_hall_name.get()==" ":
            messagebox.showerror("Error","Please enter all field",parent = self.root)
        else:
            self.dueamount()
            try:
                client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
                db = client["application"]
                col = db["Payment Details"]
                query = {"Booking ID":self.var_bookingid.get()}
                new = {"Booking ID":self.var_bookingid.get(),"Customer No":self.var_customerno.get(),"Customer Name":self.var_custname.get(),"Booking Date":self.var_bookdate.get(),"Time":self.var_time.get(),"Hall Name":self.var_hall_name.get(),"Hall Limit":self.var_hall_limit.get(),"Cooling Type":self.var_coolingtype.get(),"Hall Price":self.var_hall_price.get(),"Cooling Price":self.var_coolingprice.get(),"GST":self.var_gst.get(),"Total Amount":self.var_totalamount.get(),"Paid Amount":self.var_paidamount.get(),"Due Amount":self.var_dueamount.get()}
                col.update(query,new)
                self.welcome()
                self.fetch_deta()
                messagebox.showinfo("Update","Payment details has been updated successfully",parent = self.root)
                #self.reset()
            except:
                pass
    #======================================Delete=============================
    def delete(self):
        mdelete=messagebox.askyesno("Marriage Hall Management","Do you want delete this Payment",parent = self.root)
        if mdelete>0:
            client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
            db = client["application"]
            col = db["Payment Details"]
            query = {"Booking ID":self.var_bookingid.get()}
            col.delete_one(query)
            self.reset()
        else:
            if not mdelete:
                return
        self.fetch_deta()
    #======================Reset==================================
    def reset(self):
        self.var_bookingid.set("")
        self.var_customerno.set("")
        self.var_custname.set("")
        self.var_bookdate.set("")
        self.var_time.set("")
        self.var_hall_name.set("")
        self.var_hall_limit.set("")
        self.var_coolingtype.set("")
        self.var_hall_price.set("")
        self.var_coolingprice.set("")
        self.var_gst.set("")
        self.var_totalamount.set("")
        self.var_paidamount.set("")
        self.var_dueamount.set("")

    #========================Search===============================
    def search(self):
        client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
        db = client["application"]
        col = db["Payment Details"]
        query = {self.search_var.get():self.txt_search.get()}
        for i in col.find(query):
            rows =i
            if len(rows)!=0:
                self.payment_details_tabel.delete(*self.payment_details_tabel.get_children())
                t = tuple(rows.values())
                self.payment_details_tabel.insert("",END,values =t[1:9])
                self.search_var.set("Select")
                self.txt_search.set("")



    #===============================Bill welcome page=========================
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t\t\t  WELCOME TO MARRIAGE HALL")
        self.textarea.insert(END,"\n")

        self.textarea.insert(END,"\n\t Booking ID")
        self.textarea.insert(END,"\t\t\t :")
        self.textarea.insert(END,f"\t\t{self.var_bookingid.get()}")
        self.textarea.insert(END,"\n")

        self.textarea.insert(END,"\n\t Customer No")
        self.textarea.insert(END,"\t\t\t :")
        self.textarea.insert(END,f"\t\t{self.var_customerno.get()}")
        self.textarea.insert(END,"\n")

        self.textarea.insert(END,"\n\t Customer Name")
        self.textarea.insert(END,"\t\t\t :")
        self.textarea.insert(END,f"\t\t{self.var_custname.get()}")
        self.textarea.insert(END,"\n")

        self.textarea.insert(END,"\n************************************************************************")
        self.textarea.insert(END,"\n\t\t\tBooking and Payment Details")
        self.textarea.insert(END,"\n************************************************************************")

        self.textarea.insert(END,"\n")

        self.textarea.insert(END,"\n\t Booking Date")
        self.textarea.insert(END,"\t\t\t :")
        self.textarea.insert(END,f"\t\t{self.var_bookdate.get()}")
        self.textarea.insert(END,"\n")

        self.textarea.insert(END,"\n\t Function Time")
        self.textarea.insert(END,"\t\t\t :")
        self.textarea.insert(END,f"\t\t{self.var_time.get()}")
        self.textarea.insert(END,"\n")

        self.textarea.insert(END,"\n\t Hall Name")
        self.textarea.insert(END,"\t\t\t :")
        self.textarea.insert(END,f"\t\t{self.var_hall_name.get()}")
        self.textarea.insert(END,"\n")

        self.textarea.insert(END,"\n\t Hall Limit")
        self.textarea.insert(END,"\t\t\t :")
        self.textarea.insert(END,f"\t\t{self.var_hall_limit.get()}")
        self.textarea.insert(END,"\n")

        self.textarea.insert(END,"\n\t Cooling Type")
        self.textarea.insert(END,"\t\t\t :")
        self.textarea.insert(END,f"\t\t{self.var_coolingtype.get()}")
        self.textarea.insert(END,"\n")

        self.textarea.insert(END,"\n\t Hall Price")
        self.textarea.insert(END,"\t\t\t :")
        self.textarea.insert(END,f"\t\t{self.var_hall_price.get()}")
        self.textarea.insert(END,"\n")

        self.textarea.insert(END,"\n\tCooling Charge")
        self.textarea.insert(END,"\t\t\t :")
        self.textarea.insert(END,f"\t\t{self.var_coolingprice.get()}")
        self.textarea.insert(END,"\n")

        self.textarea.insert(END,"\n\t GST      ")
        self.textarea.insert(END,"\t\t\t :")
        self.textarea.insert(END,f"\t\t{self.var_gst.get()}")
        self.textarea.insert(END,"\n")

        self.textarea.insert(END,"\n\t Total Amount")
        self.textarea.insert(END,"\t\t\t :")
        self.textarea.insert(END,f"\t\t{self.var_totalamount.get()}")
        self.textarea.insert(END,"\n")

        self.textarea.insert(END,"\n\t Paid Amount")
        self.textarea.insert(END,"\t\t\t :")
        self.textarea.insert(END,f"\t\t{self.var_paidamount.get()}")
        self.textarea.insert(END,"\n")

        self.textarea.insert(END,"\n************************************************************************")
        self.textarea.insert(END,"\n\t Total Due")
        self.textarea.insert(END,"\t\t\t :")
        self.textarea.insert(END,f"\t\t{self.var_dueamount.get()}")




    def save_bill(self):
        m = messagebox.askyesno("Save Bill","Do you want to save this bill",parent = self.root)
        if m>0:
            self.billdata = self.textarea.get(1.0,END)
            file = open('Bills/'+str(self.var_bookingid.get())+".txt",'w')
            file.write(self.billdata)
            messagebox.showinfo("Success",f"Booking ID : {self.var_bookingid.get()} Saved Successfully",parent = self.root)
            file.close()
            self.clear()
        else:
            self.clear()

    def print_bill(self):
        q = self.textarea.get(1.0,"end-1c")
        filename =  tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")
        self.clear()


    def find_bill(self):
        found= "no"
        for i in os.listdir("Bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1 = open(f'Bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found ='yes'
        if found=='no':
            messagebox.showerror("Error","Invalid Booking ID",parent = self.root)

    def clear(self):
        self.textarea.delete(1.0,END)

        self.textarea.insert(END,"\t\t\t  WELCOME TO MARRIAGE HALL")
        self.textarea.insert(END,"\n")

        self.textarea.insert(END,"\n\t Booking ID")
        self.textarea.insert(END,"\t\t\t :")
        self.textarea.insert(END,"\n")

        self.textarea.insert(END,"\n\t Customer No")
        self.textarea.insert(END,"\t\t\t :")
        self.textarea.insert(END,"\n")

        self.textarea.insert(END,"\n\t Customer Name")
        self.textarea.insert(END,"\t\t\t :")
        self.textarea.insert(END,"\n")

        self.textarea.insert(END,"\n************************************************************************")
        self.textarea.insert(END,"\n\t\t\tBooking and Payment Details")
        self.textarea.insert(END,"\n************************************************************************")

        self.textarea.insert(END,"\n")

        self.textarea.insert(END,"\n\t Booking Date")
        self.textarea.insert(END,"\t\t\t :")
        self.textarea.insert(END,"\n")

        self.textarea.insert(END,"\n\t Function Time")
        self.textarea.insert(END,"\t\t\t :")
        self.textarea.insert(END,"\n")

        self.textarea.insert(END,"\n\t Hall Name")
        self.textarea.insert(END,"\t\t\t :")
        self.textarea.insert(END,"\n")

        self.textarea.insert(END,"\n\t Hall Limit")
        self.textarea.insert(END,"\t\t\t :")
        self.textarea.insert(END,"\n")

        self.textarea.insert(END,"\n\t Cooling Type")
        self.textarea.insert(END,"\t\t\t :")
        self.textarea.insert(END,"\n")

        self.textarea.insert(END,"\n\t Hall Price")
        self.textarea.insert(END,"\t\t\t :")
        self.textarea.insert(END,"\n")

        self.textarea.insert(END,"\n\tCooling Charge")
        self.textarea.insert(END,"\t\t\t :")
        self.textarea.insert(END,"\n")

        self.textarea.insert(END,"\n\t GST      ")
        self.textarea.insert(END,"\t\t\t :")
        self.textarea.insert(END,"\n")

        self.textarea.insert(END,"\n\t Total Amount")
        self.textarea.insert(END,"\t\t\t :")
        self.textarea.insert(END,"\n")

        self.textarea.insert(END,"\n\t Paid Amount")
        self.textarea.insert(END,"\t\t\t :")
        self.textarea.insert(END,"\n")

        self.textarea.insert(END,"\n************************************************************************")
        self.textarea.insert(END,"\n\t Total Due")
        self.textarea.insert(END,"\t\t\t :")


