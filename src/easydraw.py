# coding urf-8

import customtkinter as ctk
import configparser as cfg
from tkinter import ttk
import os

#__Author__: bsskda
#__License__: BSD 2-Clause License

# ---GLOBAL VARIABLES---
__path__ = os.getcwd()


class MainWindow(ctk.CTk):
    def __init__(self, *args):
        super().__init__()

        # Launch and read Config Parser 
        self.config = cfg.ConfigParser()
        self.config.read(f"{__path__}/config/basic.ini")
        meta = self.config['DEFAULT']
        self.size = self.config['app.config']

        self.title(f"{meta['title']} {meta['version']}")
        self.geometry(f"{self.size['width']}x{self.size['height']}")
        
        # Init GUI graphics
        self.initUI()


    def initUI(self):
        self.is_pressed = 0
        menuCFG = self.config['frames.config']

        # Create foreground
        foreground = ctk.CTkFrame(self, width=int(self.size['width']), height=int(self.size['height']), fg_color='#1f1f1f').pack()
        # Create frames of workspaces
        left_menu = ctk.CTkFrame(self, width=int(menuCFG['lm_width']), height=int(menuCFG['lm_height']), fg_color='#fff').place(x=10, y=10)
        main_menu = ctk.CTkCanvas(self, width=int(menuCFG['mm_width']), height=int(menuCFG['mm_height']), bg="#fff").place(x=331, y=20)

        # Create interaction menu
        file_btn = ctk.CTkButton(self, width=50, height=100, anchor='center', corner_radius=5,
            fg_color="#c0c0c0", hover_color="#dcdcdc", command=self.launch_file_menu,
            text="F\nI  \nL\nE", font=('Arial', 16), text_color='black').place(x=20, y=20)

        # debbuging
        self.launch_file_menu()

    # Functions file menu
    def launch_file_menu(self):
        self.is_pressed += 1
        if self.is_pressed == 2: 
            self.is_pressed = 0
            self.destroy_menu()
        else: 
            self.launch_menu()
    def launch_menu(self):
        self.frame_menu = ctk.CTkFrame(self, width=220, height=100, fg_color="#000")
        self.frame_menu.place(x=80, y=20)
    def destroy_menu(self):
        self.frame_menu.destroy()

if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()

""" TODO
    1) Add tabview to main menu (fast switch canvas)
    2) Create your own custom optionmenu widget 
"""

""" NOTE
    1) When using WM, he title and some other features are not displayed. I don't know how it 
    will look on other systems. After the first release we should add multi-system functionality
"""