# _*_ coding: utf-8 _*_
# Author: kow3388
# Date: 2025-05-17

import tkinter as tk
from tkinter.font import Font

class TensionHeadGUI:
    def __init__(self, root):
        self.bg = "#f0f0f0"
        
        self.gui = root
        self.gui.title("TensionHeadGUI")
        self.gui.attributes("-fullscreen", True)
        self.gui.configure(bg=self.bg)

        self.label_font = Font(family="Arial", size=35)

        # set row of gui (1/10 for label, others for information)
        for i in range(10):
            self.gui.rowconfigure(i, weight=1)

        self.cur_mode = "TopBar"

        # TopBar setting
        self.top_bar = ["Tension", "Calibration", "Logs"]
        self.top_bar_len = 3
        self.top_bar_idx = 0
        self.top_bar_list = []
        self.InitTopList()

        # Tension mode
        self.tension_list = []
        self.tension_idx = 0
        self.InitTensionContent()

        # Calibration mode
        self.calibration_list = []
        self.calibration_idx = 0

        # binding action
        self.gui.bind("<Return>", self.ReturnAction)
        self.gui.bind("<Left>", self.LeftAction)
        self.gui.bind("<Right>", self.RightAction)
        self.gui.bind("<Escape>", self.EscAction)
    
    def InitTopList(self):
        # create grid col first
        for i in range(2*self.top_bar_len):
            self.gui.columnconfigure(i, weight=1, uniform="equal")

        for i in range(self.top_bar_len):
            color = "gray" if i == self.top_bar_idx else "#dcdcdc"
            label = tk.Label(self.gui,
                             text=self.top_bar[i],
                             font=self.label_font,
                             border=10,
                             relief="groove",
                             fg="black",
                             bg=color)
            label.grid(row=0, column=2*i, columnspan=2, sticky="nsew", padx=0, pady=0)
            self.top_bar_list.append(label)
    
    def InitTensionContent(self):
        row_idx = 1
        rowspan = 3

        def create_spin_frame(parent):
            frame = tk.Frame(parent, bg=self.bg)
            spin_tens = tk.Spinbox(frame, from_=0, to=3, font=self.label_font, width=2)
            spin_ones = tk.Spinbox(frame, from_=0, to=9, font=self.label_font, width=2)
            spin_dot = tk.Spinbox(frame, from_=0, to=9, font=self.label_font, width=2)
            dot = tk.Label(frame, text=".", font=self.label_font, bg=self.bg)

            spin_tens.pack(side="left")
            spin_ones.pack(side="left")
            dot.pack(side="left")
            spin_dot.pack(side="left")

            return frame, spin_tens, spin_ones, spin_dot

        # Pre Tension
        pre_label = tk.Label(self.gui, text="Pre Tension: ", font=self.label_font, fg="black", bg=self.bg)
        pre_spin_frame, pre_tens, pre_ones, pre_dot = create_spin_frame(self.gui)
        pre_button = tk.Button(self.gui, text="off", font=self.label_font)

        pre_label.grid(row=row_idx, column=0, rowspan=rowspan, columnspan=2)
        pre_spin_frame.grid(row=row_idx, column=2, rowspan=rowspan, columnspan=3)
        pre_button.grid(row=row_idx, column=5, rowspan=rowspan)

        row_idx += rowspan

        # Knot
        knot_label = tk.Label(self.gui, text="Knot: ", font=self.label_font, fg="black", bg=self.bg)
        knot_spin_frame, knot_tens, knot_ones, knot_dot = create_spin_frame(self.gui)
        knot_button = tk.Button(self.gui, text="off", font=self.label_font)

        knot_label.grid(row=row_idx, column=0, rowspan=rowspan, columnspan=2)
        knot_spin_frame.grid(row=row_idx, column=2, rowspan=rowspan, columnspan=3)
        knot_button.grid(row=row_idx, column=5, rowspan=rowspan)

        row_idx += rowspan

        # Current Tension
        cur_label = tk.Label(self.gui, text="Current tension: ", font=self.label_font, fg="black", bg=self.bg)
        cur_spin_frame, cur_tens, cur_ones, cur_dot = create_spin_frame(self.gui)
        cur_button = tk.Button(self.gui, text="Start tension", font=self.label_font)

        cur_label.grid(row=row_idx, column=0, rowspan=rowspan, columnspan=2)
        cur_spin_frame.grid(row=row_idx, column=2, rowspan=rowspan, columnspan=3)
        cur_button.grid(row=row_idx, column=5, rowspan=rowspan)

        self.tension_list = [
            pre_label, pre_spin_frame, pre_tens, pre_ones, pre_dot, pre_button,
            knot_label, knot_spin_frame, knot_tens, knot_ones, knot_dot, knot_button,
            cur_label, cur_spin_frame, cur_tens, cur_ones, cur_dot, cur_button
        ]

    
    def ReturnAction(self, event=None):
        if self.cur_mode == "TopBar":
            self.cur_mode = self.top_bar[self.top_bar_idx]

    def LeftAction(self, event=None):
        if self.cur_mode == "TopBar":
            self.MoveTopIdx(-1)
    
    def RightAction(self, event=None):
        if self.cur_mode == "TopBar":
            self.MoveTopIdx(1)
    
    def MoveTopIdx(self, dir):
        # turn back the background color of current idx
        self.top_bar_list[self.top_bar_idx].configure(bg="#dcdcdc")

        # move to next index & change color
        self.top_bar_idx = (self.top_bar_idx + dir + self.top_bar_len) % self.top_bar_len
        self.top_bar_list[self.top_bar_idx].configure(bg="gray")
    
    def EscAction(self, event=None):
        if self.cur_mode == "TopBar":
            self.CloseWindow()
        else:
            self.cur_mode = "TopBar"
    
    def CloseWindow(self):
        self.gui.destroy()