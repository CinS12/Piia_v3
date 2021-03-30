"""Script with the GUI text in CATALAN.
sectionauthor:: Artur Martí Gelonch <artur.marti@students.salle.url.edu>
WARNING: choose language options still in development (no functional).
"""

class LangCAT:
    def __init__(self):
        #MENU


        #MAIN PAGE
        self.MAIN_TITLE = "Anotació d'imatges d'úlceres de pressió" #"Pressure Injuries Image Analysis"
        self.BUTTON_1 = "Processar imatges"
        self.BUTTON_2 = "Visualitzar imatges"
        # Source: (https://ca.wikipedia.org/wiki/Escala_de_Barthel)
        self.BARTHEL_DESCRIPTION = "Escala ordinal utilitzada per mesurar l'acompliment en activitats de la vida diària bàsiques (AVDB)."
        # Source: (https://www.murciasalud.es/preevid/1103)
        self.EMINA_DESCRIPTION = "L'escala Emina és un instrument de valoració del risc de desenvolupament d'úlceres de pressió en pacients hospitalitzats."

        # SEGMENTATION GUI
        self.HELPER_GRANULATION = "El teixit granulós sol tenir un aspecte vermellós i abultat, semblant a un còdol."
        self.HELPER_NECROSIS = "El teixit necrotic està compost per restes de teixit, múscul, greix, tendó o pell morta."
        self.HELPER_SLOUGH = "El teixit esfàcel és identificat com una massa fibrosa blanca/groga/verda/marró que pot no estar adherida a la zona afectada."
