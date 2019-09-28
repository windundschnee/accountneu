import os
import io
from itertools import islice
import numpy as np
from gesamt_pdf_app.latexbasisfunktionen import reibung_margin_vernachlaessigen
# from pylatex import Document, Section, Subsection, Command,Figure,TikZ, TikZNode, TikZDraw, TikZCoordinate, TikZUserPath, TikZOptions,Package
# from pylatex.utils import italic, NoEscape
# from latex import build_pdf
# from gesamt_pdf_app.latexbasisfunktionen import *
# from gesamt_pdf_app.models import GesamtPdf
# from django.forms.models import model_to_dict






def latex_waende_ergebniss(self,arg_latex,latex_waende_list,filename):
    innendruck_verfahren_wahl = latex_waende_list['innendruck_verfahren_wahl']
    ergebnisse_berechnung=arg_latex['ergebnisse_berechnung']
    ergebnisse_waende=ergebnisse_berechnung['ergebnisse_waende']
    qp_waende=ergebnisse_waende['qp_waende']
    innendruck_beruecksichtigen=latex_waende_list['innendruck_beruecksichtigen']
    windrichtung=['Norden','Osten','Süden','Westen']
    with io.open(filename,'w', encoding="UTF8") as fd:


        if any(len(element)!=1 for element in qp_waende )==True:
            fd.write("\n"+r'\begin{table}[H]')
            fd.write("\n"+r'	\begin{tabularx}{1\columnwidth}{ B{1} B{1}  }')
            fd.write("\n"+r'\rowcolor{Gray}	')
            fd.write("\n"+r'	\textbf{Böengeschwindigkeitsdruck $\updownarrow$} &  \textbf{Böengeschwindigkeitsdruck $\leftrightarrow$}\\')
            qp_latex(self,arg_latex,fd)
            fd.write("\n"+r'\end{tabularx}')
            fd.write("\n"+r'\end{table}')
        margin_ergebnisse_waende(self,arg_latex,latex_waende_list,fd)
        fd.write("\n"+r'\begin{table}[H]')
        fd.write("\n"+r'	\begin{tabularx}{1\columnwidth}{ B{1} B{1} }')
        fd.write("\n"+r'\rowcolor{Gray}	')
        fd.write("\n"+r'	\textbf{Außenwinddruck $\updownarrow$} &  \textbf{Außenwinddruck $\leftrightarrow$}\\')
        aussendruck(self,arg_latex,fd)
        if innendruck_beruecksichtigen == True:
            fd.write("\n"+r'\end{tabularx}')
            fd.write("\n"+r'\end{table}')
            fd.write("\n"+r'\begin{table}[H]')
            fd.write("\n"+r'	\begin{tabularx}{1\columnwidth}{ B{1} B{1}  }')
            ueberlagerung_dom_flaeche(self,arg_latex,innendruck_verfahren_wahl,fd)
        fd.write("\n"+r'\end{tabularx}')
        fd.write("\n"+r'\end{table}')

def aussendruck(self,arg_latex,fd):
    ergebnisse_berechnung=arg_latex['ergebnisse_berechnung']
    ergebnisse_waende=ergebnisse_berechnung['ergebnisse_waende']
    ausenwindruecke_d=ergebnisse_waende['ausenwindruecke_d']
    ausenwindruecke_a_b_c_e=ergebnisse_waende['ausenwindruecke_a_b_c_e']
    beschriftung=['A','B','C','D','E']
    for ind_list, element_list in enumerate(ausenwindruecke_a_b_c_e):
        fd.write("\n"+r'$	\begin{aligned}[t]')
        for ind_a, element_a in enumerate(ausenwindruecke_a_b_c_e[ind_list]):
            if ind_a == 3:
                if len(ausenwindruecke_d[ind_list]) == 1:
                    fd.write("\n"+r'w_{e,'+ beschriftung[ind_a]+r'}&=\spann{'+ str(ausenwindruecke_d[ind_list][0])+r'}   \\')
                else:
                    for ind_d, element_d in enumerate(ausenwindruecke_d[ind_list]):
                        fd.write("\n"+r'w_{e,'+ beschriftung[ind_a]+ str(ind_d+1)+r'}&=\spann{'+ str(element_d)+r'}   \\')
            elif ind_a ==2 and element_a ==0:
                print('keine Fläche c')
            else:
                fd.write("\n"+r'w_{e,'+ beschriftung[ind_a]+r'}&=\spann{'+ str(element_a)+r'}   \\')
        fd.write("\n"+r'		\end{aligned}		$')
        if ind_list != (len(ausenwindruecke_a_b_c_e)-1):
            fd.write("\n"+r'		&		')

