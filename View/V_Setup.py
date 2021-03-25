import tkinter as tk
from tkinter import ttk
from pubsub import pub
from View import V_MainPage, V_ProcessingPage, V_ViewPage, V_PreSegmentationGUI, V_SegmentationGUI
import abc
from abc import ABC, abstractmethod

FONT_BENVINGUDA = ("Verdana", 12)
FONT_TITOL = ("Verdana", 10)
FONT_MSG = ("Verdana", 8)

class ViewSetup:

    def __init__(self, parent):
        self.container = parent
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_rowconfigure(0, weight=1)
        self.setup()

        pub.subscribe(self.back_to_main_page, "BACK_TO_MAIN_PAGE")
        pub.subscribe(self.go_to_processing_page, "GO_TO_PROCESSING_PAGE")
        pub.subscribe(self.go_to_view_page, "GO_TO_VIEW_PAGE")
        pub.subscribe(self.popupmsg, "POPUP_MSG")
        return

    def setup(self):
        """
        Calls the functions to create and show the main window.
        """
        self.main_page = V_MainPage.MainPage(self.container)
        self.processing_page = V_ProcessingPage.ProcessingPage(self.container)
        self.view_page = V_ViewPage.ViewPage(self.container)
        self.pre_processing_gui = V_PreSegmentationGUI.PreSegmentationGUI(self.container)
        self.processing_gui = V_SegmentationGUI.SegmentationGUI(self.container)
        self.crear_menu()
        self.main_page.page.tkraise()

    def crear_menu(self):
        """
        Creates and configures the top menu bar widget.
        """

        self.menubar = tk.Menu(self.container)

        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.file_menu.add_command(label="Save settings", command=lambda: self.popupmsg("Pàgina en construcció!"))
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=quit)
        self.menubar.add_cascade(label="File", menu=self.file_menu)

        language_menu = tk.Menu(self.menubar, tearoff=0)
        language_menu.add_command(label="Català", command=lambda: self.popupmsg("Pàgina en construcció!"))
        language_menu.add_command(label="Castellano", command=lambda: self.popupmsg("Página en construcción!"))
        language_menu.add_command(label="English", command=lambda: self.popupmsg("Page is still building!"))
        self.menubar.add_cascade(label="Language", menu=language_menu)
        self.container.config(menu=self.menubar)

    def back_to_main_page(self):
        self.main_page.page.tkraise()

    def go_to_processing_page(self):
        self.processing_page.page.tkraise()

    def go_to_view_page(self):
        self.view_page.page.tkraise()

    def popupmsg(self, msg):
        """
        Displays a popup window with the message.
        Parameters
        ----------
        msg : String
           message that will be displayed to user
        """

        popup = tk.Toplevel()
        ws = popup.winfo_screenwidth()
        hs = popup.winfo_screenheight()
        w = 300
        h = 75
        x = (ws / 2) - (w / 2)
        y = (hs / 3) - (h / 3)
        popup.geometry('%dx%d+%d+%d' % (w, h, x, y))
        popup.wm_title("Atenció")
        label = ttk.Label(popup, text=msg, font=FONT_MSG)
        label.configure(anchor="center")
        label.pack(side="top", fill="x", pady=10)
        button1 = ttk.Button(popup, text="Ok", command=popup.destroy)
        button1.pack()
        popup.mainloop()

    def data_ko(self, error):
        """
        Calls a View function to warn the user what field has the wrong input data.
        Parameters
        ----------
        error : list
           wrong input data field's name
        """

        self.view.show_error(error)
        print("controller - data_ko")

    def data_ok(self):
        """
        Sets Pressure_img loaded boolean to False.
        Calls View function to reset loaded image label.
        Calls the function to save all the data entered by the user.
        """

        print("controller - data_ok")
        self.pressure_img.loaded = False
        self.view.reset_view()
        try:
            self.save_data_file()
            self.view.popupmsg("Procés finalitzat amb èxit. Prem OK per continuar.")
        except:
            self.view.popupmsg("Error de gestió de fitxers.")