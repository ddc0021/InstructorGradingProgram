import tkinter
import tkinter.font as Font
import tkinter.messagebox as messagebox

class MainMenu:
    #Closes the current window
    def CloseWindow(self, window):
        window.destroy()

    #If the username and password are a match for the database, this sends them to the next screen
    def SuccessfulLogin(self):
        print("Successful")

    #If the username and/or password isn't valid, this comes up
    def FailedLogin(self):
        messagebox.showwarning('Incorrect Login', 'Incorrect Username and/or Password.')

    #Checks if the username and password are valid
    def Login(self, username, password):
        print('Username: ' + username + '\nPassword: ' + password)
        self.FailedLogin()

    #Window that opens when the user selects to make a new account
    def NewAccount(self):
        self.newAccountWindow = tkinter.Tk()
        self.newAccountWindow.title('New Account')


    def LoginScreen(self):
        self.mainWindow = tkinter.Tk()
        self.fontName = 'Times New Roman'
        self.titleFont = Font.Font(family = self.fontName, size = 20)
        self.loginFont = Font.Font(family = self.fontName, size = 10)
        #Sets the initial window, window size
        self.mainWindow.title('Login Screen')
        self.mainWindow.geometry('900x500')
        self.mainWindow.resizable(False,False)
        #Sets the title
        self.titleText = tkinter.Label(self.mainWindow, text = "Grading Manager and Database", font = self.titleFont)
        self.titleText.place(relx = 0.5, rely = 0.2, anchor = 'center')

        #Username prompt
        self.usernameText = tkinter.Label(self.mainWindow, text = 'Username:', font = self.loginFont, justify = 'left')   
        self.usernameText.place(relx = 0.2, rely = 0.4, anchor = 'center')
        self.usernameBox = tkinter.Entry(self.mainWindow, width = 50)
        self.usernameBox.place(relx = 0.5, rely = 0.4, anchor = 'center')
        #Password prompt
        self.passwordText = tkinter.Label(self.mainWindow, text = 'Password:', font = self.loginFont, justify = 'left')
        self.passwordText.place(relx = 0.2, rely = 0.5, anchor = 'center')
        self.passwordBox = tkinter.Entry(self.mainWindow, show='*', width = 50)
        self.passwordBox.place(relx = 0.5, rely = 0.5, anchor = 'center')
        #Button to submit username and password
        self.loginButton = tkinter.Button(self.mainWindow, text = 'Login', command = lambda:self.Login(self.usernameBox.get(),self.passwordBox.get()), height = 1, width = 10)
        self.loginButton.place(relx = 0.4, rely = 0.6, anchor = 'center')
        #Button to create a new account
        self.createAccountButton = tkinter.Button(self.mainWindow, text = 'New Account', command = lambda:self.NewAccount(), height = 1, width = 10)
        self.createAccountButton.place(relx = 0.5, rely = 0.7, anchor = 'center')
        #Button to close the program
        self.quitButton = tkinter.Button(self.mainWindow, text = 'Quit', command = lambda:self.CloseWindow(self.mainWindow), height = 1, width = 10)
        self.quitButton.place(relx = 0.6, rely = 0.6, anchor = 'center')
        self.mainWindow.mainloop()

    def __init__(self):
        self.LoginScreen()

mM = MainMenu()