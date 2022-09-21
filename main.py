from ast import main
from re import M
import tkinter as tk
from tkinter.ttk import *
from tkinter import *
import random
import time
class Login(tk.Tk):

    def __init__(self):

        def NewWindow():
            openwindow = Toplevel(self)

            openwindow.title("Window")
            openwindow.geometry("1920x1080")


        def verify():

            en = first_entry.get()

            list = ['1111','070','9364','9873']
            ran_list= random.choice(list)

            if '3333' in en:

                print("s")

                first_label = tk.Label(self, text = ran_list, font=('Times', 15), fg='#4A7A8C')
                first_label.pack(pady= 3, padx = 3)
                img = PhotoImage(file='icons\icon.png')

                ver_button = tk.Button(self,image=img, compound = LEFT, text='Enter Account', font=15, bg='#4a7abc',fg='yellow', activebackground='red', activeforeground='white', command=self.destroy)
                #ver_button = tk.Button(self, image=img, command=self.destroy)
                ver_button.image = img
                #ver_button.pack(pady= 8, padx = 6)
                ver_button.pack()

        def new_window():


            def Stundenplan():
                print("W")
                


            self.geometry('1920x1080')
            self.title("Window")

            settings_menu = Menu(self)

            Schule = Menu(settings_menu, tearoff=0)
            settings_menu.add_cascade(label='Schule',menu= Schule)
            Schule.add_command(label="Stundenplan",command = Stundenplan)
            Schule.add_command(label="Notenspiegel",command = NONE)
            Schule.add_command(label="Gruppenchat",command = NONE)
            Schule.add_command(label="Notizen",command = NONE)
            self.config(menu = settings_menu)
            mainloop()
        def create_acc():




            def verify_reg():


                def destroy_2():
                    createacc1.destroy()
                    createacc2.destroy()
                    createacclabel1.destroy()
                    createacclabel2.destroy()
                    acc_button.destroy()
                    acc_label.destroy()

                acc1 = createacc1.get()
                acc2 = createacc2.get()
               

                if  "admin" in acc1 and "admin" in acc2:

          
                        print("YES")
                        acc_label = tk.Label(self, text = "Account created", font=('Times', 15), fg='#00FF40')
                        acc_label.pack(pady= 3, padx = 3)
                        acc_button = tk.Button(self,image=img, compound = LEFT, text='Enter Account', font=15, bg='#4a7abc',fg='yellow', activebackground='red', activeforeground='white', command=lambda: [destroy_2(), new_window()])
                        acc_button.image = img
                        acc_button.pack()
                




            createacclabel1 = tk.Label(self, text = "Username", font=('Times', 15), fg='#000000')
            createacclabel1.pack(pady= 3, padx = 3)

            createacc1= tk.Entry(self, width = 20,fg='black',)
            createacc1.pack(padx = 7, pady = 10)

            # acc1 = createacc1.get()

            createacclabel2 = tk.Label(self, text = 'Password', font=('Times', 15), fg='#000000')
            createacclabel2.pack(pady= 3, padx = 3)


            createacc2 = tk.Entry(self, width = 20,fg='black',)
            createacc2.pack(padx = 7, pady = 10)

            # acc2 = createacc2.get()
            def destroy_btn1():

                    create_button.destroy()

            img = PhotoImage(file='icons\icon.png')

            create_button = tk.Button(self,image=img, compound = LEFT, text='Create Account', font=15, bg='#4a7abc',fg='yellow', activebackground='red', activeforeground='white', command  =lambda: [destroy_1_btn(), destroy_btn1(), verify_reg()])
                #create_button = tk.Button(self, image=img, command=self.destroy)
            create_button.image = img
                #create_button.pack(pady= 8, padx = 6)
            create_button.pack()



        tk.Tk.__init__(self)
        self.geometry('1920x1080')
        self.title('Verify Window')
        self.configure(bg='white')
        def destroy_1():
            first_button.destroy()
            
            first_entry.destroy()

            first_label.destroy()

        def destroy_1_btn():
            third_button.destroy()
        
        first_label = tk.Label(self, text = "Verify with your digit code to access the app", font=10)
        first_label.pack(pady= 2, padx = 2)


        
        #<----------------------------------------------------------------------------------------------------------->
        
        check = PhotoImage(file ='icons\protection.png')
        check_img = check.subsample(20, 20)
        first_button = tk.Button(self,image = check, text ="Verify", compound = LEFT, command = verify)
        first_button.image = check
        first_button.pack(side = TOP)
        
        #<----------------------------------------------------------------------------------------------------------->
        
        first_entry = tk.Entry(self, width = 4,fg='black',)
        first_entry.pack(padx = 7, pady = 10)
                
        #<----------------------------------------------------------------------------------------------------------->
        logout_img = PhotoImage(file='icons\logout.png')
        second_button = tk.Button(self,image = logout_img, text="Close Window",compound = LEFT, font=15, command=self.destroy)
        second_button.image = logout_img
        second_button.pack(side = TOP)
        
        #<------------------------------------------------------------------------------------------------------------>



        create_img = PhotoImage(file='icons\icon.png')
        third_button = tk.Button(self,image = create_img, text="Create Account",compound = LEFT, font=15, command=lambda: [destroy_1(), create_acc()] )
        third_button.image = create_img
        third_button.pack(side = TOP)


    
app = Login()
app.mainloop()
