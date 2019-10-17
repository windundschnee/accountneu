from .models import SatteldachSchneeModel
from allg_berechnungen_app.algemeine_berechnungsfunktionen import liste_runden
from allg_berechnungen_app.schnee_allg_funktionen import berechnung_mue_wert
import numpy as np

def berechnung_satteldach_schnee(self):

    eingaben_satteldach_schnee = SatteldachSchneeModel.objects.get(pk=self.kwargs['pk'])



    schneeregellast =float(eingaben_satteldach_schnee.projekt.schneelast)

    neigung_alpha1 = float(eingaben_satteldach_schnee.neigung_alpha1)
    neigung_alpha2 = float(eingaben_satteldach_schnee.neigung_alpha2)


    mue_werte_alpha_1 = berechnung_mue_wert(self, neigung_alpha1)
    mue_werte_alpha_2 = berechnung_mue_wert(self, neigung_alpha2)

    mue_1_alpha_1 = mue_werte_alpha_1[0]
    mue_1_alpha_2 = mue_werte_alpha_2[0]
    mue_2_alpha_1 = mue_werte_alpha_1[1]
    mue_2_alpha_2 = mue_werte_alpha_2[1]
    if eingaben_satteldach_schnee.abrutschen_verhindert == True:
        mue_1_alpha_1 = max(mue_werte_alpha_1[0],0.8)
        mue_1_alpha_2 = max(mue_werte_alpha_2[0],0.8)
        mue_2_alpha_1 = max(mue_werte_alpha_1[1],0.8)
        mue_2_alpha_2 = max(mue_werte_alpha_2[1],0.8)

    mue=[mue_1_alpha_1,mue_1_alpha_2,mue_2_alpha_1,mue_2_alpha_2]

    gesammtschneelast=(np.array(mue)*schneeregellast).tolist()
    gesammtschneelast_halbe=(np.array(mue)*schneeregellast/2).tolist()



    # gesamtschneelast_mue_1_alpha_1 = mue_1_alpha_1 *schneeregellast
    # gesamtschneelast_mue_1_alpha_2 = mue_1_alpha_2 *schneeregellast
    # gesamtschneelast_mue_2_alpha_1 = mue_2_alpha_1 *schneeregellast
    # gesamtschneelast_mue_2_alpha_2 = mue_2_alpha_2 *schneeregellast
    # gesamtschneelast_alpha_2_halbe = gesamtschneelast_alpha_2/2
    # gesamtschneelast_alpha_2_rounded = round(gesamtschneelast_alpha_2,2)

    ergebnisse_schnee = {'mue':mue,
                                    'gesammtschneelast':gesammtschneelast,
                                    'gesammtschneelast_halbe':gesammtschneelast_halbe,
                                    'schneeregellast':schneeregellast,
                                    'neigung_alpha1':neigung_alpha1,
                                    'neigung_alpha2':neigung_alpha2,
                                    # 'gesamtschneelast_alpha_1_rounded':gesamtschneelast_alpha_1_rounded,
                                    # 'gesamtschneelast_alpha_2_rounded':gesamtschneelast_alpha_2_rounded,
                                    # 'gesamtschneelast_alpha_1_halbe':gesamtschneelast_alpha_1_halbe,
                                    # 'gesamtschneelast_alpha_2_halbe':gesamtschneelast_alpha_2_halbe,
                                    }

    return liste_runden(ergebnisse_schnee)
