from tkinter import*
root=Tk()
root.geometry('455x500')
def student():
    print(f'{nicknamevalue.get(),clvalue.get(),yearvalue.get(),phonenumbervalue.get(),oldstudentvalue.get(),full_namevalue.get()}')

    with open('record.txt','a') as f:
         f.write(f'{nicknamevalue.get(),clvalue.get(),yearvalue.get(),phonenumbervalue.get(),oldstudentvalue.get(),full_namevalue.get()}')



Label(root,text='M.S school Form',bg='blue',fg='white',font='candara 13 bold italic',padx=10).grid(row=0,column=3)

nickname=Label(root,text='Nick Name:',font='comicsansms 10 bold italic')
full_name=Label(root,text='Full Name:',font='comicsansms 10 bold italic')
cl=Label(root,text='Class:',font='comicsansms 10 bold italic')
year=Label(root,text='Age:',font='comicsansms 10 bold italic')
phonenumber=Label(root,text='Phone number:',font='comicsansms 10 bold italic',padx=8)


nickname.grid(row=1,column=2)
full_name.grid(row=2,column=2)
cl.grid(row=3,column=2)
year.grid(row=4,column=2)
phonenumber.grid(row=5,column=2)

nicknamevalue=StringVar()
full_namevalue=StringVar()
clvalue=StringVar()
yearvalue=StringVar()
phonenumbervalue=StringVar()
oldstudentvalue=IntVar()

namentry=Entry(root,textvariable=nicknamevalue).grid(row=1,column=3)
fullname=Entry(root,textvariable=full_namevalue).grid(row=2,column=3)
clentry=Entry(root,textvariable=clvalue).grid(row=3,column=3)
yearentry=Entry(root,textvariable=yearvalue).grid(row=4,column=3)
phonenumber=Entry(root,textvariable=phonenumbervalue).grid(row=5,column=3)


Checkbutton(text='Previous student',font='comissansms 8 bold',variable=oldstudentvalue).grid(row=6,column=3)
button=Button(text='submit',bg='red',command=student).grid(row=7,column=7)

root.mainloop()
