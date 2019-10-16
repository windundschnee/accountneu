from .models import PultdachSchneeModel
from allg_berechnungen_app.algemeine_berechnungsfunktionen import liste_runden
from allg_berechnungen_app.schnee_allg_funktionen import berechnung_mue_wert


def berechnung_pultdach_schnee(self):

    eingaben_pultdach_schnee = PultdachSchneeModel.objects.get(pk=self.kwargs['pk'])



    schneeregellast =float(eingaben_pultdach_schnee.projekt.schneelast)

    neigung = float(eingaben_pultdach_schnee.neigung)


    mue_werte = berechnung_mue_wert(self, neigung)

    mue_1 = mue_werte[0]
    if eingaben_pultdach_schnee.abrutschen_verhindert == True:
        mue_1 = max(mue_werte[0],0.8)

    print(mue_1)
    gesamtschneelast = mue_1 *schneeregellast
    gesamtschneelast_rounded = round(gesamtschneelast,2)


    ergebnisse_pultdach_schnee = {'mue_1':mue_1,
                                    'schneeregellast':schneeregellast,
                                    'neigung':neigung,
                                    'gesamtschneelast_rounded':gesamtschneelast_rounded,
                                    }


    return liste_runden(ergebnisse_pultdach_schnee)
