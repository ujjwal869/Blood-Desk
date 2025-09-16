global root
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from tkinter import messagebox                             
import sqlite3 as c
from time import strftime,strptime
import datetime as dt
import re
from tkcalendar import DateEntry
import subprocess

global format_date
date=dt.datetime.now()
format_date=f"{date:%d/%m/%y}"

global D
D={"A+":"Aplus","B+":"Bplus","O+":"Oplus","AB+":"ABplus","A-":"Aneg","B-":"Bneg","O-":"Oneg","AB-":"ABneg"}


def donaterdetails():
    global root
    global unit 
    global Cust_Details_Table
    global txtcname
    global combo_Gender
    global txtpostcode
    global txtmobile
    global combo_nationality
    global combo_idproof
    global txtidnumber
    global combo_age
    global combo_bloodtype
    global txtunit
    global combo_anydi
    global row
    global combo_Search
    global txtSearch
    global D
    
    root=Tk()

    root.title("Donater Details")
    root.geometry("1300x680+0+142")

    #title
    lbl_title=Label(root,text="Donater Details",font=("times new roman",18,"bold"),bg="azure2",fg="red",bd=4,relief=RIDGE)
    lbl_title.place(x=0,y=0,width=1300,height=50)

    labelframeleft=LabelFrame(root,bd=2,relief=RIDGE,text="Donater Details",padx=2,font=("times new roman",18,"bold"))
    labelframeleft.place(x=5,y=50,width=450,height=510)

    #name

    cname=Label(labelframeleft,font=("arial",11,"bold"),text="Donater Name:",padx=10,pady=8)
    cname.grid(row=0,column=0,sticky=W)

    txtcname=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
    txtcname.grid(row=0,column=1)

    #gender

    label_Gender=Label(labelframeleft,font=("arial",11,"bold"),text="Gender:",padx=10,pady=8)
    label_Gender.grid(row=1,column=0,sticky=W)
    
    combo_Gender=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27)
    combo_Gender["value"]=("Male","Female","Other")
    combo_Gender.current(0)   
    combo_Gender.grid(row=1,column=1)

    #post code

    lblpostcode=Label(labelframeleft,font=("arial",11,"bold"),text="Address:",padx=10,pady=8)
    lblpostcode.grid(row=2,column=0,sticky=W)
        
    txtpostcode=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
    txtpostcode.grid(row=2,column=1)

    # mobile number

    lblmobilenum=Label(labelframeleft,font=("arial",11,"bold"),text="Mobile Number:",padx=10,pady=8)
    lblmobilenum.grid(row=3,column=0,sticky=W)
        
    txtmobile=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
    txtmobile.grid(row=3,column=1)


    #nationality

    lblnationality=Label(labelframeleft,font=("arial",12,"bold"),text="Nationality:",padx=10,pady=8)
    lblnationality.grid(row=5,column=0,sticky=W)

    combo_nationality=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27)
    combo_nationality["value"]=("Indian","American","British","Other")
    combo_nationality.current(0)
    combo_nationality.grid(row=5,column=1)

    #id proof type combobox

    lblidproof=Label(labelframeleft,font=("arial",12,"bold"),text="ID Proof Type:",padx=10,pady=8)
    lblidproof.grid(row=6,column=0,sticky=W)

    combo_idproof=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27)
    combo_idproof["value"]=("Aadhaar Card","Driving Licence","Passport","Visa","Voter ID","Pan Card")
    combo_idproof.current(0)
    combo_idproof.grid(row=6,column=1)

    #id num

    lblidnum=Label(labelframeleft,font=("arial",11,"bold"),text="ID Number:",padx=10,pady=8)
    lblidnum.grid(row=7,column=0,sticky=W)
        
    txtidnumber=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
    txtidnumber.grid(row=7,column=1)

    #fromwhere combobox

    label_age=Label(labelframeleft,font=("arial",11,"bold"),text="Age:",padx=10,pady=8)
    label_age.grid(row=8,column=0,sticky=W)
    
    combo_age=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27)
    combo_age["value"]=("18-20","21-30","31-40","41-50","51-60","61-70")
    combo_age.current(0)   
    combo_age.grid(row=8,column=1)

    #towhere combobox

    label_bloodtype=Label(labelframeleft,font=("arial",11,"bold"),text="Blood Type:",padx=10,pady=8)
    label_bloodtype.grid(row=9,column=0,sticky=W)
    
    combo_bloodtype=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27)
    combo_bloodtype["value"]=("A+","B+","O+","AB+","A-","B-","O-","AB-")
    combo_bloodtype.current(0)   
    combo_bloodtype.grid(row=9,column=1)

    lblunit=Label(labelframeleft,font=("arial",11,"bold"),text="Unit(in ml):",padx=10,pady=8)
    lblunit.grid(row=10,column=0,sticky=W)
    
    txtunit=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
    txtunit.grid(row=10,column=1)


    label_anydi=Label(labelframeleft,font=("arial",11,"bold"),text="Any Disease(if any):",padx=10,pady=8)
    label_anydi.grid(row=11,column=0,sticky=W)
    
    combo_anydi=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27)
    combo_anydi["value"]=("Yes","No")
    combo_anydi.current(1)   
    combo_anydi.grid(row=11,column=1)

    #btns of cust

    btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
    btn_frame.place(x=8,y=435,width=417,height=40)


    #add btn in custbox

    btnAdd=Button(btn_frame,text="Add",command=adddonater,font=("arial",12,"bold"),bg="azure2",fg="red",activeforeground="red",activebackground="azure2",width=9,height=1)
    btnAdd.grid(row=0,column=0,padx=1,pady=2)

    #btn update

    btnUpdate=Button(btn_frame,text="Update",command=updatedonater,font=("arial",12,"bold"),bg="azure2",fg="red",activeforeground="red",activebackground="azure2",width=9,height=1)
    btnUpdate.grid(row=0,column=1,padx=1,pady=2)

    #btn delete

    btnDelete=Button(btn_frame,text="Delete",command=deletedonater,font=("arial",12,"bold"),bg="azure2",fg="red",activeforeground="red",activebackground="azure2",width=9,height=1)
    btnDelete.grid(row=0,column=2,padx=1,pady=2)

    #btn reset


    btnReset=Button(btn_frame,text="Reset",command=resetDonater,font=("arial",12,"bold"),bg="azure2",fg="red",activeforeground="red",activebackground="azure2",width=9,height=1)
    btnReset.grid(row=0,column=3,padx=1,pady=2)

    #cust inside frame

    Table_Frame=LabelFrame(root,bd=2,relief=RIDGE,text="View Details And Search System",padx=2,font=("times new roman",13,"bold"))
    Table_Frame.place(x=440,y=50,width=860,height=510)

    #search by (red colour)
    lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By",bg="red",fg="white")
    lblSearchBy.grid(row=0,column=0,sticky=W,padx=3)

    #search by

    combo_Search=ttk.Combobox(Table_Frame,font=("arial",12,"bold"),width=24,state="readonly")
    combo_Search["value"]=("Mobile","Idnumber")
    combo_Search.current(0)
    combo_Search.grid(row=0,column=1,padx=2)

    #search field

    txtSearch=ttk.Entry(Table_Frame,width=24,font=("times new roman",13,"bold"))
    txtSearch.grid(row=0,column=2,padx=2)

    btnSearch=Button(Table_Frame,text="Search",command=searchdonater,font=("arial",12,"bold"),bg="azure2",fg="red",activeforeground="red",activebackground="azure2",width=10)
    btnSearch.grid(row=0,column=3,padx=1,pady=2)

    btnShowAll=Button(Table_Frame,text="Show All",command=fetch_datadonater,font=("arial",12,"bold"),bg="azure2",fg="red",activeforeground="red",activebackground="azure2",width=10)
    btnShowAll.grid(row=0,column=4,padx=1,pady=2)

    #show data table

    Details_Table=Frame(Table_Frame,bd=2,relief=RIDGE)
    Details_Table.place(x=0,y=50,width=860,height=430)

    #scroll bar 

    scroll_x=ttk.Scrollbar(Details_Table,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(Details_Table,orient=VERTICAL)

    global Cust_Details_Table

    Cust_Details_Table=ttk.Treeview(Details_Table,column=("date","Name","Gender","Pincode","Mobile","Nationality","Idproof","Idnumber","Age","Bloodtype","Unitml"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x.config(command=Cust_Details_Table.xview)

    scroll_y.config(command=Cust_Details_Table.yview)

    #scroll bar column show like name,father,......
    Cust_Details_Table.heading("date",text="Date")
    Cust_Details_Table.heading("Name",text="Donater Name")
    Cust_Details_Table.heading("Gender",text="Gender")
    Cust_Details_Table.heading("Pincode",text="Address")
    Cust_Details_Table.heading("Mobile",text="Mobile")
    Cust_Details_Table.heading("Nationality",text="Nationality")
    Cust_Details_Table.heading("Idproof",text="ID Proof")
    Cust_Details_Table.heading("Idnumber",text="ID Number")
    Cust_Details_Table.heading("Age",text="Age")
    Cust_Details_Table.heading("Bloodtype",text="Blood Type")
    Cust_Details_Table.heading("Unitml",text="Unit(in ml)")
    
    

    #show karenge avi headings

    Cust_Details_Table["show"]="headings"

    #width shape karre columns ka
    Cust_Details_Table.column("date",width=80,anchor=CENTER)
    Cust_Details_Table.column("Name",width=90,anchor=CENTER)
    Cust_Details_Table.column("Gender",width=70,anchor=CENTER)
    Cust_Details_Table.column("Pincode",width=80,anchor=CENTER)
    Cust_Details_Table.column("Mobile",width=80,anchor=CENTER)
    Cust_Details_Table.column("Nationality",width=80,anchor=CENTER)
    Cust_Details_Table.column("Idproof",width=80,anchor=CENTER)
    Cust_Details_Table.column("Idnumber",width=80,anchor=CENTER)
    Cust_Details_Table.column("Age",width=80,anchor=CENTER)
    Cust_Details_Table.column("Bloodtype",width=80,anchor=CENTER)
    Cust_Details_Table.column("Unitml",width=80,anchor=CENTER)
    

    #pack karre phir expand then save karke apne adjust lelega

    Cust_Details_Table.pack(fill=BOTH,expand=1)

    Cust_Details_Table.bind("<ButtonRelease-1>",get_cuersorD)

    fetch_datadonater()

    root.mainloop()




#--Add Donater Details--#

def adddonater():
    global root
    global txtcname
    global combo_Gender
    global txtpostcode
    global txtmobile
    global combo_nationality
    global combo_idproof
    global txtidnumber
    global combo_age
    global combo_bloodtype
    global txtunit
    global combo_anydi
    global Cust_Details_Table
    global row
    global D
    global avl
    global format_date

    mobile=str(txtmobile.get())
    pin=str(txtpostcode.get())

    #Mobile number checking code

    def isvalidmobile(s):
        Pattern=re.compile("(0|91)?[6-9][0-9]{9}")
        return Pattern.match(s)


    if txtcname.get()=="" or str(combo_age.get())=="" or combo_nationality.get()=="" or combo_idproof.get()=="" or combo_Gender.get()=="" or str(txtmobile.get())=="" or str(txtpostcode.get())=="" or combo_bloodtype.get()=="" or str(txtidnumber.get())=="" or combo_anydi.get()=="" or str(txtunit.get())=="":
        messagebox.showerror("Error","All fields are required",parent=root)

    elif not str(txtcname.get()).isalpha():
        messagebox.showerror("Error","Please Enter Data in Alphabets in the Donater Name box",parent=root)

    elif str(combo_anydi.get())=="yes" or str(combo_anydi.get())=="Yes":
        messagebox.showerror("Sorry","You can`t Donate Blood\nYou are suffering from Disease",parent=root)

    elif (isvalidmobile(mobile)) is None:
        messagebox.showerror("Error","Incorrect Mobile Number"+"\nPlease Enter Indian Mobile Number",parent=root)
    
    else:
        try:
            conn=c.connect("blood.db")
            my_cursor=conn.cursor()
            
            
            my_cursor.execute("insert into donater (date,Name,Gender,Pincode,Mobile,Nationality,Idproof,Idnumber,Age,Bloodtype,Unitml)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(str(format_date),txtcname.get(),combo_Gender.get(),str(txtpostcode.get()),str(txtmobile.get()),combo_nationality.get(),combo_idproof.get(),str(txtidnumber.get()),str(combo_age.get()),combo_bloodtype.get(),str(txtunit.get())))
            
            conn.commit()
            x=int(txtunit.get())
            sql="select "+str(D[combo_bloodtype.get()])+" from total"
            my_cursor.execute(sql)
            z=my_cursor.fetchone()
            
            avl=int(z[0])
            nowavl=avl+x


            sql1="UPDATE total SET "+str(D[combo_bloodtype.get()])+"="+str(nowavl)
            my_cursor.execute(sql1)
            conn.commit()

            messagebox.showinfo("Success","Donation has been added",parent=root)

            fetch_datadonater()
            resetDonater()
            conn.close()
        except Exception as es:
            messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=root)

#--Update Donater Details--#

def updatedonater():
    #pincode 
    #mobile
    #age
    #unitml

    global root
    global txtcname
    global combo_Gender
    global txtpostcode
    global txtmobile
    global combo_nationality
    global combo_idproof
    global txtidnumber
    global combo_age
    global combo_bloodtype
    global txtunit
    global combo_anydi
    global Cust_Details_Table
    global row
    global D

    mobile=str(txtmobile.get())

    def isvalidmobile(s):
        Pattern=re.compile("(0|91)?[6-9][0-9]{9}")
        return Pattern.match(s)
    
    if txtcname.get()=="" or str(combo_age.get())=="" or combo_nationality.get()=="" or combo_idproof.get()=="" or combo_Gender.get()=="" or str(txtmobile.get())=="" or str(txtpostcode.get())=="" or combo_bloodtype.get()=="" or str(txtidnumber.get())=="" or combo_anydi.get()=="" or str(txtunit.get())=="":
        messagebox.showerror("Error","All fields are required",parent=root)

    elif not str(txtcname.get()).isalpha:
        messagebox.showerror("Error","Please Enter Data in Alphabets in the desired box",parent=root)

    elif str(combo_anydi.get())=="yes" or str(combo_anydi.get())=="Yes":
        messagebox.showerror("Sorry","You can`t Donate Blood\nYou are suffering from Disease",parent=root)
        
    elif (isvalidmobile(mobile)) is None:
        messagebox.showerror("Error","Incorrect Mobile Number"+"\nPlease Enter Indian Mobile Number",parent=root)
    
    else:
        try:
            conn=c.connect("blood.db")
            my_cursor=conn.cursor()
            po=str(txtpostcode.get())
            mo=(txtmobile.get())
            ag=str(combo_age.get())
            id=str(txtidnumber.get())
            unitml=txtunit.get()
            sql1="UPDATE donater SET Mobile='%s' WHERE Mobile='%s';"%(str(mo),row[3])
            sql2="UPDATE donater SET Pincode='%s' WHERE Mobile='%s';"%(po,str(mo))
            sql3="UPDATE donater SET Age='%s' WHERE Mobile='%s';"%(ag,str(mo))
            sql4="UPDATE donater SET Mobile='%s' WHERE Idnumber='%s';"%(str(mo),str(mo))

            my_cursor.execute(sql1)
            conn.commit()
            my_cursor.execute(sql2)
            conn.commit()
            my_cursor.execute(sql3)
            conn.commit()
            my_cursor.execute(sql4)
            conn.commit()



            conn.close()
            fetch_datadonater()
            messagebox.showinfo("Update","Donater details has been updated successfully",parent=root)
            resetDonater()
            
                

        except Exception as es:
            messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=root)
            fetch_datadonater()

    root.mainloop()


#--Get everything from table--#

def get_cuersorD(event=""):

    global root
    global txtcname
    global combo_Gender
    global txtpostcode
    global txtmobile
    global combo_nationality
    global combo_idproof
    global txtidnumber
    global combo_age
    global combo_bloodtype
    global txtunit
    global combo_anydi
    global Cust_Details_Table
    global row
    global D
    
    cusrsor_row=Cust_Details_Table.focus()
    content=Cust_Details_Table.item(cusrsor_row)

    row=content["values"]

    resetDonater()

    txtcname.insert(0,str(row[1]))
    combo_Gender.insert(0,str(row[2]))
    txtpostcode.insert(0,str(row[3]))
    txtmobile.insert(0,str(row[4]))
    combo_nationality.insert(0,str(row[5]))
    combo_idproof.insert(0,str(row[6]))
    txtidnumber.insert(0,str(row[7]))
    combo_age.insert(0,str(row[8]))
    combo_bloodtype.insert(0,str(row[9]))
    txtunit.insert(0,str(row[10]))
    combo_anydi.insert(0,str("No"))


def resetDonater():
    global root
    global txtcname
    global combo_Gender
    global txtpostcode
    global txtmobile
    global combo_nationality
    global combo_idproof
    global txtidnumber
    global combo_age
    global combo_bloodtype
    global txtunit
    global combo_anydi
    global Cust_Details_Table
    global row
    global D

    while True:
        txtcname.delete(0)
        if txtcname.get()=="":
            break
    while True:
        combo_Gender.delete(0)
        if combo_Gender.get()=="":
            break

    while True:
        combo_nationality.delete(0)
        if combo_nationality.get()=="":
            break


    while True:
        combo_idproof.delete(0)
        if combo_idproof.get()=="":
            break



    while True:
        combo_bloodtype.delete(0)
        if combo_bloodtype.get()=="":
            break

    while True:
        txtpostcode.delete(0)
        if len(txtpostcode.get())==0:
            break
        
    while True:
        txtmobile.delete(0)
        if len(txtmobile.get())==0:
            break
    
    while True:
        txtidnumber.delete(0)
        if len(txtidnumber.get())==0:
            break
    while True:
        combo_age.delete(0)
        if len(combo_age.get())==0:
            break

    while True:
        txtunit.delete(0)
        if len(txtunit.get())==0:
            break

    while True:
        combo_anydi.delete(0)
        if combo_anydi.get()=="":
            break

#--Delete Donater Details--#]
def deletedonater():
    mDelete=messagebox.askyesno("Blood Bank Management Management System","Do you want to delete this Details ?",parent=root)
    if mDelete>0:
        conn=c.connect("blood.db")
        my_cursor=conn.cursor()
        mo=(txtmobile.get())
        sql="delete from donater where Mobile='%s'"%(str(mo))
        my_cursor.execute(sql)
        fetch_datadonater()
        conn.commit()
        conn.close()
        fetch_datadonater()
        messagebox.showinfo("Deleted","Donater details has been deleted successfully",parent=root)
        
    else:
        if not mDelete:
            return



def searchdonater():
    global combo_Search
    global txtSearch
    global Cust_Details_Table

    conn=c.connect("blood.db")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from donater where "+str(combo_Search.get())+" LIKE '"+str(txtSearch.get())+"%'")
    rows=my_cursor.fetchall()

    if len(rows)!=0:
        Cust_Details_Table.delete(*Cust_Details_Table.get_children(),)
        for i in rows:
            Cust_Details_Table.insert("",END,values=i)
        conn.commit()
    else:
        messagebox.showerror("Error","No Donater details found",parent=root)
    conn.close()















#--Fetch Donater Details in Table--#

def fetch_datadonater():
    global root
    global unitml
    global txtcname
    global combo_Gender
    global txtpostcode
    global txtmobile
    global combo_nationality
    global combo_idproof
    global txtidnumber
    global combo_age
    global combo_bloodtype
    global txtunit
    global combo_anydi
    global Cust_Details_Table
    global row

    conn=c.connect("blood.db")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from donater")
    rows=my_cursor.fetchall()
    if len(rows)!=0:
        Cust_Details_Table.delete(*Cust_Details_Table.get_children())
        for i in rows:
            Cust_Details_Table.insert("",END,values=i) #inserting into table
        conn.commit()
    conn.close()

def fetch_datareceiver():
    global root
    global unitml
    global txtcname
    global combo_Gender
    global txtpostcode
    global txtmobile
    global combo_nationality
    global combo_idproof
    global txtidnumber
    global combo_age
    global combo_bloodtype
    global txtunit
    global combo_anydi
    global Cust_Details_Table
    global row

    conn=c.connect("blood.db")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from receiver")
    rows=my_cursor.fetchall()
    if len(rows)!=0:
        Cust_Details_Table.delete(*Cust_Details_Table.get_children())
        for i in rows:
            Cust_Details_Table.insert("",END,values=i) #inserting into table
        conn.commit()
    conn.close()
#get cursor receiver

def get_cuersorR(event=""):

    global root
    global txtcname
    global combo_Gender
    global txtpostcode
    global txtmobile
    global combo_nationality
    global combo_idproof
    global txtidnumber
    global combo_age
    global combo_bloodtype
    global txtunit
    global combo_em
    global Cust_Details_Table
    global row
    global D
    
    cusrsor_row=Cust_Details_Table.focus()
    content=Cust_Details_Table.item(cusrsor_row)

    row=content["values"]

    resetreceiver()

    txtcname.insert(0,str(row[1]))
    combo_Gender.insert(0,str(row[2]))
    txtpostcode.insert(0,str(row[3]))
    txtmobile.insert(0,str(row[4]))
    combo_nationality.insert(0,str(row[5]))
    combo_idproof.insert(0,str(row[6]))
    txtidnumber.insert(0,str(row[7]))
    combo_age.insert(0,str(row[8]))
    combo_bloodtype.insert(0,str(row[9]))
    txtunit.insert(0,str(row[10]))
    combo_em.insert(0,str("No"))

def resetreceiver():
    global root
    global unit 
    global Cust_Details_Table
    global txtcname
    global combo_Gender
    global txtpostcode
    global txtmobile
    global combo_nationality
    global combo_idproof
    global txtidnumber
    global combo_age
    global combo_bloodtype
    global txtunit
    global combo_em
    global row
    global combo_Search
    global txtSearch
    global D


    while True:
        txtcname.delete(0)
        if txtcname.get()=="":
            break
    while True:
        combo_Gender.delete(0)
        if combo_Gender.get()=="":
            break

    while True:
        combo_nationality.delete(0)
        if combo_nationality.get()=="":
            break


    while True:
        combo_idproof.delete(0)
        if combo_idproof.get()=="":
            break



    while True:
        combo_bloodtype.delete(0)
        if combo_bloodtype.get()=="":
            break

    while True:
        txtpostcode.delete(0)
        if len(txtpostcode.get())==0:
            break
        
    while True:
        txtmobile.delete(0)
        if len(txtmobile.get())==0:
            break
    
    while True:
        txtidnumber.delete(0)
        if len(txtidnumber.get())==0:
            break
    while True:
        combo_age.delete(0)
        if len(combo_age.get())==0:
            break

    while True:
        txtunit.delete(0)
        if len(txtunit.get())==0:
            break

    while True:
        combo_em.delete(0)
        if combo_em.get()=="":
            break


def receiverblood():
    global root
    global unit 
    global Cust_Details_Table
    global txtcname
    global combo_Gender
    global txtpostcode
    global txtmobile
    global combo_nationality
    global combo_idproof
    global txtidnumber
    global combo_age
    global combo_bloodtype
    global txtunit
    global combo_em
    global row
    global combo_Search
    global txtSearch
    global D

    root=Tk()

    root.title("Receiver Details")
    root.geometry("1300x680+0+142")

    #title
    lbl_title=Label(root,text="Receiver Details",font=("times new roman",18,"bold"),bg="azure2",fg="red",bd=4,relief=RIDGE)
    lbl_title.place(x=0,y=0,width=1300,height=50)

    labelframeleft=LabelFrame(root,bd=2,relief=RIDGE,text="Receiver Details",padx=2,font=("times new roman",18,"bold"))
    labelframeleft.place(x=5,y=50,width=450,height=510)

    #name

    cname=Label(labelframeleft,font=("arial",11,"bold"),text="Receiver Name:",padx=10,pady=8)
    cname.grid(row=0,column=0,sticky=W)

    txtcname=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
    txtcname.grid(row=0,column=1)

    #gender

    label_Gender=Label(labelframeleft,font=("arial",11,"bold"),text="Gender:",padx=10,pady=8)
    label_Gender.grid(row=1,column=0,sticky=W)
    
    combo_Gender=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27)
    combo_Gender["value"]=("Male","Female","Other")
    combo_Gender.current(0)   
    combo_Gender.grid(row=1,column=1)

    #post code

    lblpostcode=Label(labelframeleft,font=("arial",11,"bold"),text="Address:",padx=10,pady=8)
    lblpostcode.grid(row=2,column=0,sticky=W)
        
    txtpostcode=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
    txtpostcode.grid(row=2,column=1)

    # mobile number

    lblmobilenum=Label(labelframeleft,font=("arial",11,"bold"),text="Mobile Number:",padx=10,pady=8)
    lblmobilenum.grid(row=3,column=0,sticky=W)
        
    txtmobile=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
    txtmobile.grid(row=3,column=1)


    #nationality

    lblnationality=Label(labelframeleft,font=("arial",12,"bold"),text="Nationality:",padx=10,pady=8)
    lblnationality.grid(row=5,column=0,sticky=W)

    combo_nationality=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27)
    combo_nationality["value"]=("Indian","American","British","Other")
    combo_nationality.current(0)
    combo_nationality.grid(row=5,column=1)

    #id proof type combobox

    lblidproof=Label(labelframeleft,font=("arial",12,"bold"),text="ID Proof Type:",padx=10,pady=8)
    lblidproof.grid(row=6,column=0,sticky=W)

    combo_idproof=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27)
    combo_idproof["value"]=("Aadhaar Card","Driving Licence","Passport","Visa","Voter ID","Pan Card")
    combo_idproof.current(0)
    combo_idproof.grid(row=6,column=1)

    #id num

    lblidnum=Label(labelframeleft,font=("arial",11,"bold"),text="ID Number:",padx=10,pady=8)
    lblidnum.grid(row=7,column=0,sticky=W)
        
    txtidnumber=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
    txtidnumber.grid(row=7,column=1)

    label_age=Label(labelframeleft,font=("arial",11,"bold"),text="Age:",padx=10,pady=8)
    label_age.grid(row=8,column=0,sticky=W)
    
    combo_age=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27)
    combo_age["value"]=("18-20","21-30","31-40","41-50","51-60","61-70")
    combo_age.current(0)   
    combo_age.grid(row=8,column=1)

    label_bloodtype=Label(labelframeleft,font=("arial",11,"bold"),text="Blood Type:",padx=10,pady=8)
    label_bloodtype.grid(row=9,column=0,sticky=W)
    
    combo_bloodtype=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27)
    combo_bloodtype["value"]=("A+","B+","O+","AB+","A-","B-","O-","AB-")
    combo_bloodtype.current(0)   
    combo_bloodtype.grid(row=9,column=1)

    lblunit=Label(labelframeleft,font=("arial",11,"bold"),text="Unit Donated(in ml):",padx=10,pady=8)
    lblunit.grid(row=10,column=0,sticky=W)
    
    txtunit=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
    txtunit.grid(row=10,column=1)

    lblem=Label(labelframeleft,font=("arial",11,"bold"),text="Urgency:",padx=10,pady=8)
    lblem.grid(row=11,column=0,sticky=W)
    
    combo_em=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27)
    combo_em["value"]=("Normal","Urgent","Emergency")
    combo_em.current(0)   
    combo_em.grid(row=11,column=1)

    #btns of cust

    btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
    btn_frame.place(x=8,y=435,width=417,height=40)


    #add btn in custbox

    btnAdd=Button(btn_frame,text="Add",command=addreceiver,font=("arial",12,"bold"),bg="azure2",fg="red",activeforeground="red",activebackground="azure2",width=9,height=1)
    btnAdd.grid(row=0,column=0,padx=1,pady=2)

    #btn update

    btnUpdate=Button(btn_frame,text="Update",command=updatereceiver,font=("arial",12,"bold"),bg="azure2",fg="red",activeforeground="red",activebackground="azure2",width=9,height=1)
    btnUpdate.grid(row=0,column=1,padx=1,pady=2)

    #btn delete

    btnDelete=Button(btn_frame,text="Delete",command=deletereceiver,font=("arial",12,"bold"),bg="azure2",fg="red",activeforeground="red",activebackground="azure2",width=9,height=1)
    btnDelete.grid(row=0,column=2,padx=1,pady=2)

    #btn reset


    btnReset=Button(btn_frame,text="Reset",command=resetreceiver,font=("arial",12,"bold"),bg="azure2",fg="red",activeforeground="red",activebackground="azure2",width=9,height=1)
    btnReset.grid(row=0,column=3,padx=1,pady=2)

    #cust inside frame

    Table_Frame=LabelFrame(root,bd=2,relief=RIDGE,text="View Details And Search System",padx=2,font=("times new roman",13,"bold"))
    Table_Frame.place(x=440,y=50,width=860,height=510)

    #search by (red colour)
    lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By",bg="red",fg="white")
    lblSearchBy.grid(row=0,column=0,sticky=W,padx=3)

    #search by

    combo_Search=ttk.Combobox(Table_Frame,font=("arial",12,"bold"),width=24,state="readonly")
    combo_Search["value"]=("Mobile","Idnumber")
    combo_Search.current(0)
    combo_Search.grid(row=0,column=1,padx=2)

    #search field

    txtSearch=ttk.Entry(Table_Frame,width=24,font=("times new roman",13,"bold"))
    txtSearch.grid(row=0,column=2,padx=2)

    btnSearch=Button(Table_Frame,text="Search",command=searchreceiver,font=("arial",12,"bold"),bg="azure2",fg="red",activeforeground="red",activebackground="azure2",width=10)
    btnSearch.grid(row=0,column=3,padx=1,pady=2)

    btnShowAll=Button(Table_Frame,text="Show All",command=fetch_datareceiver,font=("arial",12,"bold"),bg="azure2",fg="red",activeforeground="red",activebackground="azure2",width=10)
    btnShowAll.grid(row=0,column=4,padx=1,pady=2)

    #show data table

    Details_Table=Frame(Table_Frame,bd=2,relief=RIDGE)
    Details_Table.place(x=0,y=50,width=860,height=430)

    #scroll bar 

    scroll_x=ttk.Scrollbar(Details_Table,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(Details_Table,orient=VERTICAL)

    global Cust_Details_Table

    Cust_Details_Table=ttk.Treeview(Details_Table,column=("date","Name","Gender","Pincode","Mobile","Nationality","Idproof","Idnumber","Age","Bloodtype","Unitml"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x.config(command=Cust_Details_Table.xview)

    scroll_y.config(command=Cust_Details_Table.yview)

    #scroll bar column show like name,father,......

    Cust_Details_Table.heading("date",text="Date")
    Cust_Details_Table.heading("Name",text="Receiver Name")
    Cust_Details_Table.heading("Gender",text="Gender")
    Cust_Details_Table.heading("Pincode",text="Address")
    Cust_Details_Table.heading("Mobile",text="Mobile")
    Cust_Details_Table.heading("Nationality",text="Nationality")
    Cust_Details_Table.heading("Idproof",text="ID Proof")
    Cust_Details_Table.heading("Idnumber",text="ID Number")
    Cust_Details_Table.heading("Age",text="Age")
    Cust_Details_Table.heading("Bloodtype",text="Blood Type")
    Cust_Details_Table.heading("Unitml",text="Unit(in ml)")
    
    

    #show karenge avi headings

    Cust_Details_Table["show"]="headings"

    #width shape karre columns ka

    Cust_Details_Table.column("date",width=80,anchor=CENTER)
    Cust_Details_Table.column("Name",width=90,anchor=CENTER)
    Cust_Details_Table.column("Gender",width=70,anchor=CENTER)
    Cust_Details_Table.column("Pincode",width=80,anchor=CENTER)
    Cust_Details_Table.column("Mobile",width=80,anchor=CENTER)
    Cust_Details_Table.column("Nationality",width=80,anchor=CENTER)
    Cust_Details_Table.column("Idproof",width=80,anchor=CENTER)
    Cust_Details_Table.column("Idnumber",width=80,anchor=CENTER)
    Cust_Details_Table.column("Age",width=80,anchor=CENTER)
    Cust_Details_Table.column("Bloodtype",width=80,anchor=CENTER)
    Cust_Details_Table.column("Unitml",width=80,anchor=CENTER)
    

    #pack karre phir expand then save karke apne adjust lelega

    Cust_Details_Table.pack(fill=BOTH,expand=1)

    Cust_Details_Table.bind("<ButtonRelease-1>",get_cuersorR)
    fetch_datareceiver()


    root.mainloop()

def addreceiver():
    global root
    global txtcname
    global combo_Gender
    global txtpostcode
    global txtmobile
    global combo_nationality
    global combo_idproof
    global txtidnumber
    global combo_age
    global combo_bloodtype
    global txtunit
    global combo_em
    global Cust_Details_Table
    global row
    global D
    global avl

    mobile=str(txtmobile.get())
    pin=str(txtpostcode.get())

    #Mobile number checking code

    def isvalidmobile(s):
        Pattern=re.compile("(0|91)?[6-9][0-9]{9}")
        return Pattern.match(s)

    conn=c.connect("blood.db")
    my_cursor=conn.cursor()
    x=int(txtunit.get())
    sql="select "+str(D[combo_bloodtype.get()])+" from total"
    my_cursor.execute(sql)
    z=my_cursor.fetchone()
    avl=int(z[0])
    nowavl=avl-x

    if txtcname.get()=="" or str(combo_age.get())=="" or combo_nationality.get()=="" or combo_idproof.get()=="" or combo_Gender.get()=="" or str(txtmobile.get())=="" or str(txtpostcode.get())=="" or combo_bloodtype.get()=="" or str(txtidnumber.get())=="" or combo_em.get()=="" or str(txtunit.get())=="":
        messagebox.showerror("Error","All fields are required",parent=root)

    elif not str(txtcname.get()).isalpha():
        messagebox.showerror("Error","Please Enter Data in Alphabets in the Donater Name box",parent=root)
    elif not str(txtunit.get()).isdigit():
        messagebox.showerror("Error","Please Enter Data in Digits in the Unit box",parent=root)
    elif (isvalidmobile(mobile)) is None:
        messagebox.showerror("Error","Incorrect Mobile Number"+"\nPlease Enter Indian Mobile Number",parent=root)
    elif nowavl<=0:
        messagebox.showerror("Error","Insufficient Blood",parent=root)
    
    else:
        try:
            conn=c.connect("blood.db")
            my_cursor=conn.cursor()
            
            
            my_cursor.execute("insert into receiver (date,Name,Gender,Pincode,Mobile,Nationality,Idproof,Idnumber,Age,Bloodtype,Unitml)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(str(format_date),txtcname.get(),combo_Gender.get(),str(txtpostcode.get()),str(txtmobile.get()),combo_nationality.get(),combo_idproof.get(),str(txtidnumber.get()),str(combo_age.get()),combo_bloodtype.get(),str(txtunit.get())))
            
            conn.commit()


            sql1="UPDATE total SET "+str(D[combo_bloodtype.get()])+"="+str(nowavl)
            my_cursor.execute(sql1)
            conn.commit()

            messagebox.showinfo("Success","Receiver Details has been added",parent=root)

            fetch_datareceiver()
            resetreceiver()
            conn.close()
        except Exception as es:
            messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=root)

def updatereceiver():
    #pincode 
    #mobile
    #age
    #unitml

    global root
    global txtcname
    global combo_Gender
    global txtpostcode
    global txtmobile
    global combo_nationality
    global combo_idproof
    global txtidnumber
    global combo_age
    global combo_bloodtype
    global txtunit
    global combo_em
    global Cust_Details_Table
    global row
    global D

    mobile=str(txtmobile.get())

    def isvalidmobile(s):
        Pattern=re.compile("(0|91)?[6-9][0-9]{9}")
        return Pattern.match(s)
    
    if txtcname.get()=="" or str(combo_age.get())=="" or combo_nationality.get()=="" or combo_idproof.get()=="" or combo_Gender.get()=="" or str(txtmobile.get())=="" or str(txtpostcode.get())=="" or combo_bloodtype.get()=="" or str(txtidnumber.get())=="" or combo_em.get()=="" or str(txtunit.get())=="":
        messagebox.showerror("Error","All fields are required",parent=root)

    elif not str(txtcname.get()).isalpha:
        messagebox.showerror("Error","Please Enter Data in Alphabets in the desired box",parent=root)
        
    elif (isvalidmobile(mobile)) is None:
        messagebox.showerror("Error","Incorrect Mobile Number"+"\nPlease Enter Indian Mobile Number",parent=root)
    
    else:
        try:
            conn=c.connect("blood.db")
            my_cursor=conn.cursor()
            po=str(txtpostcode.get())
            mo=(txtmobile.get())
            ag=str(combo_age.get())
            id=str(txtidnumber.get())
            unitml=txtunit.get()
            sql1="UPDATE receiver SET Mobile='%s' WHERE Mobile='%s';"%(str(mo),row[3])
            sql2="UPDATE receiver SET Pincode='%s' WHERE Mobile='%s';"%(po,str(mo))
            sql3="UPDATE receiver SET Age='%s' WHERE Mobile='%s';"%(ag,str(mo))
            sql4="UPDATE receiver SET Mobile='%s' WHERE Idnumber='%s';"%(str(mo),str(mo))

            my_cursor.execute(sql1)
            conn.commit()
            my_cursor.execute(sql2)
            conn.commit()
            my_cursor.execute(sql3)
            conn.commit()
            my_cursor.execute(sql4)
            conn.commit()
            


            conn.close()
            fetch_datareceiver()
            messagebox.showinfo("Update","Receiver details has been updated successfully",parent=root)
            resetreceiver()
            
                

        except Exception as es:
            messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=root)
            fetch_datareceiver()

    root.mainloop()

def deletereceiver():
    mDelete=messagebox.askyesno("Blood Bank Management Management System","Do you want to delete this Details ?",parent=root)
    if mDelete>0:
        conn=c.connect("blood.db")
        my_cursor=conn.cursor()
        mo=(txtmobile.get())
        sql="delete from receiver where Mobile='%s'"%(str(mo))
        my_cursor.execute(sql)
        fetch_datadonater()
        conn.commit()
        conn.close()
        fetch_datadonater()
        messagebox.showinfo("Deleted","Receiver details has been deleted successfully",parent=root)
        resetreceiver()
        
    else:
        if not mDelete:
            return



def searchreceiver():
    global combo_Search
    global txtSearch
    global Cust_Details_Table

    conn=c.connect("blood.db")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from receiver where "+str(combo_Search.get())+" LIKE '"+str(txtSearch.get())+"%'")
    rows=my_cursor.fetchall()

    if len(rows)!=0:
        Cust_Details_Table.delete(*Cust_Details_Table.get_children(),)
        for i in rows:
            Cust_Details_Table.insert("",END,values=i)
        conn.commit()
    else:
        messagebox.showerror("Error","No Receiver details found",parent=root)
    conn.close()

def printdata():
    conn=c.connect("blood.db")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from total")
    rows=my_cursor.fetchall()
    filename="filerecord.txt"
    f=open(filename,"w")
    f.write("-"*350+"\n")
    f.write("-"*350+"\n")
    f.write("\t\t\t\t\t\tTOTAL BLOOD DATABASE RECORD(in ml)"+"\n")
    f.write("-"*350+"\n")
    f.write("-"*350+"\n\n")
    f.write("-"*350+"\n")
    f.write("A+\t\tB+\t\tO+\t\tAB+\t\tA-\t\tB-\t\tO-\t\tAB-")
    f.write("\n"+"-"*350)
    if len(rows)!=0:
        for i in rows:
            f.write("\n"+str(i[0])+"\t\t"+str(i[1])+"\t\t"+str(i[2])+"\t\t"+str(i[3])+"\t\t"+str(i[4])+"\t\t"+str(i[5])+"\t\t"+str(i[6])+"\t\t"+str(i[7]))
            f.write("\n"+"-"*350+"\n")
    f.flush()
    f.close()
    program="notepad.exe"
    subprocess.Popen([program,filename])
    


#--Total Blood--#

def totalblood():
    global root
    global D
    global totalbloodavl

    root=Tk()

    root.title("Total Blood Available")
    root.geometry("1300x680+0+142")

    #title
    lbl_title=Label(root,text="TOTAL BLOOD",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
    lbl_title.place(x=0,y=0,width=1300,height=50)

    #cust inside frame


    Table_Frame=LabelFrame(root,bd=2,relief=RIDGE,text="View Current Blood Available",padx=2,font=("times new roman",13,"bold"))
    Table_Frame.place(x=10,y=53,width=1400,height=506)



    Details_Table=Frame(Table_Frame,bd=2,relief=RIDGE)
    Details_Table.place(x=0,y=10,width=1280,height=400)

    #scroll bar 

    scroll_x=ttk.Scrollbar(Details_Table,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(Details_Table,orient=VERTICAL)

    global totalbloodavl

    totalbloodavl=ttk.Treeview(Details_Table,column=("Aplus","Bplus","Oplus","ABplus","Aneg","Bneg","Oneg","ABneg"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x.config(command=totalbloodavl.xview)

    scroll_y.config(command=totalbloodavl.yview)

   

    totalbloodavl.heading("Aplus",text="A+")
    totalbloodavl.heading("Bplus",text="B+")
    totalbloodavl.heading("Oplus",text="O+")
    totalbloodavl.heading("ABplus",text="AB+")
    totalbloodavl.heading("Aneg",text="A-")
    totalbloodavl.heading("Bneg",text="B-")
    totalbloodavl.heading("Oneg",text="O-")
    totalbloodavl.heading("ABneg",text="AB-")
    


    #show karenge avi headings

    totalbloodavl["show"]="headings"

    
    #width shape karre columns ka

    totalbloodavl.column("Aplus",width=70,anchor=CENTER)
    totalbloodavl.column("Bplus",width=60,anchor=CENTER)
    totalbloodavl.column("Oplus",width=70,anchor=CENTER)
    totalbloodavl.column("ABplus",width=70,anchor=CENTER)
    totalbloodavl.column("Aneg",width=80,anchor=CENTER)
    totalbloodavl.column("Bneg",width=70,anchor=CENTER)
    totalbloodavl.column("Oneg",width=80,anchor=CENTER)
    totalbloodavl.column("ABneg",width=70,anchor=CENTER)
    

    totalbloodavl.pack(fill=BOTH,expand=2)

    details_btn=Button(Table_Frame,text="Total Available Bloods",command=printdata,width=20,height=3,font=("times new roman",16,"bold"),bg="black",fg="gold",activeforeground="gold",activebackground="black",bd=1,cursor="hand2")
    details_btn.place(x=0,y=425,width=1380,height=70)


    fetch_datadtotal()
    root.mainloop()

#fetch blood data

def fetch_datadtotal():
    global root
    global unitml
    global txtcname
    global combo_Gender
    global txtpostcode
    global txtmobile
    global combo_nationality
    global combo_idproof
    global txtidnumber
    global combo_age
    global combo_bloodtype
    global txtunit
    global combo_anydi
    global totalbloodavl
    global row

    conn=c.connect("blood.db")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from total")
    rows=my_cursor.fetchall()
    if len(rows)!=0:
        totalbloodavl.delete(*totalbloodavl.get_children())
        for i in rows:
            totalbloodavl.insert("",END,values=i) #inserting into table
        conn.commit()
    conn.close()










#--Add Tables--#

def addtables():
    conn=c.connect("blood.db")
    my_cursor=conn.cursor()
    sql="CREATE TABLE if not exists donater (\
        date varchar(20),\
        Name varchar(30),\
        Gender char(15),\
        Pincode varchar(20),\
        Mobile varchar(10),\
        Nationality varchar(50),\
        Idproof varchar(20),\
        Idnumber varchar(20) UNIQUE,\
        Age varchar(20),\
        Bloodtype varchar(20),\
        Unitml varchar(20),\
        PRIMARY KEY (Mobile));"
    my_cursor.execute(sql)

    sql="CREATE TABLE if not exists receiver (\
        date varchar(20),\
        Name varchar(30),\
        Gender char(15),\
        Pincode varchar(20),\
        Mobile varchar(10),\
        Nationality varchar(50),\
        Idproof varchar(20),\
        Idnumber varchar(20) UNIQUE,\
        Age varchar(20),\
        Bloodtype varchar(20),\
        Unitml varchar(20),\
        PRIMARY KEY (Mobile));"
    my_cursor.execute(sql)

    sql="CREATE TABLE if not exists total (\
        Aplus INT,\
        Bplus INT,\
        Oplus INT,\
        ABplus INT,\
        Aneg INT,\
        Bneg INT,\
        Oneg INT,\
        ABneg INT);"
    my_cursor.execute(sql)

    sql="CREATE TABLE if not exists login (\
        fullname varchar(30),\
        username varchar(30) UNIQUE,\
        contact varchar(30),\
        recode varchar(30),\
        pass varchar(30),\
        conpass varchar(30),\
        PRIMARY KEY (recode));"
    my_cursor.execute(sql)

    









#--MAIN--#
def Bloodbank():
    root=Tk() 
    root.title("Blood Bank Management System")
    root.geometry("1550x890+0+0")

    global unit 

    #title "HOTEL MANAGEMENT SYSTEM"

    lbl_title=Label(root,text="BLOOD BANK MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="azure2",fg="red",bd=4,relief=RIDGE)
    lbl_title.place(x=0,y=0,width=1532,height=100)

    def time():
        string=strftime('%H:%M:%S %p')
        lbl.config(text=string)
        lbl.after(1000,time)
    lbl=Label(lbl_title,font=("Times New Roman",16,"bold"),bg="azure2",fg="red")
    lbl.place(x=15,y=30,width=120,height=37)
    time()


    #MAIN FRAME

    main_frame=Frame(root,bd=4,relief=RIDGE)
    main_frame.place(x=0,y=105,width=1550,height=730)
    

    #image main center image
    img4=Image.open("mainbgf.jpg")
    img4=img4.resize((1310,680),Image.ANTIALIAS)
    photoimg4=ImageTk.PhotoImage(img4)

    lblimg=Label(main_frame,image=photoimg4,bd=4,relief=RIDGE)
    lblimg.place(x=0,y=0,width=1300,height=680)

     #MENU

    lbl_menu=Label(main_frame,text="MENU",font=("times new roman",30,"bold"),bg="azure2",fg="red",bd=4,relief=RIDGE)
    lbl_menu.place(x=1301,y=5 ,width=230,height=80)

    #BTN FRAME 

    btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
    btn_frame.place(x=1301,y=80,width=231,height=350)

    #PLAN MY JOURNEY btn

    don_btn=Button(btn_frame,text="Donater Details",command=donaterdetails,width=20,height=3,font=("times new roman",16,"bold"),bg="azure2",fg="red",activeforeground="red",activebackground="azure2",bd=1,cursor="hand2")
    don_btn.grid(row=0,column=0,pady=1)

    #BOOKINGS btn
    
    rec_btn=Button(btn_frame,text="Receiver Details",command=receiverblood,width=20,height=3,font=("times new roman",16,"bold"),bg="azure2",fg="red",activeforeground="red",activebackground="azure2",bd=1,cursor="hand2")
    rec_btn.grid(row=1,column=0,pady=1)


        #CANCEL TICKET btn

    details_btn=Button(btn_frame,text="Available Bloods",command=totalblood,width=20,height=3,font=("times new roman",16,"bold"),bg="azure2",fg="red",activeforeground="red",activebackground="azure2",bd=1,cursor="hand2")
    details_btn.grid(row=2,column=0,pady=1)

    def logoutfunc():
        x=messagebox.askyesno("Logout","Do you want to logout ?",parent=root)
        if x>0:
            root.destroy()
            log() 


    logout_btn=Button(btn_frame,text="Logout",command=logoutfunc,width=20,height=3,font=("times new roman",16,"bold"),bg="azure2",fg="red",activeforeground="red",activebackground="azure2",bd=1,cursor="hand2")
    logout_btn.grid(row=3,column=0,pady=1)


    img6=Image.open("donateblood.jpg")
    img6=img6.resize((230,250),Image.ANTIALIAS)
    photoimg6=ImageTk.PhotoImage(img6)

    lblimg=Label(main_frame,image=photoimg6,bd=4,relief=RIDGE)
    lblimg.place(x=1301,y=420,width=230,height=259)

    root.mainloop()
    addtables()

def log():
    global root
    global fname_entry
    global l_entry
    global txt_contact
    global txt_recode
    global txt_pass
    global txt_conpass
    root=Tk()
    def Register():
        global fname_entry
        global l_entry
        global txt_contact
        global txt_recode
        global txt_pass
        global txt_conpass
        global checkbtn

        root.title("Register")
        root.geometry("1600x900+0+0")

        #background image

        bg1=ImageTk.PhotoImage(file="regis1.jpg")
            
        bg1_lbl=Label(root,image=bg1,relief=RIDGE)
        bg1_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #bg 2
        bgimage=Image.open("regis2.jpg")
        bgimage=bgimage.resize((460,550),Image.ANTIALIAS)
        bg2=ImageTk.PhotoImage(bgimage)

        
        bg2_lbl=Label(root,image=bg2,bd=4,relief=RIDGE)
        bg2_lbl.place(x=130,y=130,width=460,height=550)

        #side frame

        frame=Frame(root,bg="white")
        frame.place(x=590,y=130,width=800,height=550)

        #frame inside work

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen")
        register_lbl.place(x=20,y=20)

        #--login button--#

        loginbtnreg=Button(frame,command=Login_Window,text="Login Now",font=("Arial",13,"bold"),bd=3,relief=RIDGE,fg="black",bg="aqua",activeforeground="black",activebackground="aqua")
        loginbtnreg.place(x=630,y=20,width=120,height=35)

        #labels and entry fields

        framename=Label(frame,text="First Name",font=("times new roman",20,"bold"),bg="white")
        framename.place(x=50,y=100)

        #entry field for first name

        fname_entry=ttk.Entry(frame,font=("times new roman",16,"bold"))
        fname_entry.place(x=50,y=135,width=230)

        #last name

        l_name=Label(frame,text="User Name",font=("times new roman",20,"bold"),bg="white")
        l_name.place(x=370,y=100)

        l_entry=ttk.Entry(frame,font=("times new roman",16,"bold"))
        l_entry.place(x=370,y=136,width=230)

        #contact

        contact_name=Label(frame,text="Contact No",font=("times new roman",20,"bold"),bg="white")
        contact_name.place(x=50,y=170)

        txt_contact=ttk.Entry(frame,font=("times new roman",16,"bold"))
        txt_contact.place(x=50,y=210,width=230)

        #recovery  code

        recode=Label(frame,text="Recovery Code",font=("times new roman",20,"bold"),bg="white")
        recode.place(x=370,y=170)

        txt_recode=ttk.Entry(frame,font=("times new roman",16,"bold"))
        txt_recode.place(x=370,y=207,width=230)
        
        #password

        password=Label(frame,text="Password",font=("times new roman",20,"bold"),bg="white")
        password.place(x=50,y=245)

        txt_pass=ttk.Entry(frame,font=("times new roman",16,"bold"))
        txt_pass.place(x=50,y=282,width=230)

        #confirm pass

        conpass=Label(frame,text="Confirm Password",font=("times new roman",20,"bold"),bg="white")
        conpass.place(x=370,y=240)

        txt_conpass=ttk.Entry(frame,font=("times new roman",16,"bold"))
        txt_conpass.place(x=370,y=277,width=230)


        #check btn terms and conditions
        global var_check
        var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=var_check,text="I Agree the Terms & Conditions",font=("times new roman",15,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=330)
        def registerclick():
            global var_check
            global fname_entry
            global l_entry
            global txt_contact
            global txt_recode
            global txt_pass
            global txt_conpass



            if str(fname_entry.get())=="" or str(l_entry.get())=="" or str(txt_contact.get())=="" or str(txt_recode.get())=="" or str(txt_pass.get())=="" or str(txt_conpass.get())=="":
                messagebox.showerror("Error","All fields are required",parent=root)

            elif not fname_entry.get().isalpha() or not l_entry.get().isalpha():
                messagebox.showerror("Error","Please Enter Name in alphabets",parent=root)
            elif not str(txt_contact.get()).isdigit() or not str(txt_recode.get()).isdigit():
                messagebox.showerror("Error","Please Enter Digits in the desired box",parent=root)
            elif str(txt_pass.get())!=str(txt_conpass.get()):
                messagebox.showerror("Error","Password & Confirm Password must be same",parent=root)
            elif var_check.get()==0:
                messagebox.showerror("Error","Please agree our terms and conditions",parent=root)
            else:
                messagebox.showinfo("Done","Welcome to our Blood Bank Management System",parent=root)
                conn=c.connect("blood.db")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from login where username='%s'"%(str(l_entry.get())))
                row=my_cursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist with same details\nPlease try again",parent=root)
                else:
                    my_cursor.execute("insert into login (fullname,username,contact,recode,pass,conpass)values('%s','%s','%s','%s','%s','%s')"%(str(fname_entry.get()),str(l_entry.get()),str(txt_contact.get()),str(txt_recode.get()),str(txt_pass.get()),str(txt_conpass.get())))
                    conn.commit()
                    messagebox.showinfo("Registered","Data registered successfully",parent=root)
                    conn.close()
        #register now

        img=Image.open("regis3.jpeg")
        img=img.resize((170,50),Image.ANTIALIAS)
        photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=photoimage,borderwidth=0,command=registerclick,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=203,y=390,width=300)

        

        root.mainloop()

    def Login_Window():
        global root
        global fname_entry
        global l_entry
        global txt_contact
        global txt_recode
        global txt_pass
        global txt_conpass
        global txtuser
        global txtpass
        global txt_newpass
        
        root.title("Blood Bank Management Login Pannel")
        root.geometry("1550x800+0+0")

        bgimage=Image.open(r"login1.jpeg")
        bgimage=bgimage.resize((1550,800),Image.ANTIALIAS)
        bg=ImageTk.PhotoImage(bgimage)

        lbl_bg=Label(root,image=bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(root,bg="black")
        frame.place(x=603,y=175,width=340,height=450) #x and y pos value and width and height size of box

        img1=Image.open(r"getstarted.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=180,width=100,height=100)

            #get started label

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=107,y=100)

            #user name label

        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=60,y=155)
            
        txtuser=ttk.Entry(frame,font=("times new roman",13,"bold"))       
        txtuser.place(x=35,y=180,width=270)

            #password label

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=60,y=225)

        txtpass=ttk.Entry(frame,font=("times new roman",13,"bold"),show="*")       
        txtpass.place(x=35,y=250,width=270)

            #Icon Images of username 

        img2=Image.open(r"user.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=640,y=330,width=25,height=25)

            #Icon Images of password

        img3=Image.open(r"passicon.png")
        img3=img3.resize((55,25),Image.ANTIALIAS)
        photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=639,y=400,width=25,height=25)
            
            #login btn in login pannel               here command ka kaam click karne par def login ko call karna hai
        def login():
            global txtuser
            global txtpass
            global txt_recode

            if str(txtuser.get())=="" or str(txtpass.get())=="":
                messagebox.showerror("Error","All fields required",parent=root)
            else:
                conn=c.connect("blood.db")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from login where username='%s' and pass='%s'"%(str(txtuser.get()),str(txtpass.get())))
                row=my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Username & Password",parent=root)
                else:
                    root.destroy()
                    Bloodbank()


        loginbtn=Button(frame,command=login,text="Login",font=("times new roman",13,"bold"),bd=3,relief=RIDGE,fg="black",bg="aqua",activeforeground="black",activebackground="aqua")
        loginbtn.place(x=105,y=300,width=120,height=35)

            # registerbutton for new users

        registerbtn=Button(frame,text="New User Register",command=Register,font=("times new roman",11,"bold"),bd=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=5,y=353,width=160)

            #forgot passbtn
        def forgotpass():
            global txtuser
            global txtpass
            global txt_recode
            global txt_newpass

            if str(txtuser.get())=="":
                messagebox.showerror("Error","Please Enter User Name to reset Password",parent=root)
            else:
                conn=c.connect("blood.db")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from login where username='%s'"%(str(txtuser.get())))
                row=my_cursor.fetchone()

                if row==None:
                    messagebox.showerror("Error","Please enter valid username",parent=root)
                else:
                    conn.close()
                    root2=Toplevel()
                    root2.title("Forgot Password")
                    root2.geometry("360x480+590+170")

                    l=Label(root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="blue",bg="cyan")
                    l.place(x=0,y=10,relwidth=1)

                    #recovery  code

                    recode=Label(root2,text="Recovery Code",font=("times new roman",20,"bold"),bg="cyan")
                    recode.place(x=88,y=80)

                    txt_recode=ttk.Entry(root2,font=("times new roman",16,"bold"))
                    txt_recode.place(x=50,y=130,width=250)
                    
                    #password

                    newpassword=Label(root2,text="New Password",font=("times new roman",20,"bold"),bg="cyan")
                    newpassword.place(x=88,y=180)

                    txt_newpass=ttk.Entry(root2,font=("times new roman",16,"bold"))
                    txt_newpass.place(x=50,y=220,width=250)
                    
                    def resetpass():
                        global txtuser
                        global txt_newpass
                        global txt_recode

                        

                        if str(txt_recode.get())=="":
                            messagebox.showerror("Error","Please enter Recovery Code",parent=root2)
                        elif not str(txt_recode.get()).isdigit():
                            messagebox.showerror("Error","Please enter Recovery Code in Digits",parent=root2)
                        else:
                            conn=c.connect("blood.db")
                            my_cursor=conn.cursor()
                            my_cursor.execute("select * from login where username='%s' and recode='%s'"%(str(txtuser.get()),str(txt_recode.get())))
                            row=my_cursor.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Please enter Correct Recovery Code",parent=root2)
                            else:
                                my_cursor.execute("update login set pass='%s' where username='%s' and recode='%s'"%(str(txt_newpass.get()),str(txtuser.get()),str(txt_recode.get())))
                                conn.commit()
                                conn.close()
                                messagebox.showinfo("Info","Your password has been reset\nYou can login with your new password",parent=root2) 
                                root2.destroy()


                        



                    #btn for reset

                    btn=Button(root2,text="Reset Password",command=resetpass,font=("times new roman",15,"bold"),fg="white",bg="blue")
                    btn.place(x=100,y=290)

        forgotpassbtn=Button(frame,text="Forgot Password",command=forgotpass,font=("times new roman",11,"bold"),bd=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotpassbtn.place(x=7,y=382,width=140)

        #click login func

        

        root.mainloop()
    Login_Window()


addtables()
log()






