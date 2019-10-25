from scipy.interpolate import interp2d, interp1d
import numpy as np
from allg_berechnungen_app.qp_berechnen import qp_berechnen
from allg_berechnungen_app.algemeine_berechnungsfunktionen import cpe_zwischen_1_und_10

#Berechnet die Interpolierten cpe werte für die Wände

def cpe_interpolation_a(d_zu_b,h_zu_b):
    h_zu_b_tabelle=np.array([0.5,2,5,10,20,50])
    d_zu_b_tabelle=np.array([0.2,0.7,1,2,5,10])
    a_tabelle=np.array([[-1,-1,-1,-1,-1,-1],[-1.2,-1.2,-1.2,-1.1,-1.1,-1.1],[-1.35,-1.45,-1.30,-1.25,-1.2,-1.2],[-1.5,-1.65,-1.4,-1.35,-1.3,-1.3],[-1.65,-1.8,-1.5,-1.45,-1.35,-1.35],[-1.75,-1.9,-1.6,-1.5,-1.4,-1.4]])
    interpolationsfunktion = interp2d(d_zu_b_tabelle, h_zu_b_tabelle, a_tabelle)
    cp=float(interpolationsfunktion(d_zu_b,h_zu_b))
    return cp


def cpe_interpolation_b(d_zu_b,h_zu_b):
    h_zu_b_tabelle=np.array([0.5,2,5,10,20,50])
    d_zu_b_tabelle=np.array([0.2,0.7,1,2,5,10])
    b_tabelle=np.array([[-0.7,-0.7,-0.7,-0.7,-0.7,-0.7],[-0.8,-0.9,-0.8,-0.75,-0.7,-0.7],[-1,-1.10,-0.9,-0.85,-0.75,-0.7],[-1.2,-1.3,-1,-0.9,-0.8,-0.7],[-1.4,-1.5,-1.15,-0.95,-0.85,-0.75],[-1.5,-1.70,-1.35,-1,-0.9,-0.75]])
    interpolationsfunktion = interp2d(d_zu_b_tabelle, h_zu_b_tabelle, b_tabelle)
    cp=float(interpolationsfunktion(d_zu_b,h_zu_b))
    return cp

def cpe_interpolation_c(d_zu_b,h_zu_b):
    h_zu_b_tabelle=np.array([0.5,2,5,10,20,50])
    d_zu_b_tabelle=np.array([0.2,0.7,1,2,5,10])
    c_tabelle=np.array([[-0.4,-0.4,-0.4,-0.4,-0.4,-0.4],[0,0,-0.45,-0.4,-0.4,-0.4],[0,0,-0.5,-0.45,-0.4,-0.4],[0,0,-0.6,-0.5,-0.45,-0.4],[0,0,-0.7,-0.55,-0.5,-0.4],[0,0,-0.85,-0.6,-0.5,-0.4]])
    interpolationsfunktion = interp2d(d_zu_b_tabelle, h_zu_b_tabelle, c_tabelle)
    cp=float(interpolationsfunktion(d_zu_b,h_zu_b))
    return cp

def cpe_interpolation_e(d_zu_b,h_zu_b):
    h_zu_b_tabelle=np.array([0.5,2,5,10,20,50])
    d_zu_b_tabelle=np.array([0.2,0.7,1,2,5,10])
    e_tabelle=np.array([[-0.25,-0.35,-0.3,-0.15,-0.15,-0.15],[-0.35,-0.45,-0.35,-0.2,-0.15,-0.15],[-0.5,-0.75,-0.55,-0.3,-0.15,-0.15],[-0.75,-1.1,-0.85,-0.5,-0.2,-0.15],[-1,-1.35,-1.1,-0.65,-0.2,-0.15],[-1.2,-1.6,-1.3,-0.85,-0.2,-0.15]])
    interpolationsfunktion = interp2d(d_zu_b_tabelle, h_zu_b_tabelle, e_tabelle)
    cp=float(interpolationsfunktion(d_zu_b,h_zu_b))
    return cp


def boeengeschwindigkeitsdruck(self,hoehe,breite,dicke,anzahl_streifen):
    d_zu_b=dicke/breite
    h_zu_b=hoehe/breite
    # gibt die z zur berechnung von qp aus
    if h_zu_b <= 1:
        z_hoehe=[hoehe]
    elif 1 < h_zu_b <=2:
        z_hoehe=[breite,hoehe]
    elif h_zu_b > 2:
        dicke_streifen=(hoehe-2*breite)/anzahl_streifen
        z_hoehe=[]
        for n in range(0,anzahl_streifen+1):
            z_hoehe.append(dicke_streifen * n + breite)
        z_hoehe.append(hoehe)
    #berechnet qp und gibt eine liste mit qps für die entsprechende höhe von unten beginnend
    qp=[]
    for n in z_hoehe:
        qp.append(qp_berechnen(self,n))
    list=[z_hoehe,qp]
    return list

