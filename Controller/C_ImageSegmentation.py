from pubsub import pub


class ControllerImageSegmentation:
    def __init__(self, view, pressure_img):
        self.view = view
        self.pressure_img = pressure_img

        #pub.subscribe(self.segmentation_gui, "SEGMENTATION_GUI")
        #pub.subscribe(self.whitebalance, "WHITEBALANCE")
        #pub.subscribe(self.whitebalance_confirmated, "WHITEBALANCE_CONFIRMATED")
        #pub.subscribe(self.ask_perimeter, "ASK_PERIMETER")
        return

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