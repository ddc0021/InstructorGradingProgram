import tkinter
import tkinter.font as Font

mainWindow = tkinter.Tk()
fontName = 'Times New Roman'
titleFont = Font.Font(family = fontName, size = 20)
loginFont = Font.Font(family = fontName, size = 10)

def CloseWindow(window):
    window.destroy()

def SuccessfulLogin():
    print("Successful")

def FailedLogin():
    failWindow = tkinter.Tk()
    failWindow.title('Failed login.')
    failWindow.geometry('300x150+500+300')
    failText = tkinter.Label(failWindow, text = 'Incorrect username and/or password.', font = loginFont)
    failText.place(relx = 0.5, rely = 0.3, anchor = 'center')
    failButton = tkinter.Button(failWindow, text = 'OK', command = lambda:CloseWindow(failWindow), height = 1, width = 10)
    failButton.place(relx = 0.5, rely = 0.8, anchor = 'center')

def LoginButton(username, password):
    print(username + password)
    FailedLogin()

#Sets the initial window, window size
mainWindow.title('Login Screen')
mainWindow.geometry('900x500')
#Sets the title
titleText = tkinter.Label(mainWindow, text = "Grading Manager and Database", font = titleFont)
titleText.place(relx = 0.5, rely = 0.2, anchor = 'center')

#Username prompt
usernameText = tkinter.Label(mainWindow, text = 'Username:', font = loginFont, justify = 'left')
usernameText.place(relx = 0.2, rely = 0.4, anchor = 'center')
usernameBox = tkinter.Text(mainWindow, height = 1, width = 30)
usernameBox.place(relx = 0.5, rely = 0.4, anchor = 'center')
#Password prompt
passwordText = tkinter.Label(mainWindow, text = 'Password:', font = loginFont, justify = 'left')
passwordText.place(relx = 0.2, rely = 0.5, anchor = 'center')
passwordBox = tkinter.Text(mainWindow, height = 1, width = 30)
passwordBox.place(relx = 0.5, rely = 0.5, anchor = 'center')
#Button to submit username and password

#Sets login button
loginButton = tkinter.Button(mainWindow, text = 'Login', command = lambda:LoginButton(usernameBox.get('1.0','end'),passwordBox.get('1.0','end')), height = 1, width = 10)
loginButton.place(relx = 0.4, rely = 0.6, anchor = 'center')

quitButton = tkinter.Button(mainWindow, text = 'Quit', command = lambda:CloseWindow(mainWindow), height = 1, width = 10)
quitButton.place(relx = 0.6, rely = 0.6, anchor = 'center')
mainWindow.mainloop()


