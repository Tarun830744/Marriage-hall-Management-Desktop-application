from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import pymongo
import random
from tkinter import  messagebox
from tkcalendar import DateEntry
class booking_win:
    def __init__(self,root):
        self.root= root
        self.root.title("Booking Details")
        self.root.geometry("1300x663+233+130")
        self.root.resizable(width=False, height=False)

        icon = Image.open("images/city-hall.png")
        self.icon = ImageTk.PhotoImage(icon)
        self.root.iconphoto(FALSE,self.icon)

        self.var_bookingid=StringVar()
        x =random.randint(100000,1000000)
        self.var_bookingid.set(str(x))


        self.var_customerno = StringVar()
        self.var_custname = StringVar()
        self.var_bookdate = StringVar()
        self.var_time = StringVar()
        self.var_hall_name = StringVar()
        self.var_hall_limit = StringVar()
        self.var_hall_price = StringVar()
        self.var_coolingtype = StringVar()

    #==========================logo========================
        img1 =Image.open("images/logo3.png")
        img1 = img1.resize((100,50),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(self.root,image =self.photoimg1)
        lblimg1.place(x=0,y=0,width =100,height=50)

    #==========================title======================
        lbl_title = Label(self.root,text ="Hall Booking",font =("times new roman",20,"bold"),bg = "black",fg ="gold")
        lbl_title.place(x=100,y=0,width =1195,height =50)



    #==========================footer======================
        lbl_title = Label(self.root,font =("times new roman",20,"bold"),bg = "black",fg ="gold")
        lbl_title.place(x=1,y=785,width =1550,height =55)


    #==========================label frame====================
        label_framleft = LabelFrame(self.root,text ="Booking Detailes ",font =("times new roman",18,"bold"),bd= 5 ,relief = RIDGE)
        label_framleft.place(x=780,y=60,width= 500, height =590)

    #=============================Custiomer no=============================
        lblcust_mobile = Label(label_framleft,text ="Customer No :",font =("times new roman",16),padx=6,pady=6)
        lblcust_mobile.grid(row=0,column=0,sticky=W)

        entry_mobile =ttk.Entry(label_framleft,textvariable=self.var_customerno,width=20,font =("times new roman",16))
        entry_mobile.grid(row =0,column =1,sticky = W)

    #==================================Checkbtn======================================
        btncheck = Button(label_framleft,text="CHECK",command = self.check,font =("times new roman",12,"bold"),bg = "gold",fg="black",activeforeground="black",activebackground="gold",width =10)
        btncheck.place(x = 395, y=3,width=90)


    #===========================custname===========================
        lblcust_name = Label(label_framleft,text ="Customer Name :",font =("times new roman",16),padx=6,pady=6)
        lblcust_name.grid(row=1,column=0,sticky=W)

        entry_name =ttk.Entry(label_framleft,textvariable=self.var_custname,width=20,font =("times new roman",16),state ="readonly")
        entry_name.grid(row =1,column =1,sticky=W)

    #==========================custref============================
        lblcust_ref = Label(label_framleft,text ="Booking ID :",font =("times new roman",16),padx=6,pady=6)
        lblcust_ref.grid(row=2,column=0,sticky=W)

        entry_ref =ttk.Entry(label_framleft,textvariable=self.var_bookingid,width=20,font =("times new roman",16),state = "readonly")
        entry_ref.grid(row =2,column =1,sticky=W)


    #=============================Booking Date ==============================
        lbl_book_date = Label(label_framleft,text ="Booking Date :",font =("times new roman",16),padx=6,pady=6)
        lbl_book_date.grid(row=3,column=0,sticky=W)

        entry_book_date = ttk.Entry(label_framleft,textvariable = self.var_bookdate,width = 20,font =("times new roman",16),state = "readonly")
        entry_book_date.grid(row =3,column =1 ,sticky =W)

    #=============================Book time===============================
        lbl_time = Label(label_framleft,text ="Time :",font =("times new roman",16),padx=6,pady=6)
        lbl_time.grid(row=4,column=0,sticky=W)

        entry_book_time = ttk.Entry(label_framleft,textvariable = self.var_time,width = 20,font =("times new roman",16),state = "readonly")
        entry_book_time.grid(row =4,column =1 ,sticky =W)


    #==========================Hall Name==========================================
        lblhall_name = Label(label_framleft,text ="Hall Name:",font =("times new roman",16),padx=6,pady=6)
        lblhall_name.grid(row=5,column=0,sticky=W)

        entry_hall_name =ttk.Entry(label_framleft,textvariable=self.var_hall_name,width=20,font =("times new roman",16),state = "readonly")
        entry_hall_name.grid(row =5,column =1,sticky=W)

    #==========================Hall limit===========================================
        lblhall_limit = Label(label_framleft,text ="Hall limit:",font =("times new roman",16),padx=6,pady=6)
        lblhall_limit.grid(row=6,column=0,sticky=W)

        entry_hall_limit =ttk.Entry(label_framleft,textvariable=self.var_hall_limit,width=20,font =("times new roman",16),state = "readonly")
        entry_hall_limit.grid(row =6,column =1,sticky=W)

    #==============================Hall Price=====================================
        lblhall_limit = Label(label_framleft,text ="Hall Price:",font =("times new roman",16),padx=6,pady=6)
        lblhall_limit.grid(row=7,column=0,sticky=W)

        entry_hall_limit =ttk.Entry(label_framleft,textvariable=self.var_hall_price,width=20,font =("times new roman",16),state = "readonly")
        entry_hall_limit.grid(row =7,column =1,sticky=W)


    #======================= Cooling Type ===========================================
        lbl_cooling = Label(label_framleft,text ="Cooling Type:",font =("times new roman",16),padx=6,pady=6)
        lbl_cooling.grid(row=8,column=0,sticky=W)

        combo_cooling = ttk.Combobox(label_framleft,textvariable=self.var_coolingtype,font =("times new roman",16),width = 19,state ="readonly")
        combo_cooling["value"]=("Select","AC","Non AC")
        combo_cooling.current(0)
        combo_cooling.grid(row=8,column=1,sticky=W)

    #=================================Buttons=============================
        btnadd = Button(label_framleft,text="ADD",command = self.booking_data_add,font =("times new roman",16,"bold"),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btnadd.place(x = 60, y=400,width=150)

        btnupdate = Button(label_framleft,text="UPDATE",command=self.update,font =("times new roman",16,"bold"),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btnupdate.place(x = 280, y=400,width=150)

        btndelete= Button(label_framleft,text="DELETE",command=self.delete,font =("times new roman",16,"bold"),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btndelete.place(x = 60, y=480,width=150)

        btnreset = Button(label_framleft,text="RESET",command = self.reset,font =("times new roman",16,"bold"),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btnreset.place(x = 280, y=480,width=150)

    #==================================Check Available hall ==========================
        frame_tabel = LabelFrame(self.root,text ="Check Available hall",font =("times new roman",18,"bold"),bd= 5 ,relief = RIDGE)
        frame_tabel.place(x=5,y=60,width= 770, height =280)

        self.var_date = StringVar()
        lblsearch = Label(frame_tabel,text =" Date :",font =("times new roman",14,"bold"),fg="black")
        lblsearch.grid(row=0,column=0,sticky=W,padx=2)

        entry_search=DateEntry(frame_tabel,width=20,selectmode ='day',textvariable =self.var_date,font =("times new roman",14))
        entry_search.grid(row =0,column =1,padx=2)

        self.time_var = StringVar()
        lblsearch = Label(frame_tabel,text =" Time :",font =("times new roman",14,"bold"),fg ="black")
        lblsearch.grid(row=0,column=2,sticky=W,padx=2)

        combo_search = ttk.Combobox(frame_tabel,font =("times new roman",14),textvariable = self.time_var,width = 22,state ="readonly")
        combo_search["value"]=("Select","Day","Night","Fullday")
        combo_search.current(0)
        combo_search.grid(row=0,column=3,padx=2)


        btnsearch= Button(frame_tabel,text="CHECK",command=self.bookingcheck,width =11,font =("times new roman",10,"bold"),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btnsearch.grid(row =0,column =4,padx=2)

        btncheckreset= Button(frame_tabel,text="RESET",command=self.reset_check,width =11,font =("times new roman",10,"bold"),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btncheckreset.grid(row =0,column =5,padx=2)



     #============================show check tabel data  =======================
        show_frame =Frame(frame_tabel,bd =2,relief =RIDGE)
        show_frame.place(x=5,y=35,width=750,height=210)

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
        self.available_details_tabel.bind("<ButtonRelease-1>",self.cusrsor_book)


    #===========================================Booked Hall tabel ================================================
        frame_tabel1 = LabelFrame(self.root,text ="Booked Hall data",font =("times new roman",18,"bold"),bd= 5 ,relief = RIDGE)
        frame_tabel1.place(x=5,y=340,width= 770, height =310)

        self.search_var = StringVar()
        lblsearch = Label(frame_tabel1,text ="Search By:",font =("times new roman",14,"bold"),fg ="black")
        lblsearch.grid(row=0,column=0,sticky=W,padx=2)

        combo_search = ttk.Combobox(frame_tabel1,font =("times new roman",14),textvariable = self.search_var,width = 22,state ="readonly")
        combo_search["value"]=("Select","Customer No","Customer Name","Hall Name")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search = StringVar()
        entry_search=ttk.Entry(frame_tabel1,width=22,textvariable = self.txt_search,font =("times new roman",14))
        entry_search.grid(row =0,column =2,padx=2)

        btnsearch= Button(frame_tabel1,text="SEARCH",command =self.search,width =11,font =("times new roman",12,"bold"),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btnsearch.grid(row =0,column =3,padx=2)

        btnshowall = Button(frame_tabel1,text="SHOW ALL",command=self.fetch_deta,width =11,font =("times new roman",12,"bold"),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btnshowall.grid(row =0,column =4,padx=2)

     #============================show Booked tabel data  =======================
        show_frame =Frame(frame_tabel1,bd =2,relief =RIDGE)
        show_frame.place(x=5,y=35,width=750,height=240)

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
        self.booking_details_tabel.bind("<ButtonRelease-1>",self.cursor)




    #===========================================check number is valid or not========================================
    def check(self):
        if self.var_customerno.get()=="":
            messagebox.showerror("Error","Please Enter Contact Number",parent =self.root)
        else:
            client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
            db = client["application"]
            col = db["Customer"]
            query = {"mobile":self.var_customerno.get()}
            for i in col.find(query):
                rows =i
                list1 = list(rows.values())
                self.var_custname.set(list1[2])
                messagebox.showinfo("Info","this is valid customer number",self.root)
                break
            else:
                self.var_custname.set("")
                messagebox.showerror("Error","Please Enter Valid Contact Number",parent = self.root)

    #================================add data in booking tabel===============================
    def booking_data_add(self):
        if self.var_hall_name.get()=="" or self.var_hall_limit.get()=="" or self.var_custname.get()=="" or self.var_coolingtype.get()=="Select":
            messagebox.showerror("Error","All Fields Required",parent=self.root)
        else:
            client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
            db = client["application"]
            col = db["Booking Details"]
            query = {"Booking ID":self.var_bookingid.get()}
            for i in col.find(query):
                messagebox.showerror("Error","Booking already exist",parent=self.root)
                break
            else:
                try:
                    record = {"Customer No":self.var_customerno.get(),"Customer Name":self.var_custname.get(),"Booking ID":self.var_bookingid.get(),"Booking Date":self.var_bookdate.get(),"Time":self.var_time.get(),"Hall Name":self.var_hall_name.get(),"Hall Limit":self.var_hall_limit.get(), "Hall Price":self.var_hall_price.get(),"Cooling Type":self.var_coolingtype.get()}
                    col.insert_one(record)
                    self.fetch_deta()
                    messagebox.showinfo("Success", "Booking Successfully",parent=self.root)
                    self.reset()
                except Exception as e:
                    messagebox.showwarning("Warning","Some thing went wrong",parent=self.root)

    #===============================fetch and insert data in booking table==============================================
    def fetch_deta(self):
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

    #================================cursor for update or delete=======================================
    def cursor(self,event = ""):
        cursor_row = self.booking_details_tabel.focus()
        contain = self.booking_details_tabel.item(cursor_row)
        row = contain["values"]

        self.var_customerno.set(row[0]),
        self.var_custname.set(row[1]),
        self.var_bookingid.set(row[2]),
        self.var_bookdate.set(row[3]),
        self.var_time.set(row[4]),
        self.var_hall_name.set(row[5]),
        self.var_hall_limit.set(row[6]),
        self.var_hall_price.set(row[7]),
        self.var_coolingtype.set(row[8])

    #============================cursor for booking=====================================
    def cusrsor_book(self,event = ""):
        cursor_book_row = self.available_details_tabel.focus()
        contain  = self.available_details_tabel.item(cursor_book_row)
        row = contain["values"]
        self.var_hall_name.set(row[0])
        self.var_hall_limit.set(row[1])
        self.var_hall_price.set(row[2])
        self.var_bookdate.set(self.var_date.get())
        self.var_time.set(self.time_var.get())


    #================================update btn==================================
    def update(self):
        if self.var_customerno.get()=="" or self.var_hall_name==" ":
            messagebox.showerror("Error","Please enter all field",parent = self.root)
        else:
            try:
                client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
                db = client["application"]
                col = db["Booking Details"]
                query = {"Customer No":self.var_customerno.get()}
                new = {"Customer No":self.var_customerno.get(),"Customer Name":self.var_custname.get(),"Booking ID":self.var_bookingid.get(),"Booking Date":self.var_bookdate.get(),"Time":self.var_time.get(),"Hall Name":self.var_hall_name.get(),"Hall Limit":self.var_hall_limit.get(), "Hall Price":self.var_hall_price.get(),"Cooling Type":self.var_coolingtype.get()}
                col.update(query,new)
                self.fetch_deta()
                messagebox.showinfo("Update","Booking details has been updated successfully",parent = self.root)
                self.reset()
            except:
                pass
    #======================================Delete=============================
    def delete(self):
        mdelete=messagebox.askyesno("Marriage Hall Management","Do you want delete this Booking",parent = self.root)
        if mdelete>0:
            client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
            db = client["application"]
            col = db["Booking Details"]
            query = {"Customer No":self.var_customerno.get()}
            col.delete_one(query)
            self.reset()
        else:
            if not mdelete:
                return
        self.fetch_deta()

    #======================Reset==================================
    def reset(self):
        self.var_customerno.set(""),
        self.var_custname.set(""),
        self.var_bookdate.set(""),
        self.var_time.set(""),
        self.var_hall_limit.set(""),
        self.var_hall_name.set(""),
        self.var_hall_price.set(""),
        self.var_coolingtype.set("Select")
        x =random.randint(100000,1000000)
        self.var_bookingid.set(str(x))

    #========================Search===============================
    def search(self):
        client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
        db = client["application"]
        col = db["Booking Details"]
        query = {self.search_var.get():self.txt_search.get()}
        for i in col.find(query):
            rows =i
            if len(rows)!=0:
                self.booking_details_tabel.delete(*self.booking_details_tabel.get_children())
                t = tuple(rows.values())
                self.booking_details_tabel.insert("",END,values =t[1:10])
                self.search_var.set("Select")
                self.txt_search.set("")

    #==========================Booking check================
    def bookingcheck(self):
        self.available_details_tabel.delete(*self.available_details_tabel.get_children())
        if self.time_var.get()== "Select":
            messagebox.showerror("Error","Please Select Time",parent = self.root)
        else:
            client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
            db = client["application"]
            col1 = db["Booking Details"]
            col2 = db["Hall Manage"]
            query1 ={"Booking Date":self.var_date.get(),"Time":self.time_var.get()}
            l = []
            l1 =[]
            D ={"Time":"Fullday"}
            if query1["Time"] == D["Time"]:
                for i in col1.find({"$and": [{"Booking Date":self.var_date.get()},{"Time":{"$in":["Day","Night","Fullday"]}}]}):
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
                for i in col1.find({"$and": [{"Booking Date":self.var_date.get()},{"Time":{"$in":["Day","Night","Fullday"]}}]}):
                    row1 = list(i.values())
                    l.append(row1[6])
                for i in col2.find({"Hall Name" : {"$nin":l}}):
                    row = i
                    t = tuple(row.values())
                    self.available_details_tabel.insert("",END,values =t[1:4])

    def reset_check(self):
        self.time_var.set("Select")
        self.available_details_tabel.destroy()
        self.var_date.set("")