def aussenwinddruck_waende_berechnung(self,hoehe,breite,dicke,anzahl_streifen,fehlende_korrelation_beruecksichtigen,einflussflaeche,cpe_wahl):
    d_zu_b=dicke/breite
    h_zu_b=hoehe/breite
    h_zu_d=hoehe/dicke
    #Fehlende_korrelation
    if fehlende_korrelation_beruecksichtigen == True:
        korrelation_beiwert=fehlende_korrelation(self,h_zu_d)
    else:
        korrelation_beiwert=1
    #berechnet die cpe werte
    cpe_a=cpe_interpolation_a(d_zu_b,h_zu_b)
    cpe_b=cpe_interpolation_b(d_zu_b,h_zu_b)
    cpe_c=cpe_interpolation_c(d_zu_b,h_zu_b)
    cpe_d=0.8*korrelation_beiwert
    cpe_e=cpe_interpolation_e(d_zu_b,h_zu_b)*korrelation_beiwert
    #schreibt die cpe werte in eine liste
    cpe_10_waende=[cpe_a,cpe_b,cpe_c,cpe_d,cpe_e]
    #berechnet die qp werte und gibt eine liste der qp werte aus entschprechend der Höhe
    qp_waende=boeengeschwindigkeitsdruck(self,hoehe,breite,dicke,anzahl_streifen)[1]
    #berechnet die höhenund gibt eine liste mit den höhen aus
    z_hoehe=boeengeschwindigkeitsdruck(self,hoehe,breite,dicke,anzahl_streifen)[0]

    #Transformation in Vektoren
    cpe_10_waende_vektor=np.array(cpe_10_waende)
    qp_waende_vektor=np.array(qp_waende)

    #cp1 werte
    cpe_1_waende=cpe_10_waende_vektor*1.25

    print(cpe_wahl)
    print(cpe_wahl)
    print(cpe_wahl)
    print(cpe_wahl)
    print(cpe_wahl)
    if cpe_wahl=='CPE10':
        cpe_waende=cpe_10_waende
        cpe_waende_vektor=cpe_10_waende_vektor
    elif cpe_wahl=='CPE1':
        cpe_waende=cpe_1_waende.tolist()
        cpe_waende_vektor=cpe_1_waende
    else:
        #cpe mit einflussfläche zwischen 10 und 1
        cpe_waende=cpe_zwischen_1_und_10(self,cpe_10_waende,cpe_1_waende,einflussflaeche)
        cpe_waende_vektor=np.array(cpe_waende)



    #Aussenwinddruck Berechnen
    aussenwinddruck_d=qp_waende_vektor*cpe_waende[3]
    # cpe_ohne_d=alle_anderen_seiten=np.delete(cpe_10_waende_vektor, 3, axis=0)
    aussenwinddruck_a_b_c_e=qp_waende[-1]*cpe_waende_vektor



    list={'cpe_waende':cpe_waende,
    'z_hoehe':z_hoehe,
    'qp_waende':qp_waende,
    'aussenwinddruck_d':aussenwinddruck_d.tolist(),
    'aussenwinddruck_a_b_c_e':aussenwinddruck_a_b_c_e.tolist(), #hatt auch d Dabei
    'korrelation_beiwert':korrelation_beiwert,

    }
    return list

def fehlende_korrelation(self,h_zu_d):
    h_zu_d_tabelle=np.array([1,5])
    korrelation_tabelle=np.array([0.85,1])
    if h_zu_d <= 1:
        korrelation_beiwert=0.85
    elif 1 < h_zu_d < 5:
        interpolation_korrelation=interp1d(h_zu_d_tabelle, korrelation_tabelle)
        korrelation_beiwert=interpolation_korrelation(h_zu_d)
    elif h_zu_d >= 5:
        korrelation_beiwert=1
    return float(korrelation_beiwert)

def geometrie_waende(self,hoehe,breite,dicke):
    rechenwert_e=min(breite,2*hoehe)
    laenge_a=rechenwert_e/5
    if rechenwert_e > dicke:
        laenge_b = dicke - laenge_a
    else:
        laenge_b=4/5*rechenwert_e
    laenge_c=dicke-rechenwert_e
    list={'rechenwert_e':rechenwert_e,
    'laenge_a':laenge_a,
    'laenge_b':laenge_b,
    'laenge_c':laenge_c,
    }
    return list