def aussendruckbeiwerte_waende(self,arg_latex,filename):
    ergebnisse_berechnung=arg_latex['ergebnisse_berechnung']
    ergebnisse_waende=ergebnisse_berechnung['ergebnisse_waende']
    cpe=ergebnisse_waende['cpe']
    beschriftung=['A','B','C','D','E']
    with io.open(filename,'w', encoding="UTF8") as fd:
        fd.write("\n"+r'\begin{table}[H]')
        fd.write("\n"+r'	\begin{tabularx}{1\columnwidth}{ B{1} B{1}  }')
        fd.write("\n"+r'\rowcolor{Gray}	')
        fd.write("\n"+r'	\textbf{Außendruckbeiwert $\updownarrow$} &  \textbf{Außendruckbeiwert $\leftrightarrow$} \\')
        for ind_list, element_list in enumerate(cpe):
            fd.write("\n"+r'$	\begin{aligned}[t]')
            for ind_a, element_a in enumerate(cpe[ind_list]):
                if ind_a ==2 and element_a==0:
                    print('keine Fläche c')
                else:
                    fd.write("\n"+r'c_{pe,'+ beschriftung[ind_a]+r'}&=\num{'+ str(element_a)+r'}   \\')
            fd.write("\n"+r'		\end{aligned}		$')
            if ind_list != (len(cpe)-1):
                fd.write("\n"+r'		&		')
        fd.write("\n"+r'\end{tabularx}')
        fd.write("\n"+r'\end{table}')

def qp_latex(self,arg_latex,fd):
    ergebnisse_berechnung=arg_latex['ergebnisse_berechnung']
    ergebnisse_waende=ergebnisse_berechnung['ergebnisse_waende']
    qp_waende=ergebnisse_waende['qp_waende']
    for ind_list, element_list in enumerate(qp_waende):
        fd.write("\n"+r'$	\begin{aligned}[t]')
        for ind_a, element_a in enumerate(qp_waende[ind_list]):
            fd.write("\n"+r'q_{p,'+ str(ind_a+1) +r'}&=\spann{'+ str(element_a)+r'}   \\')
        fd.write("\n"+r'		\end{aligned}		$')
        if ind_list != (len(qp_waende)-1):
            fd.write("\n"+r'		&		')



def ueberlagerung_dom_flaeche(self,arg_latex,innendruck_verfahren_wahl,fd):
    ergebnisse_berechnung=arg_latex['ergebnisse_berechnung']
    ergebnisse_waende=ergebnisse_berechnung['ergebnisse_waende']
    ergebnisse_ueberlagerung_d=ergebnisse_waende['ergebnisse_ueberlagerung_d']
    ergebnisse_ueberlagerung_a_b_c_e=ergebnisse_waende['ergebnisse_ueberlagerung_a_b_c_e']
    innendruck=ergebnisse_waende['innendruck']
    beschriftung=['A','B','C','D','E']
    fd.write("\n"+r'\rowcolor{Gray}	')
    if innendruck_verfahren_wahl == 'Innendruckbeiwerte mittels dominanter Fläche nach Abschnitt 7.2.9':
        fd.write("\n"+r' \textbf{überlagerter Winddruck $\downarrow $} & \textbf{überlagerter Winddruck $\leftarrow$}\\')
    else:
        fd.write("\n"+r' \textbf{überlagerter Winddruck $\updownarrow $} & \textbf{überlagerter Winddruck $\leftrightarrow$}\\')
    for ind_list, element_list in enumerate(ergebnisse_ueberlagerung_a_b_c_e):
        if ind_list == 2:
            fd.write("\n"+r'	 \\ \rule{0mm}{4mm}')
            fd.write("\n"+r'	 \\')
            fd.write("\n"+r'\rowcolor{Gray}	')
            fd.write("\n"+r' \textbf{überlagerter Winddruck $\uparrow $} & \textbf{überlagerter Winddruck $\rightarrow$}\\')
        fd.write("\n"+r'$	\begin{aligned}[t]')
        for ind_a, element_a in enumerate(ergebnisse_ueberlagerung_a_b_c_e[ind_list]):
            if ind_a == 3:
                if len(ergebnisse_ueberlagerung_d[ind_list]) == 1:
                    fd.write("\n"+r'w_{,'+ beschriftung[ind_a]+r'}&=\spann{'+ str(ergebnisse_ueberlagerung_d[ind_list][0])+r'}   \\')
                else:
                    for ind_d, element_d in enumerate(ergebnisse_ueberlagerung_d[ind_list]):
                        fd.write("\n"+r'w_{,'+ beschriftung[ind_a]+ str(ind_d+1)+r'}&=\spann{'+ str(element_d)+r'}   \\')
            elif ind_a ==2 and element_a ==innendruck[0]:
                print('keine Fläche c')
            else:
                fd.write("\n"+r'w_{,'+ beschriftung[ind_a]+r'}&=\spann{'+ str(element_a)+r'}   \\')
        fd.write("\n"+r'		\end{aligned}		$')
        if ind_list != (len(ergebnisse_ueberlagerung_a_b_c_e)-1) and ind_list !=1:
            fd.write("\n"+r'		&		')


