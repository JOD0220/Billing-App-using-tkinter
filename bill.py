from tkinter import *
import math,random,os
from tkinter import messagebox 
class Bill_App:

    def __init__(self,root):

        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title = Label(self.root,text="DMART",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X) 
        #========variables========
        #========Cosmetics================================
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.hair_spray=IntVar()
        self.hair_gel=IntVar()
        self.body_lotion=IntVar()
        #========Grocery================================
        self.Rice=IntVar()
        self.food_oil=IntVar()
        self.Daal=IntVar()
        self.Wheat=IntVar()
        self.sugar=IntVar()
        self.Tea=IntVar()
        #========Drinks================================
        self.Maaza=IntVar()
        self.Coco_Cola=IntVar()
        self.Frooti=IntVar()
        self.Thumbs_Up=IntVar()
        self.Limca=IntVar()
        self.Sprite=IntVar()
        #==============================Total Price and Tax Variables =============================
        self.cosmetics_price=StringVar()
        self.grocery_price=StringVar()
        self.drinks_price=StringVar()

        self.cosmetics_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()
        #================================================Customer
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar() 
       #================================================================Customer Detail Frame
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Detail",font=("times new roman",15,"bold"),fg="gold",bg=bg_color,)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl = Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=20,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl = Label(F1,text="Phone Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=20,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10) 

        c_bill_lbl = Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=20,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10) 

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=15,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=10)

        #================================================================Cosmetics Frame
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color,)
        F2.place(x=5,y=180,width=325,height=380)

        bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Face_cream_lbl=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Face_w_lbl=Label(F2,text="Facewash",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Face_w_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Hair_s_lbl=Label(F2,text="Hair Shampoo",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Hair_s_txt=Entry(F2,width=10,textvariable=self.hair_spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Hair_g_lbl=Label(F2,text="Hair Gel",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Hair_g_txt=Entry(F2,width=10,textvariable=self.hair_gel,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Body_lbl=Label(F2,text="Body Lotion",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Body_txt=Entry(F2,width=10,textvariable=self.body_lotion,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #================================================================Grocery Frame
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg=bg_color,)
        F3.place(x=340,y=180,width=325,height=380)

        g1_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=10,textvariable=self.Rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        g2_lbl=Label(F3,text="Food Oil",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        g3_lbl=Label(F3,text="Dal",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt=Entry(F3,width=10,textvariable=self.Daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        g4_lbl=Label(F3,text="Wheat",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F3,width=10,textvariable=self.Wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        g5_lbl=Label(F3,text="Sugar",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g6_lbl=Label(F3,text="Tea",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=10,textvariable=self.Tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #================================================================Cold Drink Frame
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Drinks",font=("times new roman",15,"bold"),fg="gold",bg=bg_color,)
        F4.place(x=670,y=180,width=325,height=380)

        Mazaa_lbl=Label(F4,text="Maaza",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Mazaa_txt=Entry(F4,width=10,textvariable=self.Maaza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Cola_lbl=Label(F4,text="Coco-Cola",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Cola_txt=Entry(F4,width=10,textvariable=self.Coco_Cola,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        Frooti_lbl=Label(F4,text="Frooti",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Frooti_txt=Entry(F4,width=10,textvariable=self.Frooti,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Thumbs_Up_lbl=Label(F4,text="Thumbs Up",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Thumbs_Up_txt=Entry(F4,width=10,textvariable=self.Thumbs_Up,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Limca_lbl=Label(F4,text="Limca",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Limca_txt=Entry(F4,width=10,textvariable=self.Limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Sprite_lbl=Label(F4,text="Sprite",font=("times new roman",16,"bold"),fg="lightgreen",bg=bg_color).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Sprite_txt=Entry(F4,width=10,textvariable=self.Sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #================================================================Bill Area
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=350,height=380)
        bill_title =Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea = Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        #==============================Button Frame========================================================
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)      
        
        m1_lbl=Label(F6,text="Total Cosmetics Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetics_price,font=("arial 10 bold"),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font=("arial 10 bold"),bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text="Total Drinks Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.drinks_price,font=("arial 10 bold"),bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        
        c1_lbl=Label(F6,text="GST",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.cosmetics_tax,font=("arial 10 bold"),bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2_lbl=Label(F6,text="GST",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font=("arial 10 bold"),bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3_lbl=Label(F6,text="GST",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable=self.cold_drink_tax,font=("arial 10 bold"),bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=750,width=580,height=105)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        Bill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_F,text="Clear",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold",command=self.clear_data).grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_F,text="Exit",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold", command=self.exit).grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()

    def total(self):

        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*60
        self.c_hs_p=self.hair_spray.get()*180
        self.c_g_p=self.hair_gel.get()*140
        self.c_bl_p=self.body_lotion.get()*180

        self.total_cosmetics_price=float(
                                        self.c_s_p+
                                        self.c_fc_p+
                                        self.c_fw_p+
                                        self.c_hs_p+
                                        self.c_g_p+
                                        self.c_bl_p
                                        )
        self.cosmetics_price.set("Rs. "+str(self.total_cosmetics_price))
        self.c_tax=round((self.total_cosmetics_price*0.05),2)
        self.cosmetics_tax.set("Rs. "+str(self.c_tax))



        self.g_r_p=self.Rice.get()*40
        self.g_f_p=self.food_oil.get()*120
        self.g_d_p=self.Daal.get()*60
        self.g_w_p=self.Wheat.get()*180
        self.g_s_p=self.sugar.get()*140
        self.g_t_p=self.Tea.get()*180

        self.total_grocery_price=float(
                                    self.g_r_p+
                                    self.g_f_p+
                                    self.g_d_p+
                                    self.g_w_p+
                                    self.g_s_p+
                                    self.g_t_p
                                    )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.1),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))
        

        self.d_m_p=self.Maaza.get()*60
        self.d_c_p=self.Coco_Cola.get()*60
        self.d_f_p=self.Frooti.get()*50
        self.d_t_p=self.Thumbs_Up.get()*45
        self.d_l_p=self.Limca.get()*40
        self.d_s_p=self.Sprite.get()*60
        self.total_drinks_price=float(
                                    self.d_m_p+
                                    self.d_c_p+
                                    self.d_f_p+
                                    self.d_t_p+
                                    self.d_l_p+
                                    self.d_s_p
                                    )
        self.drinks_price.set("Rs. "+str(self.total_drinks_price))
        self.d_tax=round((self.total_drinks_price*0.05),2)     
        self.cold_drink_tax.set("Rs. "+str(self.d_tax))

        self.Total_bill=float(  self.total_cosmetics_price+     
                                self.total_grocery_price+
                                self.total_drinks_price+ 
                                self.c_tax+
                                self.g_tax+
                                self.d_tax
                            )
                                                    
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t    Welcome To DMart\n")
        self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()} ")
        self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()} ")
        self.txtarea.insert(END,f"\n Phone Number : {self.c_phon.get()} ")
        self.txtarea.insert(END,f"\n======================================")
        self.txtarea.insert(END,f"\n Products\t\tQTY\t\tPrice")
        self.txtarea.insert(END,f"\n======================================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()== "":
            messagebox.showerror("ERROR$","Customer details are must")
        elif self.cosmetics_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.drinks_price.get()=="Rs. 0.0":
            messagebox.showerror("ERROR$","No product purchased")
        else:

            self.welcome_bill()
            #==================cosmetics
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.hair_spray.get()!=0:
                self.txtarea.insert(END,f"\n Shampoo\t\t{self.hair_spray.get()}\t\t{self.c_hs_p}")
            if self.hair_gel.get()!=0:
                self.txtarea.insert(END,f"\n Hair Gel\t\t{self.hair_gel.get()}\t\t{self.c_g_p}")
            if self.body_lotion.get()!=0:
                self.txtarea.insert(END,f"\n Body Lotion\t\t{self.body_lotion.get()}\t\t{self.c_bl_p}")

            #==================Grocery
            if self.Rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice\t\t{self.Rice.get()}\t\t{self.g_r_p}")
            if self.food_oil.get()!=0:
                self.txtarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f_p}")
            if self.Daal.get()!=0:
                self.txtarea.insert(END,f"\n Daal\t\t{self.Daal.get()}\t\t{self.g_d_p}")
            if self.Wheat.get()!=0:
                self.txtarea.insert(END,f"\n Wheat\t\t{self.Wheat.get()}\t\t{self.g_w_p}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.Tea.get()!=0:
                self.txtarea.insert(END,f"\n Tea\t\t{self.Tea.get()}\t\t{self.g_t_p}")


            #==============================Drinks
            if self.Maaza.get()!=0:
                self.txtarea.insert(END,f"\n Maaza\t\t{self.Maaza.get()}\t\t{self.d_m_p}")
            if self.Coco_Cola.get()!=0:
                self.txtarea.insert(END,f"\n Coke\t\t{self.Coco_Cola.get()}\t\t{self.d_c_p}")
            if self.Frooti.get()!=0:
                self.txtarea.insert(END,f"\n Frooti\t\t{self.Frooti.get()}\t\t{self.d_f_p}")
            if self.Thumbs_Up.get()!=0:
                self.txtarea.insert(END,f"\n Thumbs Up\t\t{self.Thumbs_Up.get()}\t\t{self.d_t_p}")
            if self.Limca.get()!=0:
                self.txtarea.insert(END,f"\n Limca\t\t{self.Limca.get()}\t\t{self.d_l_p}")
            if self.Sprite.get()!=0:
                self.txtarea.insert(END,f"\n Sprite\t\t{self.Sprite.get()}\t\t{self.d_s_p}")

            self.txtarea.insert(END,f"\n--------------------------------------")
            if self.cosmetics_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n CosGST\t\t\t{self.cosmetics_tax.get()}")
            if self.grocery_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n GroGST\t\t\t{self.grocery_tax.get()}")

            if self.cold_drink_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n DriGST\t\t\t{self.cold_drink_tax.get()}") 
            
            self.txtarea.insert(END,f"\n Total Bill : \t\t\t Rs. {self.Total_bill}")
            self.txtarea.insert(END,f"\n--------------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("Bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. : {self.bill_no.get()} saved successfully")
        else:
            return
    
    def find_bill(self):
        present="no"
        for i in os.listdir("Bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"Bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)     
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")    

    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you really want to clear")
        if op>0:

            #========Cosmetics================================
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.hair_spray.set(0)
            self.hair_gel.set(0)
            self.body_lotion.set(0)
            #========Grocery================================
            self.Rice.set(0)
            self.food_oil.set(0)
            self.Daal.set(0)
            self.Wheat.set(0)
            self.sugar.set(0)
            self.Tea.set(0)
            #========Drinks================================
            self.Maaza.set(0)
            self.Coco_Cola.set(0)
            self.Frooti.set(0)
            self.Thumbs_Up.set(0)
            self.Limca.set(0)
            self.Sprite.set(0)
            #==============================Total Price and Tax Variables =============================
            self.cosmetics_price.set("")
            self.grocery_price.set("")
            self.drinks_price.set("")

            self.cosmetics_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")
            #================================================Customer
            self.c_name.set("")
            self.c_phon.set("")
            self.bill_no.set("")
            
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))  

            self.search_bill.set("")
            self.welcome_bill()
       
    def exit(self):
        op=messagebox.askyesno("Exit","Do you relly want to exit")
        if op>0:
            self.root.destroy()
        
root=Tk()
obj = Bill_App(root)
root.mainloop()