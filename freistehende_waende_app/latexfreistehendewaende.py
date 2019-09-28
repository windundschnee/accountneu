import os
# from pylatex import Document, Section, Subsection, Command,Figure,TikZ, TikZNode, TikZDraw, TikZCoordinate, TikZUserPath, TikZOptions,Package
# from pylatex.utils import italic, NoEscape
# from latex import build_pdf
from gesamt_pdf_app.latexbasisfunktionen import *
from gesamt_pdf_app.models import GesamtPdf
from django.forms.models import model_to_dict






def geometrische_angaben_freistehende_waende(self,arg_latex,filename):

    wandhoehe = self.freistehende_waende.wandhoehe
    wandlaenge = self.freistehende_waende.wandlaenge
    wandverlauf = self.freistehende_waende.wandverlauf
    schenkellaenge = self.freistehende_waende.schenkellaenge
    voelligkeitsgrad = self.freistehende_waende.voelligkeitsgrad
    abschattung = self.freistehende_waende.abschattung
    abstand_abschattendewand = self.freistehende_waende.abstand_abschattendewand
    ergebnisse_freistehende_waende = arg_latex['ergebnisse_freistehende_waende']
    chi_schatt = ergebnisse_freistehende_waende['chi_schatt']
    qp=round(ergebnisse_freistehende_waende['qp'],2)
    bauteilname = self.freistehende_waende.bautteil_name.bautteil_name
    hoehe_abschattende_wand=self.freistehende_waende.hoehe_abschattende_wand
    hoehe_ueber_GOK=self.freistehende_waende.hoehe_ueber_GOK

    with io.open(filename,'w', encoding="UTF8") as fd:
        fd.write("\n"+r'\switchcolumn*')
        fd.write("\n"+r'\begin{tabular}{ r @{\dots} L{2.8cm} }')
        fd.write("\n"+r'$\ell$ & Wandlänge  ')
        fd.write("\n"+r'\\')
        fd.write("\n"+r'$h$ & Höhe  ')
        fd.write("\n"+r'\\')
        fd.write("\n"+r'$\varphi$ & Völligkeitsgrad  ')
        fd.write("\n"+r'\\')
        fd.write("\n"+r'$z$ & Höhe über Geländeoberkante  ')
        fd.write("\n"+r'\\')
        fd.write("\n"+r'$q_p$ & Böengeschwindigkeitsdruck  ')
        fd.write("\n"+r'\\')
        if abschattung=="Ja" and abstand_abschattendewand > 0:
            fd.write("\n"+r'$\psi_s$ & Abschattungsfaktor  ')
            fd.write("\n"+r'\\')
            fd.write("\n"+r'$h_{S}$ & Höhe der abschattenden Wand  ')
            fd.write("\n"+r'\\')
            fd.write("\n"+r'$x$ & Abstand zur abschattenden Wand  ')
            fd.write("\n"+r'\\')
        if wandverlauf=="Abgewinkelte Wand" and schenkellaenge > 0:
            fd.write("\n"+r'$\ell_s$ & Schenkellänge  ')
        fd.write("\n"+r'\end{tabular}')
        fd.write("\n"+r'\switchcolumn')


        fd.write("\n"+r'\begin{table}[H]')
        fd.write("\n"+r'\centering')
        fd.write("\n"+r'\begin{tabularx}{1\columnwidth}{B{1} B{1}  }')
        fd.write("\n"+r'\rowcolor{Gray}	')
        fd.write("\n"+r'\multicolumn{2}{c}{ \rule{0mm}{5mm}  \Large{\textbf{'+ str(bauteilname) +r' -- Freistehende Wand}}} \\')
        fd.write("\n"+r'		$\begin{aligned}[t]')
        fd.write("\n"+r'		h & =\lang{'+ str(wandhoehe)+r'}')
        fd.write("\n"+r'		\\')
        fd.write("\n"+r'		\ell & =\lang{'+ str(wandlaenge)+r'}')
        fd.write("\n"+r'		\\')
        fd.write("\n"+r'		q_p & =\spann{'+ str(qp)+r'}')
        if wandverlauf=="Abgewinkelte Wand" and schenkellaenge > 0:
            fd.write("\n"+r'		\\')
            fd.write("\n"+r'		\ell_s & =\lang{'+ str(schenkellaenge)+r'}')
        if abschattung=="Ja" and abstand_abschattendewand > 0:
            fd.write("\n"+r'		\\')
            fd.write("\n"+r'		x & =\lang{'+  str(round(abstand_abschattendewand, 2))+r'}')
        fd.write("\n"+r'		\end{aligned}$')
        fd.write("\n"+r'	&')
        fd.write("\n"+r'		$\begin{aligned}[t]')
        fd.write("\n"+r'		\varphi & =\num{'+ str(voelligkeitsgrad)+r'}')
        fd.write("\n"+r'		\\')
        fd.write("\n"+r'		z & =\lang{'+ str(hoehe_ueber_GOK)+r'}')
        if abschattung=="Ja" and abstand_abschattendewand > 0:
            fd.write("\n"+r'		\\')
            fd.write("\n"+r'		\psi_s & =\num{'+ str(chi_schatt)+r'}')
            fd.write("\n"+r'		\\')
            fd.write("\n"+r'		h_{S} & =\lang{'+ str(round(hoehe_abschattende_wand, 2))+r'}')
        fd.write("\n"+r'		\end{aligned}$')
        fd.write("\n"+r'\end{tabularx}')
        fd.write("\n"+r'\end{table}')
        if abschattung=="Ja" and float(abstand_abschattendewand) > 0:
            fd.write("\n"+r'\noindent')
            fd.write("\n"+r'Die Endbereiche der abgeschatteten Wand sind auf einer Länge, die gleich der Höhe h ist, für die volle Windbelastung ohne Abschattungsfaktor nachzuweisen.')


