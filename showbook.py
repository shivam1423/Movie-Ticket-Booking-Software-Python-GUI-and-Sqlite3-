from Tkinter import *
from tkMessageBox import *
import sqlite3
root=Tk()
root.configure(bg='#424242')
icon1=PhotoImage(file="img1.gif")
root.title('showbook')
root.geometry('1400x1400')
con=sqlite3.Connection('mydbshow')
cur=con.cursor()
cur.execute("create table if not exists showbook(id varchar(10) Primary Key,password varchar(10) ,mob_no number(12)  ,name varchar(20))")
Label(root,text='SHOWBOOK',font="Arial 30 bold italic",bd=5,bg="blue",relief='ridge').pack()
l=Label(root,image=icon1).pack()
Label(root,text='Enter Username').pack()
a=Entry(root)
a.pack() 
Label(root,text='Enter Password').pack()
c=Entry(root,show='*')
c.pack()

def create():
    window2 = Toplevel(root)
    window2.configure(bg='light blue')
    window2.geometry('300x300')
    Label(window2,text='Enter your name').pack()
    l=Entry(window2)
    l.pack()
    Label(window2,text='Enter Username').pack()
    a=Entry(window2)
    a.pack() 
    Label(window2,text='Enter Password').pack()
    c=Entry(window2,show='*')
    c.pack()
    Label(window2,text='Enter yor mobile number(10 digits)').pack()
    m=Entry(window2)
    m.pack()
    
    def account():
        i=0
        if a.get()=='' or c.get()=='' or m.get()=='' or l.get()=='' :
            showerror('missing input','please fill every detail')
        num=len(m.get())
        if num!=10:
            showerror('error','mobile number is invalid')
            i=1
        else:
            
            try:
                val=int(m.get())
                cur.execute("insert into showbook values (?,?,?,?)",(a.get(),c.get(),val,l.get()))
                con.commit()
            
            except ValueError:
                showerror('error','mobile number is invalid')
                i=1
            except sqlite3.IntegrityError:
                showerror('error','invalid input by the user')
                i=1
            except:
                showerror('username not unique','username already exisits')
                i=1
            if(i==0):
                showinfo('welcome','account is created')
                window2.destroy()
    Button(window2,text='create account',command=account).pack()

