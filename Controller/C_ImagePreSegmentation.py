from pubsub import pub
from pressure_image import Pressure_img

class ControllerImagePreSegmentation:

    def __init__(self, view, pressure_img):
        self.view = view
        self.pressure_img = pressure_img
        pub.subscribe(self.analyse_image, "ANALYSE_IMAGE")

    def analyse_image(self):
        """
        Checks if Pressure_img has been processed and calls processing function if not.
        """

        print("controller - analyse_image!")
        if self.pressure_img.processed == False:
            self.pressure_img.crop_image(self.pressure_img.img_origin)
        else:
            self.view.popupmsg("La imatge ja ha estat processada.")

