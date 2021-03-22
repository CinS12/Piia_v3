import cv2
from pubsub import pub
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

FONT_BENVINGUDA = ("Verdana", 12)
FONT_TITOL = ("Verdana", 10)
FONT_MSG = ("Verdana", 8)

class SegmentationGUI:

    def __init__(self, parent):
        self.container = parent
        return

    def segmentation_gui(self, img_imgtk_mask, img_cv2_mask):
        """
        Creates a GUI for the image segmentation and processing.
        Parameters
        ----------
        img_imgtk_mask : PIL Image
           image before cropping roi
        img_cv2_mask : image cv2
           image that requires user confirmation
        """

        # Crear la finestra
        self.popup_img = tk.Toplevel()
        ws = self.popup_img.winfo_screenwidth()
        hs = self.popup_img.winfo_screenheight()
        w = 1000
        h = 1100
        x = (ws / 2) - (w / 2)
        y = (hs / 3) - (h / 3)
        self.popup_img.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.popup_img.wm_title("Eina de segmentació")
        # Definir títol del popup
        title = ttk.Label(self.popup_img, text="Selecciona el perímetre total i els diferents tipus de teixits de la ferida:", font=FONT_TITOL)
        title.configure(anchor="center")
        #Frame per les dades
        balance_frame = ttk.Frame(self.popup_img, borderwidth=2, relief="groove")
        data_frame = ttk.Frame(self.popup_img)
        accept_frame = ttk.Frame(self.popup_img)
        # Botons GUI
        button_balance = ttk.Button(balance_frame, text="Whitebalance",command=lambda:self.whitebalance(img_cv2_mask))
        button_perimeter = ttk.Button(data_frame, text="Perimeter",command=self.ask_perimeter)
        button_granulation = ttk.Button(data_frame, text="Granulation", command=self.roi_granulation)
        button_necrosis = ttk.Button(data_frame, text="Necrosis", command=self.roi_necrosis)
        button_slough = ttk.Button(data_frame, text="Slough", command=self.roi_slough)
        button_accept = ttk.Button(accept_frame, text="Accept", command=self.img_processed_accepted)
        #Labels de la GUI
        self.label_balance = tk.Label(balance_frame, text="Eina en desenvolupament, requereix supervisió.", fg="black", font=FONT_MSG)
        self.label_perimeter = tk.Label(data_frame, text="Selecciona el perímetre total de la ferida", fg="black", font=FONT_MSG)
        self.label_granulation = ttk.Label(data_frame, text="Zones seleccionades: 0", font=FONT_MSG)
        self.label_necrosis = ttk.Label(data_frame, text="Zones seleccionades: 0", font=FONT_MSG)
        self.label_slough = ttk.Label(data_frame, text="Zones seleccionades: 0", font=FONT_MSG)
        # Carregar la roi
        self.img_show = tk.Label(self.popup_img, image=img_imgtk_mask)

        #Col·locar els elements
        button_balance.grid(row=1, column=1, padx=5, pady=5)
        self.label_balance.grid(row=1, column=2, padx=5, pady=5)
        button_perimeter.grid(row=2, column=1, padx=5, pady=5)
        self.label_perimeter.grid(row=2, column=2, padx=5, pady=5)
        button_granulation.grid(row=3, column=1, padx=5, pady=5)
        self.label_granulation.grid(row=3, column=2, padx=5, pady=5)
        button_necrosis.grid(row=4, column=1, padx=5, pady=5)
        self.label_necrosis.grid(row=4, column=2, padx=5, pady=5)
        button_slough.grid(row=5, column=1, padx=5, pady=5)
        self.label_slough.grid(row=5, column=2, padx=5, pady=5)
        button_accept.pack()

        title.pack(pady=10)
        balance_frame.pack(pady=5, padx=5)
        data_frame.pack(pady=5, padx=5)
        self.img_show.pack(pady=10)
        accept_frame.pack(pady=10, padx=10)

        self.popup_img.mainloop()