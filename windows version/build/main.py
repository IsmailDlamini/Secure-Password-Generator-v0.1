#©Code wizards 2023: Copyright all right reserved
#codes Ismail(backend) and Mncedisi(frontend)
#please ask for permision from us before you copy or use this code anywhere
# E-mail= iii409475@gmail.com


import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
import string
from PIL import ImageTk, Image
import random
from generator import *
import time

# variables

password_lenght = 8

password = ""
cleared = True
encrypted = "False"
encryption = "None"
copied = ""

root = Tk()

root.title('Password Generator')

window_width = 600
window_height = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# get center position of the screen 
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
root.configure(bg="black")

def error():

    messagebox.showerror('Error',"er309/23#\nPlease select atleast one option\n from (letters, Numbers, Special Letters)")

def increase_password_len():

    global password_lenght

    if password_lenght < 16:
        password_lenght += 1
        passlen_text = tk.Label(root, text=f"{password_lenght} chars", foreground="green", bg="black", width="7", height="2",
                    font="freesansbold.ttf")
        passlen_text.place(x=185, y=305)
        

def decrease_password_len():

    global password_lenght

    if password_lenght > 8:
        password_lenght -= 1
        passlen_text = tk.Label(root, text=f"{password_lenght} chars", foreground="green", bg="black", width="7", height="2",
                    font="freesansbold.ttf")
        passlen_text.place(x=185, y=305)

def save_passwords_to_file():

    global password, encrypted, encryption

    with open("saved_passwords\passwords.txt", "a") as password_file:
        password_file.write(f'--#password={password}  --# Encrypted={encrypted}  --# encryption={encryption} \n')
        password_file.write(f'Date-Generated: {time.localtime()[2]}/{time.localtime()[1]}/{time.localtime()[0]}\n')
        password_file.write('secured by Ismail and Mncedisi the Code Wizards\n')
        password_file.write('  \n')
        password_file.write('  \n')

    
def copy_pass():

    global password, copied
    
    if copied != password:
        root.clipboard_clear()
        root.clipboard_append(password)
        copied = password
    

def clear_pass():

    global password, generate_password


    password = ""
    
    show_password = tk.Label(root, text=f"{password}", foreground="green", bg="black", width=password_lenght * 2,
                    font="freesansbold.ttf")
    show_password.place(x=240 - password_lenght * 7, y=505)

    copy = Button(text='Copy', activebackground='lime green', activeforeground='white', font='Helvetica',
             bg='green', border=2, state="disabled")

    copy.place(x=90, y=420)

    clear = Button(text='Clear', activebackground='lime green', activeforeground='white', font='Helvetica',
                      bg='green', border=2, state="disabled")
    clear.place(x=450, y=420)

    generate = Button(text='Generate', activebackground='lime green', activeforeground='white', font='Helvetica',
                      bg='green', border=2, command=generate_password)
    generate.place(x=250, y=420)


def generate_password():

    global password, clear_pass, save, error

    password = generate_password_file(password, password_lenght, letters.get(), number.get(), special.get())

    if len(password) >= 12:
        
        show_password = tk.Label(root, text=f"{password}", foreground="green", bg="black", width=password_lenght * 2,
                        font="freesansbold.ttf")
        show_password.place(x=240 - password_lenght * 7, y=505)
        if save.get() == "on":
            save_passwords_to_file()
            
    if len(password) < 12:
        show_password = tk.Label(root, text=f"{password}", foreground="green", bg="black", width=password_lenght * 2,
                    font="freesansbold.ttf")
        show_password.place(x=240 - password_lenght * 5, y=505)
        if save.get() == "on":
            save_passwords_to_file()
            

    copy = Button(text='Copy', activebackground='lime green', activeforeground='white', font='Helvetica',
             bg='green', border=2, command=copy_pass)

    copy.place(x=90, y=420)

    clear = Button(text='Clear', activebackground='lime green', activeforeground='white', font='Helvetica',
                      bg='green', border=2, command=clear_pass)
    clear.place(x=450, y=420)

    

image1 = ImageTk.PhotoImage(Image.open("images\secpass.png"))
panel = Button(root, image=image1, width=430, height=180, border=0, bg="black")
panel.place(x=90, y=0)

back1 = tk.Label(root, text=f"", foreground="green", bg="green", width="40", height="8",
                    font="freesansbold.ttf")
back1.place(x=80, y=220)

back2 = tk.Label(root, text=f"", foreground="black", bg="black", width="39", height="7",
                    font="freesansbold.ttf")
back2.place(x=85, y=225)

config_label = tk.Label(root, text=f"Configurations", foreground="green", bg="black", width="12", height="1",
                    font="freesansbold.ttf")
config_label.place(x=240, y=210)

lenght_label = tk.Label(root, text=f"Password lenght", foreground="green", bg="black", width="16", height="1",
                    font="freesansbold.ttf")
lenght_label.place(x=100, y=240)

lenght_labe2 = tk.Label(root, text=f"(min=8,max=16)", foreground="green", bg="black", width="14", height="1",
                    font="freesansbold.ttf")
lenght_labe2.place(x=110, y=270)


increase = Button(text='+', activebackground='lime green', activeforeground='white', font='Helvetica',
                  bg='green', border=2, command=increase_password_len)
increase.place(x=120, y=310)

decrease = Button(text='-', activebackground='lime green', activeforeground='white', font='Helvetica',
                  bg='green', border=2, command=decrease_password_len)
decrease.place(x=155, y=310)


passlen_text = tk.Label(root, text=f"{password_lenght} chars", foreground="green", bg="black", width="7", height="2",
                    font="freesansbold.ttf")
passlen_text.place(x=185, y=305) 

lenght_label = tk.Label(root, text=f"Password contents", foreground="green", bg="black", width="16", height="1",
                    font="freesansbold.ttf")
lenght_label.place(x=330, y=240)

save = StringVar(root, string.ascii_letters)
save1 = tk.Checkbutton(root, text='save passwords to file', variable=save, bg="black", foreground="green",
                    activebackground='black', onvalue="on", offvalue="off").place(y='350', x='350')
save.set("on")

letters = StringVar(root, string.ascii_letters)
c1 = tk.Checkbutton(root, text='Letters', variable=letters, bg="black", foreground="green", activebackground='black', onvalue="on", offvalue="on").place(y='270', x='350')
letters.set("on")
special = StringVar(root, string.punctuation)
c2 = tk.Checkbutton(root, text='Special Characters', variable=special, bg="black", foreground="green", activebackground='black', onvalue="on", offvalue="off").place(y='310', x='350')
special.set("on")
number = StringVar(root, string.digits)
c3 = tk.Checkbutton(root, text='Numbers', variable=number, bg="black", foreground="green", activebackground='black', onvalue="on", offvalue="off").place(y='290', x='350')
number.set("on")
back3 = tk.Label(root, text=f"", foreground="green", bg="green", width="40", height="2",
                    font="freesansbold.ttf")
back3.place(x=82, y=500)    

back4 = tk.Label(root, text=f"", foreground="black", bg="black", width="50", height="6",
                    font="freesansbold.ttf")
back4.place(x=62, y=400)


# generate button
generate = Button(text='Generate', activebackground='lime green', activeforeground='white', font='Helvetica',
                  bg='green', border=2, command=generate_password)
generate.place(x=250, y=420)

owner_ship = tk.Label(root, text=f"©Code wizards 2023: Copyright all right reserved", foreground="green", bg="black", width="40", height="1",
                        font="freesansbold.ttf")
owner_ship.place(x=82, y=560)   

root.mainloop()
