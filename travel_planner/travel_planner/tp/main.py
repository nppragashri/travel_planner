from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from user import *

mypass = "AZaz09@23"
mydatabase = "travel_planner"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("Travel Planner")
root.minsize(width=400, height=400)
root.geometry("1800x800")

# Take n greater than 0.25 and less than 5
same = True
n = 1

# Adding a background image

background_image = Image.open('background.jpg')
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth * n) + 200
if same:
    newImageSizeHeight = int(imageSizeHeight * n)
else:
    newImageSizeHeight = int(imageSizeHeight / n)

background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)
Canvas1.create_image(0, 0, anchor=NW, image=img)
Canvas1.config(bg="white", width=1800, height=800)
Canvas1.pack(expand=True, fill=BOTH)


headingLabel = Label(root, text="Welcome to Travelo ",fg='navy',compound='center',font=('Lucida Calligraphy', 40))
headingLabel.place(relx=0.21, rely=0, relwidth=.6, relheight=.1)

btn1 = Button(root, text="Login", bg='black', fg='white', font=('Lucida Calligraphy', 40),command=register_user)
btn1.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

root.mainloop()