def margin_ergebnisse_waende(self,arg_latex,latex_waende_list,fd):
    #Margin
    innendruck_verfahren_wahl = latex_waende_list['innendruck_verfahren_wahl']
    ergebnisse_berechnung=arg_latex['ergebnisse_berechnung']
    ergebnisse_waende=ergebnisse_berechnung['ergebnisse_waende']
    reibung_beruecksichtigen=latex_waende_list['reibung_beruecksichtigen']
    reibung_vernachlaessigt=ergebnisse_berechnung['reibung_vernachlaessigt']
    innendruck_beruecksichtigen=latex_waende_list['innendruck_beruecksichtigen']
    fehlende_korrelation_beruecksichtigen=latex_waende_list['fehlende_korrelation_beruecksichtigen']
    index_dominante_seite=ergebnisse_waende['index_dominante_seite']
    gibt_es_eine_dominante_seite=ergebnisse_waende['gibt_es_eine_dominante_seite']
    windrichtung=['Norden','Osten','Süden','Westen']

    #Margin
    fd.write("\n"+r'\switchcolumn*')
    fd.write("\n"+r'\begin{tabular}{ r @{ \dots} L{2.8cm} }')
    fd.write("\n"+r' + & Winddruck')
    fd.write("\n"+r'\\')
    fd.write("\n"+r' -- & Windsog')
    fd.write("\n"+r'\\')
    fd.write("\n"+r' $e$ & Außen')
    fd.write("\n"+r'\\')
    fd.write("\n"+r' $i$ & Innen')
    fd.write("\n"+r'\\')
    fd.write("\n"+r' $\leftrightarrow$ & Wind aus Ost/West- Richtung')
    fd.write("\n"+r'\\')
    fd.write("\n"+r' $\updownarrow$ & Wind aus Nord/Süd- Richtung')
    fd.write("\n"+r'\\')
    fd.write("\n"+r' $\NSOWarrow$ & Ergebnisse für alle Windrichtungen')
    fd.write("\n"+r'\\')
    if innendruck_verfahren_wahl == 'Innendruckbeiwerte mittels dominanter Fläche nach Abschnitt 7.2.9':
        fd.write("\n"+r' $\downarrow$ & Wind aus Norden')
        fd.write("\n"+r'\\')
        fd.write("\n"+r' $\leftarrow$ & Wind aus Osten')
        fd.write("\n"+r'\\')
        fd.write("\n"+r' $\uparrow$ & Wind aus Süden')
        fd.write("\n"+r'\\')
        fd.write("\n"+r' $\rightarrow$ & Wind aus Westen')
    fd.write("\n"+r'\end{tabular}')
    fd.write("\n"+r'\vspace{3 mm}')
    fd.write("\n"+r'\\')

    reibung_margin_vernachlaessigen(self,reibung_vernachlaessigt,fd)
    if fehlende_korrelation_beruecksichtigen == True:
        fd.write("\n"+r'\\')
        fd.write("\n"+r' Die Korrelation zwischen der Luv und Lee Seite wird, bei den Wänden, berücksichtigt.')
    if gibt_es_eine_dominante_seite==True:
        windrichtung=['Nord','Ost','Süd','West']
        fd.write("\n"+r'\\')
        fd.write("\n"+r' Auf der '+ windrichtung[index_dominante_seite]+r'seite gibt es eine Dominante Öffnung.')
    fd.write("\n"+r'\switchcolumn')

