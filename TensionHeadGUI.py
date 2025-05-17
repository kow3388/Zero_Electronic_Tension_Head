# _*_ coding: utf-8 _*_
# Author: kow3388
# Date: 2025-05-17

import tkinter as tk

class TensionHeadGUI:
    def __init__(self, root):
        self.gui = root
        self.gui.title("TensionHeadGUI")
        self.gui.attributes("-fullscreen", True)
        self.gui.configure(bg="white")

        # set row of gui (1/10 for label, others for information)
        self.gui.rowconfigure(0, weight=1)
        self.gui.rowconfigure(1, weight=9)

        # mode setting
        self.mode = ["Tension", "Calibration", "Setting", "Logs"]
        self.mode_len = 4
        self.mode_idx = 0

        self.mode_list = []
        for i in range(self.mode_len):
            self.gui.columnconfigure(i, weight=1)
            color = "gray" if i == self.mode_idx else "#dcdcdc"
            label = tk.Label(self.gui,
                             text=self.mode[i],
                             font=("Arial", 35),
                             border=10,
                             relief="groove",
                             fg="black",
                             bg=color)
            label.grid(row=0, column=i, sticky="nsew", padx=0, pady=0)
            self.mode_list.append(label)
        
        self.info_label = tk.Label(self.gui,
                                   text=f"Mode: {self.mode[self.mode_idx]}",
                                   font=("Arial", 60),
                                   bg="white",
                                   fg="black")
        self.info_label.grid(row=1, column=0, columnspan=self.mode_len, sticky="nsew")

        # binding action
        self.gui.bind("<Escape>", self.close_window)
        self.gui.bind("<Left>", self.LeftAction)
        self.gui.bind("<Right>", self.RightAction)
    
    def close_window(self, event=None):
        self.gui.destroy()
    
    def LeftAction(self, event=None):
        # turn back the background color of current idx
        self.mode_list[self.mode_idx].configure(bg="#dcdcdc")

        # move to next index & change color
        self.mode_idx = (self.mode_idx - 1 + self.mode_len) % self.mode_len
        self.mode_list[self.mode_idx].configure(bg="gray")

        self.update_info()
    
    def RightAction(self, event=None):
        # turn back the background color of current idx
        self.mode_list[self.mode_idx].configure(bg="#dcdcdc")

        # move to next index & change color
        self.mode_idx = (self.mode_idx + 1 + self.mode_len) % self.mode_len
        self.mode_list[self.mode_idx].configure(bg="gray")

        self.update_info()
    
    def update_info(self):
        self.info_label.configure(text=f"Mode: {self.mode[self.mode_idx]}")