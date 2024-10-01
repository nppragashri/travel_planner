from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from destination import *

# def accommodate(selected_destination):
#     print("accommodation page")
global destination_name
def generate_accommodation():
    con = pymysql.connect(host="localhost", user="root", password="AZaz09@23", database="travel_planner")
    cur = con.cursor()
    sql_query = "SELECT Accommodation_ID FROM accommodation_table ORDER BY Accommodation_ID DESC LIMIT 1"
    # Execute the query
    cur.execute(sql_query)
    # Fetch the result
    result = cur.fetchone()
    # Close the database connection
    con.close()
    # Check if a result was returned and print the primary key value
    if result:
        primary_key_value = result[0]
        primary_key_value = int(primary_key_value)
        print("The primary key value of the last row is:", primary_key_value)
    else:
        print("No rows found in the table.")
        a_id = 100
        return a_id
    # counter = primary_key_value[1:]
    a_id = primary_key_value + 1
    return int(a_id)

def accommodate(selected_destination):
    destination_name = selected_destination
    print(selected_destination)
    # destination_name = 'Goa'

    def add_accommodation():
        dest = destination_name 
        count = folks_count_entry.get()
        folks_count = int(count)
        start_date = start_date_entry.get()
        end_date = end_date_entry.get()
        # start_date = '20-12-2023'
        # end_date = '30-12-2023'
        new_accommodation_id = generate_accommodation()


        con = pymysql.connect(host="localhost", user="root", password="user123", database="travel_planner")
        cur = con.cursor()
        sql_query = "SELECT User_ID FROM USERS_TABLE ORDER BY User_ID DESC LIMIT 1"
        cur.execute(sql_query)
        result_user = cur.fetchone()
        user_id = result_user[0]
        user_id = str(user_id)
        print(user_id)

        # Get Destination_ID based on the selected_destination
        cur.execute(f"SELECT Destination_ID FROM destination_table WHERE Destination_Name = '{dest}'")
        result_dest = cur.fetchone()
        dest_id = result_dest[0]
        destination_id = int(dest_id)
        # print(destination_id)

        # Insert accommodation data into Accommodation_Table
        print(new_accommodation_id,type(new_accommodation_id))
        print(folks_count,type(folks_count))
        print(end_date,type(end_date))
        print(start_date,type(start_date))
        print(destination_id,type(destination_id))
        print(user_id,type(user_id))
        
        Accomo = "INSERT INTO accommodation_table VALUES (%s, %s, %s, %s, %s, %s)"
        try:
            cur.execute(Accomo, (new_accommodation_id,folks_count,end_date,start_date,destination_id,user_id))
            con.commit()

            messagebox.showinfo("Success", "Accommodation details added successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add accommodation details: {str(e)}")

        con.close()

    accommodation_window = Toplevel()
    accommodation_window.title("Accommodation Form")

    folks_count_label = Label(accommodation_window, text="Folks Count:")
    folks_count_label.pack()
    folks_count_entry = Entry(accommodation_window)
    folks_count_entry.pack()

    start_date_label = Label(accommodation_window, text="Start Date (DD-MM-YYYY):")
    start_date_label.pack()
    start_date_entry = Entry(accommodation_window)
    start_date_entry.pack()

    end_date_label = Label(accommodation_window, text="End Date (DD-MM-YYYY):")
    end_date_label.pack()
    end_date_entry = Entry(accommodation_window)
    end_date_entry.pack()

    submit_button = Button(accommodation_window, text="Submit", command=add_accommodation)
    submit_button.pack()

    accommodation_window.mainloop()
# accommodate('Goa')