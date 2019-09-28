import os

def reibung_margin_tab(self,reibung_beruecksichtigen,fd):
    if reibung_beruecksichtigen==True:
        fd.write("\n"+r' $c_{fr}$ & Reibungsbeiwert')
        fd.write("\n"+r'\\')
        fd.write("\n"+r' $w_{fr}$ & Reibungsdruck')
        fd.write("\n"+r'\\')

def reibung_margin_vernachlaessigen(self,reibung_vernachlaessigt,fd):
    windrichtung=['Norden und Süden', 'Osten und Westen']
    if all(element==True for element in reibung_vernachlaessigt )==True:
        fd.write("\n"+r' Die Reibung darf für alle Windrichtungen vernachlassigt werden. \\')
    else:
        for ind, element in enumerate(reibung_vernachlaessigt):
            if element == True:
                fd.write("\n"+r' Die Reibung darf für die Windrichtungen '+ windrichtung[ind]+r' vernachlassigt werden. \\')
