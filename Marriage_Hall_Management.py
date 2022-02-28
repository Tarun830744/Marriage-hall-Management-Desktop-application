from tkinter import *
from PIL  import Image,ImageTk
import login
import hall
def main():
    win = Tk()
    app =login.Login_window(win)
    win.mainloop()

def hall_run():
    win = Tk()
    app = hall.hallmanagement(win)
    win.mainloop()

if __name__ == '__main__':
    main()
