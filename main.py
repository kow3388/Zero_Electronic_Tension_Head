# _*_ coding: utf-8 _*_
# Author: kow3388
# Date: 2025-05-17

import os
import logging
from logging import DEBUG, Formatter
import tkinter as tk
from TensionHeadGUI import TensionHeadGUI as GUI


# handler
logger = logging.getLogger("BETH")
logger.setLevel(DEBUG)

# file_path
log_path = "./log/BETH.log"
log_dir = os.path.dirname(log_path)
if not os.path.isdir(log_dir):
    os.makedirs(log_dir)

# logger format
formatter = Formatter(
    fmt="[%(asctime)s - %(levelname)s]: %(message)s", datefmt="%Y-%m-%d %H:%M"
)

# on file
file_handler = logging.FileHandler(log_path, mode="a")
file_handler.setLevel(DEBUG)
file_handler.setFormatter(formatter)

# on terminal
stream_handler = logging.StreamHandler()
stream_handler.setLevel(DEBUG)
stream_handler.setFormatter(formatter)

# intergrate to handler
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

if __name__ == "__main__":
    logger.info("Start BETH GUI")
    # create tk window
    root = tk.Tk()

    # create GUI
    gui = GUI(root=root)
    gui.mainloop()
