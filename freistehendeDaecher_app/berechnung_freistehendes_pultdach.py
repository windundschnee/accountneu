def berechnung_qp(self):


    basiswinddruck_gewählt =float(self.freistehende_daecher.projekt.basiswinddruck)
    gelaendekategorie = self.freistehende_daecher.projekt.gelaendekategorie

    hoehe_GOK = float(self.freistehende_daecher.hoehe_GOK)
    hoehe = float(self.freistehende_daecher.hoehe)
    ze = hoehe_GOK + hoehe


    if gelaendekategorie == "II":
        qp = basiswinddruck_gewählt * 2.1 * (max(5,ze) / 10) ** 0.24
    elif gelaendekategorie == "III":
        qp = basiswinddruck_gewählt * 1.75 * (max(10,ze) / 10) ** 0.29
    else:
	    qp = basiswinddruck_gewählt * 1.2 * (max(15,ze) / 10) ** 0.38

    return qp

def berechnung_flachdach(self):
    qp = berechnung_qp(self)


    breite_d = float(self.freistehende_daecher.breite_d)
    breite_b = float(self.freistehende_daecher.breite_b)
    hoehe = float(self.freistehende_daecher.hoehe)



    aref = breite_b * breite_d
    d_viertel = breite_d/4
    b_zehntel = breite_b/10
    d_zehntel = breite_d/10
    kraftbeiwerte_flachdach = berechnung_flachdach_beiwerte(self)

    ergebnisse_cf = kraftbeiwerte_flachdach['ergebnisse_cf']
    ergebnisse_cpA = kraftbeiwerte_flachdach['ergebnisse_cpA']
    ergebnisse_cpB = kraftbeiwerte_flachdach['ergebnisse_cpB']
    ergebnisse_cpC = kraftbeiwerte_flachdach['ergebnisse_cpC']

    cf_druck = ergebnisse_cf[0]
    cf_sog = ergebnisse_cf[1]

    cpA_druck = ergebnisse_cpA[0]
    cpA_sog = ergebnisse_cpA[1]

    cpB_druck = ergebnisse_cpB[0]
    cpB_sog = ergebnisse_cpB[1]

    cpC_druck = ergebnisse_cpC[0]
    cpC_sog = ergebnisse_cpC[1]

    Kraft_druck = round(cf_druck*aref*qp, 2)
    Kraft_sog = round(cf_sog*aref*qp, 2)
    #Winddruck Fläche A
    wA_druck = round(cpA_druck*qp, 2)
    wA_sog = round(cpA_sog*qp, 2)
    #Winddruck Fläche A
    wB_druck = round(cpB_druck*qp, 2)
    wB_sog = round(cpB_sog*qp, 2)
    #Winddruck Fläche A
    wC_druck = round(cpC_druck*qp, 2)
    wC_sog = round(cpC_sog*qp, 2)


    ergebnisse_flachdach = [aref, d_viertel, b_zehntel, d_zehntel,qp,
                            kraftbeiwerte_flachdach, Kraft_druck, Kraft_sog,
                            wA_druck, wA_sog, wB_druck, wB_sog ,wC_druck,
                            wC_sog]
    return ergebnisse_flachdach




