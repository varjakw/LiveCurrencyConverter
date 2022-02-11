import sys
import tkinter as tk
from tkinter import ttk, font

from tkinter import CENTER


class app:

    def __init__(self, master):
        self.master = master
        self.master.geometry("500x500")
        self.master.title("QR Code")
        self.menu()
        self.messagetext = None


    def menu(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = tk.Frame(self.master, width=300, height=300)
        self.frame1.pack()
        def_font = font.Font(family='MS Sans Serif')
        self.uppertext1 = tk.Label(self.frame1, text="Currency Converter", font=def_font)
        self.uppertext1.pack()
        self.convert_btn = tk.Button(self.frame1, text="Convert Currency", font=def_font, command=self.convert)
        self.convert_btn.pack()


    def convert(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = tk.Frame(self.master, width=300, height=300)
        self.frame2.pack()
        def_font = font.Font(family='MS Sans Serif')
        self.reg_txt2 = tk.Label(self.frame2, text="Please choose a conversion option", font=def_font)

       # self.message_label = tk.Label(self.frame2, text="Enter the input to encode", font=def_font)
       # self.message_label.pack(padx=20, pady=100)
       # self.message_entry = tk.Entry(font=(def_font, 25))  # width handled by place()
       # self.message_entry.place(x=120, y=140, width=250, height=40)

       # self.createQR_btn = tk.Button(self.frame2, text="Create QR", font=def_font, command=self.dostuff)
       # self.createQR_btn.pack()

        self.eurus_btn = tk.Button(self.frame2, text="€EUR -> $US", font=def_font, command=self.convert)
        self.eurgbp_btn = tk.Button(self.frame2, text="€EUR -> £GBP", font=def_font, command=self.convert)
        self.useur_btn = tk.Button(self.frame2, text="$US -> €EUR ", font=def_font, command=self.convert)
        self.usgbp_btn = tk.Button(self.frame2, text="$US -> £GBP ", font=def_font, command=self.convert)
        self.gbpeur_btn = tk.Button(self.frame2, text="£GBP -> €EUR", font=def_font, command=self.convert)
        self.gbpus_btn = tk.Button(self.frame2, text="£GBP -> $US", font=def_font, command=self.convert)
        self.menu_btn = tk.Button(self.frame2, text="Main Menu", font=def_font, command=self.menu)

        self.menu_btn.pack()
        self.reg_txt2.pack()
        self.eurus_btn.pack()
        self.eurgbp_btn.pack()
        self.useur_btn.pack()
        self.usgbp_btn.pack()
        self.gbpeur_btn.pack()
        self.gbpus_btn.pack()


    def dostuff(self):
        messagetext = self.message_entry.get()
        print("message: " + messagetext)
        generatedQR = self.generateqr(messagetext)


    def generateqr(self, messagetext):
        logo_display = Image.open('profile.jpg')
        logo_display.thumbnail((60, 60))

        qr.add_data(messagetext)
        qr.make(fit=True)

        qrImage = qr.make_image(fill_color="black", back_color="white").convert('RGB')

        logo_pos = ((qrImage.size[0] - logo_display.size[0]) // 2, (qrImage.size[1] - logo_display.size[1]) // 2)
        qrImage.paste(logo_display, logo_pos)

        qrImage.save("qrCode.png")
        image = Image.open('qrCode.png')
        image.show()
        sys.exit()



root = tk.Tk()
app(root)
root.mainloop()




