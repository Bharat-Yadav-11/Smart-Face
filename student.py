from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")

        # Variables
        self.var_name = StringVar()
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_sem = StringVar()
        self.var_year = StringVar()
        self.var_id = StringVar()
        self.var_roll = StringVar()
        self.var_div = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_tName = StringVar()

        # first image
        img = Image.open("Images/face2.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoImg = ImageTk.PhotoImage(img)
        f_label = Label(self.root, image=self.photoImg)
        f_label.place(x=0, y=0, width=500, height=130)
        # f_label.pack(fill=X)

        # second image
        img1 = Image.open("Images/face2.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        f_label = Label(self.root, image=self.photoImg1)
        f_label.place(x=500, y=0, width=500, height=130)

        # third image
        img2 = Image.open("Images/face2.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoImg2 = ImageTk.PhotoImage(img2)
        f_label = Label(self.root, image=self.photoImg2)
        f_label.place(x=1000, y=0, width=500, height=130)

        # background image
        img3 = Image.open("Images/face2.jpg")
        img3 = img3.resize((1510, 710), Image.LANCZOS)
        self.photoImg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoImg3)
        bg_img.place(x=0, y=140, width=1510, height=710)

        # title label
        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=(
            "times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1510, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=7, y=55, width=1480, height=580)

        # Left Label Frame
        left_Frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text="Student Details", font=("times new roman", 12, "bold"))
        left_Frame.place(x=10, y=10, width=720, height=550)

        img_left = Image.open("Images/face2.jpg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoImg_left = ImageTk.PhotoImage(img_left)
        f_label = Label(left_Frame, image=self.photoImg_left)
        f_label.place(x=0, y=0, width=720, height=130)

        # Current Course
        current_course_frame = LabelFrame(left_Frame, bd=2, bg="white", relief=RIDGE,
                                          text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=130, width=705, height=110)

        # Department Label
        dep_label = Label(current_course_frame, background="white",
                          text="Department", font=("times new roman", 12, "bold"))
        dep_label.grid(row=0, column=0, padx=10)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=(
            "times new roman", 10, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department", "Computer",
                               "IT", "Civil", "Mechanical", "Chemical", "Aerospace")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course Label
        course_label = Label(current_course_frame, background="white",
                             text="Course", font=("times new roman", 12, "bold"))
        course_label.grid(row=0, column=2, padx=10)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=(
            "times new roman", 10, "bold"), state="readonly")
        course_combo["values"] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year Label
        year_label = Label(current_course_frame, background="white",
                           text="Year", font=("times new roman", 12, "bold"))
        year_label.grid(row=1, column=0, padx=10)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=(
            "times new roman", 10, "bold"), state="readonly")
        year_combo["values"] = ("Select Year", "2022-23",
                                "2023-24", "2024-25", "2025-26")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester Label
        sem_label = Label(current_course_frame, background="white",
                          text="Semester", font=("times new roman", 12, "bold"))
        sem_label.grid(row=1, column=2, padx=10)

        sem_combo = ttk.Combobox(current_course_frame, textvariable=self.var_sem, font=(
            "times new roman", 10, "bold"), state="readonly")
        sem_combo["values"] = ("Select Semester", "Sem-1", "Sem-2")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class Student Information
        class_student_frame = LabelFrame(left_Frame, bd=2, bg="white", relief=RIDGE,
                                         text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=240, width=705, height=285)

        # StudentId Label
        studentId_label = Label(class_student_frame, background="white",
                                text="StudentID:", font=("times new roman", 12, "bold"))
        studentId_label.grid(row=0, column=0, padx=10, sticky=W)

        studentId_Entry = ttk.Entry(class_student_frame, textvariable=self.var_id, width=20, font=(
            "times new roman", 12, "bold"))
        studentId_Entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name Label
        studentName_label = Label(class_student_frame, background="white",
                                  text="Student Name:", font=("times new roman", 12, "bold"))
        studentName_label.grid(row=0, column=2, padx=10, sticky=W)

        studentName_Entry = ttk.Entry(
            class_student_frame, textvariable=self.var_name, width=20, font=("times new roman", 12, "bold"))
        studentName_Entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class division Label
        class_div_label = Label(class_student_frame, background="white",
                                text="Class Divison:", font=("times new roman", 12, "bold"))
        class_div_label.grid(row=1, column=0, padx=10, sticky=W)

        class_div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div, font=(
            "times new roman", 10, "bold"), state="readonly")
        class_div_combo["values"] = ("Select Division", "A", "B", "C", "D")
        class_div_combo.current(0)
        class_div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll No label
        rollNo_label = Label(class_student_frame, background="white",
                             text="Roll No:", font=("times new roman", 12, "bold"))
        rollNo_label.grid(row=1, column=2, padx=10, sticky=W)

        rollNo_Entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=20, font=(
            "times new roman", 12, "bold"))
        rollNo_Entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender label
        gender_label = Label(class_student_frame, background="white",
                             text="Gender:", font=("times new roman", 12, "bold"))
        gender_label.grid(row=2, column=0, padx=10, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=(
            "times new roman", 10, "bold"), state="readonly")
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Others")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # DOB label
        dob_label = Label(class_student_frame, background="white",
                          text="DOB:", font=("times new roman", 12, "bold"))
        dob_label.grid(row=2, column=2, padx=10, sticky=W)

        dob_Entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=(
            "times new roman", 12, "bold"))
        dob_Entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email label
        email_label = Label(class_student_frame, background="white",
                            text="Email:", font=("times new roman", 12, "bold"))
        email_label.grid(row=3, column=0, padx=10, sticky=W)

        email_Entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=(
            "times new roman", 12, "bold"))
        email_Entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # PhoneNo Label
        phoneNo_label = Label(class_student_frame, background="white",
                              text="Phone No:", font=("times new roman", 12, "bold"))
        phoneNo_label.grid(row=3, column=2, padx=10, sticky=W)

        phoneNo_Entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=(
            "times new roman", 12, "bold"))
        phoneNo_Entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # address Label
        address_label = Label(class_student_frame, background="white",
                              text="Address:", font=("times new roman", 12, "bold"))
        address_label.grid(row=4, column=0, padx=10, sticky=W)

        address_Entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20, font=(
            "times new roman", 12, "bold"))
        address_Entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher Name Label
        tname_label = Label(class_student_frame, background="white",
                            text="Teacher Name:", font=("times new roman", 12, "bold"))
        tname_label.grid(row=4, column=2, padx=10, sticky=W)

        tname_Entry = ttk.Entry(class_student_frame, textvariable=self.var_tName, width=20, font=(
            "times new roman", 12, "bold"))
        tname_Entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # Radio Buttons
        self.var_radio1 = StringVar()
        radio_btn1 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radio_btn1.grid(row=5, column=0)

        radio_btn2 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radio_btn2.grid(row=5, column=1)

        # buttons Frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=5, y=200, width=690, height=35)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=17, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=16, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=16, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data,  width=17, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        # Take Photo Frame
        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=5, y=235, width=690, height=30)

        take_photo_btn = Button(btn_frame1, text="Take Photo", command=self.generate_data,
                                width=34, height=1, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=1)

        update_photo_btn = Button(btn_frame1, text="Update Photo", width=34, height=1, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=2)

        # Right Label Frame
        right_Frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Student Details", font=("times new roman", 12, "bold"))
        right_Frame.place(x=740, y=10, width=720, height=550)

        img_right = Image.open("Images/face2.jpg")
        img_right = img_right.resize((720, 130), Image.LANCZOS)
        self.photoImg_right = ImageTk.PhotoImage(img_right)
        f_label = Label(right_Frame, image=self.photoImg_right)
        f_label.place(x=0, y=0, width=720, height=130)

        # ========Search System=========
        search_frame = LabelFrame(right_Frame, bd=2, bg="white", relief=RIDGE,
                                  text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=135, width=705, height=70)

        search_label = Label(search_frame, background="white",
                             text="Search By:", font=("times new roman", 12, "bold"))
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=(
            "times new roman", 10, "bold"), state="readonly")
        search_combo["values"] = ("Select", "Roll No.", "Phone No.")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_Entry = ttk.Entry(
            search_frame, width=16, font=("times new roman", 12, "bold"))
        search_Entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", width=12, font=(
            "times new roman", 13, "bold"), bg="darkblue", fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        showAll_btn = Button(search_frame, text="Show All", width=12, font=(
            "times new roman", 13, "bold"), bg="darkblue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=4)

        # ========Table Frame========
        table_frame = Frame(right_Frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=705, height=250)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("name", "dep", "course", "sem", "year", "id", "roll", "div", "gender",
                                          "dob", "email", "phone", "address", "tName", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("name", text="Name")
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="Date of Birth")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone Number")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("tName", text="Teacher Name")
        self.student_table.heading("photo", text="Photo Sample")

        self.student_table["show"] = "headings"
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.student_table.pack(fill=BOTH, expand=1)
        self.fetch_data()

    # function declaration

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror(
                "Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Bharat@2201010148",
                                               database="face_recognizer", auth_plugin='mysql_native_password')
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    self.var_name.get(),
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_sem.get(),
                    self.var_year.get(),
                    self.var_id.get(),
                    self.var_roll.get(),
                    self.var_div.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_tName.get(),
                    self.var_radio1.get()

                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Student details has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To :{str(es)}", parent=self.root)

    # Fetch Data from MySQL

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bharat@2201010148",
                                       database="face_recognizer", auth_plugin='mysql_native_password')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # Get cursor

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_name.set(data[0])
        self.var_dep.set(data[1])
        self.var_course.set(data[2])
        self.var_sem.set(data[3])
        self.var_year.set(data[4])
        self.var_id.set(data[5])
        self.var_roll.set(data[6])
        self.var_div.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_tName.set(data[13])
        self.var_radio1.set(data[14])

    # Update Function

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror(
                "Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update", "Do you want to update this student details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="Bharat@2201010148",
                                                   database="face_recognizer", auth_plugin='mysql_native_password')
                    my_cursor = conn.cursor()
                    my_cursor.execute("Update student set Name=%s, Department=%s, Course=%s, Semester=%s, Year=%s, RollNo=%s, Division=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, TeacherName=%s, Photo=%s where Id=%s", (
                        self.var_name.get(),
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_sem.get(),
                        self.var_year.get(),
                        self.var_roll.get(),
                        self.var_div.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_tName.get(),
                        self.var_radio1.get(),
                        self.var_id.get()

                    ))

                else:
                    if not Update:
                        return
                messagebox.showinfo(
                    "Success", "Student details updated Successfully", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to:{str(es)}", parent=self.root)

    # delete function

    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror(
                "Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Student delete page", "Do you want to delete this student data", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="Bharat@2201010148",
                                                   database="face_recognizer", auth_plugin='mysql_native_password')
                    my_cursor = conn.cursor()
                    sql = "delete from student where Id=%s"
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Delete", "Successfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to{str(es)}", parent=self.root)

    # reset function

    def reset_data(self):
        self.var_name.set("")
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_sem.set("Select Semester")
        self.var_year.set("Select Year")
        self.var_id.set("")
        self.var_roll.set("")
        self.var_div.set("Select Division")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_tName.set("")
        self.var_radio1.set("")

    # Generate data set or Take Photo Sample

    def generate_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror(
                "Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Bharat@2201010148",
                                               database="face_recognizer", auth_plugin='mysql_native_password')
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("Update student set Name=%s, Department=%s, Course=%s, Semester=%s, Year=%s, RollNo=%s, Division=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, TeacherName=%s, Photo=%s where Id=%s", (
                    self.var_name.get(),
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_sem.get(),
                    self.var_year.get(),
                    self.var_roll.get(),
                    self.var_div.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_tName.get(),
                    self.var_radio1.get(),
                    self.var_id.get() == id+1

                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load predefined data on face frontals from opencv

                face_classifier = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + \
                            str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50),
                                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo(
                    "Result", "Generating data sets completed successfully!!!!")

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.resizable(False, False)
    root.mainloop()
