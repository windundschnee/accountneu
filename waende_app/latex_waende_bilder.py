import os
import io
from itertools import islice
from allg_berechnungen_app.algemeine_berechnungsfunktionen import liste_runden_1
import numpy as np

def bilder_waende(self,arg_latex,latex_waende_list,filename):

    #breite westen ist die länge zwischen ost und westseite in den bezeichnungn bei der eingabe wurde das gändert nicht verwechseln
    #breite süden ist die länge zwischen süd und nordseite in den bezeichnungn bei der eingabe wurde das gändert nicht verwechseln
    #Zeichencoordinaten
    ergebnisse_berechnung=arg_latex['ergebnisse_berechnung']
    ergebnisse_waende=liste_runden_1(ergebnisse_berechnung['ergebnisse_waende'])
    geometrie_waende_norden=ergebnisse_waende['geometrie_waende_norden']
    geometrie_waende_westen=ergebnisse_waende['geometrie_waende_westen']

    z_waende=ergebnisse_waende['z_waende']
    anzahl_streifen=latex_waende_list['anzahl_streifen']

    hoehe=ergebnisse_waende['hoehe']
    breite_sued=latex_waende_list['breite_sued']
    breite_west=latex_waende_list['breite_west']

    #Längen westen

    rechenwert_e_w=geometrie_waende_westen['rechenwert_e']
    laenge_a_w=round(geometrie_waende_westen['laenge_a'],1)
    laenge_b_w=geometrie_waende_westen['laenge_b']
    laenge_c_w=geometrie_waende_westen['laenge_c']
    #Norden längen

    rechenwert_e_s=geometrie_waende_norden['rechenwert_e']
    laenge_a_s=geometrie_waende_norden['laenge_a']
    laenge_b_s=geometrie_waende_norden['laenge_b']
    laenge_c_s=geometrie_waende_norden['laenge_c']
    #Latex werte
    if breite_sued <= breite_west:
        lw=4.5
        scalefaktor=lw/float(breite_west)
        ls=float(breite_sued)*scalefaktor

        e_latex_w=rechenwert_e_w*scalefaktor

        e_latex_s=rechenwert_e_s*scalefaktor
        laenge_a_w_latex =laenge_a_w*scalefaktor
        laenge_b_w_latex=laenge_b_w*scalefaktor
        laenge_a_s_latex =laenge_a_s*scalefaktor
        laenge_b_s_latex=laenge_b_s*scalefaktor

    elif breite_sued > breite_west:
        ls=3.0
        scalefaktor=ls/float(breite_sued)
        lw=float(breite_west)*scalefaktor


        e_latex_w=rechenwert_e_w*scalefaktor

        e_latex_s=rechenwert_e_s*scalefaktor

        laenge_a_w_latex =laenge_a_w*scalefaktor
        laenge_b_w_latex=laenge_b_w*scalefaktor
        laenge_a_s_latex =laenge_a_s*scalefaktor
        laenge_b_s_latex=laenge_b_s*scalefaktor






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
        fd.write("\n"+r'\node[coordinate] at ('+ str(laenge_a_w_latex)+r',0) (nabu) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(laenge_b_w_latex+laenge_a_w_latex)+r',0) (nbcu) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(laenge_b_w_latex+laenge_a_w_latex)+r','+ str(ls)+r') (nbco) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(laenge_a_w_latex)+r','+ str(ls)+r') (nabo) {};')




        #Umrandungslinien
        fd.write("\n"+r'\draw[line width=0.25mm] (ra) -- (rb) -- (rc) -- (rd) -- cycle;')
        #Flächenbezeichnung
        fd.write("\n"+r'\node[between=ra and rd, right ]  {\normalsize{D}};')
        fd.write("\n"+r'\node[between=rb and rc, left ]  {\normalsize{E}};')
        #unten
        fd.write("\n"+r'\draw[line width=0.25mm,dotted] ($(ra)+(0,0.05)$) -- ($(nabu)+(0,0.05)$);')
        fd.write("\n"+r'\draw[line width=0.13mm] (nabu) --+ (0,0.1);')
        fd.write("\n"+r'\node[between=ra and nabu, above ]  {\normalsize{A}};')

        fd.write("\n"+r'\draw[line width=0.25mm,dashed] ($(nabu)+(0,0.05)$) -- ($(nbcu)+(0,0.05)$);')
        fd.write("\n"+r'\draw[line width=0.13mm] (nbcu) --+ (0,0.1);')
        fd.write("\n"+r'\node[between=nabu and nbcu, above ]  {\normalsize{B}};')

        #oben
        fd.write("\n"+r'\draw[line width=0.25mm,dotted] ($(rd)+(0,-0.05)$) -- ($(nabo)+(0,-0.05)$);')
        fd.write("\n"+r'\draw[line width=0.13mm] (nabo) --+ (0,-0.1);')
        fd.write("\n"+r'\node[between=rd and nabo, below ]  {\normalsize{A}};')

        fd.write("\n"+r'\draw[line width=0.25mm,dashed] ($(nabo)+(0,-0.05)$) -- ($(nbco)+(0,-0.05)$);')
        fd.write("\n"+r'\draw[line width=0.13mm] (nbco) --+ (0,-0.1);')
        fd.write("\n"+r'\node[between=nabo and nbco, below ]  {\normalsize{B}};')

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
            fd.write("\n"+r'\node[between=nbcu and rb, above ]  {\normalsize{C}};')
            fd.write("\n"+r'\draw[line width=0.25mm,dashdotted] ($(nbco)+(0,-0.05)$) -- ($(rc)+(0,-0.05)$);')
            fd.write("\n"+r'\node[between=nbco and rc, below ]  {\normalsize{C}};')
            fd.write("\n"+r'\DimlineH[nbco][rc][0.5][\num{'+ str(laenge_c_w)+r'}] ')

        #Pfeile für die Windrichtung
        fd.write("\n"+r'\pic[rotate=-90,,transform shape] at (-0.7,'+ str(ls/2)+r') {windrichtung};')

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
        fd.write("\n"+r'\node[coordinate] at (0,'+ str(laenge_a_s_latex)+r') (nabu) {};')
        fd.write("\n"+r'\node[coordinate] at (0,'+ str(laenge_b_s_latex+laenge_a_s_latex)+r') (nbcu) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(lw)+r','+ str(laenge_a_s_latex)+r') (nabo) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(lw)+r','+ str(laenge_b_s_latex+laenge_a_s_latex)+r') (nbco) {};')



        #Umrandungslinien
        fd.write("\n"+r'\draw[line width=0.25mm] (ra) -- (rb) -- (rc) -- (rd) -- cycle;')
        #Flächenbezeichnung
        fd.write("\n"+r'\node[between=ra and rb, above ]  {\normalsize{D}};')
        fd.write("\n"+r'\node[between=rd and rc, below ]  {\normalsize{E}};')
        #links
        fd.write("\n"+r'\draw[line width=0.25mm,dotted] ($(ra)+(0.05,0)$) -- ($(nabu)+(0.05,0)$);')
        fd.write("\n"+r'\draw[line width=0.13mm] (nabu) --+ (0.1,0);')
        fd.write("\n"+r'\node[between=ra and nabu, right ]  {\normalsize{A}};')
        fd.write("\n"+r'\draw[line width=0.25mm,dashed] ($(nabu)+(0.05,0)$) -- ($(nbcu)+(0.05,0)$);')
        fd.write("\n"+r'\draw[line width=0.13mm] (nbcu) --+ (0.1,0);')
        fd.write("\n"+r'\node[between=nabu and nbcu, right ]  {\normalsize{B}};')
        #rechts
        fd.write("\n"+r'\draw[line width=0.25mm,dotted] ($(rb)+(-0.05,0)$) -- ($(nabo)+(-0.05,0)$);')
        fd.write("\n"+r'\draw[line width=0.13mm] (nabo) --+ (-0.1,0);')
        fd.write("\n"+r'\node[between=rb and nabo, left ]  {\normalsize{A}};')
        fd.write("\n"+r'\draw[line width=0.25mm,dashed] ($(nabo)+(-0.05,0)$) -- ($(nbco)+(-0.05,0)$);')
        fd.write("\n"+r'\draw[line width=0.13mm] (nbco) --+ (-0.1,0);')
        fd.write("\n"+r'\node[between=nabo and nbco, left ]  {\normalsize{B}};')

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
            fd.write("\n"+r'\node[between=nbcu and rd, right ]  {\normalsize{C}};')
            fd.write("\n"+r'\draw[line width=0.25mm,dashdotted] ($(nbco)+(-0.05,0)$) -- ($(rc)+(-0.05,0)$);')
            fd.write("\n"+r'\node[between=nbco and rc, left]  {\normalsize{C}};')
            fd.write("\n"+r'\DimlineV[nbcu][rd][-0.5][\num{'+ str(laenge_c_s)+r'}] ')

        #Pfeile für die Windrichtung
        fd.write("\n"+r'\pic at ('+ str(lw/2)+r',-0.7) {windrichtung};')

        #Schnitt
        fd.write("\n"+r'\pic[rotate=90,,transform shape] at (-0.5,-0.5) {schnittsymbol};')
        fd.write("\n"+r'\begin{scope}[yscale=1,xscale=-1]')
        fd.write("\n"+r'\pic[rotate=90,transform shape] at ($(rb)+(-0.5,-0.5)$) {schnittsymbol};')
        fd.write("\n"+r'\end{scope}')

        fd.write("\n"+r'}}')

        ansicht_waende(self, z_waende[1], anzahl_streifen,breite_sued, ls,'West',fd)
        ansicht_waende(self, z_waende[0], anzahl_streifen,breite_west, lw,'Sued',fd)




        ##Margin

        fd.write("\n"+r'\switchcolumn*')
        fd.write("\n"+r'\begin{figure}[H]')
        fd.write("\n"+r'\centering')
        fd.write("\n"+r'\begin{tikzpicture}')
        fd.write("\n"+r' \pic[scale=1,fill=black,text=black] at (0,0) {compass};')
        fd.write("\n"+r'\end{tikzpicture}')
        fd.write("\n"+r'\end{figure}')
        fd.write("\n"+r'alle Werte in $[m]$')
        fd.write("\n"+r'\switchcolumn')



        ####Bild zusammenfügen
        fd.write("\n"+r'\begin{figure}[H]')
        fd.write("\n"+r'\centering')
        fd.write("\n"+r'\begin{tikzpicture}')

        # #Grundriss Wände
        fd.write("\n"+r'\node[anchor=west] at (-1,'+ str(ls+1.4)+r')  {\Large{Grundriss Wände}};')
        fd.write("\n"+r'\pic at (7.5,0) {wand_west};')
        fd.write("\n"+r'\pic at (0,0) {wand_sued};')

        #Ansicht Wände
        fd.write("\n"+r'\pic at (7.5,'+ str(ls+2.6)+r') {wand_ansicht_West};')
        fd.write("\n"+r'\pic at (0,'+ str(ls+2.6)+r') {wand_ansicht_Sued};')
        #Windrose einfügen
        # fd.write("\n"+r' \pic[scale=1,fill=black,text=black] at (0,0) {compass};')
        fd.write("\n"+r'\end{tikzpicture}')
        fd.write("\n"+r'\end{figure}')

