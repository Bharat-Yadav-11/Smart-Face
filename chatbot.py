from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.geometry("730x620+400+100")
        self.root.title("ChatBot")
        self.root.bind('<Return>', self.enter_button)


        main_frame = Frame(self.root, bd=4, bg="powder blue", width=610)
        main_frame.pack()
        
        img_chat = Image.open("Images/Chatbot1.jpeg")
        img_chat = img_chat.resize((150,70), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img_chat)


        # ==========================title label============================
        title_lbl = Label(main_frame, bd=3, relief=RAISED, width=730, anchor='nw', image=self.photoimg, compound=LEFT, text="Chat Me", font=("arial", 35, "bold"), bg="white", fg="green")
        title_lbl.pack(side=TOP)


        scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)

        self.text = Text(main_frame, width=65, height=20, bd=3, relief=RAISED, font=("arial", 14), yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.text.yview)
        self.text.pack()

        btn_frame = Frame(self.root, bd=4, bg="white", width=730)
        btn_frame.pack()

        lbl_1 = Label(btn_frame, text="Ask something", font=("arial", 14, "bold"), bg="white", fg="green")
        lbl_1.grid(row=0, column=0, padx=5, sticky=W)

        self.entry = StringVar()
        self.entry1 = ttk.Entry(btn_frame, textvariable=self.entry, width=40, font=("arial", 15, "bold"))
        self.entry1.grid(row=0, column=1, padx=5, sticky=W)


        # ==================Send Button================
        self.send = Button(btn_frame, text="Send>>", command=self.send, font=("arial", 15, "bold"), width=8, bg="green")
        self.send.grid(row=0, column=2, padx=5, sticky=W)

        self.clear = Button(btn_frame, text="Clear", command=self.clear_function, font=("arial", 15, "bold"), width=8, bg="RED", fg="WHITE")
        self.clear.grid(row=1, column=0, padx=5, sticky=W)


        self.msg = ""
        self.lbl_2 = Label(btn_frame, text=self.msg, font=("arial", 14, "bold"), fg="red", bg="white")
        self.lbl_2.grid(row=1, column=1, padx=5, sticky=W)



    def enter_button(self, event):
        self.send.invoke()
        self.entry.set('')

    def clear_function(self):
        self.text.delete('1.0', END)
        self.entry.set('')


    # =====================Function Decleration=====================
    def send(self):
        send='\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END, '\n\n'+send)
        self.text.yview(END)

        query = self.entry.get().lower()

        if(self.entry.get()==""):
            self.msg = "Please enter some input"
            self.lbl_2.config(text=self.msg, fg="red")
        
        else:
            self.msg = ""
            self.lbl_2.config(text=self.msg, fg="red")


        if 'hello' in query:
            self.text.insert(END, '\n\n'+"Bot: Hi, Please Tell me How may I help you?")

        elif 'hii' in query:
            self.text.insert(END, '\n\n'+"Bot: Hello, Please Tell me How may I help you?")

        elif 'name' in query:
            self.text.insert(END, '\n\n'+"Bot: My name is Jarvis")

        elif 'change your name' in query:
            self.text.insert(END, '\n\n'+"Bot: My name is Jarvis, Unfortunately I can't change it")

        elif 'mean of jarvis' in query:
            self.text.insert(END, '\n\n'+"Bot: Jarvis means (Just A Rather Than Very Intelligent System). It is the most powerful and smart AI in the world")

        elif 'language' in query:
            self.text.insert(END, '\n\n'+"Bot: It's top secret🙃. Sorry, I can't tell you about that.. ")

        elif 'speak' in query:
            self.text.insert(END, '\n\n'+"Bot: Currently,I can speak in English only\n\tBut I still learning it..")

        elif 'talk' in query:
            self.text.insert(END, '\n\n'+"Bot: Currently,I can talk in English only\n\tBut I still learning it..")

        elif 'face recognition system' in query:
            self.text.insert(END, '\n\n'+"Bot: Facial recognition uses technology and biometrics — typically through AI — to identify human faces. It maps facial features from a photograph or video and then compares the information with a database of known faces to find a match.")

        elif 'create' in query:
            self.text.insert(END, '\n\n'+"Bot: Code India 2023")

        elif 'how are you' in query:
            self.text.insert(END, '\n\n'+"Bot: Fantastic😉, What about you??")

        elif 'fine' in query:
            self.text.insert(END, '\n\n'+"Bot: Great, Do you need any help?")

        elif 'good' in query:
            self.text.insert(END, '\n\n'+"Bot: Nice to hear you, Do you need any help?")

        elif 'yes' in query:
            self.text.insert(END, '\n\n'+"Bot: Please tell me How may I help you?")

        elif 'no' in query:
            self.text.insert(END, '\n\n'+"Bot: Ok I am going to sleep")

        elif 'bye' in query:
            self.text.insert(END, '\n\n'+"Bot: Ok I am going to sleep")
        
        elif 'algorithm' in query:
            self.text.insert(END, '\n\n'+"Bot: LBPH(Local Binary Pattern Histogram)")

        elif 'open source' in query:
            self.text.insert(END, '\n\n'+"Bot: Open source is a licensing agreement that allows users to freely access, copy, modify, and redistribute software. Open source software is developed as a public collaboration and is made freely available to the public.")

        elif 'your system' in query:
            self.text.insert(END, '\n\n'+"Bot: There are many reasons\n 1. I am open source\n 2. My Accuracy is excellent in recognizing the face, I will never forgot you\n 3. The Best thing you know about me is.. The Programmer who made me is best\n and intelligent in the World!!!\n 4. Last but not the least, this face recognition system is easy to use for all.")

        elif 'lbph' in query:
            self.text.insert(END, '\n\n'+"Bot: LBHP stands for Local Binary Pattern Histogram is deep Machine Learning Alogorithm which is commonly used is Face Recognition.\n Its advantages:\n 1. Easy to use: Quite easy Syntax when compared to other algorithm. \n2. Accuracy: LBPH has an accuracy of 90.80% which is higher than Convolutional Neural Network(CNN) model's accuracy of 90.30%. The deepface accuracy is 91.90%")

        elif 'work' in query:
            self.text.insert(END, '\n'+"Bot: I uses the LBPH(Local Binary Pattern Histogram Algorithm The LBPH has basically 4 Parameters:\n *Radius:* the radius is used to build the circular local binary pattern and represents the radius around the central pixel. It is usually set to 1.\n *Neighbors:* the number of sample points to build the circular local binary pattern. Keep in mind: the more sample points you include, the higher the computational cost. It is usually set to 8.\n *Grid X:* the number of cells in the horizontal direction. The more cells, the finer the grid, the higher the dimensionality of the resulting feature vector. It is usually set to 8.\n *Grid Y:* the number of cells in the vertical direction. The more cells, the finer the grid, the higher the dimensionality of the resulting feature vector. It is usually set to 8.")

        else:
            self.text.insert(END, '\n\n'+"Bot: I didn't understand")

        

        
            






if __name__=="__main__":
    root = Tk()
    obj = ChatBot(root)
    root.resizable(False, False)
    root.mainloop()
