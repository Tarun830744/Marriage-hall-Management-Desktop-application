from tkinter import*
from tkinter import ttk ,messagebox
from PIL import Image,ImageTk
import pymongo
import Marriage_Hall_Management

class Login_window:
    def __init__(self,root):
        self.root= root
        self.root.title("Admin Login")
        self.root.geometry("1550x795+0+0")
        self.root.state("zoomed")
        self.root.resizable(width=False, height=False)
        self.var_passward=StringVar()
        self.var_Email=StringVar()
        self.check_btn = IntVar(value=0)

        icon = Image.open("images/city-hall.png")
        self.icon = ImageTk.PhotoImage(icon)
        self.root.iconphoto(FALSE,self.icon)
        
        #==========background image===========
        im2 = Image.open("images/background.png")
        im2 = im2.resize((1600,900),Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(im2)
        label_bg = Label(self.root,image=self.bg)
        label_bg.place(x=0,y =0,relwidth=1,relheight=1)
        
        #=========frame for login =============
        frame = Frame(self.root,bg ="black")
        frame.place(x = 610,y=170,width =340,height=450)
       
        #==========frame image=============
        img1 = Image.open("images/frameimage.png")
        img1 = img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img1)
        labelimg1= Label(image = self.photoimage,bg= "black",borderwidth=0).place(x=730,y=175,width=100,height=100)
        
        #============text on frame=========== 
        get_str = Label(frame,text="Admin Login",font =("times new roman",20,"bold"),fg = "white",bg = "black")
        get_str.place(x=100,y=100)

        #===========label for user and pass==============
        username = Label(frame,text = "Username",font =("times new roman",15,"bold"),fg = "white",bg = "black")
        username.place(x=70,y=150)

        txtuser = ttk.Entry(frame,textvariable=self.var_Email,font =("times new roman",14))
        txtuser.place(x=40,y=185,width=270)

        password = Label(frame,text = "Passward",font =("times new roman",15,"bold"),fg = "white",bg = "black")
        password.place(x=70 ,y=220)

        self.txtpass = ttk.Entry(frame,textvariable = self.var_passward,show='*',font =("times new roman",14))
        self.txtpass.place(x=40,y=250,width=270)

        checkbox = Checkbutton(frame,variable=self.check_btn,onvalue =1,offvalue=0,command = self.show,bg = "black",activebackground="black")
        checkbox.place(x=33,y=290)
        #checkbox.config(fg="black")

        showpassward = Label(frame,text = "Show Passward",font =("times new roman",12,"bold"),fg = "white",bg = "black")
        showpassward.place(x=53 ,y=289)
        
        #=========icon image for user and pass=============
        img2 = Image.open("images/frameimage.png")
        img2 = img2.resize((23,23),Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        labelimg2= Label(image = self.photoimage2,bg= "black",borderwidth=0)
        labelimg2.place(x=650,y=323,width=23,height=23)

        img3 = Image.open("images/pass.png")
        img3 = img3.resize((23,23),Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        labelimg3= Label(image = self.photoimage3,bg= "black",borderwidth=0)
        labelimg3.place(x=650,y=392,width=23,height=23)

        #==========login button===========
        loginbutton = Button(frame,command =self.login,text = "Login",font =("times new roman",15,"bold"),bd = 2,relief=RIDGE,fg = "white",bg = "darkred",activeforeground="black",activebackground="darkred")
        loginbutton.place(x=110,y=350,width=120,height=35)

    def show(self):
        if(self.check_btn.get()==1):
            self.txtpass.config(show='')#passward visible
        else:
            self.txtpass.config(show='*')#passward not visible


    
    def login(self):
        if self.var_passward.get()=="" or self.var_Email.get()=="":
            messagebox.showerror("Error", "all field required",parent = self.root)
        else:
            client = pymongo.MongoClient("mongodb+srv://Tarun830744:Tarun369@cluster0.rfpx7.mongodb.net/application?retryWrites=true&w=majority")
            db = client["application"]
            collection = db["Login"]
            myquery = {"Email":self.var_Email.get(),"Passward":self.var_passward.get()}
            for i in collection.find(myquery):
                open_main = messagebox.askyesno("YesNo","Access")
                if open_main>0:
                    self.root.destroy()
                    Marriage_Hall_Management.hall_run()
                else:
                    if not open_main:
                        return
                break
            else:
                messagebox.showerror("Error", "please enter valid email and passward",parent = self.root)
