from pubsub import pub
from View import V_Setup
from Model.M_PressureImage import Pressure_img
from Controller import C_Metadata, C_ImagePreSegmentation, C_ImageSegmentation
from Model import M_MetadataManager, M_ImageReader, M_FileDataManager

class ControllerSetup:

    def __init__(self, parent):
        self.parent = parent
        self.model_reader = M_ImageReader.ImageReader()
        self.model_metadata = M_MetadataManager.MetadataManager()
        self.view = V_Setup.ViewSetup(parent)
        self.metadata = C_Metadata.ControllerMetadata(self.model_metadata, self.view)
        self.file_data_manager = M_FileDataManager.FileDataManager()

        pub.subscribe(self.button_1_pressed, "BUTTON_1_PRESSED")
        pub.subscribe(self.button_2_pressed, "BUTTON_2_PRESSED")
        pub.subscribe(self.button_3_pressed, "BUTTON_3_PRESSED")
        pub.subscribe(self.load_image, "LOAD_IMAGE")
        pub.subscribe(self.image_loaded, "IMAGE_LOADED")

        pub.subscribe(self.analyse_image, "ANALYSE_IMAGE")
        pub.subscribe(self.ask_mask_confirmation, "ASK_MASK_CONFIRMATION")
        pub.subscribe(self.pre_segmentation_confirmated, "PRE_SEGMENTATION_CONFIRMATED")

        pub.subscribe(self.segmentation_gui, "SEGMENTATION_GUI")
        pub.subscribe(self.whitebalance, "WHITEBALANCE")
        pub.subscribe(self.whitebalance_confirmated, "WHITEBALANCE_CONFIRMATED")
        pub.subscribe(self.ask_perimeter, "ASK_PERIMETER")

        pub.subscribe(self.target_not_found, "TARGET_NOT_FOUND")

        pub.subscribe(self.ask_roi_confirmation, "ASK_ROI_CONFIRMATION")

        pub.subscribe(self.roi_granulation, "ROI_GRANULATION")
        pub.subscribe(self.roi_necrosis, "ROI_NECROSIS")
        pub.subscribe(self.roi_slough, "ROI_SLOUGH")

        pub.subscribe(self.closed_zone, "CLOSED_ZONE")
        pub.subscribe(self.ring_zone, "RING_ZONE")
        pub.subscribe(self.ring_ext, "RING_EXT")
        pub.subscribe(self.ring_int, "RING_INT")

        pub.subscribe(self.roi_confirmated, "ROI_CONFIRMATED")

        pub.subscribe(self.image_accepted, "IMG_ACCEPTED")

        pub.subscribe(self.tot_ple_ko, "TOT_PLE_KO")
        pub.subscribe(self.data_ko, "DATA_KO")
        pub.subscribe(self.data_ok, "DATA_OK")

        pub.subscribe(self.data_files_ko, "DATA_FILES_KO")
        pub.subscribe(self.data_n_elements, "DATA_N_ELEMENTS")

        pub.subscribe(self.ask_image_i, "ASK_IMAGE_i")
        pub.subscribe(self.load_image_i, "IMAGE_LOAD_i")
        pub.subscribe(self.load_metadata_i, "METADATA_LOAD_i")


    def button_1_pressed(self):
        """
        Prints that button_1 from view has been pressed.
        """

        print("controller - Botó 1!")

    def button_2_pressed(self):
        """
        Prints that button_2 from view has been pressed and calls the function.
        load_data from Data_manager.
        """

        print("MVC controller - Botó 2!")
        self.file_data_manager.load_data()

    def button_3_pressed(self, data):
        """
        Prints that button_3 from view has been pressed.
        Calls the functions to check metadata and images before saving.
        Parameters
        ----------
        data : list
           a list with all the metadata field's information written by the user
        """

        print("controller - Botó 3!")
        #try:
        if self.pressure_img.loaded:
            if self.pressure_img.processed:
                self.model_metadata.getData(data)
            else:
                self.view.popupmsg("És necessari processar la imatge.")
        else:
            self.view.popupmsg("És necessari carregar una imatge")
        #except:
            #self.view.popupmsg("És necessari carregar una imatge")

    def load_image(self):
        """
        Calls the function to load a pressure injury's image.
        WARNING: For optimal visualization, images must be '560x390'
        """

        print("MVC controller - load imatge")
        self.model_reader.carregar_imatge()

    def image_loaded(self, image_original, image_tk):
        """
        Defines a Pressure_img object and saves its image.
        Calls the update_image from View to update the label with the loaded image.
        Calls the function from View to show "process" button.
        Parameters
        ----------
        image_tk : PIL Image
           image ready to be loaded in a label
        """
        self.pressure_img = Pressure_img()
        self.pressure_img.img_origin = image_original
        self.pressure_img.loaded = True
        self.view.processing_page.update_image(image_tk)
        self.view.processing_page.botoImg()
        #self.pre_processing = C_ImagePreSegmentation.ControllerImagePreSegmentation(self.view, self.pressure_img)
        #self.processing = C_ImageSegmentation.ControllerImageSegmentation(self.view, self.pressure_img)

        # PRE-SEGMENTATION

    def analyse_image(self):
        """
        Checks if Pressure_img has been processed and calls processing function if not.
        """
        print("MVC controller - analyse_image!")
        if self.pressure_img.processed == False:
            self.pressure_img.crop_image(self.pressure_img.img_origin)
        else:
            self.view.popupmsg("La imatge ja ha estat processada.")

    def ask_mask_confirmation(self, img_cv2_mask, scale_factor):
        """
        Calls the View function to ask user confirmation about an image's mask.
        Parameters
        ----------
        img_cv2_mask : image cv2
           image that requires user confirmation
        scale_factor : int
           image resize value (default = 100)
        """

        print("MVC controller - ask_mask_confirmation!")
        try:
            self.view.pre_processing_gui.ask_mask_confirmation(img_cv2_mask, scale_factor)
        except:
            self.view.popupmsg("Alguna cosa ha fallat. Torna-ho a intentar!")

    def pre_segmentation_confirmated(self, img_imgtk_mask, img_cv2_mask):
        """
        Calls the Pressure_img function for the first image segmentation.
        Parameters
        ----------
        img_imgtk_mask : PIL Image
           image before cropping roi
        img_cv2_mask : image cv2
           image that requires user confirmation
        """
        print("controller - pre_segmentation_confirmated!")
        scale_factor = 100
        self.pressure_img.begin_segmentation(img_imgtk_mask=img_imgtk_mask, img_cv2_mask=img_cv2_mask,
                                             scale_factor=scale_factor)

    #SEGMENTATION

    def segmentation_gui(self, img_imgtk_mask, img_cv2_mask):
        """
        Updates the Pressure_img mask image, calls the target_detection process and calls the View UI for processing.
        Parameters
        ----------
        img_imgtk_mask : PIL Image BGR
           image before cropping roi
        img_cv2_mask : image cv2 BGR
           image that requires user confirmation
        """
        print("controller - segmentation_gui!")
        self.pressure_img.close_all()
        self.pressure_img.mask = img_cv2_mask
        self.view.processing_gui.segmentation_gui(img_imgtk_mask, img_cv2_mask)

    def whitebalance(self, img_cv2_mask):
        """
        Checks if flash reduction has been called and calls
        Pressure_img function to reduce flash if not.
        Calls the View function to ask user confirmation.
        Parameters
        ----------
        img_cv2_mask : image cv2
           image selected by user to reduce its flash
        """

        print("controller - whitebalance!")
        if self.pressure_img.whitebalanced == False:
                img_whitebalanced = self.pressure_img.target_detector.whiteBalance()
                self.view.processing_gui.ask_whitebalance_confirmation(img_cv2_mask, img_whitebalanced)
        else:
            self.view.popupmsg("Ja s'ha aplicat la reducció.")

    def whitebalance_confirmated(self, img_cv2_whitebalanced):
        """
        Updates Pressure_img mask and flash_reduced boolean.
        Calls the View function to update image label.
        Parameters
        ----------
        img_cv2_mask : image cv2
           image selected and validated by user to reduce its flash
        """

        print("controller - whitebalance_confirmated!")
        self.pressure_img.whitebalanced = True
        self.pressure_img.mask = img_cv2_whitebalanced
        self.pressure_img.img = img_cv2_whitebalanced.copy()
        self.view.processing_gui.update_whitebalanced_label(img_cv2_whitebalanced)

    def ask_perimeter(self):
        """
        Checks if perimeter has been cropped and calls the Pressure_img function if not.
        """

        print("controller - ask_perimeter!")
        img_cv2_mask = self.pressure_img.mask
        if self.pressure_img.perimetre_done:
            self.view.popupmsg("El perímetre ja ha estat seleccionat")
        else:
            self.pressure_img.roi_crop(img_cv2_mask, "Perimeter")

    def target_not_found(self):
        print("controller - target_not_found")
        self.view.popupmsg("Atenció. No s'ha trobat el target!")

    def ask_roi_confirmation(self, img_cv2_mask, img_cv2_roi, tissue, scale_factor, px_perimeter, ring):
        """
        Calls the View function to ask user confirmation about a image's roi.
        Parameters
        ----------
        img_cv2_mask : image cv2
           image before cropping roi
        img_cv2_roi : image cv2
           image that requires user confirmation
        tissue : String
            tissue of the roi
        scale_factor : int
           image resize value (default = 100)
        """
        print("controller - ask_roi_confirmation!")
        self.pressure_img.close_all()
        #try:
        cm_perimeter = px_perimeter * self.pressure_img.target_detector.px_dist
        print("Perímetre zona seleccionada: ",cm_perimeter)
        self.view.processing_gui.ask_roi_confirmation(img_cv2_mask, img_cv2_roi, tissue, scale_factor, ring)
        #except:
            #self.view.popupmsg("Alguna cosa ha fallat. Torna-ho a intentar!")

    def roi_granulation(self):
        """
        Updates the Pressure_img mask image
        Calls the Pressure_img function to allow the user to select the granulation roi.
        """

        print("controller - roi_granulation!")
        self.view.processing_gui.ask_zone_type("Granulation")

    def roi_necrosis(self):
        """
        Updates the Pressure_img mask image
        Calls the Pressure_img function to allow the user to select the necrosis roi.
        """

        print("controller - roi_necrosis!")
        self.view.processing_gui.ask_zone_type("Necrosis")

    def roi_slough(self):
        """
        Updates the Pressure_img mask image
        Calls the Pressure_img function to allow the user to select the slough roi.
        """
        print("controller - roi_slough!")
        self.view.processing_gui.ask_zone_type("Slough")

    def closed_zone(self, tissue):
        img_cv2_mask = self.pressure_img.mask
        self.pressure_img.roi_crop(img_cv2_mask, tissue)

    def ring_zone(self, tissue):
        print("controller - ring_zone!")
        self.view.processing_gui.ask_ring_out(tissue)

    def ring_ext(self, tissue):
        print("controller - ring_ext!")
        img_cv2_mask = self.pressure_img.mask
        self.pressure_img.roi_crop(img_cv2_mask, tissue, 1)

    def ring_int(self, tissue):
        print("controller - ring_int!")
        img_cv2_mask = self.pressure_img.ring_ext
        self.pressure_img.roi_crop(img_cv2_mask, tissue, 2)

    def roi_confirmated(self, img_cv2_roi, tissue, ring):
        """
        Calls the Pressure_img function to update granulation/necrosis/slough fields.
        Parameters
        ----------
        img_cv2_roi : image cv2
           roi selected by the user
        tissue : String
            tissue of the roi
        """
        print("controller - roi_confirmated!")
        self.view.processing_gui.updateLabelGUI(self.pressure_img.mask)
        if(ring == 0):
            #Zona tancada
            self.pressure_img.save_mask_data(img_cv2_roi, tissue)
        if(ring==1):
            #Anella ext
            print("Anella exterior")
            self.pressure_img.ring_ext = img_cv2_roi
            self.view.processing_gui.ask_ring_in(tissue)
        if(ring==2):
            #Anella interna
            print("Anella interior")
            self.pressure_img.ring_int = img_cv2_roi
            self.pressure_img.save_mask_data(img_cv2_roi, tissue)
            #Guardar imatge

    def image_accepted(self):
        """
        Updates Pressure_img processed boolean to True.
        """

        print("controller - image_accepted!")
        self.pressure_img.close_all()
        self.view.processing_page.update_main_label(self.pressure_img.mask)
        self.pressure_img.processed = True

    def tot_ple_ko(self):
        """
        Calls a View function to warn the user that all metadata fields must be filled.
        """

        print("controller - tot_ple_ko!")
        self.view.popupmsg("S'han d'omplir tots els camps")
    def data_ko(self, error):
        """
        Calls a View function to warn the user what field has the wrong input data.
        Parameters
        ----------
        error : list
           wrong input data field's name
        """

        self.view.processing_page.show_error(error)
        print("controller - data_ko")

    def data_ok(self):
        """
        Sets Pressure_img loaded boolean to False.
        Calls View function to reset loaded image label.
        Calls the function to save all the data entered by the user.
        """

        print("controller - data_ok")
        self.pressure_img.loaded = False
        self.view.processing_page.reset_view()
        try:
            self.file_data_manager.save_data(self.model_metadata.metadata, self.pressure_img)
            self.view.popupmsg("Procés finalitzat amb èxit. Prem OK per continuar.")
        except:
            self.view.popupmsg("Error de gestió de fitxers.")

    def data_files_ko(self):
        """
        Calls the View function to warn the user about a file manager error.
        """

        print("controller - data_files_ko")
        self.view.popupmsg("Error de gestió dels fitxers.")

    def data_n_elements(self, num):
        """
        Calls the View function to update the element's label counter with a new value.
        Parameters
        ----------
        num : int
           number of images found in the storage directory
        """

        print("controller - data_n_elements")
        self.view.view_page.update_data_n_elements(num)

    def ask_image_i(self, i):
        """
        Calls the Data_manager functions to read and load the image and metadata "i".
        Parameters
        ----------
        i : int
           id of the image and metadata that have to be read
        """

        print("controller - ask_img_i")
        self.file_data_manager.load_img_i(i)
        self.file_data_manager.load_metadata_i(i)

    def load_image_i(self, img_tk):
        """
        Calls the View function to load the image_tk to the p2_label_img.
        Parameters
        ----------
        img_tk : PIL Image
           image ready to be loaded to a label
        """

        print("controller - load_img_i")
        self.view.view_page.load_image_i(img_tk)

    def load_metadata_i(self, metadata):
        """
        Calls the View function to load the metadata to the p2_label_metadata.
        Parameters
        ----------
        metadata : JSON Object
           data sent to be loaded into a label
        """

        print("controller - load_metadata_i")
        self.view.view_page.load_metadata_i(metadata)