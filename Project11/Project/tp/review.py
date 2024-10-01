from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from destination import *
# def give_review(selected_destination):
#     print("review page")

def give_review(user_id, destination_name, rating, comment):
    con = pymysql.connect(host="localhost", user="root", password="AZaz09@23", database="travel_planner")
    cur = con.cursor()

    # Get DestinationID for the selected destination
    query = f"SELECT DestinationID FROM destination_table WHERE Destination_Name = '{destination_name}'"
    cur.execute(query)
    destination_id = cur.fetchone()[0]

    # Insert the review into the Reviews table
    insert_query = "INSERT INTO Reviews (UserID, DestinationID, Rating, Comment) VALUES (%s, %s, %s, %s)"
    data = (user_id, destination_id, rating, comment)

    try:
        cur.execute(insert_query, data)
        con.commit()
        con.close()
    except Exception as e:
        con.rollback()
        con.close()
        raise e
