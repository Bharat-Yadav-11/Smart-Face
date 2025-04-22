from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1510x790+0+0")
        self.root.title("Developer")

        # title label
        title_lbl = Label(self.root,text="DEVELOPER", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1500, height=45)

        img1 = Image.open("Images/developer2.jpeg")
        img1 = img1.resize((1510,800),Image.LANCZOS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        f_label = Label(self.root, image = self.photoImg1)
        f_label.place(x=0, y=55, width=1510, height=800)

        # Developer info
        dev_lbl = Label(f_label, text="codeindia2023@gmail.com", font=("times new roman", 25, "bold"), bg="black", fg="blue")
        dev_lbl.place(x=600, y=150)







if __name__=="__main__":
    root = Tk()
    obj = Developer(root)
    root.resizable(False, False)
    root.mainloop()