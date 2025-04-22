from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")

        # title label
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)


        img_top = Image.open("Images/train.jpg")
        img_top = img_top.resize((1530,550),Image.LANCZOS)
        self.photoImg_top = ImageTk.PhotoImage(img_top)
        f_label = Label(self.root, image = self.photoImg_top)
        f_label.place(x=0, y=55, width=1530, height=325)


        b1 = Button(self.root, text="Train Data", command=self.train_classifier, cursor="hand2",font=("times new roman", 30, "bold"), bg="blue", fg="white")
        b1.place(x=0, y=380, width=1530, height=60)


        img_bottom1 = Image.open("Images/faceimg_bing.jpeg")
        img_bottom1 = img_bottom1.resize((765,345),Image.LANCZOS)
        self.photoImg_bottom1 = ImageTk.PhotoImage(img_bottom1)
        f_label = Label(self.root, image = self.photoImg_bottom1)
        f_label.place(x=0, y=440, width=765, height=345)


        img_bottom2 = Image.open("Images/robo_img_bing.jpeg")
        img_bottom2 = img_bottom2.resize((765,345),Image.LANCZOS)
        self.photoImg_bottom2 = ImageTk.PhotoImage(img_bottom2)
        f_label = Label(self.root, image = self.photoImg_bottom2)
        f_label.place(x=765, y=440, width=765, height=345)



    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L') #Convert into Gray Scale image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13
        ids = np.array(ids)

        # Train the Classifier and Save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed successfully")

            






if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.resizable(False, False)
    root.mainloop()
