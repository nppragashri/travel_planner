import pymysql
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from destination import *
# Function to register a new user

def generate_user_id():
    con = pymysql.connect(host="localhost", user="root", password="AZaz09@23", database="travel_planner")
    cur = con.cursor()
    sql_query = "SELECT User_ID FROM users_table ORDER BY User_ID DESC LIMIT 1"
    # Execute the query
    cur.execute(sql_query)
    # Fetch the result
    result = cur.fetchone()
    # Close the database connection
    con.close()
    # Check if a result was returned and print the primary key value
    if result:
        primary_key_value = result[0]
        print("The primary key value of the last row is:", primary_key_value)
    else:
        print("No rows found in the table.")
        u_id = "U001"
        return u_id
    counter = primary_key_value[1:]
    counter = int(counter) + 1
    print("new counter :",counter)
    u_id = 'U' + str(counter).zfill(3)
    return u_id

def userlogin():
    global counter 
    User_id = generate_user_id()
    # Fname = clientfn.get()
    # User_id = Uphone.get()
    User_Name = Uname.get()
    Ph_no = Uphone.get()
    Email = Uemail.get()
    Password = Upwd.get()

    clientInfo = "INSERT INTO users_table VALUES (%s, %s, %s, %s, %s)"
    try:
        cur.execute(clientInfo, (User_id, User_Name ,Ph_no, Email, Password))
        con.commit()

        messagebox.showinfo('Success', "User added successfully")
        select_destination()

    except Exception as e:
        messagebox.showinfo("Error", f"Can't add data into Database: {str(e)}")
        print(e)

def register_user():
    # Connect to the MySQL database
    root = Tk()
    root.title("User Login")
    root.minsize(width=400,height=400)
    root.geometry("1800x800")

    global Uname,Uphone,Uemail,Upwd
    global Canvas1,con,cur,usertable

    con = pymysql.connect(host="localhost", user="root", password="user123", database="travel_planner")
    cur = con.cursor()

    usertable = "users_table"

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="User Login", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
    # user name
    lb1 = Label(labelFrame,text="User Name : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)     
    Uname = Entry(labelFrame)
    Uname.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)  
    #phone
    lb2 = Label(labelFrame,text="Phone: ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)   
    Uphone = Entry(labelFrame)
    Uphone.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08) 
    # email
    lb3 = Label(labelFrame,text="Email : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.5, relheight=0.08)  
    Uemail = Entry(labelFrame)
    Uemail.place(relx=0.3,rely=0.5, relwidth=0.62, relheight=0.08) 
    # Password
    lb4 = Label(labelFrame,text="Password: ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
    Upwd = Entry(labelFrame)
    Upwd.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
    SubmitBtn = Button(labelFrame,text="Login",bg='#d1ccc0', fg='black',command=userlogin)
    SubmitBtn.place(relx=0.41,rely=0.85, relwidth=0.18,relheight=0.08)
    