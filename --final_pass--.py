from tkinter import*
import time
from pwgenfunc import RandPass
from tkinter import messagebox


#<-------------------Password Generator-------------------------->

def pwGenerator(size = 8):
    data = RandPass(size)
    new_password = data[0]
    pw_strength = data[1]
    pw_color = data[2]
    PASSWORD.set(new_password);
    lbl_strength.configure(foreground="white", background=pw_color, text=pw_strength, font=('sans serif', 10, 'bold'), bd=10, height=1, width=10)
    window.clipboard_clear()
    window.clipboard_append(new_password)
    window.update()
    time.sleep(.02)
    window.update()
    window.mainloop()


#<-------------------Save Password-------------------------->

def save():
    
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:

        is_ok= messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail/Username: {email} "
                                                       f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} |  {email} | {password}\n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)



#<-------------------GUI Setup-------------------------->

window = Tk()
window.title("Password Manager")
window.geometry("900x530")
window.resizable(True, True)

#<----------------------BG Image-------------------->

bg=PhotoImage(file="images/back1.png")
bg_image=Label(image=bg).place(x=0, y=0, relwidth=1, relheight=1)

#<------------------pass frame-------------------->
Frame_pass_manager=Frame(bg="white")
Frame_pass_manager.place(x=40, y=50, height=435, width=470)


canvas = Canvas(height=75, width=100, bg='#191b4b', bd=0, relief='ridge')
logo_img = PhotoImage(file="logo.png")
canvas.create_image(50, 40, image=logo_img)
canvas.place(x=75, y=53)


###<------------------------VARIABLES------------------>

PASSWORD = StringVar()
PW_SIZE = IntVar()
e1 = Entry(window, text=PW_SIZE)
PW_SIZE.set(8) # sets the default value for PW size/length

#<------------------Lables-------------------->

title=Label(Frame_pass_manager, text="      My Password", anchor="center", font=("Impact",35), fg="White", bg="#191b4b",
            width=23).place(x=0, y=10)

website=Label(Frame_pass_manager, text="Website:",font=("Arial Rounded MT Bold",12,"bold"), fg="#191b4b", bg="white").place(x=10, y=120)
website_entry=Entry(Frame_pass_manager, font=("Times new roman",13), bg="lightgray")
website_entry.place(x=165, y=120, width=280, height=25)
        
email=Label(Frame_pass_manager, text="Email/Username:",font=("Arial Rounded MT Bold",12,"bold"), fg="#191b4b", bg="white").place(x=10, y=160)
email_entry=Entry(Frame_pass_manager, font=("Times new roman",13), bg="lightgray")
email_entry.place(x=165, y=160, width=280, height=25)
        
password=Label(Frame_pass_manager, text="Password:",font=("Arial Rounded MT Bold",12,"bold"), fg="#191b4b", bg="white").place(x=10, y=200)
password_entry=Entry(Frame_pass_manager, textvariable=PASSWORD, font=("Times new roman",13), bg="lightgray")
password_entry.place(x=165, y=200, width=160, height=25)
        
lbl_strength = Label(Frame_pass_manager, font=('sans serif', 10, 'bold'), foreground="white", background="#6d0001", text="Weak",
                     bd=10, height=1, width=10)
lbl_strength.place(x=340, y=195)

lbl_pw_size=Label(Frame_pass_manager, text="Size:",font=("Arial Rounded MT Bold",12,"bold"), fg="#191b4b", bg="white").place(x=10, y=250)

pw_size1=Scale(Frame_pass_manager, from_=8, to=24, length=275, width=24, sliderlength=14, orient=HORIZONTAL, bd=0, variable=PW_SIZE,
                font=(18), bg="white").place(x=165, y=240)
        
        
#<------------------Buttons-------------------->

Generate_pass=Button(Frame_pass_manager, text="Generate Password", font=("Arial Black",13,"bold"), bg="#191b4b", fg="white",
                     command=lambda: pwGenerator(PW_SIZE)).place(x=140, y=325)

Add=Button(Frame_pass_manager, text="Add", font=("Arial Rounded MT Bold",13,"bold"), width=30, bg="#191b4b",
           fg="white", command=save).place(x=50, y=380)



window.mainloop()
