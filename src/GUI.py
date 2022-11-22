import tkinter
import customtkinter
from PIL import Image, ImageTk
from tkinter import Canvas, filedialog, messagebox
from tkinter.filedialog import askdirectory
import os
import time
import eigenFace

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

PATH = os.path.dirname(os.path.realpath(__file__))

class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("TUBES ALGEO 2 YGY")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="TUBES IF2123",
                                              text_font=("Roboto Medium", -20))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Face Recognition",
                                                command=self.button_event)
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Camera",
                                                command=self.button_event)
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        self.frame_info2 = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info2.grid(row=2, column=0, columnspan=1, rowspan=4, pady=20, padx=20, sticky="nsew")

        self.frame_info3 = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info3.grid(row=2, column=1, columnspan=1, rowspan=4, pady=20, padx=20, sticky="nsew")

        self.frame_info4 = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info4.grid(row=8, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        self.add_folder_image = self.load_image("/GUI/test_images/add-folder.png", 20)
        self.add_list_image = self.load_image("/GUI/test_images/add-list.png", 20)
        self.add_logo_image = self.load_image("/GUI/test_images/logo.png", 120)

        self.label_2 = customtkinter.CTkLabel(master=self.frame_right,
                                              text="Insert Your Dataset:",
                                              text_font=("Roboto Medium", -15))  # font name and size in px
        self.label_2.grid(row=0, column=2, columnspan=1, pady=20, padx=10, sticky="")

        self.label_3 = customtkinter.CTkLabel(master=self.frame_right,
                                              text="Insert Your Image:",
                                              text_font=("Roboto Medium", -15))  # font name and size in px
        self.label_3.grid(row=2, column=2, columnspan=1, pady=20, padx=10, sticky="")

        self.label_4 = customtkinter.CTkLabel(master=self.frame_right,
                                              text="Result:",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_4.grid(row=6, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.label_5 = customtkinter.CTkLabel(master=self.frame_right,
                                              text="Execution time:",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_5.grid(row=7, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.label_6 = customtkinter.CTkLabel(master=self.frame_right,
                                              text="00.00",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_6.place(x = 1155, y = 565)

        self.label_7 = customtkinter.CTkLabel(master=self.frame_left, image=self.add_logo_image)
        self.label_7.grid(row=4, column=0, pady=10, padx=10)

        self.button_3 = customtkinter.CTkButton(master=self.frame_right, image=self.add_folder_image, compound="right",
                                                text="Insert",
                                                command=self.select_folder,
                                                height=40, width=130)
        self.button_3.grid(row=1, column=2, pady=10, padx=20)

        self.button_4 = customtkinter.CTkButton(master=self.frame_right, image=self.add_list_image, compound="right",
                                                text="Insert",
                                                command=self.select_picture,
                                                height=40, width=130)
        self.button_4.grid(row=3, column=2, pady=10, padx=20)

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Exit",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                bg_color= "#ff0000",
                                                height=40, width=130,
                                                command=self.quit)
        self.button_5.grid(row=10, column=2, columnspan=1, pady=20, padx=20, sticky="we")
        
        self.button_6 = customtkinter.CTkButton(master=self.frame_right, compound="right",
                                                text="",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                state="Disabled",
                                                bg_color="#464646",
                                                height=40, width=40)
        self.button_6.place(x = 1205, y = 415)

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        self.frame_info2.rowconfigure(0, weight=1)
        self.frame_info2.columnconfigure(0, weight=1)

        self.frame_info3.rowconfigure(0, weight=1)
        self.frame_info3.columnconfigure(0, weight=1)

        self.frame_info4.rowconfigure(0, weight=1)
        self.frame_info4.columnconfigure(0, weight=1)

        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text="FACE RECOGNITION",
                                                   text_font=("Roboto Medium", 30), 
                                                   height=100,
                                                   corner_radius=6,  # <- custom corner radius
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

        self.label_info_2 = customtkinter.CTkLabel(master=self.frame_info2,
                                                   text="Test Image",
                                                   text_font=("Roboto Medium", -20), 
                                                   height=100,
                                                   corner_radius=6,  # <- custom corner radius
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        self.label_info_2.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

        self.label_info_3 = customtkinter.CTkLabel(master=self.frame_info3,
                                                   text="Closest Result",
                                                   text_font=("Roboto Medium", -20), 
                                                   height=100,
                                                   corner_radius=6,  # <- custom corner radius
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        self.label_info_3.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

        self.button_6 = customtkinter.CTkButton(master=self.frame_info4,
                                                text="START",
                                                command=self.button_event,
                                                height=40, width=530)
        self.button_6.grid(row=8, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        # set default values
        self.optionmenu_1.set("Dark")

    def button_event(self):
        global closest_result
        start = time.time()
        eigenFace.main(foldername, imagename)
        #eigenFace.facenotfound
        end = time.time()
        timetaken = round(end-start,2)
        self.label_time = customtkinter.CTkLabel(master=self.frame_right,
                                              text=timetaken,
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_time.place(x = 1155, y = 565)
        
        x = Image.open("../test/res.png")
        resize_image = x.resize((400, 400))
        closest_result = ImageTk.PhotoImage(resize_image)

        self.image_label = tkinter.Label(master=self, image=closest_result)
        self.image_label.place(x=1100, y=400)
        self.result()

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
    
    def load_image(self, path, image_size):
        """ load rectangular image with path relative to PATH """
        return ImageTk.PhotoImage(Image.open(PATH + path).resize((image_size, image_size)))

    def select_folder(self):
        global folderTest
        global foldername
        self.foldername = filedialog.askdirectory()
        foldername = self.foldername
        self.folder = customtkinter.CTkLabel(master=self.frame_right, text_font=("Roboto Medium", 10, "bold"),
                                             text=self.foldername.split('/')[len(self.foldername.split('/'))-1]).place(x = 1155, y = 65)

    def select_picture(self):
        global imageTest
        global imagename
        self.imagename = filedialog.askopenfilename(initialdir="ALGEO02-21077", title="Select an image", filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"), ("All Files", "*.*")))
        imagename = self.imagename
        self.image = customtkinter.CTkLabel(master=self.frame_right, text_font=("Roboto Medium", 10, "bold"),
                                             text=self.imagename.split('/')[len(self.imagename.split('/'))-1]).place(x = 1155, y = 265)
        
        img = Image.open(self.imagename)
        imageTest = ImageTk.PhotoImage(img)
        new_width = 100
        new_height = int(new_width*imageTest.height() / imageTest.width())

        if (new_height > 115):
            new_height = 115
            new_width = int(new_width * imageTest.width() / imageTest.height())

        size = img.resize((new_width, new_height), Image.ANTIALIAS)
        imageTest = ImageTk.PhotoImage(size)

        self.label_8 = customtkinter.CTkLabel(master=self.frame_info2, image=imageTest)
        self.label_8.grid(column=0, row=1, sticky="nwe", padx=15, pady=15)
    
    def result(self):
        if (eigenFace.facenotfound) :
            self.label_final = customtkinter.CTkLabel(master=self.frame_right,
                                                text="Tidak Berhasil",
                                                text_font=("Roboto Medium", -16))  # font name and size in px
            self.label_final.place(x=1155, y=500)

            # self.button_6.config(bg_color='red')
            # self.button_6 = customtkinter.CTkButton(bg_color='red')
        else :
            self.label_final = customtkinter.CTkLabel(master=self.frame_right,
                                                text="Berhasil",
                                                text_font=("Roboto Medium", -16))  # font name and size in px
            self.label_final.place(x=1155, y=500)
            # self.button_6.config(bg_color='green')
            # self.button_6 = customtkinter.CTkButton(bg_color='green')
            

if __name__ == "__main__":
    app = App()
    app.mainloop()