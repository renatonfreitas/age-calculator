from tkinter import *
from tkinter import ttk

#JANELA
root = Tk()
root.title("SmiiLe Age Calculator")
root.geometry('340x420')

#FRAME
mainframe = ttk.Frame(root, width=320, height=420)

#TÍTULO
title_label = ttk.Label(mainframe, text='Age calculator')
title_style = ttk.Style()
title_style.configure('TLabel', font=('Candara', 20))

#DATA DE NASCIMENTO
date = StringVar()
date.set('18/08/2023')
birth = ttk.Combobox(mainframe, textvariable=date)


#INSERINDO NA TELA
mainframe.grid(row=0, column=0)
title_label.grid(row=1, column=0, padx=85, pady=10)
# title_label.place(x=90, y=20)
birth.grid(row=5, column=0, pady=30)


root.mainloop()