def berechnung_flachdach_beiwerte(self):
    alpha = float(self.freistehende_daecher.alpha)
    phi = float(self.freistehende_daecher.phi)


    liste_0_grad_cf = [phi, 0.2,    -0.5, -1.3, 0.5, -0.6, -1.5, 1.8, -1.3, -1.8, 1.1, -1.4, -2.2]
    liste_5_grad_cf = [phi, 0.4,    -0.7, -1.4, 0.8, -1.1, -1.6, 2.1, -1.7, -2.2, 1.3, -1.8, -2.5]
    liste_10_grad_cf = [phi, 0.5,   -0.9, -1.4, 1.2, -1.5, -1.6, 2.4, -2, -2.6, 1.6, -2.1, -2.7]
    liste_15_grad_cf = [phi, 0.7,   -1.1, -1.4, 1.4, -1.8, -1.6, 2.7, -2.4, -2.9, 1.8, -2.5, -3]
    liste_20_grad_cf = [phi, 0.8,   -1.3, -1.4, 1.7, -2.2, -1.6, 2.9, -2.8, -2.9, 2.1, -2.9, -3]
    liste_25_grad_cf = [phi, 1,     -1.6, -1.4, 2,   -2.6, -1.5, 3.1, -3.2, -2.5, 2.3, -3.2, -2.8]
    liste_30_grad_cf = [phi, 1.2,   -1.8, -1.4, 2.2, -3,   -1.5, 3.2, -3.8, -2.2, 2.4, -3.6, -2.7]


    if alpha == 0:
        cf_1 = function_cf(liste_0_grad_cf)
        cf = cf_1
        cf_druck_1 = liste_0_grad_cf[1]
        ergebnisse_cf = [cf_druck_1, cf]

        #Winddruck Bereich A

        cpA_1 = function_flaeche_A(liste_0_grad_cf)
        cpA = cpA_1
        cpA_druck_1 = liste_0_grad_cf[4]
        ergebnisse_Flache_A = [cpA_druck_1, cpA]


        cpB_1 = function_flaeche_B(liste_0_grad_cf)
        cpB = cpB_1
        cpB_druck_1 = liste_0_grad_cf[7]
        ergebnisse_Flache_B = [cpB_druck_1, cpB]


        cpC_1 = function_flaeche_C(liste_0_grad_cf)
        cpC = cpC_1
        cpC_druck_1 = liste_0_grad_cf[10]

        ergebnisse_Flache_C = [cpC_druck_1, cpC]




    elif 0 < alpha <= 5:
        #Untere Schranke cf alpha = 0°
        cf_1 = function_cf(liste_0_grad_cf)
        #Obere Schranke cf alpha = 5°
        cf_2 = function_cf(liste_5_grad_cf)
        #Interpolation der cf-Werte Sog zwischen phi 0-1
        cf = cf_1 + ((cf_2-cf_1)/5)*alpha
        #cf-Werte Sog
        cf_druck_1 = liste_0_grad_cf[1]
        cf_druck_2 = liste_5_grad_cf[1]
        #Interpolation der cf-Werte Druck zwischen phi 0-1
        cf_druck = cf_druck_1 + ((cf_druck_2-cf_druck_1)/5)*alpha
        #Ergebnisse
        ergebnisse_cf = [cf_druck, cf]

        #Winddruck Bereich A obere Schranke alpha = 0°
        cpA_1 = function_flaeche_A(liste_0_grad_cf)
        #Winddruck Bereich A untere Schranke alpha = 5°
        cpA_2 = function_flaeche_A(liste_5_grad_cf)
        #Interpolation der cpA-Werte zwischen
        cpA = cpA_1 + ((cpA_2-cpA_1)/5)*alpha
        #cpA-Werte Sog
        cpA_druck_1 = liste_0_grad_cf[4]
        cpA_druck_2 = liste_5_grad_cf[4]
        #Interpolation der cpA-Werte Druck zwischen phi 0-1
        cpA_druck = cpA_druck_1 + ((cpA_druck_2-cpA_druck_1)/5)*alpha
        #Ergebnisse
        ergebnisse_cpA = [cpA_druck, cpA]


        #Winddruck Bereich B obere Schranke alpha = 0°
        cpB_1 = function_flaeche_B(liste_0_grad_cf)
        #Winddruck Bereich A untere Schranke alpha = 5°
        cpB_2 = function_flaeche_B(liste_5_grad_cf)
        #Interpolation der cf-Werte zwischen
        cpB = cpB_1 + ((cpB_2-cpB_1)/5)*alpha
        #cpC-Werte Sog
        cpB_druck_1 = liste_0_grad_cf[7]
        cpB_druck_2 = liste_5_grad_cf[7]
        #Interpolation der cpC-Werte Druck zwischen phi 0-1
        cpB_druck = cpB_druck_1 + ((cpB_druck_2-cpB_druck_1)/5)*alpha
        #Ergebnisse
        ergebnisse_cpB = [cpB_druck, cpB]



        #Winddruck Bereich C obere Schranke alpha = 0°
        cpC_1 = function_flaeche_C(liste_0_grad_cf)
        #Winddruck Bereich A untere Schranke alpha = 5°
        cpC_2 = function_flaeche_C(liste_5_grad_cf)
        #Interpolation der cpC-Werte zwischen
        cpC = cpC_1 + ((cpC_2-cpC_1)/5)*alpha
        #cpC-Werte Sog
        cpC_druck_1 = liste_0_grad_cf[10]
        cpC_druck_2 = liste_5_grad_cf[10]
        #Interpolation der cpC-Werte Druck zwischen phi 0-1
        cpC_druck = cpC_druck_1 + ((cpC_druck_2-cpC_druck_1)/5)*alpha
        #Ergebnisse
        ergebnisse_cpC = [cpC_druck, cpC]




    elif 5 < alpha <= 10:
        #Untere Schranke cf alpha = 5°
        cf_1 = function_cf(liste_5_grad_cf)
        #Obere Schranke cf alpha = 10°
        cf_2 = function_cf(liste_10_grad_cf)
        #Interpolation der cf-Werte zwischen
        cf = cf_1 + ((cf_2-cf_1)/5)*(alpha-5)
        #cf-Werte Sog
        cf_druck_1 = liste_5_grad_cf[1]
        cf_druck_2 = liste_10_grad_cf[1]
        #Interpolation der cf-Werte Druck zwischen phi 0-1
        cf_druck = cf_druck_1 + ((cf_druck_2-cf_druck_1)/5)*(alpha-5)
        #Ergebnisse
        ergebnisse_cf = [cf_druck, cf]

        #Winddruck Bereich A obere Schranke alpha = 5°
        cpA_1 = function_flaeche_A(liste_5_grad_cf)
        #Winddruck Bereich A untere Schranke alpha = 10°
        cpA_2 = function_flaeche_A(liste_10_grad_cf)
        #Interpolation Winddruck Bereich A
        cpA = cpA_1 + ((cpA_2-cpA_1)/5)*(alpha-5)

        #cpA-Werte Sog
        cpA_druck_1 = liste_5_grad_cf[4]
        cpA_druck_2 = liste_10_grad_cf[4]
        #Interpolation der cpA-Werte Druck zwischen phi 0-1
        cpA_druck = cpA_druck_1 + ((cpA_druck_2-cpA_druck_1)/5)*(alpha-5)
        #Ergebnisse
        ergebnisse_cpA = [cpA_druck, cpA]


        #Winddruck Bereich B obere Schranke alpha = 0°
        cpB_1 = function_flaeche_B(liste_5_grad_cf)
        #Winddruck Bereich A untere Schranke alpha = 5°
        cpB_2 = function_flaeche_B(liste_10_grad_cf)
        #Interpolation der cf-Werte zwischen
        cpB = cpB_1 + ((cpB_2-cpB_1)/5)*(alpha-5)
        #cpC-Werte Sog
        cpB_druck_1 = liste_5_grad_cf[7]
        cpB_druck_2 = liste_10_grad_cf[7]
        #Interpolation der cpC-Werte Druck zwischen phi 0-1
        cpB_druck = cpB_druck_1 + ((cpB_druck_2-cpB_druck_1)/5)*(alpha-5)
        #Ergebnisse
        ergebnisse_cpB = [cpB_druck, cpB]


        #Winddruck Bereich C obere Schranke alpha = 0°
        cpC_1 = function_flaeche_C(liste_5_grad_cf)
        #Winddruck Bereich A untere Schranke alpha = 5°
        cpC_2 = function_flaeche_C(liste_10_grad_cf)
        #Interpolation der cf-Werte zwischen
        cpC = cpC_1 + ((cpC_2-cpC_1)/5)*(alpha-5)

        #cpC-Werte Sog
        cpC_druck_1 = liste_5_grad_cf[10]
        cpC_druck_2 = liste_10_grad_cf[10]
        #Interpolation der cpC-Werte Druck zwischen phi 0-1
        cpC_druck = cpC_druck_1 + ((cpC_druck_2-cpC_druck_1)/5)*(alpha-5)
        #Ergebnisse
        ergebnisse_cpC = [cpC_druck, cpC]



    elif 10 < alpha <= 15:
        #Untere Schranke cf alpha = 5°
        cf_1 = function_cf(liste_10_grad_cf)
        #Obere Schranke cf alpha = 10°
        cf_2 = function_cf(liste_15_grad_cf)
        #Interpolation der cf-Werte zwischen
        cf = cf_1 + ((cf_2-cf_1)/5)*(alpha-10)

        #cf-Werte Sog
        cf_druck_1 = liste_10_grad_cf[1]
        cf_druck_2 = liste_15_grad_cf[1]
        #Interpolation der cf-Werte Druck zwischen phi 0-1
        cf_druck = cf_druck_1 + ((cf_druck_2-cf_druck_1)/5)*(alpha-10)
        #Ergebnisse
        ergebnisse_cf = [cf_druck, cf]

        #Winddruck Bereich A obere Schranke alpha = 5°
        cpA_1 = function_flaeche_A(liste_10_grad_cf)
        #Winddruck Bereich A untere Schranke alpha = 10°
        cpA_2 = function_flaeche_A(liste_15_grad_cf)
        #Interpolation Winddruck Bereich A
        cpA = cpA_1 + ((cpA_2-cpA_1)/5)*(alpha-10)

        #cpA-Werte Sog
        cpA_druck_1 = liste_10_grad_cf[4]
        cpA_druck_2 = liste_15_grad_cf[4]
        #Interpolation der cpA-Werte Druck zwischen phi 0-1
        cpA_druck = cpA_druck_1 + ((cpA_druck_2-cpA_druck_1)/5)*(alpha-10)
        #Ergebnisse
        ergebnisse_cpA = [cpA_druck, cpA]



        #Winddruck Bereich B obere Schranke alpha = 0°
        cpB_1 = function_flaeche_B(liste_10_grad_cf)
        #Winddruck Bereich A untere Schranke alpha = 5°
        cpB_2 = function_flaeche_B(liste_15_grad_cf)
        #Interpolation der cf-Werte zwischen
        cpB = cpB_1 + ((cpB_2-cpB_1)/5)*(alpha-10)
        #cpB-Werte Sog
        cpB_druck_1 = liste_10_grad_cf[7]
        cpB_druck_2 = liste_15_grad_cf[7]
        #Interpolation der cpC-Werte Druck zwischen phi 0-1
        cpB_druck = cpB_druck_1 + ((cpB_druck_2-cpB_druck_1)/5)*(alpha-10)
        #Ergebnisse
        ergebnisse_cpB = [cpB_druck, cpB]


        #Winddruck Bereich C obere Schranke alpha = 0°
        cpC_1 = function_flaeche_C(liste_10_grad_cf)
        #Winddruck Bereich A untere Schranke alpha = 5°
        cpC_2 = function_flaeche_C(liste_15_grad_cf)
        #Interpolation der cf-Werte zwischen
        cpC = cpC_1 + ((cpC_2-cpC_1)/5)*(alpha-10)

        #cpC-Werte Sog
        cpC_druck_1 = liste_10_grad_cf[10]
        cpC_druck_2 = liste_15_grad_cf[10]
        #Interpolation der cpC-Werte Druck zwischen phi 0-1
        cpC_druck = cpC_druck_1 + ((cpC_druck_2-cpC_druck_1)/5)*(alpha-10)
        #Ergebnisse
        ergebnisse_cpC = [cpC_druck, cpC]


    elif 15 < alpha <= 20:
        #Untere Schranke cf alpha = 5°
        cf_1 = function_cf(liste_15_grad_cf)
        #Obere Schranke cf alpha = 10°
        cf_2 = function_cf(liste_20_grad_cf)
        #Interpolation der cf-Werte zwischen
        cf = cf_1 + ((cf_2-cf_1)/5)*(alpha-15)

        #cf-Werte Sog
        cf_druck_1 = liste_15_grad_cf[1]
        cf_druck_2 = liste_20_grad_cf[1]
        #Interpolation der cf-Werte Druck zwischen phi 0-1
        cf_druck = cf_druck_1 + ((cf_druck_2-cf_druck_1)/5)*(alpha-15)
        #Ergebnisse
        ergebnisse_cf = [cf_druck, cf]

        #Winddruck Bereich A obere Schranke alpha = 5°
        cpA_1 = function_flaeche_A(liste_15_grad_cf)
        #Winddruck Bereich A untere Schranke alpha = 10°
        cpA_2 = function_flaeche_A(liste_20_grad_cf)
        #Interpolation Winddruck Bereich A
        cpA = cpA_1 + ((cpA_2-cpA_1)/5)*(alpha-15)

        #cpA-Werte Sog
        cpA_druck_1 = liste_15_grad_cf[4]
        cpA_druck_2 = liste_20_grad_cf[4]
        #Interpolation der cpA-Werte Druck zwischen phi 0-1
        cpA_druck = cpA_druck_1 + ((cpA_druck_2-cpA_druck_1)/5)*(alpha-15)
        #Ergebnisse
        ergebnisse_cpA = [cpA_druck, cpA]


        #Winddruck Bereich B obere Schranke alpha = 0°
        cpB_1 = function_flaeche_B(liste_15_grad_cf)
        #Winddruck Bereich A untere Schranke alpha = 5°
        cpB_2 = function_flaeche_B(liste_20_grad_cf)
        #Interpolation der cf-Werte zwischen
        cpB = cpB_1 + ((cpB_2-cpB_1)/5)*(alpha-15)

        #cpB-Werte Sog
        cpB_druck_1 = liste_15_grad_cf[7]
        cpB_druck_2 = liste_20_grad_cf[7]
        #Interpolation der cpC-Werte Druck zwischen phi 0-1
        cpB_druck = cpB_druck_1 + ((cpB_druck_2-cpB_druck_1)/5)*(alpha-15)
        #Ergebnisse
        ergebnisse_cpB = [cpB_druck, cpB]

        #Winddruck Bereich C obere Schranke alpha = 0°
        cpC_1 = function_flaeche_C(liste_15_grad_cf)
        #Winddruck Bereich A untere Schranke alpha = 5°
        cpC_2 = function_flaeche_C(liste_20_grad_cf)
        #Interpolation der cf-Werte zwischen
        cpC = cpC_1 + ((cpC_2-cpC_1)/5)*(alpha-15)

        #cpC-Werte Sog
        cpC_druck_1 = liste_15_grad_cf[10]
        cpC_druck_2 = liste_20_grad_cf[10]
        #Interpolation der cpC-Werte Druck zwischen phi 0-1
        cpC_druck = cpC_druck_1 + ((cpC_druck_2-cpC_druck_1)/5)*(alpha-15)
        #Ergebnisse
        ergebnisse_cpC = [cpC_druck, cpC]

    elif 20 < alpha <= 25:
        #Untere Schranke cf alpha = 5°
        cf_1 = function_cf(liste_20_grad_cf)
        #Obere Schranke cf alpha = 10°
        cf_2 = function_cf(liste_25_grad_cf)
        #Interpolation der cf-Werte zwischen
        cf = cf_1 + ((cf_2-cf_1)/5)*(alpha-20)

        #cf-Werte Sog
        cf_druck_1 = liste_20_grad_cf[1]
        cf_druck_2 = liste_25_grad_cf[1]
        #Interpolation der cf-Werte Druck zwischen phi 0-1
        cf_druck = cf_druck_1 + ((cf_druck_2-cf_druck_1)/5)*(alpha-20)
        #Ergebnisse
        ergebnisse_cf = [cf_druck, cf]

        #Winddruck Bereich A obere Schranke alpha = 5°
        cpA_1 = function_flaeche_A(liste_20_grad_cf)
        #Winddruck Bereich A untere Schranke alpha = 10°
        cpA_2 = function_flaeche_A(liste_25_grad_cf)
        #Interpolation Winddruck Bereich A
        cpA = cpA_1 + ((cpA_2-cpA_1)/5)*(alpha-20)

        #cpA-Werte Sog
        cpA_druck_1 = liste_20_grad_cf[4]
        cpA_druck_2 = liste_25_grad_cf[4]
        #Interpolation der cpA-Werte Druck zwischen phi 0-1
        cpA_druck = cpA_druck_1 + ((cpA_druck_2-cpA_druck_1)/5)*(alpha-20)
        #Ergebnisse
        ergebnisse_cpA = [cpA_druck, cpA]

        #Winddruck Bereich B obere Schranke alpha = 0°
        cpB_1 = function_flaeche_B(liste_20_grad_cf)
        #Winddruck Bereich A untere Schranke alpha = 5°
        cpB_2 = function_flaeche_B(liste_25_grad_cf)
        #Interpolation der cf-Werte zwischen
        cpB = cpB_1 + ((cpB_2-cpB_1)/5)*(alpha-20)

        #cpB-Werte Sog
        cpB_druck_1 = liste_20_grad_cf[7]
        cpB_druck_2 = liste_25_grad_cf[7]
        #Interpolation der cpC-Werte Druck zwischen phi 0-1
        cpB_druck = cpB_druck_1 + ((cpB_druck_2-cpB_druck_1)/5)*(alpha-20)
        #Ergebnisse
        ergebnisse_cpB = [cpB_druck, cpB]

        #Winddruck Bereich C obere Schranke alpha = 0°
        cpC_1 = function_flaeche_C(liste_20_grad_cf)
        #Winddruck Bereich A untere Schranke alpha = 5°
        cpC_2 = function_flaeche_C(liste_25_grad_cf)
        #Interpolation der cf-Werte zwischen
        cpC = cpC_1 + ((cpC_2-cpC_1)/5)*(alpha-20)

        #cpC-Werte Sog
        cpC_druck_1 = liste_20_grad_cf[10]
        cpC_druck_2 = liste_25_grad_cf[10]
        #Interpolation der cpC-Werte Druck zwischen phi 0-1
        cpC_druck = cpC_druck_1 + ((cpC_druck_2-cpC_druck_1)/5)*(alpha-20)
        #Ergebnisse
        ergebnisse_cpC = [cpC_druck, cpC]

    elif 25 < alpha <= 30:
        #Untere Schranke cf alpha = 5°
        cf_1 = function_cf(liste_25_grad_cf)
        #Obere Schranke cf alpha = 10°
        cf_2 = function_cf(liste_30_grad_cf)
        #Interpolation der cf-Werte zwischen
        cf = cf_1 + ((cf_2-cf_1)/5)*(alpha-25)

        #cf-Werte Sog
        cf_druck_1 = liste_25_grad_cf[1]
        cf_druck_2 = liste_30_grad_cf[1]
        #Interpolation der cf-Werte Druck zwischen phi 0-1
        cf_druck = cf_druck_1 + ((cf_druck_2-cf_druck_1)/5)*(alpha-25)
        #Ergebnisse
        ergebnisse_cf = [cf_druck, cf]

        #Winddruck Bereich A obere Schranke alpha = 5°
        cpA_1 = function_flaeche_A(liste_25_grad_cf)
        #Winddruck Bereich A untere Schranke alpha = 10°
        cpA_2 = function_flaeche_A(liste_30_grad_cf)
        #Interpolation Winddruck Bereich A
        cpA = cpA_1 + ((cpA_2-cpA_1)/5)*(alpha-25)

        #cpA-Werte Sog
        cpA_druck_1 = liste_25_grad_cf[4]
        cpA_druck_2 = liste_30_grad_cf[4]
        #Interpolation der cpA-Werte Druck zwischen phi 0-1
        cpA_druck = cpA_druck_1 + ((cpA_druck_2-cpA_druck_1)/5)*(alpha-25)
        #Ergebnisse
        ergebnisse_cpA = [cpA_druck, cpA]

        #Winddruck Bereich B obere Schranke alpha = 0°
        cpB_1 = function_flaeche_B(liste_25_grad_cf)
        #Winddruck Bereich A untere Schranke alpha = 5°
        cpB_2 = function_flaeche_B(liste_30_grad_cf)
        #Interpolation der cf-Werte zwischen
        cpB = cpB_1 + ((cpB_2-cpB_1)/5)*(alpha-25)

        #cpB-Werte Sog
        cpB_druck_1 = liste_25_grad_cf[7]
        cpB_druck_2 = liste_30_grad_cf[7]
        #Interpolation der cpC-Werte Druck zwischen phi 0-1
        cpB_druck = cpB_druck_1 + ((cpB_druck_2-cpB_druck_1)/5)*(alpha-25)
        #Ergebnisse
        ergebnisse_cpB = [cpB_druck, cpB]

        #Winddruck Bereich C obere Schranke alpha = 0°
        cpC_1 = function_flaeche_C(liste_25_grad_cf)
        #Winddruck Bereich A untere Schranke alpha = 5°
        cpC_2 = function_flaeche_C(liste_30_grad_cf)
        #Interpolation der cf-Werte zwischen
        cpC = cpC_1 + ((cpC_2-cpC_1)/5)*(alpha-25)

        #cpC-Werte Sog
        cpC_druck_1 = liste_25_grad_cf[10]
        cpC_druck_2 = liste_30_grad_cf[10]
        #Interpolation der cpC-Werte Druck zwischen phi 0-1
        cpC_druck = cpC_druck_1 + ((cpC_druck_2-cpC_druck_1)/5)*(alpha-25)
        #Ergebnisse
        ergebnisse_cpC = [cpC_druck, cpC]

    else:

        print('alpha ist nicht 0 <= alpha <=30')

    ergebnisse_anzeigetafeln = { 'ergebnisse_cf':ergebnisse_cf,
                                'ergebnisse_cpA':ergebnisse_cpA,
                                'ergebnisse_cpB':ergebnisse_cpB,
                                'ergebnisse_cpC':ergebnisse_cpC,

                                }

    return ergebnisse_anzeigetafeln