def ergebnisse_freistehende_waende_latex(self,arg_latex,filename):
    ergebnisse_freistehende_waende = arg_latex['ergebnisse_freistehende_waende']
    l_zu_h = ergebnisse_freistehende_waende['l_zu_h']
    cpA = ergebnisse_freistehende_waende['cpA']
    cpB = ergebnisse_freistehende_waende['cpB']
    cpC = ergebnisse_freistehende_waende['cpC']
    cpD = ergebnisse_freistehende_waende['cpD']
    wA = ergebnisse_freistehende_waende['wA']
    wB = ergebnisse_freistehende_waende['wB']
    wC = ergebnisse_freistehende_waende['wC']
    wD = ergebnisse_freistehende_waende['wD']
    wA_abgem = ergebnisse_freistehende_waende['wA_abgem']
    wB_abgem = ergebnisse_freistehende_waende['wB_abgem']
    wC_abgem = ergebnisse_freistehende_waende['wC_abgem']
    wD_abgem = ergebnisse_freistehende_waende['wD_abgem']


    abschattung = self.freistehende_waende.abschattung
    abstand_abschattendewand = self.freistehende_waende.abstand_abschattendewand
    with io.open(filename,'w', encoding="UTF8") as fd:

        fd.write("\n"+r'\begin{table}[H]')
        #fd.write("\n"+r'\caption*{\textbf{Ergebnisse}}'))
        if abschattung=="Ja" and float(abstand_abschattendewand) > 0:
            fd.write("\n"+r'	\begin{tabularx}{1\columnwidth}{ B{1} B{1} B{1} }')
            fd.write("\n"+r'\rowcolor{Gray}	')
            fd.write("\n"+r'	\textbf{Druckbeiwerte} & \textbf{Winddruck ohne Abschattungsfaktor} & \textbf{Winddruck mit Abschattungsfaktor} \\')
        else:
            fd.write("\n"+r'	\begin{tabularx}{1\columnwidth}{ B{1} B{1}}')
            fd.write("\n"+r'\rowcolor{Gray}	')
            fd.write("\n"+r'	\textbf{Druckbeiwerte} & \textbf{Winddruck} \\')
        fd.write("\n"+r'	$	\begin{aligned}')
        if l_zu_h > 4:
            fd.write("\n"+r'	c_{p,A}&= \SI{'+ str(cpA)+r'}{} \\ ')
            fd.write("\n"+r'	c_{p,B}&=\SI{'+ str(cpB)+r'}{}    \\')
            fd.write("\n"+r'c_{p,C}&=\SI{'+ str(cpC)+r'}{}   \\')
            fd.write("\n"+r'	c_{p,D}&=\SI{'+ str(cpD)+r'}{}  ')
        elif 2 < l_zu_h <= 4:
            fd.write("\n"+r'	c_{p,A}&= \SI{'+ str(cpA)+r'}{} \\ ')
            fd.write("\n"+r'	c_{p,B}&=\SI{'+ str(cpB)+r'}{}    \\')
            fd.write("\n"+r'c_{p,C}&=\SI{'+ str(cpC)+r'}{}   ')
        elif l_zu_h <=2:
            fd.write("\n"+r'	c_{p,A}&= \SI{'+ str(cpA)+r'}{} \\ ')
            fd.write("\n"+r'	c_{p,B}&=\SI{'+ str(cpB)+r'}{}    ')
        fd.write("\n"+r'		\end{aligned}		$')
        fd.write("\n"+r'	&')
        fd.write("\n"+r'		$\begin{aligned}')
        if l_zu_h > 4:
            fd.write("\n"+r'		w_{A}&= \SI{'+ str(wA)+r'}{\kilo\newton\per\square\meter} \\')
            fd.write("\n"+r'	w_{B}&=\SI{'+ str(wB)+r'}{\kilo\newton\per\square\meter}  \\')
            fd.write("\n"+r'		w_{C}&=\SI{'+ str(wC)+r'}{\kilo\newton\per\square\meter}  \\')
            fd.write("\n"+r'		w_{D}&=\SI{'+ str(wD)+r'}{\kilo\newton\per\square\meter} ')
        elif 2 < l_zu_h <= 4:
            fd.write("\n"+r'		w_{A}&= \SI{'+ str(wA)+r'}{\kilo\newton\per\square\meter} \\')
            fd.write("\n"+r'	w_{B}&=\SI{'+ str(wB)+r'}{\kilo\newton\per\square\meter}  \\')
            fd.write("\n"+r'		w_{C}&=\SI{'+ str(wC)+r'}{\kilo\newton\per\square\meter}  ')
        elif l_zu_h <=2:
            fd.write("\n"+r'		w_{A}&= \SI{'+ str(wA)+r'}{\kilo\newton\per\square\meter} \\')
            fd.write("\n"+r'	w_{B}&=\SI{'+ str(wB)+r'}{\kilo\newton\per\square\meter}  ')
        fd.write("\n"+r'		\end{aligned}$')
        if abschattung=="Ja" and abstand_abschattendewand > 0:
                fd.write("\n"+r'	&')
                fd.write("\n"+r'		$\begin{aligned}')
                if l_zu_h > 4:
                    fd.write("\n"+r'		w_{A}&= \SI{'+ str(wA_abgem)+r'}{\kilo\newton\per\square\meter} \\')
                    fd.write("\n"+r'	w_{B}&=\SI{'+ str(wB_abgem)+r'}{\kilo\newton\per\square\meter}  \\')
                    fd.write("\n"+r'		w_{C}&=\SI{'+ str(wC_abgem)+r'}{\kilo\newton\per\square\meter}  \\')
                    fd.write("\n"+r'		w_{D}&=\SI{'+ str(wD_abgem)+r'}{\kilo\newton\per\square\meter} ')
                elif 2 < l_zu_h <= 4:
                    fd.write("\n"+r'		w_{A}&= \SI{'+ str(wA_abgem)+r'}{\kilo\newton\per\square\meter} \\')
                    fd.write("\n"+r'	w_{B}&=\SI{'+ str(wB_abgem)+r'}{\kilo\newton\per\square\meter}  \\')
                    fd.write("\n"+r'		w_{C}&=\SI{'+ str(wC_abgem)+r'}{\kilo\newton\per\square\meter}  ')
                elif l_zu_h <=2:
                    fd.write("\n"+r'		w_{A}&= \SI{'+ str(wA_abgem)+r'}{\kilo\newton\per\square\meter} \\')
                    fd.write("\n"+r'	w_{B}&=\SI{'+ str(wB_abgem)+r'}{\kilo\newton\per\square\meter}  ')
                fd.write("\n"+r'		\end{aligned}$')
        fd.write("\n"+r'\end{tabularx}')
        fd.write("\n"+r'\end{table}')


