"""Script with the GUI text in CATALAN.
sectionauthor:: Artur Martí Gelonch <artur.marti@students.salle.url.edu>
WARNING: choose language options still in development (no functional).
"""

class LangCAST:
    def __init__(self):
        #MENU


        #MAIN PAGE
        self.MAIN_TITLE = "Anotación de imágenes de úlceras de presión"
        self.BUTTON_1 = "Procesar imágenes"
        self.BUTTON_2 = "Visualizar imágenes"
        # Source: (https://ca.wikipedia.org/wiki/Escala_de_Barthel)
        self.BARTHEL_DESCRIPTION = "Escalera ordinal utilizada para mesurar el cumplimiento de actividades básicas de la vida diaria (AVDB)."
        # Source: (https://www.murciasalud.es/preevid/1103)
        self.EMINA_DESCRIPTION = "La escalera Emina es un instrumiento de valoración del riesgo de desarrollo de úlceras de presión en pacientes hospitalizados."

        # SEGMENTATION GUI
        self.HELPER_GRANULATION = "El tejido granuloso suele tener un aspecto rojizo i abultado, parecido a un guijarro."
        self.HELPER_NECROSIS = "El tejido necrotico está compuesto por restos de tejido granulado, músculo, grasa, tendón y/o piel muerta."
        self.HELPER_SLOUGH = "El tejido esfacelo se identifica como una masa fibrosa blanca/amarilla/verde/marrón que puede no estar adherida a la zona afectada."
