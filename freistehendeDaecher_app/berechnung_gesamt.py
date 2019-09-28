from .berechnung_freistehendes_pultdach import berechnung_flachdach
from .berechnung_freistehendes_satteldach import berechnung_satteldach
from .models import FreistehendeDaecherModel


def freistehende_daecher_berechnung(self):

    some_field_radio = self.freistehende_daecher.some_field_radio

    if some_field_radio == 'Freistehendes Flach/Pultdach':
        ergebnisse_flachdach = berechnung_flachdach(self)
        #print(ergebnisse_flachdach)
        return ergebnisse_flachdach

        ergebnisse = ergebnisse_flachdach
    else:
        ergebnisse_satteldach = berechnung_satteldach(self)
        #print(ergebnisse_satteldach)


        return ergebnisse_satteldach