def bilder_freistehende_waende(self, arg_latex,filename):
    # L_groesser4_freistehende_waende_filename = os.path.join(os.path.dirname(__file__), 'static','freistehende_waende_app','L_groesser4_freistehende_waende.pdf')
    # L_groesser4_freistehende_waende_filename_latex=L_groesser4_freistehende_waende_filename.replace("\\", "/")
    # L_kleiner4_freistehende_waende_filename = os.path.join(os.path.dirname(__file__), 'static','freistehende_waende_app','L_kleiner4_freistehende_waende.pdf')
    # L_kleiner4_freistehende_waende_filename_latex=L_kleiner4_freistehende_waende_filename.replace("\\", "/")
    # L_kleiner2_freistehende_waende_filename = os.path.join(os.path.dirname(__file__), 'static','freistehende_waende_app','L_kleiner2_freistehende_waende.pdf')
    # L_kleiner2_freistehende_waende_filename_latex=L_kleiner2_freistehende_waende_filename.replace("\\", "/")
    # geradliniger_verlauf_freistehende_waende_filename = os.path.join(os.path.dirname(__file__), 'static','freistehende_waende_app','geradliniger_verlauf_freistehende_waende.pdf')
    # geradliniger_verlauf_freistehende_waende_filename_latex=geradliniger_verlauf_freistehende_waende_filename.replace("\\", "/")
    # schenkellaenge_freistehende_waende_filename = os.path.join(os.path.dirname(__file__), 'static','freistehende_waende_app','schenkellaenge_freistehende_waende.pdf')
    # schenkellaenge_freistehende_waende_filename_latex=schenkellaenge_freistehende_waende_filename.replace("\\", "/")

    wandverlauf = self.freistehende_waende.wandverlauf
    ergebnisse_freistehende_waende = arg_latex['ergebnisse_freistehende_waende']
    l_zu_h = ergebnisse_freistehende_waende['l_zu_h']
    laengeA = ergebnisse_freistehende_waende['laengeA']
    laengeB = ergebnisse_freistehende_waende['laengeB']
    laengeC = ergebnisse_freistehende_waende['laengeC']
    laengeD = ergebnisse_freistehende_waende['laengeD']


    wandhoehe = self.freistehende_waende.wandhoehe
    wandlaenge = self.freistehende_waende.wandlaenge
    schenkellaenge = self.freistehende_waende.schenkellaenge
    hoehe_ueber_GOK=self.freistehende_waende.hoehe_ueber_GOK

    hoehe=2.5
    laenge_A_zeichnen=0.3*hoehe
    laenge_B_zeichnen=2*hoehe
    laenge_C_zeichnen=4*hoehe
    laenge_D_zeichnen=4*hoehe + 2
    if hoehe_ueber_GOK > 0:
        z_zeichen=0.5
    else:
        z_zeichen=0

    with io.open(filename,'w', encoding="UTF8") as fd:
        # fd.write("\n"+r'\tikzset{')
        # fd.write("\n"+r'pics/pfeilBeschriftung/.style args={#1}{')
        # fd.write("\n"+r'code = {')
        # fd.write("\n"+r'\draw[->] (0,0)--(0.3,0) node[right]{#1};')
        # fd.write("\n"+r'}}}')
        fd.write("\n"+r'\def\PfeilBeschriftung[#1][#2]{')
        fd.write("\n"+r'\draw[<-] #1-- +(0.2,0) node[right]{\scriptsize{#2}};')
        fd.write("\n"+r'\draw #1-- +(0,0.15);')
        fd.write("\n"+r'\draw #1-- +(0,-0.15);')
        fd.write("\n"+r'}')


        ###############
        #Ansicht
        fd.write("\n"+r'\tikzset{')
        fd.write("\n"+r'freistehende_waende_Ansicht/.pic = {')
        #unten
        fd.write("\n"+r'\node[coordinate] at (0,0) (nau) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(laenge_A_zeichnen)+r',0) (nabu) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(laenge_B_zeichnen)+r',0) (nbcu) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(laenge_C_zeichnen)+r',0) (ncdu) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(laenge_D_zeichnen)+r',0) (ndu) {};')
        #oben
        fd.write("\n"+r'\node[coordinate] at (0,'+ str(hoehe)+r') (nao) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(laenge_A_zeichnen)+r','+ str(hoehe)+r') (nabo) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(laenge_B_zeichnen)+r','+ str(hoehe)+r') (nbco) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(laenge_C_zeichnen)+r','+ str(hoehe)+r') (ncdo) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(laenge_D_zeichnen)+r','+ str(hoehe)+r') (ndo) {};')
        fd.write("\n"+r'\node[coordinate] at ($(nau)+(0,-'+ str(z_zeichen)+r')$) (ngrund) {};')
        ###########Bereich A
        fd.write("\n"+r'\draw[line width=0.25mm] (nau) -- (nabu) -- (nabo) -- (nao) -- (nau);')

        #Grund
        fd.write("\n"+r'\draw[line width=0.35mm] ($(nau)+(0,-'+ str(z_zeichen)+r')$) -- +(-0.5,0);')
        fd.write("\n"+r'\draw[line width=0.35mm] ($(nau)+(0,-'+ str(z_zeichen)+r')$) -- ($(nabu)+(0,-'+ str(z_zeichen)+r')$);')
        fd.write("\n"+r'\fill[pattern,pattern= north east lines] ($(nau)-(0.5,'+ str(z_zeichen)+r')$) rectangle ($(nabu)+(0.0,-'+ str(z_zeichen)+r'-0.3)$);')
        #Beschriftung
        fd.write("\n"+r'\node[between=nau and nabo]  {\Large{A}};')
        fd.write("\n"+r'\PfeilBeschriftung[($(nao)+(0,0.4)$)][$0$]')
        fd.write("\n"+r'\PfeilBeschriftung[($(nabo)+(0,0.4)$)][\num{'+ str(laengeA)+r'}]')
        fd.write("\n"+r'\DimlineV[nau][nao][-0.7][\num{'+ str(wandhoehe)+r'}]')
        fd.write("\n"+r'\DimlineH[nau][nabu]['+ str(-z_zeichen-0.9)+r'][\num{'+ str(laengeA)+r'}] ')
        if hoehe_ueber_GOK > 0:
            fd.write("\n"+r'\DimlineV[ngrund][nau][-0.7][\num{'+ str(hoehe_ueber_GOK)+r'}]')


        ###########Bereich B
        fd.write("\n"+r'\draw[line width=0.25mm] (nabu) -- (nbcu) -- (nbco) -- (nabo);')

        #Grund
        fd.write("\n"+r'\draw[line width=0.35mm] ($(nabu)+(0,-'+ str(z_zeichen)+r')$) -- ($(nbcu)+(0,-'+ str(z_zeichen)+r')$);')
        fd.write("\n"+r'\fill[pattern,pattern= north east lines] ($(nabu)-(0,'+ str(z_zeichen)+r')$) rectangle ($(nbcu)+(0.0,-'+ str(z_zeichen)+r'-0.3)$);')
        #Beschriftung
        fd.write("\n"+r'\node[between=nabu and nbco]  {\Large{B}};')
        fd.write("\n"+r'\PfeilBeschriftung[($(nbco)+(0,0.4)$)][\num{'+ str(laengeA+laengeB)+r'}]')
        fd.write("\n"+r'\DimlineH[nabu][nbcu]['+ str(-z_zeichen-0.9)+r'][\num{'+ str(laengeB)+r'}] ')
        if l_zu_h <=2:
            fd.write("\n"+r'\draw[line width=0.35mm] ($(nbcu)+(0,-'+ str(z_zeichen)+r')$) -- +(0.5,0);')
            fd.write("\n"+r'\fill[pattern,pattern= north east lines] ($(nbcu)-(0,'+ str(z_zeichen)+r')$) rectangle ($(nbcu)+(0.5,-'+ str(z_zeichen)+r'-0.3)$);')
            fd.write("\n"+r'\DimlineH[nau][nbcu]['+ str(-z_zeichen-1.4)+r'][\num{'+ str(wandlaenge)+r'}] ')
        if l_zu_h >2:
            ###########Bereich C
            fd.write("\n"+r'\draw[line width=0.25mm] (nbcu) -- (ncdu) -- (ncdo) -- (nbco);')

            #Grund
            fd.write("\n"+r'\draw[line width=0.35mm] ($(nbcu)+(0,-'+ str(z_zeichen)+r')$) -- ($(ncdu)+(0,-'+ str(z_zeichen)+r')$);')
            fd.write("\n"+r'\fill[pattern,pattern= north east lines] ($(nbcu)-(0,'+ str(z_zeichen)+r')$) rectangle ($(ncdu)+(0.0,-'+ str(z_zeichen)+r'-0.3)$);')
            #Beschriftung
            fd.write("\n"+r'\node[between=nbcu and ncdo]  {\Large{C}};')
            fd.write("\n"+r'\PfeilBeschriftung[($(ncdo)+(0,0.4)$)][\num{'+ str(laengeA+laengeB+laengeC)+r'}]')
            fd.write("\n"+r'\DimlineH[nbcu][ncdu]['+ str(-z_zeichen-0.9)+r'][\num{'+ str(laengeC)+r'}] ')
        if 2 < l_zu_h <= 4:
            fd.write("\n"+r'\draw[line width=0.35mm] ($(ncdu)+(0,-'+ str(z_zeichen)+r')$) -- +(0.5,0);')
            fd.write("\n"+r'\fill[pattern,pattern= north east lines] ($(ncdu)-(0,'+ str(z_zeichen)+r')$) rectangle ($(ncdu)+(0.5,-'+ str(z_zeichen)+r'-0.3)$);')
            fd.write("\n"+r'\DimlineH[nau][ncdu]['+ str(-z_zeichen-1.4)+r'][\num{'+ str(wandlaenge)+r'}] ')
        if l_zu_h > 4:
            ###########Bereich D
            fd.write("\n"+r'\draw[line width=0.25mm] (ncdu) -- (ndu) -- (ndo) -- (ncdo);')

            #Grund
            fd.write("\n"+r'\draw[line width=0.35mm] ($(ncdu)+(0,-'+ str(z_zeichen)+r')$) -- ($(ndu)+(0,-'+ str(z_zeichen)+r')$);')
            fd.write("\n"+r'\fill[pattern,pattern= north east lines] ($(ncdu)-(0,'+ str(z_zeichen)+r')$) rectangle ($(ndu)+(0.0,-'+ str(z_zeichen)+r'-0.3)$);')
            fd.write("\n"+r'\draw[line width=0.35mm] ($(ndu)+(0,-'+ str(z_zeichen)+r')$) -- +(0.5,0);')
            fd.write("\n"+r'\fill[pattern,pattern= north east lines] ($(ndu)-(0,'+ str(z_zeichen)+r')$) rectangle ($(ndu)+(0.5,-'+ str(z_zeichen)+r'-0.3)$);')
            #Beschriftung
            fd.write("\n"+r'\node[between=ncdu and ndo]  {\Large{D}};')
            fd.write("\n"+r'\DimlineH[ncdu][ndu]['+ str(-z_zeichen-0.9)+r'][\num{'+ str(laengeD)+r'}] ')
            fd.write("\n"+r'\DimlineH[nau][ndu]['+ str(-z_zeichen-1.4)+r'][\num{'+ str(wandlaenge)+r'}] ')

        fd.write("\n"+r'}}')

        #Grundriss Gerade
        fd.write("\n"+r'\tikzset{')
        fd.write("\n"+r'freistehende_waende_Grundriss_gerade/.pic = {')
        #Coordinaten
        fd.write("\n"+r'\node[coordinate] at (0,0) (na) {};')
        if l_zu_h <=2:
            fd.write("\n"+r'\node[coordinate] at ('+ str(laenge_B_zeichnen)+r',0) (nb) {};')
        elif 2 < l_zu_h <= 4:
            fd.write("\n"+r'\node[coordinate] at ('+ str(laenge_C_zeichnen)+r',0) (nb) {};')
        elif l_zu_h > 4:
            fd.write("\n"+r'\node[coordinate] at ('+ str(laenge_D_zeichnen)+r',0) (nb) {};')
        #Wand
        fd.write("\n"+r'\draw[fill=Gray] (na) rectangle ($(nb)+(0.0,0.2)$);')
        #Bemasung
        fd.write("\n"+r'\DimlineH[na][nb][-0.5][\num{'+ str(wandlaenge)+r'}] ')
        #Pfeile für die Windrichtung
        fd.write("\n"+r'\pic[rotate=-45,,transform shape] at (-0.3,-0.3) {windrichtung};')


        fd.write("\n"+r'}}')

        #Grundriss Schänkellänge
        fd.write("\n"+r'\tikzset{')
        fd.write("\n"+r'freistehende_waende_Grundriss_schenkelaenge/.pic = {')
        #Coordinaten
        fd.write("\n"+r'\node[coordinate] at (0,0) (na) {};')
        fd.write("\n"+r'\node[coordinate] at (0,1.0) (nc) {};')
        if l_zu_h <=2:
            fd.write("\n"+r'\node[coordinate] at ('+ str(laenge_B_zeichnen)+r',0) (nb) {};')
        elif 2 < l_zu_h <= 4:
            fd.write("\n"+r'\node[coordinate] at ('+ str(laenge_C_zeichnen)+r',0) (nb) {};')
        elif l_zu_h > 4:
            fd.write("\n"+r'\node[coordinate] at ('+ str(laenge_D_zeichnen)+r',0) (nb) {};')
        #Wand
        fd.write("\n"+r'\fill[Gray] (na) rectangle ($(nb)+(0.0,0.2)$);')
        fd.write("\n"+r'\fill[Gray] (na) rectangle ($(nc)+(0.2,0.0)$);')
        fd.write("\n"+r'\draw (na) -- (nb) --  ($(nb)+(0,0.2)$) -- (0.2,0.2) -- ($(nc)+(0.2,0)$)--(nc)--(na);')
        #Bemasung
        fd.write("\n"+r'\DimlineH[na][nb][-0.5][\num{'+ str(wandlaenge)+r'}] ')
        fd.write("\n"+r'\DimlineV[na][nc][-0.3][\num{'+ str(schenkellaenge)+r'}]')
        #Pfeile für die Windrichtung
        fd.write("\n"+r'\pic[rotate=-45,,transform shape] at (-0.3,-0.3) {windrichtung};')


        fd.write("\n"+r'}}')





        #Figure zusammenfügen
        ##Margin
        fd.write("\n"+r'\switchcolumn*')
        fd.write("\n"+r'alle Werte in $[m]$')
        #fd.write("\n"+r'\begin{tikzpicture}')
        #fd.write("\n"+r' \pic[scale=1,fill=black,text=black] at (0,0) {compass};')
        #fd.write("\n"+r'\end{tikzpicture}')
        fd.write("\n"+r'\switchcolumn')

        fd.write("\n"+r'\begin{figure}[H]')
        fd.write("\n"+r'\centering')
        fd.write("\n"+r'\begin{tikzpicture}')
        #Ansicht einfügen
        fd.write("\n"+r'\node at (0,4)  {\Large{Ansicht}};')
        fd.write("\n"+r'\pic at (0,0) {freistehende_waende_Ansicht};')
        fd.write("\n"+r'\node at (0,-2.5)  {\Large{Grundriss}};')
        if wandverlauf=="Gerade Wand":
            fd.write("\n"+r'\pic at (0,-3.5) {freistehende_waende_Grundriss_gerade};')
        else:
            fd.write("\n"+r'\pic at (0,-4.5) {freistehende_waende_Grundriss_schenkelaenge};')



        fd.write("\n"+r'\end{tikzpicture}')
        fd.write("\n"+r'\end{figure}')