def function_cf(liste_0_grad_cf):
    phi = liste_0_grad_cf[0]

    cf_sog_min_1 = liste_0_grad_cf[2]
    cf_sog_max_1 = liste_0_grad_cf[3]

    cf_1 = cf_sog_min_1 + (cf_sog_max_1-cf_sog_min_1)*phi

    return cf_1

def function_flaeche_A(liste_0_grad_cf):
    phi = liste_0_grad_cf[0]

    cpA_sog_min_1 = liste_0_grad_cf[5]
    cpA_sog_max_1 = liste_0_grad_cf[6]
    cpA_1 = cpA_sog_min_1 + (cpA_sog_max_1-cpA_sog_min_1)*phi

    return cpA_1

def function_flaeche_B(liste_0_grad_cf):
    phi = liste_0_grad_cf[0]

    cpB_sog_min_1 = liste_0_grad_cf[8]
    cpB_sog_max_1 = liste_0_grad_cf[9]
    cpB_1 = cpB_sog_min_1 + (cpB_sog_max_1-cpB_sog_min_1)*phi

    return cpB_1

def function_flaeche_C(liste_0_grad_cf):
    phi = liste_0_grad_cf[0]

    cpC_sog_min_1 = liste_0_grad_cf[11]
    cpC_sog_max_1 = liste_0_grad_cf[12]
    cpC_1 = cpC_sog_min_1 + (cpC_sog_max_1-cpC_sog_min_1)*phi

    return cpC_1
