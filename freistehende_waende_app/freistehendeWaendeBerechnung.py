from .models import FreistehendeWaende


def freistehende_waende_berechnung(self):

    gelaendekategorie = self.freistehende_waende.projekt.gelaendekategorie




    #Eingabewerte einzeln
    basiswinddruck_gewählt =float(self.freistehende_waende.projekt.basiswinddruck)


    #Eingabewerte einzeln
    hoehe_ueber_GOK = float(self.freistehende_waende.hoehe_ueber_GOK)
    wandhoehe = float(self.freistehende_waende.wandhoehe)
    wandlaenge = float(self.freistehende_waende.wandlaenge)
    schenkellaenge = self.freistehende_waende.schenkellaenge

    if schenkellaenge == None:
        schenkellaenge = 0.00
    else:
        schenkellaenge = float(self.freistehende_waende.schenkellaenge)




    voelligkeitsgrad = self.freistehende_waende.voelligkeitsgrad
    abschattung = self.freistehende_waende.abschattung
    if abschattung == 'Ja':
        abstand_abschattendewand = float(self.freistehende_waende.abstand_abschattendewand)
        hoehe_abschattende_wand = float(self.freistehende_waende.hoehe_abschattende_wand)
    else:
        abstand_abschattendewand = 0
        hoehe_abschattende_wand = 0




    z = hoehe_ueber_GOK+wandhoehe
    ze=round(z,2)


    if gelaendekategorie == "II":
        qp = float(basiswinddruck_gewählt) * 2.1 * (max(5,z) / 10) ** 0.24
    elif gelaendekategorie == "III":
        qp = float(basiswinddruck_gewählt) * 1.75 * (max(10,z) / 10) ** 0.29
    else:
        qp = float(basiswinddruck_gewählt) * 1.2 * (max(15,z) / 10) ** 0.38


    l_zu_h = wandlaenge/wandhoehe

    if voelligkeitsgrad == '1,0':

            if  schenkellaenge == 0 and l_zu_h <= 3:
                cpA = 2.3
                cpB = 1.4
                cpC = 1.2
                cpD = 1.2


            elif schenkellaenge == 0 and 3 < l_zu_h <= 5:
                delta = 2
                deltacpA = 0.6
                cpA = round(2.3 + deltacpA / delta * (l_zu_h - 3), 2)
                deltacpB = 0.4
                cpB = round(1.4 + deltacpB / delta * (l_zu_h - 3), 2)
                deltacpC = 0.2
                cpC = round(1.2 + deltacpC / delta * (l_zu_h - 3), 2)
                cpD = 1.2

            elif schenkellaenge == 0 and 5 < l_zu_h <= 10:
                delta = 5
                deltacpA = 0.5
                cpA = round(2.9 + deltacpA / delta * (l_zu_h - 5), 2)
                deltacpB = 0.3
                cpB = round(1.8 + deltacpB / delta * (l_zu_h - 5), 2)
                deltacpC = 0.3
                cpC = round(1.4 + deltacpC / delta * (l_zu_h - 5), 2)
                cpD = 1.2

            elif schenkellaenge == 0 and l_zu_h >= 10:
                cpA = 3.4
                cpB = 2.1
                cpC = 1.7
                cpD = 1.2


            elif  0 < schenkellaenge < wandhoehe and l_zu_h <= 3:
                cpA1 = 2.3
                cpB1 = 1.4
                cpC1 = 1.2
                cpD1 = 1.2

                deltacpA2 = round(cpA1-2.1, 2)
                delta = wandhoehe

                cpA = round(2.1 + deltacpA2 / delta * (wandhoehe-schenkellaenge), 2)
                deltacpB2 = cpB1-1.8
                cpB = round(1.8 + deltacpB2 / delta * (wandhoehe-schenkellaenge), 2)
                cpC = 1.4
                cpD = 1.2

            elif  0 < schenkellaenge < wandhoehe and 3 < l_zu_h <= 5:

                delta = 2
                deltacpA = 0.6
                cpA1 = round(2.3 + deltacpA / delta * (l_zu_h - 3), 2)
                deltacpB = 0.4
                cpB1 = round(1.4 + deltacpB / delta * (l_zu_h - 3), 2)
                deltacpC = 0.2
                cpC1 = round(1.2 + deltacpC / delta * (l_zu_h - 3), 2)


                delta2 = wandhoehe

                deltacpA2 = round(cpA1-2.1, 2)
                cpA = round(2.1 + deltacpA2 / delta2 * (wandhoehe-schenkellaenge), 2)
                deltacpB2 = cpB1-1.8
                cpB = round(1.8 + deltacpB2 / delta2 * (wandhoehe-schenkellaenge), 2)
                deltacpC2 = cpC1-1.4
                cpC = round(1.4 + deltacpC2 / delta2 * (wandhoehe-schenkellaenge), 2)
                cpD = 1.2

            elif  0 < schenkellaenge < wandhoehe and 5 < l_zu_h <= 10:
                delta = 5
                deltacpA = 0.5
                cpA1 = round(2.9 + deltacpA / delta * (l_zu_h - 5), 2)
                deltacpB = 0.3
                cpB1 = round(1.8 + deltacpB / delta * (l_zu_h - 5), 2)
                deltacpC = 0.3
                cpC1 = round(1.4 + deltacpC / delta * (l_zu_h - 5), 2)
                cpD1 = 1.2


                delta2 = wandhoehe
                deltacpA2 = round(cpA1-2.1, 2)

                cpA = round(2.1 + deltacpA2 / delta2 * (wandhoehe-schenkellaenge), 2)
                deltacpB2 = cpB1-1.8
                cpB = round(1.8 + deltacpB2 / delta2 * (wandhoehe-schenkellaenge), 2)
                deltacpC2 = cpC1-1.4
                cpC =  round(1.4 + deltacpC2 / delta2 * (wandhoehe-schenkellaenge), 2)
                cpD = 1.2

            elif  0 < schenkellaenge < wandhoehe and l_zu_h >= 10:
                cpA1 = 3.4
                cpB1 = 2.1
                cpC1 = 1.7
                cpD1 = 1.2

                delta2 = wandhoehe
                deltacpA2 = round(cpA1-2.1, 2)
                cpA = round(2.1 + deltacpA2 / delta2 * (wandhoehe-schenkellaenge), 2)
                deltacpB2 = cpB1-1.8
                cpB = round(1.8 + deltacpB2 / delta2 * (wandhoehe-schenkellaenge), 2)
                deltacpC2 = cpC1-1.4
                cpC = round(1.4 + deltacpC2 / delta2 * (wandhoehe-schenkellaenge), 2)
                cpD = 1.2


            elif schenkellaenge >= wandhoehe:
                cpA = 2.1
                cpB = 1.8
                cpC = 1.4
                cpD = 1.2

            else:
                print("invalid")

    else:
        cpA = 1.2
        cpB = 1.2
        cpC = 1.2
        cpD = 1.2


    if wandlaenge > 4 * wandhoehe:
        laengeA = round(0.3 * wandhoehe, 2)
        laengeB = round(1.7 * wandhoehe, 2)
        laengeC = round(2 * wandhoehe,2 )
        laengeD = round(wandlaenge - 4 * wandhoehe,2)

    if 2 * wandhoehe < wandlaenge <= 4 * wandhoehe:
        laengeA = round(0.3 * wandhoehe, 2)
        laengeB = round(1.7 * wandhoehe, 2)
        laengeC = round(wandlaenge - 2 * wandhoehe,2)
        laengeD = 0

    if wandlaenge <= 2 * wandhoehe:
        laengeA = round(0.3 * wandhoehe, 2)
        laengeB = round(wandlaenge - 0.3 * wandhoehe, 2)
        laengeC = 0
        laengeD = 0


    if abschattung == "Nein":

        chi_schatt = 1

        wA = round(cpA * qp, 2)
        wB = round(cpB * qp, 2)
        wC = round(cpC * qp, 2)
        wD = round(cpD * qp, 2)

        wA_abgem = 0
        wB_abgem = 0
        wC_abgem = 0
        wD_abgem = 0



    if abschattung == "Ja":
        x_zu_h = abstand_abschattendewand / hoehe_abschattende_wand

        if x_zu_h <= 5:
            chi_schatt = 0.3

        if 5 < x_zu_h <= 10 and voelligkeitsgrad == "1,0":
            chi_schatt = round(0.07 * x_zu_h - 0.05, 2)


        if 5 < x_zu_h <= 10 and voelligkeitsgrad == "0,8":
            chi_schatt = round(0.03 * x_zu_h + 0.15, 2)


        if 10 < x_zu_h <= 15 and voelligkeitsgrad == "1,0":
            chi_schatt = round(0.04 * x_zu_h + 0.25, 2)
        if 10 < x_zu_h <= 15 and voelligkeitsgrad == "0.8":
            chi_schatt = round(0.04 * x_zu_h + 0.05, 2)

        if 15 < x_zu_h <= 20 and voelligkeitsgrad == "1,0":
            chi_schatt = round(0.03 * x_zu_h + 0.4, 2)
        if 15 < x_zu_h <= 20 and voelligkeitsgrad == "0,8":
            chi_schatt = round(0.07 * x_zu_h - 0.4, 2)

        if x_zu_h > 20:
            chi_schatt = 1
        #abgeminderte Windlasten
        wA_abgem = round(cpA * qp * chi_schatt, 2)
        wB_abgem = round(cpB * qp * chi_schatt, 2)
        wC_abgem = round(cpC * qp * chi_schatt, 2)
        wD_abgem = round(cpD * qp * chi_schatt, 2)
        #volle Windlasten
        wA = round(cpA * qp, 2)
        wB = round(cpB * qp, 2)
        wC = round(cpC * qp, 2)
        wD = round(cpD * qp, 2)








    ergebnisse_freistehende_waende = {  'l_zu_h':l_zu_h,
                                        'chi_schatt':chi_schatt,
                                        'laengeA':laengeA,
                                        'laengeB':laengeB,
                                        'laengeC':laengeC,
                                        'laengeD':laengeD,
                                        'cpA':cpA,
                                        'cpB':cpB,
                                        'cpC':cpC,
                                        'cpD':cpD,
                                        'qp': qp,
                                        'wA':wA,
                                        'wB':wB,
                                        'wC':wC,
                                        'wD':wD,
                                        'wA_abgem':wA_abgem,
                                        'wB_abgem':wB_abgem,
                                        'wC_abgem':wC_abgem,
                                        'wD_abgem':wD_abgem,
                                        'ze':ze,
                                        }

    return ergebnisse_freistehende_waende
