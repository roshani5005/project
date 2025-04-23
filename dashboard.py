from tkinter import*
from PIL import Image,ImageTk  #pip install pillow
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from  sales import  salesClass
import sqlite3
from tkinter import messagebox
import os
import time
class IMS:
    def __init__(self,root):
        self.root=root  #("1350x700+0+0")
        self.root.geometry("1350x750+0+0")
        self.root.title("Inventory Management System ")
        self.root.config(bg="white")
       # self.root.resizable(0,0)
        #====== title==========
        self.icon_title=PhotoImage(file="image\window.png")
        title=Label(self.root,text="Inventory Managemnet system",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        
        #==btn_Logout====
        btn_logout=Button(self.root,text="Logout",command=self.logout,font=("time new roman",15,"bold"),bg='#0f4d7d',fg="white",cursor="hand2").place(x=1100,y=10,height=50,width=150)
       
        #=====clock======
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Managemnet system\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15,"bold"),bg="#4D636D",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        
        #====Left Menu=====
        self.MenuLogo=Image.open("image/logo.png")
        self.MenuLogo=self.MenuLogo.resize((160,160),Image.LANCZOS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        
        LeftMenu=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=100,width=200,height=550)
          
        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)   
        
        self.icon_side=PhotoImage(file="image/logo.png")
        lbl_menu=Label(LeftMenu,text="Menu",font=("time new roman",30),bg="#009688").pack(side=TOP,fill=X)
        self.employee_icon=PhotoImage(file="image/employee.png")
        btn_employee=Button(LeftMenu,text="Employees",command=self.employee,image=self.employee_icon,compound=LEFT,padx=5,anchor="w",font=("time new roman",20),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
       
        self.supplier_icon=PhotoImage(file="image/supplier.png")
        btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,image=self.supplier_icon,compound=LEFT,padx=5,anchor="w",font=("time new roman",20),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
       
        self.category_icon=PhotoImage(file="image/category.png")
        btn_category=Button(LeftMenu,text="Category",command=self.category,image=self.category_icon,compound=LEFT,padx=5,anchor="w",font=("time new roman",20),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        self.product_icon=PhotoImage(file="image/product.png")
        btn_product=Button(LeftMenu,text="Product",command=self.product,image=self.product_icon,compound=LEFT,padx=5,anchor="w",font=("time new roman",20),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        self.sales_icon=PhotoImage(file="image/sales.png")
        btn_sales=Button(LeftMenu,text="Sales",command=self.sales,image=self.sales_icon,compound=LEFT,padx=5,anchor="w",font=("time new roman",20),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        self.exit_icon=PhotoImage(file="image/exit.png")
        btn_exit=Button(LeftMenu,text="Exit",command=self.exit,image=self.exit_icon,compound=LEFT,padx=5,anchor="w",font=("time new roman",20),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

       
        #==========content===========
         #==========content==========="#2C3E50"
        emp_frame=Frame(root,bg="#607d8b",bd=3,relief=RIDGE)
        emp_frame.place(x=400,y=115,height=165,width=270) 
        self.total_emp_icon=PhotoImage(file="image/total_emp.png")
        total_emp_icon_label=Label(emp_frame,image=self.total_emp_icon,bg="#607d8b")
        total_emp_icon_label.pack()
        total_emp_Label=Label(emp_frame,text="Total Employees",bg="#607d8b",fg='white',font=("goudy old style",20,"bold"))
        total_emp_Label.pack()
        self.total_emp_count_Label=Label(emp_frame,text="0",bg="#607d8b",fg='white',font=("goudy old style",30,"bold"))
        self.total_emp_count_Label.pack()
              
        sup_frame=Frame(root,bg="#8E44AD",bd=3,relief=RIDGE)
        sup_frame.place(x=770,y=115,height=165,width=270)
        self.total_sup_icon=PhotoImage(file="image/total_sup.png")
        total_sup_icon_label=Label(sup_frame,image=self.total_sup_icon,bg="#8E44AD")
        total_sup_icon_label.pack()
        total_sup_Label=Label(sup_frame,text="Total Suppliers",bg='#8E44AD',fg='white',font=("goudy old style",20,"bold"))
        total_sup_Label.pack()
        self.total_sup_count_Label=Label(sup_frame,text="0",bg="#8E44AD",fg='white',font=("goudy old style",30,"bold"))
        self.total_sup_count_Label.pack()
        
        cat_frame=Frame(root,bg="#27AE60",bd=3,relief=RIDGE)
        cat_frame.place(x=400,y=300,height=165,width=270)
        self.total_cat_icon=PhotoImage(file="image/total_cat.png")
        total_cat_icon_label=Label(cat_frame,image=self.total_cat_icon,bg="#27AE60")
        total_cat_icon_label.pack()
        total_cat_Label=Label(cat_frame,text="Total Categories",bg="#27AE60",fg='white',font=("goudy old style",20,"bold"))
        total_cat_Label.pack()
        self.total_cat_count_Label=Label(cat_frame,text="0",bg="#27AE60",fg='white',font=("goudy old style",30,"bold"))
        self.total_cat_count_Label.pack()
        
        prod_frame=Frame(root,bg="#009688",bd=3,relief=RIDGE)
        prod_frame.place(x=770,y=300,height=165,width=270)
        self.total_prod_icon=PhotoImage(file="image/total_prod.png")
        total_prod_icon_label=Label(prod_frame,image=self.total_prod_icon,bg="#009688")
        total_prod_icon_label.pack()
        total_prod_Label=Label(prod_frame,text="Total Product",bg="#009688",fg='white',font=("goudy old style",20,"bold"))
        total_prod_Label.pack()
        self.total_prod_count_Label=Label(prod_frame,text="0",bg="#009688",fg='white',font=("goudy old style",30,"bold"))
        self.total_prod_count_Label.pack()
        
        sales_frame=Frame(root,bg="#E74C3C",bd=3,relief=RIDGE)
        sales_frame.place(x=600,y=476,height=165,width=270)
        self.total_sales_icon=PhotoImage(file="image/total_sales.png")
        total_sales_icon_label=Label( sales_frame,image=self.total_sales_icon,bg="#E74C3C")
        total_sales_icon_label.pack()
        total_sales_Label=Label(sales_frame,text="Total Sales",bg='#E74C3C',fg='white',font=("goudy old style",20,"bold"))
        total_sales_Label.pack()
        self.total_sale_count_Label=Label(sales_frame,text="0",bg='#E74C3C',fg='white',font=("goudy old style",30,"bold"))
        self.total_sale_count_Label.pack()
          
        self.update_content()  
           
#===================================================   
    def employee(self):
        self.new_win=Toplevel(self.root)  
        self.new_obj=employeeClass(self.new_win)
    
    def supplier(self):
        self.new_win=Toplevel(self.root)  
        self.new_obj=supplierClass(self.new_win)
        
    def category(self):
        self.new_win=Toplevel(self.root)  
        self.new_obj=categoryClass(self.new_win)
        
    def product(self):
        self.new_win=Toplevel(self.root)  
        self.new_obj=productClass(self.new_win)
        
    def sales(self):
        self.new_win=Toplevel(self.root)  
        self.new_obj=salesClass(self.new_win)
        
                          
    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.total_prod_count_Label.config(text=(len(product)))
           
            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.total_sup_count_Label.config(text=len(supplier))
           
            cur.execute("select * from category")
            category=cur.fetchall()
            self.total_cat_count_Label.config(text=len(category))
                
            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.total_emp_count_Label.config(text=len(employee))
            
            bill=(len(os.listdir('bill')))
            self.total_sale_count_Label.config(text=str(bill))
            
         
            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m-%Y")  
            self.lbl_clock.config(text=f"Welcome to Inventory Managemnet system\t\t Date: {str(date_)}\t\t Time:{str(time_)}")
            self.lbl_clock.after(200,self.update_content)       

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)      
       
    def logout(self):
        self.root.destroy
        os.system("python login.py")     
    
    
    def exit(self):
        op=messagebox.askyesno("Confirm","DO you really want to Exist?",parent=self.root) 
        if op==True:
           self.root.destroy()
      #  os.system("python login.py")    
         
  #  def login(self):
   #     if self.usename.get()=="" or self.password.get()=="":
    #        messagebox.showerror("Error","All Fields are required")
     #   elif self.usename.get()!="Rosahni" or self.password.get()!="123456":
      #      messagebox.showerror("Error","Invaild Username or Password\nTry again with correct creder")    
       # else:
        #    messagebox.showinfo("Informationa",f"welcome :{self.usename.get()}\nYour Password: {self}) 
       
       
           
if __name__=="__main__":
   root=Tk()
   obj=IMS(root)
   root.mainloop()    