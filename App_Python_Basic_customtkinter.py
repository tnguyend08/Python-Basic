import customtkinter
import tkinter

# custom giao dien
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# tuy chinh cua so lua chon 1
menu = customtkinter.CTk()
menu.title("Code test 4")
menu.geometry("230x350")
menu.resizable(width = False, height = False)

#hàm tổng
def Phep_tinh_2_so(): 
    menu.destroy()
    a = customtkinter.set_appearance_mode("dark")
    a = customtkinter.CTk()
    a.title("Tính 2 số")
    a.geometry("300x250")
    a.resizable(height=False, width=False)

    label1 = customtkinter.CTkLabel(a, text="Nhập số thứ nhất:", font=("Times New Roman",15))
    label1.place(relx= 0.05, rely = 0.1)
    entry1 = customtkinter.CTkEntry(a, height=30, width=150)
    entry1.place(relx=0.7, rely= 0.17,anchor = tkinter.CENTER)

    label2 = customtkinter.CTkLabel(a, text="Nhập số thứ hai:", font=("Times New Roman",15))
    label2.place(relx= 0.05, rely = 0.3)
    entry2 = customtkinter.CTkEntry(a, height=30, width=150)
    entry2.place(relx=0.7, rely= 0.37,anchor = tkinter.CENTER)   

    #Tạo hộp chọn Combobox
    label3 = customtkinter.CTkLabel(a, text="Nhập phép tính:", font=("Times New Roman",15))
    label3.place(relx= 0.05, rely = 0.5)

    variable_box = customtkinter.StringVar(value="Chọn phép tính")
    combo = customtkinter.CTkComboBox(a, values=['+', '-', 'x', '÷'], variable=variable_box)
    combo.place(relx = 0.45, rely = 0.5)

    # ham tinh toán
    def tong():
        label4 = customtkinter.CTkLabel(a, text="Tổng 2 số là: " + str(float(entry1.get())+float(entry2.get())) + "                                             ", font=("Times New Roman",15),bg_color="#242424")
        label4.place(relx= 0.05, rely = 0.84)    
        return
    def hieu():
        label4 = customtkinter.CTkLabel(a, text="Hiệu 2 số là: " + str(float(entry1.get())-float(entry2.get())) + "                                             ", font=("Times New Roman",15),bg_color="#242424")
        label4.place(relx= 0.05, rely = 0.84)    
        return
    def nhan():
        label4 = customtkinter.CTkLabel(a, text="Tích 2 số là: " + str(float(entry1.get())*float(entry2.get())) + "                                             ", font=("Times New Roman",15),bg_color="#242424")
        label4.place(relx= 0.05, rely = 0.84)    
    def chia():
        label4 = customtkinter.CTkLabel(a, text="Tích 2 số là: " + str(float(entry1.get())/float(entry2.get())) + "                                             ", font=("Times New Roman",15),bg_color="#242424")
        label4.place(relx= 0.05, rely = 0.84)    

    def phep_tinh():
        if combo.get() == "+":
            return tong()
        elif combo.get() == "-":
            return hieu()
        elif combo.get() == "x":
            return nhan()
        elif combo.get() == "÷":
            return chia()
        else:
            return

    button = customtkinter.CTkButton(a, text="Tính", font=("Times New Roman",15), command=phep_tinh)
    button.place(relx=0.5, rely = 0.75, anchor = tkinter.CENTER)

    a.mainloop()
    return

# hàm snt
def so_nguyen_to():
    menu.destroy()
    b = customtkinter.set_appearance_mode("dark")
    b = customtkinter.CTk()
    b.title("xác định số nguyên tố")
    b.geometry("300x200")
    b.resizable(height=False, width=False)

    label1 = customtkinter.CTkLabel(b, text="Nhập số cần xác định:", font=("Times New Roman",15))
    label1.place(relx= 0.05, rely = 0.1)

    entry1 = customtkinter.CTkEntry(b, height=30, width=120)
    entry1.place(relx=0.73, rely= 0.17,anchor = tkinter.CENTER)  

    def snt():
        if float(entry1.get())<2:
            label2 = customtkinter.CTkLabel(b, text="Số " + entry1.get() + " không phải số nguyên tố"+"                                             ", font=("Times New Roman",15),bg_color="#242424")
            label2.place(relx= 0.05, rely = 0.69)
        elif float(entry1.get())%1==0:
            sntt = int(entry1.get())
            c = 0
            for i in range(2,sntt):
                if sntt%i==0:
                    c = 1
                    label2 = customtkinter.CTkLabel(b, text="Số " + entry1.get() + " không phải số nguyên tố"+"                                             ", font=("Times New Roman",15),bg_color="#242424")
                    label2.place(relx= 0.05, rely = 0.69)
                    return
            if c == 0:
                label2 = customtkinter.CTkLabel(b, text="Số " + entry1.get() + " là số nguyên tố"+"                                             ", font=("Times New Roman",15),bg_color="#242424")
                label2.place(relx= 0.05, rely = 0.69)
                return    
        else:
            label2 = customtkinter.CTkLabel(b, text="Số " + entry1.get() + " không phải số nguyên tố"+"                                             ", font=("Times New Roman",15),bg_color="#242424")
            label2.place(relx= 0.05, rely = 0.69)
        return
       
    button = customtkinter.CTkButton(b, text="Xác định", font=("Times New Roman",15), command=snt)
    button.place(relx=0.5, rely = 0.5, anchor = tkinter.CENTER)

    b.mainloop()  

