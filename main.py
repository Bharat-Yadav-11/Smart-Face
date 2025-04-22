from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from chatbot import ChatBot
from attendance import Attendance
from developer import Developer


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")
        self.root.configure(bg='#2E2E2E')  # Dark mode background color
        
        # Colors for Dark Mode
        self.bg_color = '#2E2E2E'
        self.fg_color = '#FFFFFF'
        self.button_color = '#1F3B5C'
        self.hover_color = '#3A5C8D'

        # First image
        img = Image.open("Images/face2.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoImg = ImageTk.PhotoImage(img)
        f_label = Label(self.root, image=self.photoImg)
        f_label.place(x=0, y=0, width=500, height=130)

        # Second image
        img1 = Image.open("Images/face2.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        f_label = Label(self.root, image=self.photoImg1)
        f_label.place(x=500, y=0, width=500, height=130)

        # Third image
        img2 = Image.open("Images/face2.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoImg2 = ImageTk.PhotoImage(img2)
        f_label = Label(self.root, image=self.photoImg2)
        f_label.place(x=1000, y=0, width=500, height=130)

        # Background Image
        img3 = Image.open("Images/face_reco_bing.jpeg")
        img3 = img3.resize((1510, 710), Image.LANCZOS)
        self.photoImg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoImg3)
        bg_img.place(x=0, y=140, width=1510, height=710)

        # Title Label with Hinglish Flavor
        title_lbl = Label(bg_img, text="Face Recognition Attendance System Software", font=("times new roman", 35, "bold"), bg=self.bg_color, fg="red")
        title_lbl.place(x=0, y=0, width=1510, height=45)

        # Student Detail Button
        img4 = Image.open("Images/Student_Details.jpg")
        img4 = img4.resize((220, 220), Image.LANCZOS)
        self.photoImg4 = ImageTk.PhotoImage(img4)
        b1 = Button(bg_img, command=self.student_details, image=self.photoImg4, cursor="hand2", bd=0, relief="solid", bg=self.button_color)
        b1.place(x=200, y=100, width=220, height=220)

        b1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg=self.button_color, fg="white", relief="solid")
        b1.place(x=200, y=300, width=220, height=40)

        # Detect Face Button
        img5 = Image.open("Images/Face_Recognition.png")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoImg5 = ImageTk.PhotoImage(img5)
        b1 = Button(bg_img, image=self.photoImg5, command=self.face_data, cursor="hand2", bd=0, relief="solid", bg=self.button_color)
        b1.place(x=500, y=100, width=220, height=220)

        b1 = Button(bg_img, text="Face Detector", command=self.face_data, cursor="hand2", font=("times new roman", 15, "bold"), bg=self.button_color, fg="white", relief="solid")
        b1.place(x=500, y=300, width=220, height=40)

        # Attendance Button
        img6 = Image.open("Images/Attendance.png")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoImg6 = ImageTk.PhotoImage(img6)
        b1 = Button(bg_img, image=self.photoImg6, command=self.attendance_data, cursor="hand2", bd=0, relief="solid", bg=self.button_color)
        b1.place(x=800, y=100, width=220, height=220)

        b1 = Button(bg_img, text="Attendance", command=self.attendance_data, cursor="hand2", font=("times new roman", 15, "bold"), bg=self.button_color, fg="white", relief="solid")
        b1.place(x=800, y=300, width=220, height=40)

        # Help Button
        img7 = Image.open("Images/Chatbot2.jpeg")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoImg7 = ImageTk.PhotoImage(img7)
        b1 = Button(bg_img, image=self.photoImg7, command=self.chatbot, cursor="hand2", bd=0, relief="solid", bg=self.button_color)
        b1.place(x=1100, y=100, width=220, height=220)

        b1 = Button(bg_img, text="Help Desk", command=self.chatbot, cursor="hand2", font=("times new roman", 15, "bold"), bg=self.button_color, fg="white", relief="solid")
        b1.place(x=1100, y=300, width=220, height=40)

        # Train Face Button
        img8 = Image.open("Images/faceimg_bing.jpeg")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoImg8 = ImageTk.PhotoImage(img8)
        b1 = Button(bg_img, image=self.photoImg8, command=self.train_data, cursor="hand2", bd=0, relief="solid", bg=self.button_color)
        b1.place(x=200, y=380, width=220, height=220)

        b1 = Button(bg_img, text="Train Data", command=self.train_data, cursor="hand2", font=("times new roman", 15, "bold"), bg=self.button_color, fg="white", relief="solid")
        b1.place(x=200, y=580, width=220, height=40)

        # Photos Button
        img9 = Image.open("Images/Photos.png")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoImg9 = ImageTk.PhotoImage(img9)
        b1 = Button(bg_img, image=self.photoImg9, command=self.open_img, cursor="hand2", bd=0, relief="solid", bg=self.button_color)
        b1.place(x=500, y=380, width=220, height=220)

        b1 = Button(bg_img, text="Photos", command=self.open_img, cursor="hand2", font=("times new roman", 15, "bold"), bg=self.button_color, fg="white", relief="solid")
        b1.place(x=500, y=580, width=220, height=40)

        # Developer Button
        img10 = Image.open("Images/Developer_Img.png")
        img10 = img10.resize((220, 220), Image.LANCZOS)
        self.photoImg10 = ImageTk.PhotoImage(img10)
        b1 = Button(bg_img, image=self.photoImg10, command=self.developer_data, cursor="hand2", bd=0, relief="solid", bg=self.button_color)
        b1.place(x=800, y=380, width=220, height=220)

        b1 = Button(bg_img, text="Developer", command=self.developer_data, cursor="hand2", font=("times new roman", 15, "bold"), bg=self.button_color, fg="white", relief="solid")
        b1.place(x=800, y=580, width=220, height=40)

        # Exit Button
        img11 = Image.open("Images/Exit Image.png")
        img11 = img11.resize((220, 220), Image.LANCZOS)
        self.photoImg11 = ImageTk.PhotoImage(img11)
        b1 = Button(bg_img, image=self.photoImg11, command=self.exit, cursor="hand2", bd=0, relief="solid", bg=self.button_color)
        b1.place(x=1100, y=380, width=220, height=220)

        b1 = Button(bg_img, text="Exit", command=self.exit, cursor="hand2", font=("times new roman", 15, "bold"), bg=self.button_color, fg="white", relief="solid")
        b1.place(x=1100, y=580, width=220, height=40)

        # Adding a little animation
        self.animate_buttons()

    def open_img(self):
        os.startfile("data")

    # Function buttons with Hinglish touch
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def chatbot(self):
        self.new_window = Toplevel(self.root)
        self.app = ChatBot(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def exit(self):
        self.root.destroy()

    # Adding animation to buttons
    def animate_buttons(self):
        def hover_in(button, color):
            button.config(bg=color)

        def hover_out(button):
            button.config(bg=self.button_color)

        # Buttons hover animation
        all_buttons = [*self.root.winfo_children()]
        for button in all_buttons:
            if isinstance(button, Button):
                button.bind("<Enter>", lambda e, button=button: hover_in(button, self.hover_color))
                button.bind("<Leave>", lambda e, button=button: hover_out(button))
    

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.resizable(False, False)
    root.mainloop()
