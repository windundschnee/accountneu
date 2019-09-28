from .pultdachBerechnung_EN import pultdach_berechnung_en
from .pultdachBerechnung_NA import pultdach_berechnung_na

def pultdach_berechnung(self):

    verfahren_wahl = self.pultdach.verfahren_wahl
    if verfahren_wahl == 'Verfahren gemäß ÖNORM EN 1991-1-4, Abschnitt 7.2.4':
        ergebnisse_pultdach = pultdach_berechnung_en(self)

    else:
        ergebnisse_pultdach = pultdach_berechnung_na(self)
        print('sVereinfachte Verfahren hani no nöd')
    return ergebnisse_pultdach
