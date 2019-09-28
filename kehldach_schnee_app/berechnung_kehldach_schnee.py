from .models import KehldachSchneeModel

def berechnung_mue_wert(self,neigung):


    if 0<= neigung <=30:
        mue_1 = 0.8
        mue_2 = 0.8+0.8*(neigung/30)


    elif 30< neigung <60:
        mue_1 = 0.8*(60-neigung)/30
        mue_2 = 1.6

    else:
        mue_1 = 0
        mue_2 = 0

    mue_werte = [mue_1,mue_2]
    return mue_werte

def berechnung_kehldach_schnee(self):

    eingaben_kehldach_schnee = KehldachSchneeModel.objects.get(pk=self.kwargs['pk'])



    schneeregellast =float(eingaben_kehldach_schnee.projekt.schneelast)

    neigung_alpha1 = float(eingaben_kehldach_schnee.neigung_alpha1)
    neigung_alpha2 = float(eingaben_kehldach_schnee.neigung_alpha2)
    neigung_alpha_strich = (neigung_alpha1+neigung_alpha2)/2


    mue_werte_alpha_1 = berechnung_mue_wert(self, neigung_alpha1)
    mue_werte_alpha_2 = berechnung_mue_wert(self, neigung_alpha2)
    mue_werte_alpha_strich = berechnung_mue_wert(self, neigung_alpha_strich)
    mue_alpha_1 = mue_werte_alpha_1[0]
    mue_alpha_2 = mue_werte_alpha_2[0]
    mue_alpha_strich = mue_werte_alpha_strich[0]


    gesamtschneelast_alpha_1 = mue_alpha_1 *schneeregellast
    gesamtschneelast_alpha_1_rounded = round(gesamtschneelast_alpha_1,2)

    gesamtschneelast_alpha_2 = mue_alpha_2 *schneeregellast

    gesamtschneelast_alpha_2_rounded = round(gesamtschneelast_alpha_2,2)

    gesamtschneelast_alpha_strich = mue_alpha_strich *schneeregellast
    gesamtschneelast_alpha_strich_rounded = round(gesamtschneelast_alpha_strich,2)

    ergebnisse_pultdach_schnee = {'mue_alpha_1':mue_alpha_1,
                                    'mue_alpha_2':mue_alpha_2,
                                    'schneeregellast':schneeregellast,
                                    'neigung_alpha1':neigung_alpha1,
                                    'neigung_alpha2':neigung_alpha2,
                                    'gesamtschneelast_alpha_1_rounded':gesamtschneelast_alpha_1_rounded,
                                    'gesamtschneelast_alpha_2_rounded':gesamtschneelast_alpha_2_rounded,

                                    'gesamtschneelast_alpha_strich_rounded':gesamtschneelast_alpha_strich_rounded,
                                    }
    print(ergebnisse_pultdach_schnee)

    return ergebnisse_pultdach_schnee
