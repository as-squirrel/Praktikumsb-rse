from tkinter import ttk
import tkinter as tk
from tkinter.ttk import *
from tkinter import *
import random
import time
class Window(tk.Tk):
    def __init__(self):

        tk.Tk.__init__(self)

        self.title('Login self')
        self.configure(bg='#424242')
        self.geometry("1920x1080")
        def destroy_1():
                first_button.destroy()
                    
                first_entry.destroy()

                first_label.destroy()

        def destroy_1_btn():
            third_button.destroy()

        def Mathematik():
                file_path = 'files/data.txt'
                with open(file_path) as file:
                        read = file.read()
                        createacclabel1 = ttk.Label(self, text = read)
                        createacclabel1.pack(pady= 3, padx = 3)


        def account():

                account_button1 = ttk.Button(self,text='Mathematik',  command=Mathematik)
                account_button1.place(x = 200, y= 100, width=100)
                account_button2 = ttk.Button(self,text='Deutsch',  command=NONE)
                account_button2.place(x = 200, y= 130, width=100)
                account_button3 = ttk.Button(self,text='Sport',  command=NONE)
                account_button3.place(x = 200, y= 160, width=100)
                account_button4 = ttk.Button(self,text='Ethik',  command=NONE)
                account_button4.place(x = 200, y= 190, width=100)
                account_button5 = ttk.Button(self,text='Englisch',  command=NONE)
                account_button5.place(x = 200, y= 220, width=100)






        def verify():

            en = first_entry.get()

            list = ['1111','070','9364','9873']
            ran_list= random.choice(list)

            if '3333' in en:

                print("s")

                    
                first_label = tk.Label(self, text = ran_list, font=('Times', 15), fg='#4A7A8C')
                first_label.pack(pady= 3, padx = 3)
                img = PhotoImage(file='icons/icon.png')

                ver_button = tk.Button(self,image=img, compound = LEFT, text='Enter Account', font=15, bg='#4a7abc',fg='yellow', activebackground='red', activeforeground='white', command=self.destroy)
                        #ver_button = tk.Button(self, image=img, command=self.destroy)
                ver_button.image = img
                        #ver_button.pack(pady= 8, padx = 6)
                ver_button.pack()

        #def main_self():
            win = ThemedTk(theme="blue")
            win.title('Login ')
            win.configure(bg='grey')


            win.mainloop()

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
                            acc_button = ttk.Button(self, text='Enter Account',  command=lambda: [destroy_2(), account()])
                            acc_button.pack()
                        




            createacclabel1 = ttk.Label(self, text = "Username")
            createacclabel1.pack(pady= 3, padx = 3)

            createacc1= ttk.Entry(self, width = 20)
            createacc1.pack(padx = 7, pady = 10)

                    # acc1 = createacc1.get()

            createacclabel2 = ttk.Label(self, text = 'Password')
            createacclabel2.pack(pady= 3, padx = 3)


            createacc2 = ttk.Entry(self, width = 20)
            createacc2.pack(padx = 7, pady = 10)

                    # acc2 = createacc2.get()
            def destroy_btn1():

                create_button.destroy()

            create_button = ttk.Button(self,text='Create Account', command  =lambda: [destroy_1_btn(), destroy_btn1(), verify_reg()])
                        #create_button = tk.Button(self, image=img, command=self.destroy)
                        #create_button.pack(pady= 8, padx = 6)
            create_button.pack()




                
            
        first_label = ttk.Label(self, text = "Verify with your digit code to access the app",font=("Microsoft"))
        first_label.pack(pady= 2, padx = 2)


                
                #<----------------------------------------------------------------------------------------------------------->
                
        check = PhotoImage(file ='icons/protection.png')
        check_img = check.subsample(20, 20)
        first_button = ttk.Button(self,image = check, text ="Verify", compound = LEFT, command = verify)
        first_button.image = check
        first_button.pack(side = TOP)
                
                #<----------------------------------------------------------------------------------------------------------->
                
        first_entry = ttk.Entry(self, width = 4)
        first_entry.pack(padx = 7, pady = 10)
                        
                #<----------------------------------------------------------------------------------------------------------->
        second_button = ttk.Button(self,text="Close self", command=self.destroy)
        second_button.pack(side = TOP)
        second_button.place(x = 1500, y= 50, width=150)

                
                #<------------------------------------------------------------------------------------------------------------>

        img_label = PhotoImage(file='icons/background.png')
        imglabel = ttk.Label(image=img_label).place(x=50,y=250)
        #imglabel.pack()


        #create_img = PhotoImage(file='icons/icon.png')
        third_button = ttk.Button(self, text="Create Account",command=lambda: [destroy_1(),destroy_1_btn(),create_acc()] )
        third_button.pack(side = TOP)
appid = Window()
appid.mainloop()