def bilder_waende(self,arg_latex,latex_waende_list,filename):
    #Zeichencoordinaten
    ergebnisse_berechnung=arg_latex['ergebnisse_berechnung']
    ergebnisse_waende=ergebnisse_berechnung['ergebnisse_waende']
    geometrie_waende_norden=ergebnisse_waende['geometrie_waende_norden']
    geometrie_waende_westen=ergebnisse_waende['geometrie_waende_westen']

    z_waende=ergebnisse_waende['z_waende']
    anzahl_streifen=latex_waende_list['anzahl_streifen']

    hoehe=ergebnisse_waende['hoehe']
    breite_sued=latex_waende_list['breite_sued']
    breite_west=latex_waende_list['breite_west']

    #Längen westen

    rechenwert_e_w=geometrie_waende_westen['rechenwert_e']
    laenge_a_w=geometrie_waende_westen['laenge_a']
    laenge_b_w=geometrie_waende_westen['laenge_b']
    laenge_c_w=geometrie_waende_westen['laenge_c']
    #Norden längen

    rechenwert_e_s=geometrie_waende_norden['rechenwert_e']
    laenge_a_s=geometrie_waende_norden['laenge_a']
    laenge_b_s=geometrie_waende_norden['laenge_b']
    laenge_c_s=geometrie_waende_norden['laenge_c']
    #Latex werte
    lw=4
    ls=3
    if laenge_c_w <=0:
        e_latex_w=lw
    else:
        e_latex_w=2.5

    if laenge_c_s <=0:
        e_latex_s=ls
    else:
        e_latex_s=2.5


    with io.open(filename,'w', encoding="UTF8") as fd:

        ##Schnittsymbol
        fd.write("\n"+r'\tikzset{')
        fd.write("\n"+r'schnittsymbol/.pic = {')
        fd.write("\n"+r'\draw[line width=0.13mm] (0,0) -- (0,-0.5) ;')
        fd.write("\n"+r'\draw[line width=0.13mm] (0,0) -- (0.2,0) ;')
        fd.write("\n"+r'\fill[line width=0.13mm,black] (0.2,0) -- + (0,0.1) -- +(0.15,0) -- +(0,-0.1) -- cycle ;')
        fd.write("\n"+r'}}')

        ###############
        #Grundriss West
        fd.write("\n"+r'\tikzset{')
        fd.write("\n"+r'wand_west/.pic = {')
        fd.write("\n"+r'\node[coordinate] at (0,0) (ra) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(lw)+r',0) (rb) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(lw)+r','+ str(ls)+r') (rc) {};')
        fd.write("\n"+r'\node[coordinate] at (0,'+ str(ls)+r') (rd) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(e_latex_w/5)+r',0) (nabu) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(e_latex_w)+r',0) (nbcu) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(e_latex_w/5)+r','+ str(ls)+r') (nabo) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(e_latex_w)+r','+ str(ls)+r') (nbco) {};')



        #Umrandungslinien
        fd.write("\n"+r'\draw[line width=0.25mm] (ra) -- (rb) -- (rc) -- (rd) -- cycle;')
        #Flächenbezeichnung
        fd.write("\n"+r'\node[between=ra and rd, right ]  {\large{D}};')
        fd.write("\n"+r'\node[between=rb and rc, left ]  {\large{E}};')
        #unten
        fd.write("\n"+r'\draw[line width=0.25mm,dotted] ($(ra)+(0,0.05)$) -- ($(nabu)+(0,0.05)$);')
        fd.write("\n"+r'\draw[line width=0.13mm] (nabu) --+ (0,0.1);')
        fd.write("\n"+r'\node[between=ra and nabu, above ]  {\large{A}};')

        fd.write("\n"+r'\draw[line width=0.25mm,dashed] ($(nabu)+(0,0.05)$) -- ($(nbcu)+(0,0.05)$);')
        fd.write("\n"+r'\draw[line width=0.13mm] (nbcu) --+ (0,0.1);')
        fd.write("\n"+r'\node[between=nabu and nbcu, above ]  {\large{B}};')

        #oben
        fd.write("\n"+r'\draw[line width=0.25mm,dotted] ($(rd)+(0,-0.05)$) -- ($(nabo)+(0,-0.05)$);')
        fd.write("\n"+r'\draw[line width=0.13mm] (nabo) --+ (0,-0.1);')
        fd.write("\n"+r'\node[between=rd and nabo, below ]  {\large{A}};')

        fd.write("\n"+r'\draw[line width=0.25mm,dashed] ($(nabo)+(0,-0.05)$) -- ($(nbco)+(0,-0.05)$);')
        fd.write("\n"+r'\draw[line width=0.13mm] (nbco) --+ (0,-0.1);')
        fd.write("\n"+r'\node[between=nabo and nbco, below ]  {\large{B}};')

        #Himmelsrichtungen
        fd.write("\n"+r'\node[between=rd and rc, above ]  {Norden};')
        fd.write("\n"+r'\node[between=rb and rc, below ,rotate=90]  {Osten};')
        fd.write("\n"+r'\node[between=ra and rb, below ]  {Süden};')
        fd.write("\n"+r'\node[between=ra and rd, above ,rotate=90]  {Westen};')


        #Bemaßungslinien
        fd.write("\n"+r'\DimlineH[rd][nabo][0.5][\num{'+ str(laenge_a_w)+r'}] ')
        fd.write("\n"+r'\DimlineH[nabo][nbco][0.5][\num{'+ str(laenge_b_w)+r'}] ')

        fd.write("\n"+r'\DimlineH[rd][rc][1][\num{'+ str(breite_west)+r'}] ')
        fd.write("\n"+r'\DimlineV[rb][rc][0.9][\num{'+ str(breite_sued)+r'}] ')
        if laenge_c_w > 0:
            fd.write("\n"+r'\draw[line width=0.25mm,dashdotted] ($(nbcu)+(0,0.05)$) -- ($(rb)+(0,0.05)$);')
            fd.write("\n"+r'\node[between=nbcu and rb, above ]  {\large{C}};')
            fd.write("\n"+r'\draw[line width=0.25mm,dashdotted] ($(nbco)+(0,-0.05)$) -- ($(rc)+(0,-0.05)$);')
            fd.write("\n"+r'\node[between=nbco and rc, below ]  {\large{C}};')
            fd.write("\n"+r'\DimlineH[nbco][rc][0.5][\num{'+ str(laenge_c_w)+r'}] ')

        #Pfeile für die Windrichtung
        fd.write("\n"+r'\pic[rotate=-90,,transform shape] at (-0.5,'+ str(ls/2)+r') {windrichtung};')

        #Schnitt
        fd.write("\n"+r'\pic at (-0.5,'+ str(ls+0.5)+r') {schnittsymbol};')
        fd.write("\n"+r'\begin{scope}[yscale=1,xscale=-1]')
        fd.write("\n"+r'\pic[rotate=180,,transform shape]  at ($(ra)+(0.5,-0.5)$) {schnittsymbol};')
        fd.write("\n"+r'\end{scope}')

        fd.write("\n"+r'}}')


        ###############
        #Grundriss Süd
        fd.write("\n"+r'\tikzset{')
        fd.write("\n"+r'wand_sued/.pic = {')
        fd.write("\n"+r'\node[coordinate] at (0,0) (ra) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(lw)+r',0) (rb) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(lw)+r','+ str(ls)+r') (rc) {};')
        fd.write("\n"+r'\node[coordinate] at (0,'+ str(ls)+r') (rd) {};')
        fd.write("\n"+r'\node[coordinate] at (0,'+ str(e_latex_s/5)+r') (nabu) {};')
        fd.write("\n"+r'\node[coordinate] at (0,'+ str(e_latex_s)+r') (nbcu) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(lw)+r','+ str(e_latex_s/5)+r') (nabo) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(lw)+r','+ str(e_latex_s)+r') (nbco) {};')



        #Umrandungslinien
        fd.write("\n"+r'\draw[line width=0.25mm] (ra) -- (rb) -- (rc) -- (rd) -- cycle;')
        #Flächenbezeichnung
        fd.write("\n"+r'\node[between=ra and rb, above ]  {\large{D}};')
        fd.write("\n"+r'\node[between=rd and rc, below ]  {\large{E}};')
        #links
        fd.write("\n"+r'\draw[line width=0.25mm,dotted] ($(ra)+(0.05,0)$) -- ($(nabu)+(0.05,0)$);')
        fd.write("\n"+r'\draw[line width=0.13mm] (nabu) --+ (0.1,0);')
        fd.write("\n"+r'\node[between=ra and nabu, right ]  {\large{A}};')
        fd.write("\n"+r'\draw[line width=0.25mm,dashed] ($(nabu)+(0.05,0)$) -- ($(nbcu)+(0.05,0)$);')
        fd.write("\n"+r'\draw[line width=0.13mm] (nbcu) --+ (0.1,0);')
        fd.write("\n"+r'\node[between=nabu and nbcu, right ]  {\large{B}};')
        #rechts
        fd.write("\n"+r'\draw[line width=0.25mm,dotted] ($(rb)+(-0.05,0)$) -- ($(nabo)+(-0.05,0)$);')
        fd.write("\n"+r'\draw[line width=0.13mm] (nabo) --+ (-0.1,0);')
        fd.write("\n"+r'\node[between=rb and nabo, left ]  {\large{A}};')
        fd.write("\n"+r'\draw[line width=0.25mm,dashed] ($(nabo)+(-0.05,0)$) -- ($(nbco)+(-0.05,0)$);')
        fd.write("\n"+r'\draw[line width=0.13mm] (nbco) --+ (-0.1,0);')
        fd.write("\n"+r'\node[between=nabo and nbco, left ]  {\large{B}};')

        #Himmelsrichtungen
        fd.write("\n"+r'\node[between=rd and rc, above ]  {Norden};')
        fd.write("\n"+r'\node[between=rb and rc, below ,rotate=90]  {Osten};')
        fd.write("\n"+r'\node[between=ra and rb, below ]  {Süden};')
        fd.write("\n"+r'\node[between=ra and rd, above ,rotate=90]  {Westen};')



        #Bemaßungslinien
        fd.write("\n"+r'\DimlineV[ra][nabu][-0.5][\num{'+ str(laenge_a_s)+r'}] ')
        fd.write("\n"+r'\DimlineV[nabu][nbcu][-0.5][\num{'+ str(laenge_b_s)+r'}] ')

        fd.write("\n"+r'\DimlineH[rd][rc][0.5][\num{'+ str(breite_west)+r'}] ')
        fd.write("\n"+r'\DimlineV[ra][rd][-1.0][\num{'+ str(breite_sued)+r'}] ')
        if laenge_c_s > 0:
            fd.write("\n"+r'\draw[line width=0.25mm,dashdotted] ($(nbcu)+(0.05,0)$) -- ($(rd)+(0.05,0)$);')
            fd.write("\n"+r'\node[between=nbcu and rd, right ]  {\large{C}};')
            fd.write("\n"+r'\draw[line width=0.25mm,dashdotted] ($(nbco)+(-0.05,0)$) -- ($(rc)+(-0.05,0)$);')
            fd.write("\n"+r'\node[between=nbco and rc, left]  {\large{C}};')
            fd.write("\n"+r'\DimlineV[nbcu][rd][-0.5][\num{'+ str(laenge_c_s)+r'}] ')

        #Pfeile für die Windrichtung
        fd.write("\n"+r'\pic at ('+ str(lw/2)+r',-0.7) {windrichtung};')

        #Schnitt
        fd.write("\n"+r'\pic[rotate=90,,transform shape] at (-0.5,-0.5) {schnittsymbol};')
        fd.write("\n"+r'\begin{scope}[yscale=1,xscale=-1]')
        fd.write("\n"+r'\pic[rotate=90,transform shape] at ($(rb)+(-0.5,-0.5)$) {schnittsymbol};')
        fd.write("\n"+r'\end{scope}')

        fd.write("\n"+r'}}')

        if len(z_waende[1]) >1:
            ansicht_waende(self, z_waende[1], anzahl_streifen,breite_sued, ls,'West',fd)
        if len(z_waende[0]) >1:
            ansicht_waende(self, z_waende[0], anzahl_streifen,breite_west, lw,'Sued',fd)




        ##Margin
        fd.write("\n"+r'\switchcolumn*')
        fd.write("\n"+r'alle Werte in $[m]$')
        #fd.write("\n"+r'\begin{tikzpicture}')
        #fd.write("\n"+r' \pic[scale=1,fill=black,text=black] at (0,0) {compass};')
        #fd.write("\n"+r'\end{tikzpicture}')
        fd.write("\n"+r'\switchcolumn')


        ####Bild zusammenfügen
        fd.write("\n"+r'\begin{figure}[H]')
        fd.write("\n"+r'\centering')
        fd.write("\n"+r'\begin{tikzpicture}')



        # #Grundriss Wände
        fd.write("\n"+r'\node[anchor=west] at (-1,4.3)  {\Large{Grundriss Wände}};')
        fd.write("\n"+r'\pic at (7.5,0) {wand_west};')
        fd.write("\n"+r'\pic at (0,0) {wand_sued};')

        #Ansicht Wände
        if len(z_waende[1]) >1:
            fd.write("\n"+r'\pic at (7.5,6) {wand_ansicht_West};')
        if len(z_waende[0]) >1:
            fd.write("\n"+r'\pic at (0,6) {wand_ansicht_Sued};')
        #Windrose einfügen
        # fd.write("\n"+r' \pic[scale=1,fill=black,text=black] at (0,0) {compass};')
        fd.write("\n"+r'\end{tikzpicture}')
        fd.write("\n"+r'\end{figure}')

