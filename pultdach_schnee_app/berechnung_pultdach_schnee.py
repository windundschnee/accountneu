from .models import PultdachSchneeModel

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

    return ergebnisse_pultdach_schnee
