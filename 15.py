import tkinter, time

app_window = tkinter.Tk()
app_window.title('Digital Clock')
app_window.geometry('450x150')
app_window.resizable(1, 1)

text_font = ('Boulder', 68, 'bold')
background = '#f2e750'
foreground = '#363529'
border_width = 25

label = tkinter.Label(app_window, font=text_font, bg=background, foreground=foreground)
label.grid(row=0, column=1)

def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)

digital_clock()
app_window.mainloop()