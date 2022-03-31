from tkinter import *


class Application:
    def __init__(self, master=None):
        self.defaultFont = ("Lucida Sans", "10")
        self.firstContainer = Frame(master)
        self.firstContainer["pady"] = 10
        self.firstContainer.pack()

        self.secondContainer = Frame(master)
        self.secondContainer["padx"] = 20
        self.secondContainer.pack()

        self.thirdContainer = Frame(master)
        self.thirdContainer["padx"] = 20
        self.thirdContainer.pack()

        self.fourthContainer = Frame(master)
        self.fourthContainer["pady"] = 20
        self.fourthContainer.pack()

        self.title = Label(self.firstContainer, text="User Data")
        self.title["font"] = ('Lucida sans', '10', 'bold')
        self.title.pack()

        self.nameLabel = Label(self.secondContainer,
                               text="Name:", font=self.defaultFont)
        self.nameLabel.pack(side=LEFT)

        self.name = Entry(self.secondContainer)
        self.name["width"] = 30
        self.name["font"] = self.defaultFont
        self.name.pack(side=LEFT)

        self.passwordLabel = Label(
            self.thirdContainer, text="Key:", font=self.defaultFont)
        self.passwordLabel.pack(side=LEFT)

        self.password = Entry(self.thirdContainer)
        self.password["width"] = 30
        self.password["font"] = self.defaultFont
        self.password["show"] = "*"
        self.password.pack(side=LEFT)

        self.authenticate = Button(self.fourthContainer)
        self.authenticate["text"] = "Authenticate"
        self.authenticate["font"] = ("Arial", "7")
        self.authenticate["width"] = 12
        self.authenticate["command"] = self.checkPassword
        self.authenticate.pack()

        self.message = Label(self.fourthContainer,
                             text=" ", font=self.defaultFont)
        self.message.pack()

    def checkPassword(self):
        user = self.name.get()
        password = self.password.get()
        if user == "myuser" and password == "gotcha":
            self.message["text"] = "Authenticated"
        else:
            self.message["text"] = "Authenticate Error (Try Again)"


rootApli = Tk()
Application(rootApli)
rootApli.mainloop()
