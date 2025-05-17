# _*_ coding: utf-8 _*_
# Author: kow3388
# Date: 2025-05-17

import tkinter as tk
from TensionHeadGUI import TensionHeadGUI as GUI

if __name__ == "__main__":
    # create tk window
    root = tk.Tk()

    # create GUI
    gui = GUI(root=root)
    gui.gui.mainloop()