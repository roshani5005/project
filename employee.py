from tkinter import*
from PIL import Image,ImageTk  #pip install pillow
from tkinter import ttk,messagebox
import calendar
import time
from tkcalendar import DateEntry
import sqlite3
import re
class employeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1080x520+190+120")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()
        
        #============================
        #All Variables==========
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
          
        self.var_emp_id=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        
        self.var_emptype=StringVar()
        self.var_eduction=StringVar()
        self.var_workshift=StringVar()
        
        self.var_address=StringVar()
        self.var_doj=StringVar()
        self.var_salary=StringVar()
       
        self.var_pass=StringVar()
        self.var_utype=StringVar()
       
         
         #==========searchFrame====
        #SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        #SearchFrame.place(x=250,y=20,width=600,height=70)
        
        #======option============
        cmb_search=ttk.Combobox(self.root,textvariable=self.var_searchby,values=("Search By","name","Email","contact"),state='readonly',justify=CENTER,font=(" goudy old style",15))
        cmb_search.place(x=150,y=50,width=180,height=30)        
        cmb_search.current(0)
        Text_search=Entry(self.root,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=350,y=50,height=30)
       
        btn_search=Button(self.root, text="Search",command=self.search,font=("goudy old style",20),bg="#0f4d7d",fg="white",cursor="hand2").place(x=580,y=50,width=140,height=30)
        btn_show_all=Button(self.root,text="Show All",command=self.show_all,font=("goudy old style",20),bg='#0f4d7d',fg="white",cursor="hand2").place(x=770,y=50,width=140,height=30)
  
        #========title========
        title=Label(self.root,text="Manage Employee Details",font=("goudy old style",20),bg='#0f4d7d',fg="white").place(x=0,y=4,width=1100)
       
         #bd=3,
         #=== content==========
        #========row1=============
        
        lbl_empid=Label(self.root,text="Emp ID",font=("goudy old style",15),bg="white").place(x=25,y=260)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=420,y=260)
        lbl_email=Label(self.root,text="Email",font=("goudy old style",15),bg="white").place(x=770,y=260)
        
        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("goudy old style",15),bg="lightyellow").place(x=190,y=260,width=200)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=555,y=260,width=200)
        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15),bg="lightyellow").place(x=870,y=260,width=200)
       
        #========row2=============
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15),bg="white").place(x=25,y=300)
        lbl_dob=Label(self.root,text="Date of Birth",font=("goudy old style",15),bg="white").place(x=420,y=300)
        lbl_Contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=770,y=300)

        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_gender.place(x=190,y=300,width=200)       
        cmb_gender.current(0)
       
        txt_dob_entry=DateEntry(self.root,textvariable=self.var_dob,font=("goudy old style",15),bg="lightyellow",state="readonly",date_pattern='dd/mm/YYYY')
        txt_dob_entry.place(x=555,y=300,width=200)  
        
        txt_Contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=870,y=300,width=200)
       
       #========row3================
        lbl_emptype=Label(self.root,text="Employment Type",font=("goudy old style",15),bg="white").place(x=25,y=340)
        lbl_eduction=Label(self.root,text="Education",font=("goudy old style",15),bg="white").place(x=420,y=340)
        lbl_workshift=Label(self.root,text="Work Shift",font=("goudy old style",15),bg="white").place(x=770,y=340)
 
        cmb_emptype=ttk.Combobox(self.root,textvariable=self.var_emptype,values=("Select","Full Time","Part Time"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_emptype.place(x=190,y=340,width=200)       
        cmb_emptype.current(0)
        
        cmb_eduction=ttk.Combobox(self.root,textvariable=self.var_eduction,values=("Select","B.Tech","B.Com","M.Com","B.SC","M.SC","BBA","LLB"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_eduction.place(x=555,y=340,width=200)       
        cmb_eduction.current(0)
        
        cmb_workshift=ttk.Combobox(self.root,textvariable=self.var_workshift,values=("Select","Morning","Evening","Night"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_workshift.place(x=870,y=340,width=200)       
        cmb_workshift.current(0)
         #========row4=============
        
        lbl_address=Label(self.root,text="Address",font=("goudy old style",15),bg="white").place(x=25,y=380)
        lbl_doj=Label(self.root,text="Date of Joining",font=("goudy old style",15),bg="white").place(x=420,y=380)
        lbl_salary=Label(self.root,text="Salary",font=("goudy old style",15),bg="white").place(x=770,y=380)

        self.txt_address=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_address.place(x=190,y=380,width=200,height=90)
      #  txt_doj=Entry(self.root,textvariable=self.var_doj,font=("goudy old style",15),bg="lightyellow").place(x=555,y=380,width=200)
        txt_doj_entry=DateEntry(self.root,textvariable=self.var_doj,font=("goudy old style",15),bg="lightyellow",state="readonly",date_pattern='dd/mm/YYYY')
        txt_doj_entry.place(x=555,y=380,width=200) 
       # txt_doj_DataEntry=DateEntry(self.root,textvariable=self.var_doj,font=("goudy old style",15),bg="lightyellow",state="readonly",date_pattern='dd/mm/YYYY')
        #txt_doj_DataEntry.place(x=555,y=100,width=200)
        
        txt_salary=Entry(self.root,textvariable=self.var_salary,font=("goudy old style",15),bg="lightyellow").place(x=870,y=380,width=200)  
        
       
      #========row5=============
        
        lbl_pass=Label(self.root,text="Password",font=("goudy old style",15),bg="white").place(x=420,y=430)
        lbl_utype=Label(self.root,text="User Type",font=("goudy old style",15),bg="white").place(x=770,y=430)

        txt_pass=Entry(self.root,textvariable=self.var_pass,show="*",font=("goudy old style",15),bg="lightyellow").place(x=555,y=430,width=200)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Select","Admin","Employee"),state='readonly',justify=CENTER,font=(" goudy old style",15))
        cmb_utype.place(x=870,y=430,width=200)     
        cmb_utype.current(0)
       
       
      #===============buttons============
        btn_add=Button(self.root, text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=300,y=480,width=110,height=28)
        btn_update=Button(self.root, text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=450,y=480,width=110,height=28)
        btn_delete=Button(self.root, text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=600,y=480,width=110,height=28)
        btn_clear=Button(self.root, text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=750,y=480,width=110,height=28)
 
        #================Employee===========
        
        emp_Frame=Frame(self.root,bd=3,relief=RAISED)
        emp_Frame.place(x=0,y=85,relwidth=1,height=155)
        
        scrolly=Scrollbar(emp_Frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_Frame,orient=HORIZONTAL)
       
        self.EmployeeTable=ttk.Treeview(emp_Frame,columns=("eid","name","email","gender","dob","contact","emptype","education","wshift","address","doj","salary","pass","utype"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        
        self.EmployeeTable.heading("eid",text="EMP ID")
        self.EmployeeTable.heading("name",text="Name")
        self.EmployeeTable.heading("email",text="Email")
        self.EmployeeTable.heading("gender",text="Gender")
        self.EmployeeTable.heading("dob",text="Date of Birth")
        self.EmployeeTable.heading("contact",text="Contact")
        self.EmployeeTable.heading("emptype",text="Employement Type")
        self.EmployeeTable.heading("education",text="Education")
        self.EmployeeTable.heading("wshift",text="Work Shift")
        self.EmployeeTable.heading("address",text="Address")
        self.EmployeeTable.heading("doj",text="Date of Joining")
        self.EmployeeTable.heading("salary",text="Salary")
        self.EmployeeTable.heading("pass",text="Password")
        self.EmployeeTable.heading("utype",text="User Type")
        
        
        self.EmployeeTable["show"]="headings"
        
        self.EmployeeTable.column("eid",width=90)
        self.EmployeeTable.column("name",width=160)
        self.EmployeeTable.column("email",width=160)
        self.EmployeeTable.column("gender",width=100)
        self.EmployeeTable.column("dob",width=100)
        self.EmployeeTable.column("contact",width=100)
        self.EmployeeTable.column("emptype",width=110)
        self.EmployeeTable.column("education",width=100)
        self.EmployeeTable.column("wshift",width=100)
        self.EmployeeTable.column("address",width=160)
        self.EmployeeTable.column("doj",width=100)
        self.EmployeeTable.column("salary",width=100)
        self.EmployeeTable.column("pass",width=90)
        self.EmployeeTable.column("utype",width=100)
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
#======================================================
  
    def add(self):
        con=sqlite3.connect(database=r'ims.db') 
        cur=con.cursor()     
   
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Must be required",parent=self.root)
          
            elif self.var_emp_id.get()=="" or self.var_name.get()=="" or self.var_email.get()=="" or self.var_gender.get()=="Select" or  self.var_contact.get()=="" or  self.var_dob.get()=="" or self.var_doj.get()=="" or self.var_utype.get()=="select" or self.var_salary.get()=="":
                messagebox.showerror("Error","All Fields are required",parent=self.root) 
                
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Employee ID already assigned, try different",parent=self.root)
                else:
                    cur.execute("Insert into employee (eid,name,email,gender,dob,contact,emptype,education,wshift,address,doj,salary,pass,utype) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",( 
                                        self.var_emp_id.get(),  
                                        self.var_name.get(),
                                        self.var_email.get(),
                                        
                                        self.var_gender.get(),
                                        self.var_dob.get(),
                                        self.var_contact.get(),
                                           
                                        self.var_emptype.get(),
                                        self.var_eduction.get(),
                                        self.var_workshift.get(),
                                        
                                        self.txt_address.get('1.0',END),
                                        self.var_doj.get(),
                                        self.var_salary.get(),
                                        
                                        self.var_pass.get(),
                                        self.var_utype.get(),
                                       
                                      
                    ))
                    con.commit() 
                    messagebox.showinfo("Success","Employee Addedd Sucessfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)        
       
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
           cur.execute("Select * from employee")
           rows=cur.fetchall()
           self.EmployeeTable.delete(*self.EmployeeTable.get_children())
           for row in rows:
               self.EmployeeTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)        
    
    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    cur.execute("Update employee set name=?,email=?,gender=?,dob=?,contact=?,emptype=?,education=?,wshift=?,address=?,doj=?,salary=?,pass=?,utype=? where eid=? ",( 
                                        self.var_name.get(),
                                        self.var_email.get(),
                                        self.var_gender.get(),
                                        self.var_dob.get(),
                                        self.var_contact.get(),
                                        self.var_emptype.get(),
                                        self.var_eduction.get(),
                                        self.var_workshift.get(),
                                        self.txt_address.get('1.0',END),
                                        self.var_doj.get(),
                                        self.var_salary.get(),
                                        self.var_pass.get(),
                                        self.var_utype.get(),
                                        self.var_emp_id.get(),
                                     
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Updated Sucessfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)        
       
     
    def get_data(self,ev):                                       
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
       # print(row)                                                              
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_contact.set(row[5])
        self.var_emptype.set(row[6])
        self.var_eduction.set(row[7])
        self.var_workshift.set(row[8])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[9])
        self.var_doj.set(row[10])
        self.var_salary.set(row[11])                             
        self.var_pass.set(row[12])
        self.var_utype.set(row[13])
       
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:   
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID Must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:  
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True: 
                       cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))       
                       con.commit()
                       messagebox.showinfo("Delete","Employee Delted Sucessfully",parent=self.root)
                       self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)        
    
    
    def clear(self):  
        
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_emptype.set("Select")
        self.var_eduction.set("Select")
        self.var_workshift.set("Select")                               
        self.txt_address.delete('1.0',END)
        self.var_doj.set("")
        self.var_salary.set("")                               
        self.var_pass.set("")
        self.var_utype.set("Admin")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()
       
    def search(self):  
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select search By option",parent=self.root)
            elif self.var_searchtxt.get()=="":  
                messagebox.showerror("Error","Search input should be required",parent=self.root)  
           
            else:
                cur.execute("Select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","NO record found!!!",parent=self.root)  
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)        
     
    def show_all(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:            
            cur.execute("select eid,name,email,gender,dob,contact,emptype,education,wshift,address,doj,salary,pass,utype from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
               self.EmployeeTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)        
        
   

if __name__=="__main__":
   root=Tk()
   obj=employeeClass(root)
   root.mainloop()         