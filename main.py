#  Ahmed NSER ELDIN MOHAMED ELKATRy- Section 4 - Eng.Mohammed Yousry

from tkinter import Tk, Label, Button, Entry

root = Tk()
root.title("Simple GUI - Ahmed NSER ELDIN ELKATRy")
root.geometry("400x400")
root.configure(bg="black")

    
def show_success():
    success_label = Label(root, text="Successful!", fg="white", bg="black", font=("Roboto", 12))
    success_label.pack() 

def save_credentials():
    if not entry_name.get() or not entry_password.get():
        error_window = Tk()
        error_window.title("Error")
        error_window.geometry("300x150")
        error_label = Label(error_window, text="Both fields are required!", fg="red", font=("Arial", 12))
        error_label.pack(pady=20)
        button_close = Button(error_window, text="Close", command=error_window.destroy)
        button_close.pack(pady=10)
        error_window.mainloop()
        return

    username = entry_name.get()
    password = entry_password.get()
    show_success()

label = Label(root, text="Welcome to the GUI Task", font=("Roboto", 14), bg="black", fg="white")
label.pack(pady=20)
label_name = Label(root, text="Username:", bg="black", fg="white")
label_name.pack(pady=5)
entry_name = Entry(root)
entry_name.pack(pady=5)
label_password = Label(root, text="Password:", bg="black", fg="white")
label_password.pack(pady=5)
entry_password = Entry(root, show='*')
entry_password.pack(pady=5)
ton_submit = Button(root, text="Submit", command=lambda: [save_credentials()]) # add window sign in open
ton_submit.pack(pady=20)

root.mainloop()