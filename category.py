from tkinter import*
from PIL import Image,ImageTk  #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1080x520+190+120")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()
        
        #===========Variable===========
        self.var_cat_id=StringVar()
        self.var_name=StringVar()
        self.var_desc=StringVar()
        
        #===========title=================
       # lbl_title=Label(self.root,text=" Manage Product Details",font=("goudy old style",30,),bg='#184a45',fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
        title=Label(self.root,text="Manage Category Details",font=("goudy old style",20),bg='#0f4d7d',fg="white").place(x=0,y=4,width=1100)
       
        lbl_name=Label(self.root,text="Category Name",font=("goudy old style",20),bg="white").place(x=520,y=70)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",18),bg="lightyellow").place(x=710,y=70,width=245)
        
        lbl_desc=Label(self.root,text="Description",font=("goudy old style",20),bg="white").place(x=520,y=120)
        txt_desc=Entry(self.root,textvariable=self.var_desc,font=("goudy old style",18),bg="lightyellow").place(x=710,y=120,width=245,height=100)
        
       
        btn_add=Button(self.root,text="ADD",command=self.add,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=690,y=260,width=90,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="red",fg="white",cursor="hand2").place(x=800,y=260,width=90,height=30)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=910,y=260,width=90,height=30)
 
       
        #================category Detalis===========
        
        cat_Frame=Frame(self.root,bd=3,relief=RAISED)
        cat_Frame.place(x=520,y=300,width=550,height=210)
        
        scrolly=Scrollbar(cat_Frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_Frame,orient=HORIZONTAL)
       
        self.category_table=ttk.Treeview(cat_Frame,columns=("cid","name","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.category_table.xview)
        scrolly.config(command=self.category_table.yview)

        
        self.category_table.heading("cid",text="CID")
        self.category_table.heading("name",text="Name")
        self.category_table.heading("desc",text="Description")
        self.category_table["show"]="headings" 
        self.category_table.column("cid",width=40)
        self.category_table.column("name",width=150)
        self.category_table.column("desc",width=190)
        self.category_table.pack(fill=BOTH,expand=1)
        self.category_table.bind("<ButtonRelease-1>",self.get_data)

        
#======================================================
                                         
     #  #==========images==============
        self.im1=Image.open("image/product_category.png")
        #self.im1=self.im1.resize((500,250),Image.LANCZOS)
        self.im1=ImageTk.PhotoImage(self.im1)
          
        self.lbl_im1=Label(self.root,image=self.im1,bg="white")
        self.lbl_im1.place(x=10,y=90)   
        self.show()
        
          
#=======================function=================                                         
                
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Category name should be required",parent=self.root)
              
            else:
                cur.execute("Select * from category where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Category already present , try different",parent=self.root)
                else:
                    cur.execute("Insert into category(name,desc) values(?,?)",( 
                                self.var_name.get(),
                                self.var_desc.get(),
                    ))  
                    con.commit()            
                    messagebox.showinfo("Success","Category addedd Sucessfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)        
             
                      
    
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from category")
            rows=cur.fetchall()
            self.category_table.delete(*self.category_table.get_children())
            for row in rows:
              self.category_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)        
    
        
    def get_data(self,ev):
        f=self.category_table.focus()
        content=(self.category_table.item(f))
        row=content['values']
       # print(row) 
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])
        self.var_desc.set(row[2])
       
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:   
            if self.var_cat_id.get()=="":
                messagebox.showerror("Error","Please Select  Category From The List",parent=self.root)
            else:
                cur.execute("Select * from category where cid=?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Error,please try again.",parent=self.root)
                else:  
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True: 
                       cur.execute("delete from category where cid=?",(self.var_cat_id.get(),))       
                       con.commit()
                       messagebox.showinfo("Delete","Category Delted Sucessfully",parent=self.root)
                       self.show()
                       self.var_cat_id.set("")
                       self.var_name.set("")
                       self.var_desc.set("")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)        
    
    
    def clear(self):  
      
       self.var_name.set("")
       self.var_desc.set("")
       self.show()
    
    
           
  
if __name__=="__main__":
   root=Tk()
   obj=categoryClass(root)
   root.mainloop()     