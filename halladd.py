from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import pymongo
import random
from tkinter import  messagebox
from pymongo import collection


class hall_win:
    def __init__(self,root):
        self.root= root
        self.root.title("Hall Manage")
        self.root.geometry("1300x663+233+130")
        #self.root.state("zoomed")
        self.root.resizable(width=False, height=False)

        icon = Image.open("images/city-hall.png")
        self.icon = ImageTk.PhotoImage(icon)
        self.root.iconphoto(FALSE,self.icon)

    #==========================Hall id generate================================
        self.var_hallname=StringVar()
        self.var_halllimit=StringVar()
        self.var_hallprice=StringVar()

    #==========================logo========================
        img1 =Image.open("images/logo3.png")
        img1 = img1.resize((100,50),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(self.root,image =self.photoimg1)
        lblimg1.place(x=0,y=0,width =100,height=50)

    #==========================title======================
        lbl_title = Label(self.root,text ="Hall Manage",anchor=CENTER,font =("times new roman",20,"bold"),bg = "black",fg ="gold")
        lbl_title.place(x=100,y=0,width =1195,height =50)


    #==========================label and entry frame====================
        label_framleft = LabelFrame(self.root,text ="Hall Manage",font =("times new roman",18,"bold"),bd= 5 ,relief = RIDGE)
        label_framleft.place(x=5,y=60,width= 450,height =320)

        #==============================Hall Name======================
        lbl_hotel_name = Label(label_framleft,text ="Hall Name :",font =("times new roman",14),padx=6,pady=6)
        lbl_hotel_name.grid(row=0,column=0,sticky=W)

        entry_hotel_name =ttk.Entry(label_framleft,textvariable=self.var_hallname,width=29,font =("times new roman",13))
        entry_hotel_name.grid(row =0,column =1)

        #===========================Hall Limit============================
        lblhall_limit = Label(label_framleft,text ="Hall Limit :",font =("times new roman",14),padx=6,pady=6)
        lblhall_limit.grid(row=1,column=0,sticky=W)

        entry_hall_limit =ttk.Entry(label_framleft,textvariable=self.var_halllimit,width=29,font =("times new roman",13))
        entry_hall_limit.grid(row =1,column =1)

        #=============================Hall Price====================
        lbl_hotel_price = Label(label_framleft,text ="Hall Price:",font =("times new roman",14),padx=6,pady=6)
        lbl_hotel_price.grid(row=2,column=0,sticky=W)

        entry_hotel_price =ttk.Entry(label_framleft,textvariable = self.var_hallprice,width=29,font =("times new roman",13))
        entry_hotel_price.grid(row =2,column =1)

    #=================================Buttons=============================
        btnadd = Button(label_framleft,text="ADD",command = self.hall_data_add,font =("times new roman",13),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btnadd.place(x = 40, y=180,width=150)

        btnupdate = Button(label_framleft,text="UPDATE",command = self.update,font =("times new roman",13),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btnupdate.place(x = 240, y=180,width=150)

        btndelete= Button(label_framleft,text="DELETE",command = self.delete,font =("times new roman",13),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btndelete.place(x = 40, y=230,width=150)

        btnreset = Button(label_framleft,text="RESET",command = self.reset,font =("times new roman",13),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btnreset.place(x = 240, y=230,width=150)

    #============================Hall Image============================
        img2 =Image.open("images/hall.jpg")
        img2 = img2.resize((450,270),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root,image =self.photoimg2)
        lblimg2.place(x=5,y=385,width =450,height=270)
    #=================================tabel Frame=============================
        frame_tabel = LabelFrame(self.root,text ="Search ",font =("times new roman",18,"bold"),bd= 5,relief = RIDGE)
        frame_tabel.place(x=460,y=60,width= 830, height =600)

        self.search_var = StringVar()
        lblsearch = Label(frame_tabel,text ="Search By :",font =("times new roman",14,"bold"),fg="black")
        lblsearch.grid(row=0,column=0,sticky=W,padx=2)

        combo_search = ttk.Combobox(frame_tabel,font =("times new roman",14),textvariable = self.search_var,width = 24,state ="readonly")
        combo_search["value"]=("Select","Hall Limit","Hall Price")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search = StringVar()
        entry_search=ttk.Entry(frame_tabel,width=24,textvariable = self.txt_search,font =("times new roman",14))
        entry_search.grid(row =0,column =2,padx=2)

        btnsearch= Button(frame_tabel,text="SEARCH",width =12,command = self.search,font =("times new roman",13),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btnsearch.grid(row =0,column =3,padx=2)

        btnshowall = Button(frame_tabel,text="SHOW ALL",width =12,command = self.fetch_deta,font =("times new roman",13),bg = "gold",fg="black",activeforeground="black",activebackground="gold")
        btnshowall.grid(row =0,column =4,padx=2)

     #============================show data tabel =======================
        show_frame =Frame(frame_tabel,bd =2,relief =RIDGE)
        show_frame.place(x=3,y=50,width=815,height=515)

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
        self.hall_details_tabel.bind("<ButtonRelease-1>",self.cursor)

    #=================================add hall=====================================
    def hall_data_add(self):
        if self.var_hallname.get()=="" or self.var_hallprice.get()==""or self.var_halllimit.get()=="":
            messagebox.showerror("Error","All Fields Required",parent=self.root)
        else:
            client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
            db = client["application"]
            col = db["Hall Manage"]
            query = {"Hall Name":self.var_hallname.get()}
            for i in col.find(query):
                messagebox.showerror("Error","Hall already exist",parent=self.root)
                break
            else:
                try:
                    record = {"Hall Name":self.var_hallname.get(),"Hall Limit":self.var_halllimit.get(), "Hall Price":self.var_hallprice.get()}
                    col.insert_one(record)
                    self.fetch_deta()
                    messagebox.showinfo("Success","Hall Added Successfully",parent=self.root)
                    self.reset()
                except Exception as e:
                    messagebox.showwarning("Warning","Some thing went wrong",parent=self.root)

    def fetch_deta(self):
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

    def cursor(self,event = ""):
        cursor_row = self.hall_details_tabel.focus()
        contain = self.hall_details_tabel.item(cursor_row)
        row = contain["values"]
        self.var_hallname.set(row[0]),
        self.var_halllimit.set(row[1]),
        self.var_hallprice.set(row[2])

    def update(self):
        if self.var_hallname.get()=="" or self.var_hallprice==" ":
            messagebox.showerror("Error","Please enter all field",parent = self.root)
        else:
            try:
                client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
                db = client["application"]
                col = db["Hall Manage"]
                query = {"Hall Name":self.var_hallname.get()}
                new = {"Hall Name":self.var_hallname.get(),"Hall Limit":self.var_halllimit.get(), "Hall Price":self.var_hallprice.get()}
                col.update(query,new)
                self.fetch_deta()
                messagebox.showinfo("Update","Hall details has been updated successfully",parent = self.root)
                self.reset()
            except:
                pass

    def delete(self):
        mdelete=messagebox.askyesno("Marriage Hall Management","Do you want delete this Hall",parent = self.root)
        if mdelete>0:
            client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
            db = client["application"]
            col = db["Hall Manage"]
            query = {"Hall Name":self.var_hallname.get()}
            col.delete_one(query)
        else:
            if not mdelete:
                return
        self.fetch_deta()
        self.reset()

    def reset(self):
        self.var_hallname.set(""),
        self.var_halllimit.set(""),
        self.var_hallprice.set("")

    def search(self):
        client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
        db = client["application"]
        col = db["Hall Manage"]
        query = {self.search_var.get():self.txt_search.get()}
        for i in col.find(query):
            rows =i
            if len(rows)!=0:
                self.hall_details_tabel.delete(*self.hall_details_tabel.get_children())
                t = tuple(rows.values())
                self.hall_details_tabel.insert("",END,values =t[1:4])
                self.search_var.set("Select")
                self.txt_search.set("")


