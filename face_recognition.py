from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
import mysql.connector
import cv2
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")

        # title label
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)


        # ============Left Image============
        img_left = Image.open("Images/face_reco_bing.jpeg")
        img_left = img_left.resize((650,700),Image.LANCZOS)
        self.photoImg_left = ImageTk.PhotoImage(img_left)
        f_label = Label(self.root, image = self.photoImg_left)
        f_label.place(x=0, y=55, width=650, height=700)

        # ==============Right Image==========
        img_right = Image.open("Images/face_recognition.jpg")
        img_right = img_right.resize((950,700),Image.LANCZOS)
        self.photoImg_right = ImageTk.PhotoImage(img_right)
        f_label = Label(self.root, image = self.photoImg_right)
        f_label.place(x=650, y=55, width=950, height=700)

        # =================Face Recognition Button==============
        b1 = Button(f_label, text="Face Recognition",command=self.face_recog, cursor="hand2",font=("times new roman", 18, "bold"), bg="darkgreen", fg="white")
        b1.place(x=375, y=620, width=200, height=40)



    # ==============Attendance Function==================
    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"{i},{r},{n},{d},{dtString},{d1},Present\n")


    # ==============Face Recognition Function==================
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x,y,w,h) in features:
                cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)
                id,predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", user="root", password="Bharat@2201010148", database="face_recognizer", auth_plugin='mysql_native_password')
                my_cursor = conn.cursor()
                
                my_cursor.execute("select Id from student where Id="+str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)
                
                my_cursor.execute("select RollNo from student where Id="+str(id))
                r = my_cursor.fetchone()
                r = "+".join(r) 

                my_cursor.execute("select Name from student where Id="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n) 


                my_cursor.execute("select Department from student where Id="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d) 



                

                if confidence>77:
                    cv2.putText(img, f"Id:{i}", (x,y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
                    cv2.putText(img, f"RollNo:{r}", (x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
                    cv2.putText(img, f"Name:{n}", (x,y-35), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
                    cv2.putText(img, f"Department:{d}", (x,y-15), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
                    self.mark_attendance(i,r,n,d)

                else:
                    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 3)
                    cv2.putText(img, "Unknown Face", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)

                    coord = [x,y,w,h]

            return coord
        
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255,25,255), "Face", clf)
            return img
        
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()





if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.resizable(False, False)
    root.mainloop()