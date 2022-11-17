from tkinter import *

def success_alert(barcode):
    root = Tk()
    root.title('Success')
    root.geometry('1280x720')
    root.config(bg='green')

    root_pad = Label (root, text='', bg='green', fg='white', font=('helvetica', 30))
    root_pad.pack(pady=40)

    root_label = Label (root, text='Codigo detectado:', bg='green', fg='white', font=('helvetica', 40))
    root_label.pack(pady=10)

    root_pad = Label (root, text=barcode, bg='green', fg='white', font=('helvetica', 40))
    root_pad.pack(pady=1)

    root.after(4000, lambda:root.destroy())

    root.mainloop()

def error_alert():
    root = Tk()
    root.title('Error')
    root.geometry('1280x720')
    root.config(bg='red')

    root_pad = Label (root, text='', bg='red', fg='white', font=('helvetica', 30))
    root_pad.pack(pady=40)

    root_label = Label (root, text='Codigo NO detectado', bg='white', fg='red', font=('helvetica', 40))
    root_label.pack(pady=10)

    root_pad = Label (root, text='Intente nuevamente', bg='red', fg='white', font=('helvetica', 40))
    root_pad.pack(pady=1)

    root.after(4000, lambda:root.destroy())

    root.mainloop()
    