def login():
    cur.execute(('SELECT * FROM showbook WHERE id = ? and password = ?'),[(a.get()),(c.get())])
    b=cur.fetchall()
    print b
    if b:
        window1 = Toplevel(root)
        window1.configure(bg='light blue')
        window1.geometry('300x300')
        def bookticket():
            window = Toplevel(window1)
            window.configure(bg='light blue')
            window.geometry('300x300')
            cur.execute("create table if not exists bticket(id varchar(10) ,movie varchar(10),date date,num_ticket number(10))")
            Label(window,text='select movie:',bg='light blue').pack()
            v1=IntVar()
            r=Radiobutton(window,text='Robot 2.0',variable=v1,value=1,bg='light blue')
            r.pack()
            r=Radiobutton(window,text='Fantastic Beasts the Crimes of Grindelwald',variable=v1,value=2,bg='light blue')
            r.pack()
            r=Radiobutton(window,text='Zero',variable=v1,value=3,bg='light blue')
            r.pack()
            r=Radiobutton(window,text='Baazar',variable=v1,value=4,bg='light blue')
            r.pack()
            r=Radiobutton(window,text='Thugs of hindostan',variable=v1,value=5,bg='light blue')
            r.pack()
            Label(window,text='enter the date(yyyy-mm-dd)',bg='light blue').pack()
            e=Entry(window)
            e.pack()
            Label(window,text='enter number of tickets to book',bg='light blue').pack()
            h=Entry(window)
            h.pack()
            def check():
                
                if(v1.get()==1):
                    f='robot 2.0'
                if(v1.get()==2):
                    f='fantastic beasts the crimes of grindelwald'
                if(v1.get()==3):
                    f='Zero'
                if(v1.get()==4):
                    f='Baazar'
                if(v1.get()==5):
                    f='Thugs of hindostan'
                cur.execute("select sum(num_ticket) from bticket where movie = ? and date = ?",[(f),e.get()])
                k=cur.fetchone()
                print k[0]
                if(k[0]==None):
                    j=150
                else:
                    j=150-k[0]
                Label(window,text='available seats:-'+str(j),bg='light blue').pack()
            Button(window,text='check availability tickets',command=check).pack()
            def book():
                if(v1.get()==1):
                    f='robot 2.0'
                if(v1.get()==2):
                    f='fantastic beasts the crimes of grindelwald'
                if(v1.get()==3):
                    f='Zero'
                if(v1.get()==4):
                    f='Baazar'
                if(v1.get()==5):
                    f='Thugs of hindostan'
                if v1.get()==0 or e.get()=='' or h.get()=='':
                    showerror('missing input','please fill every detail')
                else:
                    cur.execute("insert into bticket values (?,?,?,?)",(a.get(),f,e.get(),h.get()))
                    con.commit()
                    showinfo('well done','tickets are booked')
                    window.destroy()
                
            Button(window,text='book tickets',command=book).pack()
        def myticket():
            window = Toplevel(window1)
            window.configure(bg='light blue')
            window.geometry('550x300')
            cur.execute(('SELECT * FROM bticket WHERE id = ?'),[(a.get())])
            g=cur.fetchall()
            Label(window,text='   username',bg='light blue').grid(row=0,column=0)
            Label(window,text='   movie name',bg='light blue').grid(row=0,column=1)
            Label(window,text='   date of the show',bg='light blue').grid(row=0,column=2)
            Label(window,text='   number of tickets',bg='light blue').grid(row=0,column=3)
            if(g==[]):
                showerror('bookings','no bookings yet!!')
                window.destroy()
                
            else:
                j=0
                for i in g:
                    Label(window,text=g[j][0],bg='light blue').grid(row=j+1,column=0)
                    Label(window,text=g[j][1],bg='light blue').grid(row=j+1,column=1)
                    Label(window,text=g[j][2],bg='light blue').grid(row=j+1,column=2)
                    Label(window,text=g[j][3],bg='light blue').grid(row=j+1,column=3)
                    j=j+1
                    
        def cancel():
            window = Toplevel(window1)
            window.configure(bg='light blue')
            window.geometry('300x300')
            Label(window,text='select movie to cancel:',bg='light blue').pack()
            v2=IntVar()
            r=Radiobutton(window,text='Robot 2.0',variable=v2,value=1,bg='light blue')
            r.pack()
            r1=Radiobutton(window,text='Fantastic Beasts the Crimes of Grindelwald',variable=v2,value=2,bg='light blue')
            r1.pack()
            r=Radiobutton(window,text='Zero',variable=v2,value=3,bg='light blue')
            r.pack()
            r=Radiobutton(window,text='Baazar',variable=v2,value=4,bg='light blue')
            r.pack()
            r=Radiobutton(window,text='Thugs of hindostan',variable=v2,value=5,bg='light blue')
            r.pack()
            Label(window,text='enter the date(yyyy-mm-dd)',bg='light blue').pack()
            e=Entry(window)
            e.pack()
            def cancel_1():
                
                if v2.get()==0 or e.get()=='':
                    showerror('missing input','please fill every detail')
                else:
                    if(v2.get()==1):
                        j='robot 2.0'
                    if(v2.get()==2):
                        j='fantastic beasts the crimes of grindelwald'
                    if(v2.get()==3):
                        j='Zero'
                    if(v2.get()==4):
                        j='Baazar'
                    if(v2.get()==5):
                        j='Thugs of hindostan'
                    cur.execute(("select * from bticket WHERE id = ? and movie = ? and date = ?"),(a.get(),j,e.get()))
                    n=cur.fetchall()
                    if(n==[]):
                        showerror('error',"there is no such ticket of your's!!!")
                    else:
                        cur.execute(('delete FROM bticket WHERE id = ? and movie = ? and date = ?'),(a.get(),j,e.get()))
                        con.commit()
                        showinfo('cancelled','your ticket has been cancelled')
                        window.destroy()
                
            Button(window,text='cancel ticket',bd=5,command=cancel_1).pack()

        Label(window1,text='       SELECT YOUR CHOICE       ',bg='light blue',font="Arial 10 bold italic").pack()
        Button(window1,text='book new tickets',bd=5,command=bookticket).pack()
        Label(window1,text='------------------',bg='light blue').pack()
        Button(window1,text='my tickets',bd=5,command=myticket).pack()
        Label(window1,text='------------------',bg='light blue').pack()
        Button(window1,text='cancel ticket',bd=5,command=cancel).pack()
        Label(window1,text='------------------',bg='light blue').pack()
        
    else:
        showerror('invalid user','invalid username or password')

Label(root,text='                 ',bg='#424242').pack()
Button(root,text='create account',bd=5,bg='light blue',command=create).pack()
Label(root,text='                 ',bg='#424242').pack()
Button(root,text='Login',bd=5,command=login,bg='light blue').pack()
root.mainloop()