def ansicht_waende(self, z_hoehe, anzahl_streifen,breite, breite_latex,himmelsrichtung,fd):

    if z_hoehe[-1] > breite:
        h_latex=6
        scalefaktor=h_latex/z_hoehe[-1]
        breite_latex=float(breite)*scalefaktor
        z_latex=(np.array(z_hoehe)*scalefaktor).tolist()
    elif z_hoehe[-1] <= breite:
        scalefaktor=breite_latex/float(breite)
        z_latex=(np.array(z_hoehe)*scalefaktor).tolist()

    z_latex=[0]+z_latex


    # if len(z_hoehe)==2:
    #     z_latex=[0,breite_latex,h_latex]
    # elif len(z_hoehe) > 2:
    #     dicke_streifen=0.5
    #     z_latex=[0]
    #     for n in range(0,anzahl_streifen+1):
    #         z_latex.append(dicke_streifen * n + breite_latex)
    #     gesammthoehe=z_latex[-1]+breite_latex
    #     z_latex.append(gesammthoehe)


    hoehendifferenz=np.diff(np.array(z_hoehe)).tolist()
    hoehendifferenz.insert(0,z_hoehe[0])
    for ind, element in enumerate(hoehendifferenz):
        hoehendifferenz[ind]=round(element,1)





    fd.write("\n"+r'\tikzset{')
    fd.write("\n"+r'wand_ansicht_'+ himmelsrichtung+r'/.pic = {')
    #nodes und horizontale linien
    for ind, element in enumerate(z_latex):
        fd.write("\n"+r'\node[coordinate] at (0,'+ str(element)+r') (n'+ str(ind)+r'l) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(breite_latex)+r','+ str(element)+r') (n'+ str(ind)+r'r) {};')
        fd.write("\n"+r'\draw[line width=0.25mm] (n'+ str(ind)+r'l) -- (n'+ str(ind)+r'r) ;')

    #Beschriftung und Bemaßung
    for ind in range(0,len(z_hoehe)):
        fd.write("\n"+r'\node[between=n'+ str(ind)+r'l and n'+ str(ind+1)+r'r]  {\normalsize{$D_{'+ str(ind+1)+r'}$}};')
        fd.write("\n"+r'\DimlineV[n'+ str(ind)+r'l][n'+ str(ind+1)+r'l][-0.5][\num{'+ str(hoehendifferenz[ind])+r'}] ')

    if len(z_hoehe) > 1:
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
