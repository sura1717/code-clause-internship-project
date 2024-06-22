
import tkinter as tk
from tkinter import filedialog,messagebox

def new_file():
    text_area.delete(1.0,tk.END)
    root.title("United Simple Text Editor")

def open_file():
    path=filedialog.askopenfilename(filetypes=[("Text Files","*.txt"),("All Files","*.*")])
    if path:
        with open(path,"r") as file:
            text_area.delete(1.0,tk.END)
            text_area.insert(tk.END,file.read())
        root.title(f"{path} - Simple Text Editor")

def save_file():
    try:
        path=filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text Files","*.txt"),("All Files","*.*")])
        if path:
            with open(path,"w") as file:
                content=text_area.get(1.0,tk.END)
                file.write(content)
            root.title(f"{path} - Simple Text Editor")
            messagebox.showinfo("Save File","File Saved Successfully ! ")
        else:
            messagebox.showinfo("Save File","Save Operation Cancelled !")
    except Exception as e:
        messagebox.showinfo("Save File",f"An error occurred while saving the file:{e}")
def exit_file():
    root.quit()



root=tk.Tk()
root.title("Simple Text Editor")

text_area = tk.Text(root,wrap="word",undo=True)
text_area.pack(expand="yes",fill="both")

menu_bar=tk.Menu(root)
root.config(menu=menu_bar)

file_menu=tk.Menu(menu_bar,tearoff=False)
menu_bar.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=lambda: new_file())
file_menu.add_command(label="Open",command=lambda: open_file())
file_menu.add_command(label="Save",command=lambda: save_file())
file_menu.add_separator()
file_menu.add_command(label="Exit",command=lambda: exit_file())

root.mainloop()