def ansicht_waende(self, z_hoehe, anzahl_streifen,breite, breite_latex,himmelsrichtung,fd):
    h_latex=5

    if len(z_hoehe)==2:
        z_latex=[0,breite_latex,h_latex]
    elif len(z_hoehe) > 2:
        dicke_streifen=0.5
        z_latex=[0]
        for n in range(0,anzahl_streifen+1):
            z_latex.append(dicke_streifen * n + breite_latex)
        gesammthoehe=z_latex[-1]+breite_latex
        z_latex.append(gesammthoehe)


    hoehendifferenz=np.diff(np.array(z_hoehe)).tolist()
    hoehendifferenz.insert(0,breite)




    fd.write("\n"+r'\tikzset{')
    fd.write("\n"+r'wand_ansicht_'+ himmelsrichtung+r'/.pic = {')
    #nodes und horizontale linien
    for ind, element in enumerate(z_latex):
        fd.write("\n"+r'\node[coordinate] at (0,'+ str(element)+r') (n'+ str(ind)+r'l) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(breite_latex)+r','+ str(element)+r') (n'+ str(ind)+r'r) {};')
        fd.write("\n"+r'\draw[line width=0.25mm] (n'+ str(ind)+r'l) -- (n'+ str(ind)+r'r) ;')

    #Beschriftung und Bemaßung
    for ind in range(0,len(z_hoehe)):
        fd.write("\n"+r'\node[between=n'+ str(ind)+r'l and n'+ str(ind+1)+r'r]  {\large{$D_{'+ str(ind+1)+r'}$}};')
        fd.write("\n"+r'\DimlineV[n'+ str(ind)+r'l][n'+ str(ind+1)+r'l][-0.5][\num{'+ str(hoehendifferenz[ind])+r'}] ')

    fd.write("\n"+r'\DimlineV[n'+ str(0)+r'l][n'+ str(len(z_hoehe))+r'l][-1][\num{'+ str(z_hoehe[-1])+r'}] ')

    #Vertikale Linien
    fd.write("\n"+r'\draw[line width=0.25mm] (n'+ str(0)+r'l) -- (n'+ str(len(z_hoehe))+r'l) ;')
    fd.write("\n"+r'\draw[line width=0.25mm] (n'+ str(0)+r'r) -- (n'+ str(len(z_hoehe))+r'r) ;')
    #Grund
    fd.write("\n"+r'\draw[line width=0.35mm] ($(n'+ str(0)+r'l)+(-0.5,0)$) -- ($(n'+ str(0)+r'r)+(0.5,0)$) ;')
    fd.write("\n"+r'\fill[pattern,pattern= north east lines] ($(n'+ str(0)+r'l)+(-0.5,0)$) rectangle ($(n'+ str(0)+r'r)+(0.5,-0.3)$);')

    if himmelsrichtung=='West':
        fd.write("\n"+r'\node[anchor=west] at (-1,'+ str(z_latex[-1]+0.7)+r')  {\Large{West--Ansicht}};')
    if himmelsrichtung=='Sued':
        fd.write("\n"+r'\node[anchor=west] at (-1,'+ str(z_latex[-1]+0.7)+r')  {\Large{Süd--Ansicht}};')











    fd.write("\n"+r'}}')
