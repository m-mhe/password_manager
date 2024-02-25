#importing nessesyry libarry
from cProfile import label
from tkinter import *
from PIL import ImageTk, Image
import sqlite3
from setuptools import Command



#Defining root
root=Tk()
root.title('PASSWORD MANEGER')
root.geometry('700x500')
root.resizable(width=False, height=False)
root.configure(background='green')


def windo():
    global access_pass
    access_pass = str(ac_e.get())
    ac_e.delete(0, END)
    if access_pass == "22467":
        def delete():
            connect = sqlite3.connect('pass.db')
            c = connect.cursor()
            c.execute("DELETE from password WHERE oid= "+delete_e.get())
            connect.commit()
            connect.close()
            delete_e.delete(0, END)
        global img
        img=ImageTk.PhotoImage(Image.open('/home/mmhe/CODEX/Python/password_m/icons8-secure-100.png'))
        window=Toplevel()
        window.geometry('500x800')
        window.configure(background='green')
        new_window_lbl=Label(window,bg='green', image=img).grid(row=0,column=0, ipadx=192,ipady=10,columnspan=2)
        new_window_button=Button(window, text='<< BACK', bg='green',font=('bold',10),fg='white', command=window.destroy).grid(row=3,padx=(120,0),column=0)
        connect = sqlite3.connect('pass.db')
        c = connect.cursor()
        c.execute("SELECT *, oid FROM password")
        all_record=c.fetchall()
        global print_record
        print_record=""
        for record in all_record:
            print_record += str(record[3])+"   "+str(record[0]) + "   " + str(record[1])+ "   "+ str(record[2]) + "\n"
        show_lable=Label(window, text=print_record,font=('bold', 8), bg='white', fg='green',pady=10, padx=10)
        show_lable.grid(row=1, column=0, columnspan=2,pady=10, ipadx=60)
        delete_e=Entry(window, width=30, fg='green', bg='white', font=("bold", 14), justify=CENTER)
        delete_e.grid(row=2,column=0, padx=(40, 15), pady=(0,10) )
        d_b=Button(window,text='DELETE ID', bg='green',font=('bold',10),fg='white', command=delete).grid(row=2,column=1, padx=(0, 35), pady=(0,10) )
        connect.commit()
        connect.close()

    elif access_pass == "creat a database":
        connect = sqlite3.connect('pass.db')
        c = connect.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS password (
                p_n text,
                u_n text,
                pass text
                )""")

        connect.commit()
        connect.close()

    else:
        ac_e.insert(0, "--Password is in INCORRECT!!--")

            
        

    





def submit():
    
    connect = sqlite3.connect('pass.db')
    c = connect.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS password (
            p_n text,
            u_n text,
            pass text
            )""")
    
    c.execute("INSERT INTO password VALUES (:p_n, :u_n, :pass)",
             {
                 'p_n':p_e.get(),
                 'u_n':u_e.get(),
                 'pass':ps_e.get() 
             }
             )
    connect.commit()
    connect.close()
    p_e.delete(0, END)
    u_e.delete(0, END)
    ps_e.delete(0, END)





pass_img=ImageTk.PhotoImage(Image.open("/home/mmhe/CODEX/Python/password_m/password_manager.png"))
img_l = Label(root, bg="green", image=pass_img).grid(row=0, ipadx=272,ipady=30, column=0, columnspan=2)
p_b=Button(root, text=" PLATFORM ",fg='white',font=("bold",10), bg="green").grid(row=1,column=0, padx=(134, 4), pady=(0,10))
p_e=Entry(width=30, fg='green', bg='white', font=("bold", 14), justify=CENTER)
p_e.grid(row=1,column=1, padx=(0, 110), pady=(0,10))
u_b=Button(root, text="USER NAME",fg='white',font=("bold",10), bg="green").grid(row=2, column=0, padx=(134, 4), pady=(0,10))
u_e=Entry(width=30, fg='green', bg='white', font=("bold", 14), justify=CENTER)
u_e.grid(row=2,column=1, padx=(0, 110), pady=(0,10))
ps_b=Button(root, text="PASSWORD",fg='white',font=("bold",10), bg="green").grid(row=3,column=0, padx=(134, 4), pady=(0,10))
ps_e=Entry(width=30, fg='green', bg='white', font=("bold", 14), justify=CENTER)
ps_e.grid(row=3,column=1, padx=(0, 110), pady=(0,10))
a_b=Button(root, text="ADD",fg='white',font=("bold",10), bg="green", command=submit).grid(row=4, column=0, columnspan=2,padx=(25,0),pady=(0,10),ipadx=196)
ac_b=Button(root, text="PASSWORD",fg='white',font=("bold",10), bg="green").grid(row=5,column=0, padx=(134, 4), pady=(0,10))
ac_e=Entry(width=30, fg='green', bg='white', font=("bold", 14), justify=CENTER)
ac_e.grid(row=5,column=1, padx=(0, 110), pady=(0,10))
s_b=Button(root, text="SHOW SAVED PASSWORD",fg='white',font=("bold",10), bg="green", command=windo).grid(row=6, column=0, columnspan=2,padx=(25,0),pady=(0,10),ipadx=132)




#runing mainloop
root.mainloop()