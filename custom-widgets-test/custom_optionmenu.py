
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1920x1080")
        self.initUI()
    
    def initUI(self):
        
        self.is_pressed = 0

        # Size and its derivatives
        main_width = 300
        main_height = 100


        label = ctk.CTkLabel(self, width=main_width, height=main_height, text="Files", fg_color="blue", corner_radius=15, 
        font=('Arial', 25), text_color="#fff", anchor="w", padx=30).place(x=500, y=400)
        btn = ctk.CTkButton(self, width=80, height=80, fg_color='white', border_width=3, border_color='black', 
        corner_radius=15,bg_color="blue", command=self.counter).place(x=700, y=410)

    def counter(self):
        self.is_pressed += 1
        if self.is_pressed == 2:
            self.is_pressed = 0
            self.destroy_menu()
        else:
            self.open_menu()

        print(self.is_pressed)

    def open_menu(self):
        self.frm = ctk.CTkFrame(self, width=300, height=300, fg_color='blue', corner_radius=15) 
        self.frm.place(x=100, y=100)

    def destroy_menu(self):
        self.frm.destroy()


if __name__ == '__main__':
    app = App()
    app.mainloop()