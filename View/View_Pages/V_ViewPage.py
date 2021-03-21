import tkinter as tk
from tkinter import ttk
from pubsub import pub

FONT_BENVINGUDA = ("Verdana", 12)
FONT_TITOL = ("Verdana", 10)
FONT_MSG = ("Verdana", 8)


class ViewPage:
    def __init__(self, parent):
        self.container = parent
        self.crear_view_page()
        self.inserir_view_page()
        return

    def crear_view_page(self):
        """
               Creates the frame and main labels of page_2's UI (View images).
               """

        self.page = tk.Frame(self.container)
        self.p2_label_2 = ttk.Label(self.page, text="Visualitzar imatges", font=FONT_BENVINGUDA)
        self.p2_button_1 = ttk.Button(self.page, text="Enrere", command=self.tornar_main)
        self.crear_elements_p2()

    def inserir_view_page(self):
        self.page.grid(row=0, column=0, sticky="NESW")
        self.p2_label_2.pack(pady=20)
        self.p2_button_1.pack(pady=0)
        self.p2_frame_list.pack(pady=20)
        self.p2_frame_elements.pack(pady=20)
        self.p2_frame_img.grid(row=1, column=1, pady=20, padx=20, sticky="w")
        self.p2_frame_metadata.grid(row=1, column=2, pady=20, padx=20, sticky="w")
    def crear_elements_p2(self):
        """
        Creates and places the main frames and labels of page 2 (View images).
        """

        self.p2_frame_list = tk.Frame(self.page, borderwidth=2, relief="groove")
        self.p2_label_info = ttk.Label(self.p2_frame_list, text="Elements trobats: ", font=FONT_TITOL)
        self.p2_label_info.pack()
        scrollbar = tk.Scrollbar(self.p2_frame_list)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.llista = tk.Listbox(self.p2_frame_list, yscrollcommand=scrollbar.set)
        self.llista.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar.config(command=self.llista.yview)
        self.p2_frame_elements = tk.Frame(self.page)
        self.p2_frame_img = tk.Frame(self.p2_frame_elements)
        self.p2_frame_metadata = tk.Frame(self.p2_frame_elements)
        self.p2_label_metadata_code = ttk.Label(self.p2_frame_metadata, text="", font=FONT_MSG)
        self.p2_label_metadata_code.grid(row=1, column=2, padx=5, pady=5)
        self.p2_label_metadata_grade = ttk.Label(self.p2_frame_metadata, text="", font=FONT_MSG)
        self.p2_label_metadata_grade.grid(row=2, column=2, padx=5, pady=5)
        self.p2_label_metadata_cm = ttk.Label(self.p2_frame_metadata, text="", font=FONT_MSG)
        self.p2_label_metadata_cm.grid(row=3, column=2, padx=5, pady=5)
        self.assemble_img_frame()

    def assemble_img_frame(self):
        """
        Creates and places the label_img of page 2 (View images).
        """

        self.p2_label_img = ttk.Label(self.p2_frame_img, text="<Doble clic per carregar un element de la llista>",
                                      font=FONT_MSG)
        self.p2_label_img.grid(row=1, column=2, padx=5, pady=5)

    def tornar_main(self):
        pub.sendMessage("BACK_TO_MAIN_PAGE")