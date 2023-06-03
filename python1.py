from tkinter import *

class multiple:
    def __init__ (self,root):
        self.root = root
        self.root.geometry("1000x1000")
        self.root.title("Home Page")
        
        login=Button(self.root,text="log in",font=("bold","15"),width=30,height=15,bg="#E9F7EF",command=self.login_page)
        login.place(x=150,y=100)
        
        signin=Button(self.root,text="sign in",font=("bold","15"),width=30,height=15,bg="#FEF5E7",command=self.signin_page)
        signin.place(x=800,y=100)
        
        label=Label(self.root,text="Facing any Technical Issue",font=("normal","12"))
        label.place(x=500,y=550)
        log=Button(self.root,text="Click Here",font=("bold","9"),command=self.support_page)
        log.place(x=690,y=550)
        
        
    def login_page(self):
        window1= Tk()
        window1.geometry("1000x1200")
        window1.title("Login Page")
        window1.config(bg="#E9F7EF")
        
        
        label=Label(window1,text="log in",font=("bold","30"),bg="#E9F7EF")
        label.place(x=550,y=50)
        line=Label(window1,text="____________________________________",bg="#E9F7EF")
        line.place(x=510,y=100)
        
        login1=Button(window1,text="User 1",font=("bold","30"),bg="#696969",fg="white",command=self.userlogin_page)
        login1.place(x=50,y=250)
        login2=Button(window1,text="user 2",font=("bold","30"),bg="#EE82EE",fg="white",command=self.userlogin_page)
        login2.place(x=220,y=250)
        login3=Button(window1,text="user 3",font=("bold","30"),bg="#00BFFF",fg="white",command=self.userlogin_page)
        login3.place(x=380,y=250)
        login4=Button(window1,text="user 4",font=("bold","30"),bg="#FFC300",fg="white",command=self.userlogin_page)
        login4.place(x=540,y=250)
        login5=Button(window1,text="user 5",font=("bold","30"),bg="#4169E1",fg="white",command=self.userlogin_page)
        login5.place(x=700,y=250)
        login6=Button(window1,text="New user login",font=("bold","30"),bg="#7FFF00",fg="white",command=self.userlogin_page)
        login6.place(x=900,y=250)
        label1=Label(window1,text="If you don't have an Account",font=("normal","10"),bg="#7FFF00")
        label1.place(x=500,y=502)
        login7=Button(window1,text="Sign in Here.",font=("bold","8"),bg="#7FFF00",command=self.signin_page)
        login7.place(x=670,y=500)
        label2=Label(window1,text="Facing any Technical Issue",font=("normal","10"),bg="#E9F7EF")
        label2.place(x=505,y=530)
        login8=Button(window1,text="Click Here",font=("bold","8"),bg="#E9F7EF",command=self.support_page)
        login8.place(x=670,y=530)
        
    def support_page(self):
        window=Tk()
        window.title("Support Page")
        window.geometry("1200x1000")
        window.config(bg="#E9F7EF")
        
        label=Label(window,text="Support Page",font=("bold","20"),bg="maroon",fg="white")
        label.pack()
        label=Label(window,text="Name              :",font=("bold","18"),bg="#E9F7EF")
        label.place(x=150,y=150)
        label=Label(window,text="Mail Id             :",font=("bold","18"),bg="#E9F7EF")
        label.place(x=150,y=190)
        label=Label(window,text="Type of issue   :",font=("bold","18"),bg="#E9F7EF")
        label.place(x=150,y=240)
        label=Label(window,text="On which page you are getting issue :",font=("bold","18"),bg="#E9F7EF")
        label.place(x=150,y=290)
        label=Label(window,text="Explain the issue : ",font=("bold","18"),bg="#E9F7EF")
        label.place(x=150,y=330)
        submit=Button(window,text="submit",font=("bold","10"),bg="maroon",fg="white")
        submit.place(x=550,y=450)
        
        entry=Entry(window,font=("11"),width="20")
        entry.place(x=350,y=150)
        entry=Entry(window,font=("11"),width="20")
        entry.place(x=350,y=190)
        entry=Entry(window,font=("11"),width="30")
        entry.place(x=350,y=240)
        entry=Entry(window,font=("11"),width="30")
        entry.place(x=570,y=295)
        
        rad1=Radiobutton(window,text="can't log in with a Microsoft account",font=("arial",10),bg="#E9F7EF",value=1)
        rad1.place(x=370,y=335)
        rad2=Radiobutton(window,text="can't log in with my password",font=("arial",10),bg="#E9F7EF",value=2)
        rad2.place(x=370,y=355)
        rad3=Radiobutton(window,text="can't log in after an update",font=("arial",10),bg="#E9F7EF",value=3)
        rad3.place(x=370,y=375)
        
    def signin_page(self):
        window2= Tk()
        window2.title("Sign In Page")
        window2.geometry("1000x1000")
        window2.config(bg="#E9F7EF")
        
        label=Label(window2,text="Sign In",font=("bold","30"),bg="white")
        label.place(x=550,y=50)
        label1=Label(window2,text="User Id :",font=("bold","20"),bg="#E9F7EF")
        label1.place(x=550,y=200)
        label2=Label(window2,text="Passward :",font=("bold","20"),bg="#E9F7EF")
        label2.place(x=550,y=240)
        label3=Label(window2,text="Re-enter Passward :",font=("bold","20"),bg="#E9F7EF")
        label3.place(x=550,y=280)
        label4=Label(window2,text="Mobile Number :",font=("bold","20"),bg="#E9F7EF")
        label4.place(x=550,y=320)
        label5=Label(window2,text="Nick Name :",font=("bold","20"),bg="#E9F7EF")
        label5.place(x=550,y=360)
        label4=Label(window2,text="",height="20",bg="black")
        label4.place(x=450,y=160)
        
        label=Label(window2,text='''Note:
        1.Passward should be        
          Upper case,Lower case,
          Special Char,Number     
        2.Nick Name Must              
        3.Number Must                  ''',font=("bold","15"))
        label.place(x=100,y=250)
        
        user_id=Entry(window2,font=("normal","15"),width="30")
        user_id.place(x=850,y=200)
        passward=Entry(window2,font=("normal","15"),width="30")
        passward.place(x=850,y=240)
        re_enter=Entry(window2,font=("normal","15"),width="30")
        re_enter.place(x=850,y=280)
        mobile_number=Entry(window2,font=("normal","15"),width="30")
        mobile_number.place(x=850,y=320)
        nick_name=Entry(window2,font=("normal","15"),width="30")
        nick_name.place(x=850,y=360)
        login=Button(window2,text="login",font=("bold","15"),bg="#000080",fg="white")
        login.place(x=600,y=450)
        
    def userlogin_page(self):
        window3 = Tk()
        window3.title("User login")
        window3.geometry("1000x1000")
        window3.config(bg="#E9F7EF")
        
        label=Label(window3,text="log in",font=("bold","30"),bg="#FFFFFF")
        label.place(x=550,y=100)
        label1=Label(window3,text="User Id.     :",font=("bold","20"),bg="#E9F7EF")
        label1.place(x=350,y=250)
        label2=Label(window3,text="Password  :",font=("bold","20"),bg="#E9F7EF")
        label2.place(x=350,y=300)
        
        userid=Entry(window3,font=("normal","15"),bg="#D3D3D3",width="30")
        userid.place(x=500,y=260)
        password=Entry(window3,font=("normal","15"),bg="#D3D3D3",width="30")
        password.place(x=500,y=310)
        login=Button(window3,text="log in",font=("bold","15"),bg="#4169E1",fg="#FFFFFF")
        login.place(x=570,y=400)
    
root =Tk()
obj= multiple(root)
root.mainloop()