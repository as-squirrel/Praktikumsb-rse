from tkinter import ttk
import tkinter as tk
from tkinter.ttk import *
from tkinter import *
import random
from cgitb import text
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.themes import *

class Window(tk.Tk):
    def __init__(self):

        tk.Tk.__init__(self)

        self.title('Login self')
        self.configure(bg='#424242')
        self.geometry("1920x1080")


        Labelframe1 = ttk.LabelFrame(padding=10, width= 700,bootstyle="primary")
        Labelframe1.pack(ipadx=10, ipady=20, expand= False, fill= BOTH)




        #Labelframe1.pack()

        def delete_labelframe1():
            Labelframe1.destroy()

        def destroy_1():
                first_button.destroy()
                    
                first_entry.destroy()

                #first_label.destroy()

        def destroy_1_btn():
            third_button.destroy()

        def Bewerbungen():
                ttk.Meter(bootstyle="success",subtextstyle="warning").pack()

        def Noten():
            print("s")

        def Notizen():
            print("")

        def Kontakte():
            print("a")

        def Profil_bearbeiten():
            print("g")

        def Account():

            Labelframe2 = ttk.LabelFrame(padding=10, width= 500, height= 500,bootstyle="warning")
            Labelframe2.pack(ipadx=30, ipady=30, expand= False, fill= BOTH)

            accountmenu1 = ttk.Label(Labelframe2, text = "a",bootstyle="primary")
            accountmenu1.pack(pady= 3, padx = 3)
        def Settings():

            print("a")


        def gui1():


                account_button6 = ttk.Button(self,text='Account',bootstyle="warning-outline",  command=profile1)
                account_button6.place(x = 100, y= 40, width=100)
                account_button7 = ttk.Button(self,text='Settings',bootstyle="warning-outline",  command=Settings)
                account_button7.place(x = 100, y= 10, width=100)



        def profile1():
            account_button1 = ttk.Button(self,text='Bewerbungen',  command=Bewerbungen)
            account_button1.place(x = 200, y= 70, width=100)
            account_button2 = ttk.Button(self,text='Noten',  command=NONE)
            account_button2.place(x = 200, y= 100, width=100)
            account_button3 = ttk.Button(self,text='Notizen',  command=NONE)
            account_button3.place(x = 200, y= 130, width=100)
            account_button4 = ttk.Button(self,text='Kontakte',  command=NONE)
            account_button4.place(x = 200, y= 160, width=100)
            account_button5 = ttk.Button(self,text='bearbeiten',  command=NONE)
            account_button5.place(x = 200, y= 190, width=100)



        def suche():

            search_entry1 = ttk.Entry(Labelframe1, width = 20,bootstyle="primary")
            search_entry1.pack(padx = 7, pady = 10)

            search_btn1 = ttk.Button(self,text='Finden',bootstyle="warning-outline",  command=Settings)
            search_btn1.place(x = 1030, y= 35, width=70)



        def verify():

            en = first_entry.get()

            list = ['1111','070','9364','9873']
            ran_list= random.choice(list)

            if '3333' in en:

                print("s")

                    
                first_label = tk.Label(self, text = ran_list, font=('Times', 15), fg='#4A7A8C')
                first_label.pack(pady= 3, padx = 3)

                ver_button = tk.Button(self, compound = LEFT, text='Enter Account', font=15, bg='#4a7abc',fg='yellow', activebackground='red', activeforeground='white', command=self.destroy)
                ver_button.pack()




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
                            acc_label = ttk.Label(self, text = "Account created",)
                            acc_label.pack(pady= 3, padx = 3)
                            acc_button = ttk.Button(self, text='Enter Account',  command=lambda: [destroy_2(),delete_labelframe1 ,gui1(),suche()])
                            acc_button.pack()
                        


            createacclabel1 = ttk.Label(Labelframe1, text = "Username",bootstyle="primary")
            createacclabel1.pack(pady= 3, padx = 3)

            createacc1= ttk.Entry(Labelframe1, width = 20,bootstyle="primary")
            createacc1.pack(padx = 7, pady = 10)



            createacclabel2 = ttk.Label(Labelframe1, text = 'Password',bootstyle="primary")
            createacclabel2.pack(pady= 3, padx = 3)


            createacc2 = ttk.Entry(Labelframe1, width = 20,bootstyle="primary")
            createacc2.pack(padx = 7, pady = 10)

            def destroy_btn1():

                create_button.destroy()

            create_button = ttk.Button(Labelframe1,text='Create Account', command  =lambda: [destroy_1_btn(), destroy_btn1(), verify_reg()])
            create_button.pack()





            
        #first_label = ttk.Label(self, text = "Verify with your digit code to access the app",font=("Microsoft"))
        #first_label.pack(pady= 2, padx = 2)


                
                #<----------------------------------------------------------------------------------------------------------->
                
        first_button = ttk.Button(self, text ="Verify",bootstyle="success-outline", compound = LEFT, command = verify)
        first_button.pack(side = TOP)
                
                #<----------------------------------------------------------------------------------------------------------->
                
        first_entry = ttk.Entry(self, width = 4)
        first_entry.pack(padx = 7, pady = 10)
                        
                #<----------------------------------------------------------------------------------------------------------->
        second_button = ttk.Button(self,text="Close Window", command=self.destroy)
        second_button.pack(side = TOP)
        second_button.place(x = 1300, y= 20, width=100)


                
                #<------------------------------------------------------------------------------------------------------------>


        def delete_labelframe1():
            Labelframe1.destroy()

        third_button = ttk.Button(Labelframe1, text="Create Account", bootstyle="info-outline",command=lambda: [destroy_1(),destroy_1_btn(),create_acc()] )
        third_button.pack(side = TOP)
appid = Window()
appid.mainloop()
