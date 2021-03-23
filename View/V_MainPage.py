import tkinter as tk
from tkinter import ttk
from pubsub import pub

FONT_BENVINGUDA = ("Verdana", 12)
FONT_TITOL = ("Verdana", 10)
FONT_MSG = ("Verdana", 8)


class MainPage:
    def __init__(self, parent):
        self.container = parent
        self.crear_main_page()
        self.inserir_main_page()
        return

    def crear_main_page(self):
        """
        Creates the frame and main labels of page_0's UI (Main Menu).
        """

        self.page = tk.Frame(self.container)
        self.p0_label_0 = ttk.Label(self.page, text="Pressure Injuries Image Analysis", font=FONT_BENVINGUDA)
        self.p0_button_1 = ttk.Button(self.page, text="Processar imatges", command=self.apretar_boto_1)
        self.p0_button_2 = ttk.Button(self.page, text="Visualitzar imatges", command=self.apretar_boto_2)

    def inserir_main_page(self):
        self.page.grid(row=0,column=0, sticky="NESW")
        self.p0_label_0.pack(pady=20)
        self.p0_button_1.pack()
        self.p0_button_2.pack()

    def apretar_boto_1(self):
        """
        Shows page_1 UI (Process images).
        """

        pub.sendMessage("GO_TO_PROCESSING_PAGE")

    def apretar_boto_2(self):
        """
        Shows page_2 UI (View images).
        """
        pub.sendMessage("BUTTON_2_PRESSED")
        pub.sendMessage("GO_TO_VIEW_PAGE")