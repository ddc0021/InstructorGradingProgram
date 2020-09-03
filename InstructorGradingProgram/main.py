import MainMenu
import LoginDatabase

if __name__ == '__main__':
    mM = MainMenu.MainMenu()
    dB = LoginDatabase.Database()
    dB.create_connection('loginDatabase.db')