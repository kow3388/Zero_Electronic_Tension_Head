# _*_ coding: utf-8 _*_
# Author: kow3388
# Date: 2025-05-17

import logging
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.font import Font
from tkinter.scrolledtext import ScrolledText


logger = logging.getLogger("BETH")


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
            self.gui.rowconfigure(i, weight=1, uniform="equal")

        self.cur_mode = "TopBar"

        # TopBar setting
        self.top_bar = ["Tension", "Calibration", "Logs"]
        self.top_bar_len = 3
        self.top_bar_idx = 0
        self.top_bar_list = []
        self._init_top_list()

        # Tension mode
        self.tension_list = []
        self.tension_spinbox = []
        self.tension_idx = 0
        self._init_tension()

        # Calibration mode
        self.calibration_list = []
        self.calibration_spinbox = []
        self.calibration_idx = 0
        self.init_calibration = False

        # Log mode
        self.logger_file = "./log/BETH.log"
        self.log_list = []
        self.init_log = False

        # binding action
        self.gui.bind("<Return>", self._return_action)
        self.gui.bind("<Left>", self._left_action)
        self.gui.bind("<Right>", self._right_action)
        self.gui.bind("<Escape>", self._esc_action)

    def _init_top_list(self):
        # create grid col first
        for i in range(2 * self.top_bar_len):
            self.gui.columnconfigure(i, weight=1, uniform="equal", minsize=350)

        for i in range(self.top_bar_len):
            color = "gray" if i == self.top_bar_idx else "#dcdcdc"
            label = tk.Label(
                self.gui,
                text=self.top_bar[i],
                font=self.label_font,
                border=10,
                relief="groove",
                fg="black",
                bg=color,
            )
            label.grid(row=0, column=2 * i, columnspan=2, sticky="nsew")
            self.top_bar_list.append(label)

    def _init_tension(self):
        row_idx = 1
        rowspan = 3

        # Pre Tension
        pre_label = tk.Label(
            self.gui, text="Pre Tension: ", font=self.label_font, fg="black", bg=self.bg
        )
        pre_spin_frame, pre_tens, pre_ones, pre_dot = self._create_spin_frame()
        pre_button = tk.Button(self.gui, text="off", font=self.label_font)

        pre_label.grid(row=row_idx, column=0, rowspan=rowspan, columnspan=2)
        pre_spin_frame.grid(row=row_idx, column=2, rowspan=rowspan, columnspan=3)
        pre_button.grid(row=row_idx, column=5, rowspan=rowspan)

        row_idx += rowspan

        separator1 = ttk.Separator(self.gui, orient="horizontal")
        separator1.grid(row=row_idx - 1, column=0, columnspan=6, sticky="ew")

        # Knot
        knot_label = tk.Label(
            self.gui, text="Knot: ", font=self.label_font, fg="black", bg=self.bg
        )
        knot_spin_frame, knot_tens, knot_ones, knot_dot = self._create_spin_frame()
        knot_button = tk.Button(self.gui, text="off", font=self.label_font)

        knot_label.grid(row=row_idx, column=0, rowspan=rowspan, columnspan=2)
        knot_spin_frame.grid(row=row_idx, column=2, rowspan=rowspan, columnspan=3)
        knot_button.grid(row=row_idx, column=5, rowspan=rowspan)

        row_idx += rowspan

        separator2 = ttk.Separator(self.gui, orient="horizontal")
        separator2.grid(row=row_idx - 1, column=0, columnspan=6, sticky="ew")

        # Current Tension
        cur_label = tk.Label(
            self.gui,
            text="Current tension: ",
            font=self.label_font,
            fg="black",
            bg=self.bg,
        )
        cur_spin_frame, cur_tens, cur_ones, cur_dot = self._create_spin_frame()
        cur_button = tk.Button(self.gui, text="Start", font=self.label_font)

        cur_label.grid(row=row_idx, column=0, rowspan=rowspan, columnspan=2)
        cur_spin_frame.grid(row=row_idx, column=2, rowspan=rowspan, columnspan=3)
        cur_button.grid(row=row_idx, column=5, rowspan=rowspan)

        self.tension_list = [
            pre_label,
            pre_spin_frame,
            pre_button,
            separator1,
            knot_label,
            knot_spin_frame,
            knot_button,
            separator2,
            cur_label,
            cur_spin_frame,
            cur_button,
        ]
        self.tension_spinbox = [
            pre_tens,
            pre_ones,
            pre_dot,
            knot_tens,
            knot_ones,
            knot_dot,
            cur_tens,
            cur_ones,
            cur_dot,
        ]

    def _init_calibration(self):
        row_idx = 1
        rowspan = 4

        exp_label = tk.Label(
            self.gui,
            text="Expect tension: ",
            font=self.label_font,
            fg="black",
            bg=self.bg,
        )
        exp_spin_frame, exp_tens, exp_ones, exp_dot = self._create_spin_frame()
        exp_button = tk.Button(self.gui, text="Start", font=self.label_font)

        exp_label.grid(row=row_idx, column=0, rowspan=rowspan, columnspan=2)
        exp_spin_frame.grid(row=row_idx, column=2, rowspan=rowspan, columnspan=3)
        exp_button.grid(row=row_idx, column=5, rowspan=rowspan)

        row_idx += rowspan

        separator1 = ttk.Separator(self.gui, orient="horizontal")
        separator1.grid(row=row_idx - 1, column=0, columnspan=6, sticky="ew")

        act_label = tk.Label(
            self.gui,
            text="Actual tension: ",
            font=self.label_font,
            fg="black",
            bg=self.bg,
        )
        act_spin_frame, act_tens, act_ones, act_dot = self._create_spin_frame()
        act_button = tk.Button(self.gui, text="Cal", font=self.label_font)

        act_label.grid(row=row_idx, column=0, rowspan=rowspan, columnspan=2)
        act_spin_frame.grid(row=row_idx, column=2, rowspan=rowspan, columnspan=3)
        act_button.grid(row=row_idx, column=5, rowspan=rowspan)

        row_idx += rowspan

        separator2 = ttk.Separator(self.gui, orient="horizontal")
        separator2.grid(row=row_idx - 1, column=0, columnspan=6, sticky="ew")

        self.calibration_list = [
            exp_label,
            exp_spin_frame,
            exp_button,
            separator1,
            act_label,
            act_spin_frame,
            act_button,
            separator2,
        ]
        self.calibration_spinbox = [
            exp_tens,
            exp_ones,
            exp_dot,
            act_tens,
            act_ones,
            act_dot,
        ]
        self.init_calibration = True
    
    def _init_log(self):
        # create text
        self.log_text = ScrolledText(
            self.gui, state="disabled", font=("Arial", 20), heigh=5
        )

        rowspan, colspan = 9, 6
        self.log_text.grid(
            row=1, column=0, rowspan=rowspan, columnspan=colspan, sticky="nswe"
        )
        self.log_list.append(self.log_text)
        self._update_logger()
    
    def _update_logger(self):
        # read logger
        with open(self.logger_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        self.log_text.config(state="normal")
        self.log_text.delete(1.0, tk.END)
        self.log_text.insert(tk.END, "".join(lines))
        self.log_text.config(state="disable")

    def _return_action(self, event=None):
        if self.cur_mode == "TopBar":
            self.cur_mode = self.top_bar[self.top_bar_idx]

    def _left_action(self, event=None):
        logger.info("Left Test")
        if self.cur_mode == "TopBar":
            self._move_top_idx(-1)

    def _right_action(self, event=None):
        logger.info("Right Test")
        if self.cur_mode == "TopBar":
            self._move_top_idx(1)

    def _move_top_idx(self, dir):
        # turn back the background color of current idx
        self.top_bar_list[self.top_bar_idx].configure(bg="#dcdcdc")

        # move to next index & change color
        self.top_bar_idx = (
            self.top_bar_idx + dir + self.top_bar_len
        ) % self.top_bar_len

        self._show_content()

        self.top_bar_list[self.top_bar_idx].configure(bg="gray")

    def _esc_action(self, event=None):
        if self.cur_mode == "TopBar":
            self._closw_window()
        else:
            self.cur_mode = "TopBar"

    def _closw_window(self):
        self.gui.destroy()

    def _create_spin_frame(self):
        frame = tk.Frame(self.gui, bg=self.bg)
        spin_tens = tk.Spinbox(frame, from_=0, to=3, font=self.label_font, width=2)
        spin_ones = tk.Spinbox(frame, from_=0, to=9, font=self.label_font, width=2)
        spin_dot = tk.Spinbox(frame, from_=0, to=9, font=self.label_font, width=2)
        dot = tk.Label(frame, text=".", font=self.label_font, bg=self.bg)

        spin_tens.pack(side="left")
        spin_ones.pack(side="left")
        dot.pack(side="left")
        spin_dot.pack(side="left")

        return frame, spin_tens, spin_ones, spin_dot

    def _show_content(self):
        # if on tension show only tension
        if self.top_bar_idx == 0:
            for ele in self.calibration_list:
                ele.grid_remove()
            
            for ele in self.log_list:
                ele.grid_remove()

            for ele in self.tension_list:
                ele.grid()
        # if on calibration and haven't initialed calibration
        elif self.top_bar_idx == 1 and not self.init_calibration:
            for ele in self.tension_list:
                ele.grid_remove()
            
            for ele in self.log_list:
                ele.grid_remove()

            self._init_calibration()
        # if on calibration and have initialed
        elif self.top_bar_idx == 1:
            for ele in self.tension_list:
                ele.grid_remove()
            
            for ele in self.log_list:
                ele.grid_remove()

            for ele in self.calibration_list:
                ele.grid()
        # if on log and haven't initialed log
        elif self.top_bar_idx == 2 and not self.init_log:
            for ele in self.tension_list:
                ele.grid_remove()
            
            for ele in self.calibration_list:
                ele.grid_remove()
            
            self._init_log()
        # log and initialed log
        else:
            for ele in self.tension_list:
                ele.grid_remove()
            
            for ele in self.calibration_list:
                ele.grid.remove()
            
            self._update_logger()
            for ele in self.log_list:
                ele.grid()

    def mainloop(self):
        self.gui.mainloop()
