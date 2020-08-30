import tkinter
import tkinter.font as Font
import tkinter.messagebox as messagebox

mainWindow = tkinter.Tk()
fontName = 'Times New Roman'
titleFont = Font.Font(family = fontName, size = 20)
loginFont = Font.Font(family = fontName, size = 10)

#Closes the current window
def CloseWindow(window):
    window.destroy()

#If the username and password are a match for the database, this sends them to the next screen
def SuccessfulLogin():
    print("Successful")

#If the username and/or password isn't valid, this comes up
def FailedLogin():
    messagebox.showwarning('Incorrect Login', 'Incorrect Username and/or Password.')

#Checks if the username and password are valid
def Login(username, password):
    print('Username: ' + username + '\nPassword: ' + password)
    FailedLogin()

#Window that opens when the user selects to make a new account
def NewAccount():
    newAccountWindow = tkinter.Tk()
    newAccountWindow.title('New Account')


def LoginScreen():
    #Sets the initial window, window size
    mainWindow.title('Login Screen')
    mainWindow.geometry('900x500')
    mainWindow.resizable(False,False)
    #Sets the title
    titleText = tkinter.Label(mainWindow, text = "Grading Manager and Database", font = titleFont)
    titleText.place(relx = 0.5, rely = 0.2, anchor = 'center')

    #Username prompt
    usernameText = tkinter.Label(mainWindow, text = 'Username:', font = loginFont, justify = 'left')   
    usernameText.place(relx = 0.2, rely = 0.4, anchor = 'center')
    usernameBox = tkinter.Entry(mainWindow, width = 50)
    usernameBox.place(relx = 0.5, rely = 0.4, anchor = 'center')
    #Password prompt
    passwordText = tkinter.Label(mainWindow, text = 'Password:', font = loginFont, justify = 'left')
    passwordText.place(relx = 0.2, rely = 0.5, anchor = 'center')
    passwordBox = tkinter.Entry(mainWindow, show='*', width = 50)
    passwordBox.place(relx = 0.5, rely = 0.5, anchor = 'center')
    #Button to submit username and password
    loginButton = tkinter.Button(mainWindow, text = 'Login', command = lambda:Login(usernameBox.get(),passwordBox.get()), height = 1, width = 10)
    loginButton.place(relx = 0.4, rely = 0.6, anchor = 'center')
    #Button to create a new account
    createAccountButton = tkinter.Button(mainWindow, text = 'New Account', command = lambda:NewAccount(), height = 1, width = 10)
    createAccountButton.place(relx = 0.5, rely = 0.7, anchor = 'center')
    #Button to close the program
    quitButton = tkinter.Button(mainWindow, text = 'Quit', command = lambda:CloseWindow(mainWindow), height = 1, width = 10)
    quitButton.place(relx = 0.6, rely = 0.6, anchor = 'center')
    mainWindow.mainloop()

LoginScreen()


