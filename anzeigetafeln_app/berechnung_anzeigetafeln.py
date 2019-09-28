from .models import AnzeigetafelnModel

def berechnung_anzeigetafel(self):

    eingaben_anzeigetafeln = AnzeigetafelnModel.objects.get(pk=self.kwargs['pk'])



    gelaendekategorie = eingaben_anzeigetafeln.projekt.gelaendekategorie

    basiswinddruck_gewählt =float(eingaben_anzeigetafeln.projekt.basiswinddruck)

    hoehe = float(eingaben_anzeigetafeln.hoehe)
    breite = float(eingaben_anzeigetafeln.breite)
    abstand_zum_grund = float(eingaben_anzeigetafeln.abstand_zum_grund)


    bezugshoehe = round(abstand_zum_grund+hoehe/2, 2)

    if gelaendekategorie == "II":
        qp = basiswinddruck_gewählt * 2.1 * (max(5,bezugshoehe) / 10) ** 0.24
    elif gelaendekategorie == "III":
        qp = basiswinddruck_gewählt * 1.75 * (max(10,bezugshoehe) / 10) ** 0.29
    else:
        qp = basiswinddruck_gewählt * 1.2 * (max(15,bezugshoehe) / 10) ** 0.38


    aref = round(hoehe * breite, 2)
    abstand_e = round(0.25 * breite, 2)
    cf = 1.8

    Kraft_f = round(qp * 1 * aref * cf, 2)

    ergebnisse_anzeigetafeln = {'bezugshoehe':bezugshoehe,
                                'qp':round(qp,2),
                                'aref':aref,
                                'abstand_e':abstand_e,
                                'cf':cf,
                                'Kraft_f':Kraft_f,

                                }
    print(ergebnisse_anzeigetafeln)
    return ergebnisse_anzeigetafeln
