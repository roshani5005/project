import sqlite3
def create_db():

    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text ,email text,gender text,dob text,contact text,emptype text,education text,wshift text,address text,doj text,salary text,pass text,utype text)")
    con.commit()                                                                                    
   
    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,name text,contact text,desc text)")
    con.commit()
 
    cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text,desc text )")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT,Category text,Supplier text,name text,price text,qty text,status text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF  NOT EXISTS name(eid INTEGER PRIMARY KEY AUTOINCREMENT,f_name text,l_name text,contact text,email text,password text)")
   
   # cur.execute("CREATE TABLE IF  NOT EXISTS user(eid INTEGER PRIMARY KEY AUTOINCREMENT,f_name text,l_name text,contact text,email text,utype text,password text)")
 #   con.commit()
 
create_db()   