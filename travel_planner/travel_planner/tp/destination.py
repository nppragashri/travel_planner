from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from review import *
from accommodation import accommodate

def display_destination(Destination_Name):
    con = pymysql.connect(host="localhost", user="root", password="AZaz09@23", database="travel_planner")
    cur = con.cursor()
    # Query to retrieve destination information based on the destination_name
    query = f"SELECT Country, Image_URL, Climate, Destination_ID FROM destination_table WHERE Destination_Name = '{Destination_Name}'"

    try:
        cur.execute(query)
        destination_data = cur.fetchone()  # Assuming there's only one matching destination

        if destination_data:
            country, Image_URL, climate, Destination_ID = destination_data
            # Create a new window to display the information
            destination_window = Toplevel()
            destination_window.title(Destination_Name)

            # Display the retrieved information
            Label(destination_window, text=f"Country: {country}").pack()
            Label(destination_window, text=f"Climate: {climate}").pack()
            image = Image.open(Image_URL)
            photo = ImageTk.PhotoImage(image)
            image_label = Label(destination_window, image=photo)
            image_label.image = photo
            image_label.pack()

            # Fetch and display activity information
            activity_query = f"SELECT Type, Cost FROM ACTIVITY_TABLE WHERE Destination_ID = '{Destination_ID}'"
            cur.execute(activity_query)
            activity_data = cur.fetchall()

            if activity_data:
                Label(destination_window, text="Activities:").pack()
                for activity in activity_data:
                    Type, Cost = activity
                    Label(destination_window, text=f"- {Type}: ${Cost}").pack()
            
        else:
            messagebox.showerror("Error", f"Destination '{Destination_Name}' not found.")

    except Exception as e:
        messagebox.showerror("Error", str(e))

    con.close()

def finalize_destination(selected_destination):
    accommodate(selected_destination)
# def go_to_review(selected_destination):
#     give_review(selected_destination)

def select_destination():
    root = Tk()
    root.title("Destination")
    root.minsize(width=400,height=400)
    root.geometry("1800x800")

    con = pymysql.connect(host="localhost", user="root", password="user123", database="travel_planner")
    cur = con.cursor()

    desttable = "DESTINATION_TABLE"

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Select Destination", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
    #Submit Button
    # SubmitBtn1 = Button(labelFrame,text="Login",bg='#d1ccc0', fg='black',command=userlogin)
    # SubmitBtn1.place(relx=0.41,rely=0.85, relwidth=0.18,relheight=0.08)

    # Dropdown list with destination options
    destination_options = ["Florida", "Goa", "Interlaken"]
    selected_destination = StringVar(root)
    # selected_destination.set(destination_options[0])  # Default selection

    SubmitBtn1 = Button(labelFrame,text="Florida",bg='#d1ccc0', fg='black',command=lambda: display_destination("Florida"))
    SubmitBtn1.place(relx=0.41,rely=0.30, relwidth=0.18,relheight=0.08)

    SubmitBtn2 = Button(labelFrame,text="Goa",bg='#d1ccc0', fg='black',command=lambda: display_destination("Goa"))
    SubmitBtn2.place(relx=0.41,rely=0.40, relwidth=0.18,relheight=0.08)

    SubmitBtn3 = Button(labelFrame,text="Interlaken",bg='#d1ccc0', fg='black',command=lambda: display_destination("Interlaken"))
    SubmitBtn3.place(relx=0.41,rely=0.50, relwidth=0.18,relheight=0.08)

    dropdown = OptionMenu(labelFrame, selected_destination, *destination_options)
    dropdown.place(relx=0.41, rely=0.60, relwidth=0.18, relheight=0.08)

    #Button to finalize the destination
    SubmitBtn = Button(labelFrame, text="Finalize Destination", bg='#d1ccc0', fg='black', command=lambda: finalize_destination(selected_destination.get()))
    SubmitBtn.place(relx=0.41, rely=0.70, relwidth=0.18, relheight=0.08)

    # SubmitBtn = Button(labelFrame, text="Give Review", bg='#d1ccc0', fg='black', command=lambda: go_to_review(selected_destination.get()))
    # SubmitBtn.place(relx=0.41, rely=0.70, relwidth=0.18, relheight=0.08)
    root.mainloop()

