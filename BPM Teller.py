from tkinter import * 
window = Tk()
window.title('BPM Teller')




HighBloodP = 'Heart Pressure Is High, Lower It.'
LowBloodP = 'Heart Pressure Is Low, Raise It.'
GoodP = 'Heart Pressure Is Fine.'

def click():
    user = entry.get()
    if int(user) < 60:
        answer.config(text = LowBloodP)
    elif int(user) > 100:
        answer.config(text = HighBloodP)
    else:
        answer.config(text= GoodP)
    


# its the question in the GUI
label = Label(window, text= 'What is your BPM Number? ',font=('Arial',20,'bold'),width= 30)
label.pack()

# where your gonna write the number 
entry = Entry(window,font=('Arial', 50,'bold'), fg='black',width= 4, )
entry.pack()

# the button
button = Button(window, text='Click',font=('Arial',30,'bold'),command= click)
button.pack()

answer = Label(window, text= '',font=('Arial',20,"bold"))
answer.pack()






window.mainloop()