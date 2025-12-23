import tkinter as tk

def print_custom(message) : 
    print(message)

root = tk.Tk()

root.geometry("400x400")
root.title("My Tkinter Window")

label = tk.Label(root, text = "Hello, Tkinter!", font = ("Arial",22))
label.pack(padx=20,pady=20)

textbox = tk.Text(root,height = 3,font = ("Arial",16))
textbox.pack(padx = 20,pady=20)

# myEntry = tk.Entry(root)
# myEntry.pack()

button = tk.Button(root, text = "Press Here", font = ("Arial",16),command=lambda:print_custom("button pressed!"))
button.pack(padx=20)
root.mainloop()