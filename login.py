from ast import main
import tkinter as tk
from tkinter import *
import random
class Login(tk.Tk):

    def __init__(self):


        def verify():

            en = first_entry.get()

            list = ['1111','070','9364','9873']
            ran_list= random.choice(list)

            if '3333' in en:

                print("s")

                first_label = tk.Label(self, text = ran_list, font=('Times', 15), fg='#4A7A8C')
                first_label.pack(pady= 3, padx = 3)
                img = PhotoImage(file='icons/icon.png')

                ver_button = tk.Button(self,image=img, compound = LEFT, text='access account', font=15, bg='#4a7abc',fg='yellow', activebackground='red', activeforeground='white', command=self.destroy)
                #ver_button = tk.Button(self, image=img, command=self.destroy)
                ver_button.image = img
                #ver_button.pack(pady= 8, padx = 6)
                ver_button.pack()

        def create_acc():

            createacclabel1 = tk.Label(self, text = "Username", font=('Times', 15), fg='#4A7A8C')
            createacclabel1.pack(pady= 3, padx = 3)

            createacc1= tk.Entry(self, width = 20,fg='red',)
            createacc1.pack(padx = 7, pady = 10)

            acc = createacc1.get()

            createacclabel2 = tk.Label(self, text = 'Password', font=('Times', 15), fg='#4A7A8C')
            createacclabel2.pack(pady= 3, padx = 3)


            createacc2 = tk.Entry(self, width = 20,fg='red',)
            createacc2.pack(padx = 7, pady = 10)

            acc = createacc2.get()



            



                


        tk.Tk.__init__(self)
        self.geometry('1920x1080')
        self.title('Verify Window')
        self.configure(bg='blue')
        first_label = tk.Label(self, text = "Verify with your digit code to access the app", font=10)
        first_label.pack(pady= 2, padx = 2)
        
        #<----------------------------------------------------------------------------------------------------------->
        
        check = PhotoImage(file ='icons/protection.png')
        check_img = check.subsample(20, 20)
        first_button = tk.Button(self,image = check, text ="Verify", compound = LEFT, command = verify)
        first_button.image = check
        first_button.pack(side = TOP)
        
        #<----------------------------------------------------------------------------------------------------------->
        
        first_entry = tk.Entry(self, width = 4,fg='green',)
        first_entry.pack(padx = 7, pady = 10)
                
        #<----------------------------------------------------------------------------------------------------------->
        logout_img = PhotoImage(file='logout.png')
        second_button = tk.Button(self,image = logout_img, text="Close Window",compound = LEFT, font=15, command=self.destroy)
        second_button.image = logout_img
        second_button.pack(side = TOP)
        
        #<------------------------------------------------------------------------------------------------------------>



        create_img = PhotoImage(file='icons/icon.png')
        third_button = tk.Button(self,image = create_img, text="Create Account",compound = LEFT, font=15, command=create_acc)
        third_button.image = create_img
        third_button.pack(side = TOP)


    
app = Login()
app.mainloop()
