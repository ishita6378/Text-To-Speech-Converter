import pyttsx3
from tkinter import *
text=StringVar
root = Tk()
root.geometry("645x450")
f1 = Frame(root,bg="Black")
f1.grid()
instruction_img = PhotoImage(file = r"C:\Users\ishit\Downloads\text.png")
instruction_img_main = instruction_img.subsample(1,1)
instruction_label = Label(f1,image=instruction_img_main)
instruction_label.grid(row=1,column=0)
def speak(text,gender):
    engine = pyttsx3.init('sapi5')
    voice = engine.getProperty('voices')  # not important
    engine.setProperty("voice", voice[gender].id)  # not important
    engine.say(text)
    engine.runAndWait()
def male_button():
    speak(s1.get(),0)
def female_button():
    speak(s1.get(),1)
a=StringVar()
a.set("  ")
L1=Label(f1,text="YOUR MESSAGE")
L1.grid(row=2,column=0)
s1=Entry(f1,textvariable=a)
s1.grid(row=2,column=1,ipadx=100)
img_male= PhotoImage(file=r"C:\Users\ishit\Downloads\male.png")
img_male_main = img_male.subsample(8,8)
b1 = Button(f1,text = "MALE",command=male_button,image=img_male_main)
b1.grid(row=3,column=0)
img_female = PhotoImage(file=r"C:\Users\ishit\Downloads\female.png")
img_female_main = img_female.subsample(10,10)
b2 = Button(f1,text = "FEMALE",command=female_button,image=img_female_main)
b2.grid(row=4,column=0)
root.mainloop()