import tkinter

root = tkinter.Tk()

root.title("Hello tkinter")
root.geometry('600x400')

menu = tkinter.Menu(root)
item = tkinter.Menu(menu)
item.add_command(label='New')
item.add_command(label='Save')
item.add_command(label='Open')
item.add_command(label='Close')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

label = tkinter.Label(root, text='Are you okay?')
label.grid()

txt = tkinter.Entry(root, width=10)
txt.grid(column=1, row=0)

def clicked():
    label.configure(text='I just got clicked')

button = tkinter.Button(root, text='Click me', fg='red', command=clicked)
button.grid(column=2, row=0)

root.mainloop()