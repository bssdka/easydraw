# coding urf-8

import customtkinter as ctk
import configparser as cfg
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
        menuCFG = self.config['frames.config']

        # Create foreground
        foreground = ctk.CTkFrame(self, width=int(self.size['width']), height=int(self.size['height']), fg_color='#1f1f1f').pack()
        # Create frames of workspaces
        left_menu = ctk.CTkFrame(self, width=int(menuCFG['lm_width']), height=int(menuCFG['lm_height']), fg_color='#fff').place(x=10, y=10)
        main_menu = ctk.CTkCanvas(self, width=int(menuCFG['mm_width']), height=int(menuCFG['mm_height']), bg="#fff").place(x=331, y=20)

        # Create interaction menu
        


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