# hàm UCLN
def ucln():
    menu.destroy()
    c = customtkinter.set_appearance_mode("dark")
    c = customtkinter.CTk()
    c.title("Tìm ƯCLN")
    c.geometry("300x200")
    c.resizable(height=False, width=False)

    label1 = customtkinter.CTkLabel(c, text="Nhập số N thứ nhất:", font=("Times New Roman",15))
    label1.place(relx= 0.05, rely = 0.1)
    entry1 = customtkinter.CTkEntry(c, height=30, width=150)
    entry1.place(relx=0.725, rely= 0.17,anchor = tkinter.CENTER)

    label2 = customtkinter.CTkLabel(c, text="Nhập số N thứ hai:", font=("Times New Roman",15))
    label2.place(relx= 0.05, rely = 0.3)
    entry2 = customtkinter.CTkEntry(c, height=30, width=150)
    entry2.place(relx=0.725, rely= 0.37,anchor = tkinter.CENTER)

    def ham_xd_ucln():
        a1 = float(entry1.get())
        a2 = float(entry1.get())
        b1 = float(entry2.get())
        b2 = float(entry2.get())
        if a1%1 == 0 and b1%1 == 0:
            while a1 and b1 >0:
                if a1 == b1:
                    label3 = customtkinter.CTkLabel(c, text="ƯCLN của " + str(int(a2)) + " và " + str(int(b2)) + " là: " + str(int(a1)) + "                                            ", font=("Times New Roman",15),bg_color="#242424")
                    label3.place(relx= 0.05, rely = 0.74)
                    break 
                elif a1 > b1:
                    a1 -= b1
                elif b1 > a1:
                    b1 -= a1
        return

    button = customtkinter.CTkButton(c, text="Xác định", font=("Times New Roman",15), command=ham_xd_ucln)
    button.place(relx=0.5, rely = 0.6, anchor = tkinter.CENTER)

    c.mainloop()

    return

# hàm BCNN
def bcnn():
    menu.destroy()
    d = customtkinter.set_appearance_mode("dark")
    d = customtkinter.CTk()
    d.title("Tìm BCNN")
    d.geometry("300x200")
    d.resizable(height=False, width=False)

    label1 = customtkinter.CTkLabel(d, text="Nhập số N thứ nhất:", font=("Times New Roman",15))
    label1.place(relx= 0.05, rely = 0.1)
    entry1 = customtkinter.CTkEntry(d, height=30, width=150)
    entry1.place(relx=0.725, rely= 0.17,anchor = tkinter.CENTER)

    label2 = customtkinter.CTkLabel(d, text="Nhập số N thứ hai:", font=("Times New Roman",15))
    label2.place(relx= 0.05, rely = 0.3)
    entry2 = customtkinter.CTkEntry(d, height=30, width=150)
    entry2.place(relx=0.725, rely= 0.37,anchor = tkinter.CENTER)

    def ham_xd_bcnn():
        a1 = float(entry1.get())
        a2 = float(entry1.get())
        b1 = float(entry2.get())
        b2 = float(entry2.get())
        #code xd ucln
        if a1%1 == 0 and b1%1 == 0:
            while a1 and b1 >0:
                if a1 == b1:
                    break 
                elif a1 > b1:
                    a1 -= b1
                elif b1 > a1:
                    b1 -= a1
        label3 = customtkinter.CTkLabel(d, text="BCNN của " + str(int(a2)) + " và " + str(int(b2)) + " là: " + str(int((a2*b2)/a1)) + "                                            ", font=("Times New Roman",15),bg_color="#242424")
        label3.place(relx= 0.05, rely = 0.74)
   
        return

    button = customtkinter.CTkButton(d, text="Xác định", font=("Times New Roman",15), command=ham_xd_bcnn)
    button.place(relx=0.5, rely = 0.6, anchor = tkinter.CENTER)

    d.mainloop()


label = customtkinter.CTkLabel(menu, text="MENU", font=("Times New Roman",23))
label.place(relx = 0.5, rely = 0.15, anchor = tkinter.CENTER)

# button của tính 2 số
button1 = customtkinter.CTkButton(menu, text = "Tính 2 số", font=("Times New Roman", 15), command=Phep_tinh_2_so)
button1.place(relx=0.5, rely = 0.3, anchor = tkinter.CENTER)

# button của xác định số nguyên tố
button2 = customtkinter.CTkButton(menu, text = "Xác định số nguyên tố", font=("Times New Roman", 15), command=so_nguyen_to)
button2.place(relx=0.5, rely = 0.45, anchor = tkinter.CENTER)

# button tìm UCLN
button3 = customtkinter.CTkButton(menu, text = "Tìm ƯCLN", font=("Times New Roman", 15), command=ucln)
button3.place(relx=0.5, rely = 0.6, anchor = tkinter.CENTER)

# button tìm BCNN
button3 = customtkinter.CTkButton(menu, text = "Tìm BCNN", font=("Times New Roman", 15), command=bcnn)
button3.place(relx=0.5, rely = 0.75, anchor = tkinter.CENTER)

menu.mainloop()
