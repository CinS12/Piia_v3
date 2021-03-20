import tkinter as tk
import ctypes
from Controller import Controller
import Controller.C_Setup as C_Setup
import Test.kk

if __name__ == "__main__":
    Test.kk.testkk()
    root = tk.Tk()
    user32 = ctypes.windll.user32
    #screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    #print(screensize)
    #w = screensize[0]
    #h = screensize[1]
    w = 1920
    h = 1080
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 3) - (h / 3)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    # mainwin.resizable(0, 0)
    root.title("PIIA")

    app = C_Setup.ControllerSetup(root)
    root.mainloop()