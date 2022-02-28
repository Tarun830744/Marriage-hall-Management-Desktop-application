from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import pymongo
import random
from tkinter import  messagebox
import re
import hall
class cust_win:
    def __init__(self,root):
        self.root= root
        self.root.title("Customer")
        self.root.geometry("1300x663+233+130")
        self.root.resizable(width=False, height=False)

        icon = Image.open("images/city-hall.png")
        self.icon = ImageTk.PhotoImage(icon)
        self.root.iconphoto(FALSE,self.icon)
        
        #====================variable===========================
        self.var_ref=StringVar()
        x =random.randint(100,100000)
        self.var_ref.set(str(x))

        self.var_cname=StringVar()
        self.var_fname=StringVar()
        self.var_gender=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_idproof=StringVar()
        self.var_idnumber=StringVar()
        self.var_idnumber=StringVar()
        self.var_address=StringVar()
        self.var_pin=StringVar()
    #==========================logo========================
        img1 =Image.open("images/logo3.png")
        img1 = img1.resize((100,50),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(self.root,image =self.photoimg1)
        lblimg1.place(x=0,y=0,width =100,height=50)
    

    #==========================title======================
        lbl_title = Label(self.root,text ="ADD CUSTOMER DETAILS",font =("times new roman",20,"bold"),bg = "black",fg ="gold")
        lbl_title.place(x=100,y=0,width =1195,height =50)



    #==========================label frame====================
        label_framleft = LabelFrame(self.root,text ="Customer Details",font =("times new roman",18,"bold"),bd= 5 ,relief = RIDGE)
        label_framleft.place(x=5,y=60,width=450, height =590)

    #==========================labels and entry===================
        #==========================custref============================
        lblcust_ref = Label(label_framleft,text ="Customer Ref :",font =("times new roman",14),padx=6,pady=6)
        lblcust_ref.grid(row=0,column=0,sticky=W)

        entry_ref =ttk.Entry(label_framleft,textvariable=self.var_ref,width=29,font =("times new roman",13),state = "readonly")
        entry_ref.grid(row =0,column =1)

        #===========================custname===========================
        lblcust_name = Label(label_framleft,text ="Customer Name :",font =("times new roman",14),padx=6,pady=6)
        lblcust_name.grid(row=1,column=0,sticky=W)

        entry_name =ttk.Entry(label_framleft,textvariable=self.var_cname,width=29,font =("times new roman",13))
        entry_name.grid(row =1,column =1)

        #===========================father name========================
        lblcust_fname = Label(label_framleft,text ="Father Name :",font =("times new roman",14),padx=6,pady=6)
        lblcust_fname.grid(row=2,column=0,sticky=W)

        entry_fname =ttk.Entry(label_framleft,textvariable=self.var_fname,width=29,font =("times new roman",13))
        entry_fname.grid(row =2,column =1)

        #=============================gender============================
        lblcust_gen = Label(label_framleft,text ="Gender :",font =("times new roman",14),padx=6,pady=6)
        lblcust_gen.grid(row=3,column=0,sticky=W)

        combo_gender = ttk.Combobox(label_framleft,textvariable=self.var_gender,font =("times new roman",13),width = 27,state ="readonly")
        combo_gender["value"]=("Select","Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        #=============================mobile no=============================
        lblcust_mobile = Label(label_framleft,text ="Mobile No. :",font =("times new roman",14),padx=6,pady=6)
        lblcust_mobile.grid(row=4,column=0,sticky=W)

        entry_mobile =ttk.Entry(label_framleft,textvariable=self.var_mobile,width=29,font =("times new roman",13))
        entry_mobile.grid(row =4,column =1)


        #===============================email address=========================
        lblcust_email = Label(label_framleft,text ="Email :",font =("times new roman",14),padx=6,pady=6)
        lblcust_email.grid(row=5,column=0,sticky=W)

        entry_email =ttk.Entry(label_framleft,width=29,textvariable=self.var_email,font =("times new roman",13))
        entry_email.grid(row =5,column =1)


        #=================================nationality===========================
        lblcust_nat = Label(label_framleft,text ="Nationality :",font =("times new roman",14),padx=6,pady=6)
        lblcust_nat.grid(row=6,column=0,sticky=W)

        combo_nation = ttk.Combobox(label_framleft,textvariable=self.var_nationality,font =("times new roman",13),width = 27,state ="readonly")
        combo_nation["value"]=("Select","Indian","American","British","Other")
        combo_nation.current(0)
        combo_nation.grid(row=6,column=1)


        #============================idproof type==============================
        lblcust_idp = Label(label_framleft,text ="Id Proof Type:",font =("times new roman",14),padx=6,pady=6)
        lblcust_idp.grid(row=7,column=0,sticky=W)

        combo_idproof = ttk.Combobox(label_framleft,textvariable=self.var_idproof,font =("times new roman",13),width = 27,state ="readonly")
        combo_idproof["value"]=("Select","AdharCard","DrivingLicense","Passport","Pancard")
        combo_idproof.current(0)
        combo_idproof.grid(row=7,column=1)


        #==============================id_number========================
        lblcust_idn = Label(label_framleft,text ="Id Number :",font =("times new roman",14),padx=6,pady=6)
        lblcust_idn.grid(row=8,column=0,sticky=W)

        entry_idn =ttk.Entry(label_framleft,textvariable=self.var_idnumber,width=29,font =("times new roman",13))
        entry_idn.grid(row =8,column =1)

        #===============================address===========================
        lblcust_add = Label(label_framleft,text ="Address :",font =("times new roman",14),padx=6,pady=6)
        lblcust_add.grid(row=9,column=0,sticky=W)

        entry_add =ttk.Entry(label_framleft,textvariable=self.var_address,width=29,font =("times new roman",13))
        entry_add.grid(row =9,column =1)

        #===============================pincode=============================
        lblcust_pin = Label(label_framleft,text ="PinCode:",font =("times new roman",14),padx=6,pady=6)
        lblcust_pin.grid(row=10,column=0,sticky=W)

        entry_pin =ttk.Entry(label_framleft,textvariable=self.var_pin,width=29,font =("times new roman",13))
        entry_pin.grid(row =10,column =1)

        #=================================Buttons=============================
        btnadd = Button(label_framleft,command =self.add_data,text="ADD",font =("times new roman",13,"bold"),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btnadd.place(x = 30, y=430,width=150)

        btnupdate = Button(label_framleft,text="UPDATE",command =self.update,font =("times new roman",13,"bold"),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btnupdate.place(x = 240, y=430,width=150)

        btndelete= Button(label_framleft,text="DELETE",command = self.delete,font =("times new roman",13,"bold"),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btndelete.place(x = 30, y=480,width=150)
            
        btnreset = Button(label_framleft,text="RESET",command = self.reset,font =("times new roman",13,"bold"),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btnreset.place(x = 240, y=480,width=150)

        #=================================tabel Frame=============================
        frame_tabel = LabelFrame(self.root,text ="Search ",font =("times new roman",18,"bold"),bd= 5 ,relief = RIDGE)
        frame_tabel.place(x=460,y=60,width= 830, height =590)

        self.search_var = StringVar()
        lblsearch = Label(frame_tabel,text ="Search By :",font =("times new roman",14,"bold"),fg="black")
        lblsearch.grid(row=0,column=0,sticky=W,padx=2)

        combo_search = ttk.Combobox(frame_tabel,font =("times new roman",14),textvariable = self.search_var,width = 24,state ="readonly")
        combo_search["value"]=("Select","mobile","reference")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search = StringVar()
        entry_search=ttk.Entry(frame_tabel,width=24,textvariable =self.txt_search,font =("times new roman",14))
        entry_search.grid(row =0,column =2,padx=2)

        btnsearch= Button(frame_tabel,text="SEARCH",width =11,command = self.search,font =("times new roman",13,"bold"),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btnsearch.grid(row =0,column =3,padx=2)

            
        btnshowall = Button(frame_tabel,text="SHOW ALL",width =11,command = self.fetch_deta,font =("times new roman",13,"bold"),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btnshowall.grid(row =0,column =4,padx=2)

        #============================show data tabel =======================
        show_frame =Frame(frame_tabel,bd =2,relief =RIDGE)
        show_frame.place(x=3,y=50,width=815,height=505)

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
        self.cust_details_tabel.bind("<ButtonRelease-1>",self.cursor)


    def add_data(self):
        if self.var_mobile.get()==""or self.var_cname.get()=="" or self.var_idnumber.get()==""or self.var_gender.get()==""or self.var_gender.get()=="Select"or self.var_nationality.get()=="Select" or self.var_idproof.get()=="Select":
            messagebox.showerror("Error","All Fields Required",parent=self.root)
        else:
            contact = self.var_mobile.get() 
            mail = self.var_email.get()
            pincode = self.var_pin.get()
            if contact.isdigit() and len(str(contact)) ==10:
                if len(mail)>7 and re.match("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$",mail):
                    if len(pincode)==6:
                        client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
                        db = client["application"]
                        col = db["Customer"]
                        query = {"email":self.var_email.get(),"mobile":self.var_mobile.get(),"idnumber":self.var_idnumber.get()}
                        for i in col.find(query):
                            messagebox.showerror("Error","Customer already exist",parent=self.root)
                            break
                        else:
                            try:
                                record = {"reference":self.var_ref.get(),"cname":self.var_cname.get(), "fname" :self.var_fname.get(),"gender":self.var_gender.get(),"mobile":self.var_mobile.get(), "email":self.var_email.get(),"nationality":self.var_nationality.get(),"Id Proof":self.var_idproof.get(),"idnumber":self.var_idnumber.get(),"address":self.var_address.get(),"pincode":self.var_pin.get()}
                                col.insert_one(record)
                                self.fetch_deta()
                                messagebox.showinfo("Success","Customer Added Successfully",parent=self.root)
                                self.reset()
                            except Exception as e:
                                messagebox.showwarning("Warning","Some thing went wrong",parent=self.root)
                    else:
                        messagebox.showerror("Error","Please enter valid pincode",parent = self.root)
                else:
                    messagebox.showerror("Error","Please enter valid emial",parent = self.root)
            else:
                messagebox.showerror("Error","please enter valid number",parent = self.root)

    def fetch_deta(self):
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


    def cursor(self,event = ""):
        cursor_row = self.cust_details_tabel.focus()
        contain = self.cust_details_tabel.item(cursor_row)
        row = contain["values"]
        self.var_ref.set(row[0]),
        self.var_cname.set(row[1]),
        self.var_fname.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_mobile.set(row[4]),
        self.var_email.set(row[5]),
        self.var_nationality.set(row[6]),
        self.var_idproof.set(row[7]),
        self.var_idnumber.set(row[8]),
        self.var_address.set(row[9]),
        self.var_pin.set(row[10])

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent = self.root)
        else:
            try:
                client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
                db = client["application"]
                col = db["Customer"]
                query = {"reference":self.var_ref.get()}
                new = {"reference":self.var_ref.get(),"cname":self.var_cname.get(), "fname" :self.var_fname.get(),"gender":self.var_gender.get(),"mobile":self.var_mobile.get(), "email":self.var_email.get(),"nationality":self.var_nationality.get(),"Id Proof":self.var_idproof.get(),"idnumber":self.var_idnumber.get(),"address":self.var_address.get(),"pincode":self.var_pin.get()}
                col.update(query,new)
                self.fetch_deta()
                messagebox.showinfo("Update","Customer details hasbeen updated successfully",parent = self.root)
                self.reset()
            except:
                pass

    def delete(self):
        mdelete=messagebox.askyesno("Marriage Hall Management","Do you want delete this customer",parent = self.root)
        if mdelete>0:
            client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
            db = client["application"]
            col = db["Customer"]
            query = {"reference":self.var_ref.get()}
            col.delete_one(query)
        else:
            if not mdelete:
                return
        self.fetch_deta()
        self.reset()


    def reset(self):
        #self.var_ref.set(""),
        self.var_cname.set(""),
        self.var_fname.set(""),
        self.var_gender.set("Select"),
        self.var_mobile.set(""),
        self.var_email.set(""),
        self.var_nationality.set("Select"),
        self.var_idproof.set("Select"),
        self.var_idnumber.set(""),
        self.var_address.set(""),
        self.var_pin.set(""),
        x =random.randint(1000,99999)
        self.var_ref.set(str(x))

    def search(self):
        client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
        db = client["application"]
        col = db["Customer"]
        query = {self.search_var.get():self.txt_search.get()}
        for i in col.find(query):
            rows =i
            if len(rows)!=0:
                self.cust_details_tabel.delete(*self.cust_details_tabel.get_children())
                t = tuple(rows.values())
                self.cust_details_tabel.insert("",END,values =t[1:12])
                self.search_var.set("Select")
                self.txt_search.set("")


