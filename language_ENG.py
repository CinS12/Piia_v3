"""Script with the GUI text in CATALAN.
sectionauthor:: Artur Martí Gelonch <artur.marti@students.salle.url.edu>
WARNING: choose language options still in development (no functional).
"""
class LangENG:
    def __init__(self):

        #MENU


        #MAIN PAGE
        self.MAIN_TITLE = "Pressure Injuries Image Analysis"
        self.BUTTON_1 = "Image processing"
        self.BUTTON_2 = "Image viewer"
        # Source: (https://ca.wikipedia.org/wiki/Escala_de_Barthel)
        BARTHEL_DESCRIPTION = "Escala ordinal utilitzada per mesurar l'acompliment en activitats de la vida diària bàsiques (AVDB)."
        # Source: (https://www.murciasalud.es/preevid/1103)
        EMINA_DESCRIPTION = "L'escala Emina és un instrument de valoració del risc de desenvolupament d'úlceres de pressió en pacients hospitalitzats."

        # SEGMENTATION GUI
        self.HELPER_GRANULATION = "Granulation tissue often appears as red, bumpy tissue that is described as “cobblestone-like” in appearance."
        self.HELPER_NECROSIS = "Necrosis tissue is composed of dead granulation tissue, muscle, fat, tendon or skin."
        self.HELPER_SLOUGH = "Slough can be identified as a stringy white/yellow/green/brown mass that may or may not be firmly attached to surrounding tissue."