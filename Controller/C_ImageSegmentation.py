from pubsub import pub


class ControllerImageSegmentation:
    def __init__(self, view, pressure_img):
        self.view = view
        self.pressure_img = pressure_img

        pub.subscribe(self.segmentation_gui, "SEGMENTATION_GUI")
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