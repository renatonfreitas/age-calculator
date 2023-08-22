from datetime import date
from tkinter import *
from tkinter import ttk

# ---------- FUNCTIONS ----------


def calculate():
    try:
        month_hash = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 30,
            9: 31,
            10: 30,
            11: 31,
            12: 30,
        }

        begin = input_date.get()
        begin_year = int(begin[6:])
        begin_month = int(begin[3:5])
        begin_day = int(begin[:2])
        end = date.today()

        years_calculated = end.year - begin_year
        months_calculated = end.month - begin_month
        if months_calculated < 0:
            years_calculated -= 1
            months_calculated += 12
        days_calculated = end.day - begin_day
        if days_calculated < 0:
            months_calculated -= 1
            days_calculated += month_hash[end.month - 1]

        years['text'] = years_calculated
        months['text'] = months_calculated
        days['text'] = days_calculated

    except ValueError:
        years['text'] = '--'
        months['text'] = '--'
        days['text'] = '--'


# ---------- GUI ----------

root = Tk()
root.title('SmiiLe Age Calculator')
root.geometry('310x400')
root.minsize(310, 400)
root.maxsize(310, 400)

# ---------- COLORS ----------

color1 = '#292525'  # dark black
color2 = '#3b3b3b'  # light black
color3 = '#ffffff'  # white
color4 = '#fcba03'  # yellow

# ---------- FRAMES ----------

frame_style = ttk.Style()
frame_style.configure('upper.TFrame', background=color1)
frame_style.configure('lower.TFrame', background=color2)

upper_frame = ttk.Frame(
    root, width=310, height=140, padding=0, relief=FLAT, style='upper.TFrame'
)
lower_frame = ttk.Frame(
    root, width=310, height=260, padding=0, relief=FLAT, style='lower.TFrame'
)

# ---------- LABELS ----------

label_style = ttk.Style()
label_style.configure(
    'title.TLabel',
    background=color1,
    foreground=color4,
    font=('Arial 21 bold'),
)
label_style.configure(
    'birthday.TLabel', background=color2, foreground=color3, font=('Ivi 12')
)
label_style.configure(
    'pattern.TLabel',
    background=color2,
    foreground=color4,
    font=('Ivi 10 bold'),
)
label_style.configure(
    'numbers.TLabel',
    background=color2,
    foreground=color3,
    font=('Ivy 25 bold'),
)
label_style.configure(
    'written.TLabel',
    background=color2,
    foreground=color3,
    font=('Ivy 15 bold'),
)

title = ttk.Label(
    upper_frame,
    text='AGE CALCULATOR',
    padding=(3, 1),
    width=25,
    relief=FLAT,
    anchor=CENTER,
    style='title.TLabel',
)
birthday = ttk.Label(
    lower_frame,
    text="Birthday's date",
    padding=(0, 1),
    relief=FLAT,
    style='birthday.TLabel',
)
input_date = ttk.Entry(lower_frame, width=9, font=('Ivi 12'))
pattern = ttk.Label(
    lower_frame,
    text='(dd/mm/yyyy)',
    padding=0,
    relief=FLAT,
    style='pattern.TLabel',
)

years = ttk.Label(lower_frame, text='--', style='numbers.TLabel')
years_written = ttk.Label(lower_frame, text='years', style='written.TLabel')
months = ttk.Label(lower_frame, text='--', style='numbers.TLabel')
months_written = ttk.Label(lower_frame, text='months', style='written.TLabel')
days = ttk.Label(lower_frame, text='--', style='numbers.TLabel')
days_written = ttk.Label(lower_frame, text='days', style='written.TLabel')

# ---------- BUTTON ----------

button_style = ttk.Style()
button_style.configure('TButton', background=color2, font=('Ivi 20'))
button = Button(
    lower_frame,
    text='Calculate',
    width=20,
    activebackground=color2,
    activeforeground=color3,
    background=color2,
    foreground=color3,
    relief=RAISED,
    overrelief=SUNKEN,
    font=('Ivi 15'),
    command=calculate,
)

# ---------- PLACING THE WIDGETS ON THE SCREEN ----------

upper_frame.grid(row=0, column=0)
lower_frame.grid(row=1, column=0)
title.place(x=-50, y=50)
birthday.place(x=50, y=30)
input_date.place(x=180, y=30)
pattern.place(x=180, y=60)
years.place(x=50, y=110)
years_written.place(x=42, y=150)
months.place(x=138, y=110)
months_written.place(x=121, y=150)
days.place(x=220, y=110)
days_written.place(x=215, y=150)
button.place(x=38, y=210)

input_date.focus()
input_date.bind('<Return>', lambda event: calculate())
root.mainloop()
