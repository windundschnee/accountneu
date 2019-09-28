import numpy as np

def reibung(self,qp,c_fr):
    w_fr=qp*float(c_fr)
    return w_fr

def reibung_vernachlaessigen(self,breite,dicke,hoehe):
    if breite*dicke <= 4*breite*hoehe:
        reibung_vernachlaessigbar=True
    else:
        reibung_vernachlaessigbar=False
    return reibung_vernachlaessigbar
