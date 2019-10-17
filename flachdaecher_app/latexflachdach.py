import os
import io
from gesamt_pdf_app.reibung import reibung_margin_vernachlaessigen,reibung_margin_tab
# from pylatex import Document, Section, Subsection, Command,Figure,TikZ, TikZNode, TikZDraw, TikZCoordinate, TikZUserPath, TikZOptions,Package
# from pylatex.utils import italic, NoEscape
# from latex import build_pdf
# from gesamt_pdf_app.latexbasisfunktionen import *
# from gesamt_pdf_app.models import GesamtPdf
# from django.forms.models import model_to_dict






def geometrische_angaben_flachdach(self,arg_latex,filename):

    art_traufenbereich = self.flachdach.art_traufenbereich
    hoehe = self.flachdach.hoehe
    hoehe_attika = self.flachdach.hoehe_attika
    radius = self.flachdach.radius
    alpha = self.flachdach.alpha
    breite_x = self.flachdach.breite_x
    breite_y = self.flachdach.breite_y
    vereinfachtes_verfahren = self.flachdach.some_field
    bauteilname = self.flachdach.bautteil_name.bautteil_name
    oeffnung_nord_flaeche=self.flachdach.oeffnung_nord_flaeche
    oeffnung_ost_flaeche=self.flachdach.oeffnung_ost_flaeche
    oeffnung_sued_flaeche=self.flachdach.oeffnung_sued_flaeche
    oeffnung_west_flaeche=self.flachdach.oeffnung_west_flaeche
    oeffnungen_beruecksichtigen=self.flachdach.oeffnungen_beruecksichtigen
    oeffnungen_flaeche=[oeffnung_nord_flaeche,oeffnung_ost_flaeche,oeffnung_sued_flaeche,oeffnung_west_flaeche]
    windrichtung=['Norden','Osten','Süden','Westen']
    ergebnisse_berechnung =  arg_latex['ergebnisse_berechnung']
    ergebnisse_waende=ergebnisse_berechnung['ergebnisse_waende']
    qp=ergebnisse_berechnung['qp']



    with io.open(filename,'w', encoding="UTF8") as fd:
        #Beschreibung in Margin
        fd.write("\n"+r'\switchcolumn*')
        fd.write("\n"+r'\begin{tabular}{ r @{\dots} L{2.8cm} }')
        fd.write("\n"+r'$\ell_W$ & Länge Westseite  ')
        fd.write("\n"+r'\\')
        fd.write("\n"+r'$\ell_S$ & Länge Südseite  ')
        fd.write("\n"+r'\\')
        fd.write("\n"+r'$h$ & Traufenhöhe  ')
        fd.write("\n"+r'\\')
        fd.write("\n"+r'$q_p$ & Böengeschwin- digkeitsdruck  ')
        fd.write("\n"+r'\\')
        if art_traufenbereich=="mit Attika" and vereinfachtes_verfahren=='Verfahren gemäß ÖNORM EN 1991-1-4, Abschnitt 7.2.3':
            fd.write("\n"+r'$h_p$ & Höhe Attika  ')
            fd.write("\n"+r'\\')
        elif art_traufenbereich=="abgerundeter Traufbereich"  and vereinfachtes_verfahren=='Verfahren gemäß ÖNORM EN 1991-1-4, Abschnitt 7.2.3':
            fd.write("\n"+r'$r$ & Radius der Abrundung  ')
            fd.write("\n"+r'\\')
        elif art_traufenbereich=="mansardenartig abgeschrägter Traufbereich"  and vereinfachtes_verfahren=='Verfahren gemäß ÖNORM EN 1991-1-4, Abschnitt 7.2.3':
            fd.write("\n"+r'$\alpha$ &  Winkel Mansarde  ')
            fd.write("\n"+r'\\')
        if oeffnungen_beruecksichtigen==True:
            fd.write("\n"+r'$A_{Ö}$ &  Öffnungsfläche an der jeweiligen Wandseite ')
            fd.write("\n"+r'\\')
        fd.write("\n"+r'\end{tabular}')
        fd.write("\n"+r'\switchcolumn')

        #####geometrische geometrische_angaben_flachdach
        fd.write("\n"+r'\begin{table}[H]')
        fd.write("\n"+r'\centering')
        if oeffnungen_beruecksichtigen==True:
            fd.write("\n"+r'\begin{tabularx}{1\columnwidth}{B{1} B{1} B{1} }')
            fd.write("\n"+r'\rowcolor{Gray}	')
            fd.write("\n"+r'\multicolumn{3}{c}{  \rule{0mm}{5mm} \Large{\textbf{'+ str(bauteilname) +r' -- Gebäude mit Flachdach }}} \\')
        else:
            fd.write("\n"+r'\begin{tabularx}{1\columnwidth}{B{1} B{1}  }')
            fd.write("\n"+r'\rowcolor{Gray}	')
            fd.write("\n"+r'\multicolumn{2}{c}{ \rule{0mm}{5mm} \Large{\textbf{'+ str(bauteilname) +r' -- Gebäude mit Flachdach}}} \\')
        fd.write("\n"+r'		$\begin{aligned}[t]')
        fd.write("\n"+r'		\ell_S & =\lang{'+ str(breite_y)+r'}')
        fd.write("\n"+r'		\\')
        fd.write("\n"+r'		\ell_W & =\lang{'+ str(breite_x)+r'}')
        fd.write("\n"+r' \\		q_p & =\spann{'+ str(qp)+r'}')

        fd.write("\n"+r'		\end{aligned}$')
        fd.write("\n"+r'	&')
        fd.write("\n"+r'		$\begin{aligned}[t]')
        fd.write("\n"+r'		h & =\lang{'+  str(hoehe)+r'}')
        fd.write("\n"+r'		\\')
        if art_traufenbereich=="mit Attika" and vereinfachtes_verfahren=='Verfahren gemäß ÖNORM EN 1991-1-4, Abschnitt 7.2.3':
            fd.write("\n"+r'		h_p & =\lang{'+ str(hoehe_attika)+r'}')
        elif art_traufenbereich=="abgerundeter Traufbereich"  and vereinfachtes_verfahren=='Verfahren gemäß ÖNORM EN 1991-1-4, Abschnitt 7.2.3':
            fd.write("\n"+r'		r & =\lang{'+ str(radius)+r'}')
        elif art_traufenbereich=="mansardenartig abgeschrägter Traufbereich"  and vereinfachtes_verfahren=='Verfahren gemäß ÖNORM EN 1991-1-4, Abschnitt 7.2.3':
            fd.write("\n"+r'		\alpha & =\ang{'+ str(alpha)+r'}')

        fd.write("\n"+r'		\end{aligned}$')
        if oeffnungen_beruecksichtigen==True:
            fd.write("\n"+r'	&')
            fd.write("\n"+r'		$\begin{aligned}[t]')
            for ind, element in enumerate(oeffnungen_flaeche):
                fd.write("\n"+r'  A_{Ö,'+ windrichtung[ind]+r'}&=\SI{'+ str(element)+r'}{\square\meter}  \\ ')
            fd.write("\n"+r'		\end{aligned}$')

        fd.write("\n"+r'\end{tabularx}')
        fd.write("\n"+r'\end{table}')


def aussendruckbeiwerte(self,arg_latex,cpe_dach,einflussflaeche,fd):

    ergebnisse_berechnung=arg_latex['ergebnisse_berechnung']
    #print(ergebnisse_berechnung)

    vereinfachtes_verfahren = self.flachdach.some_field
    art_traufenbereich = self.flachdach.art_traufenbereich
    cp_f=cpe_dach[0]
    cp_g=cpe_dach[1]

    fd.write("\n"+r'	$	\begin{aligned}[t]')
    fd.write("\n"+r'	c_{pe,'+ str(einflussflaeche)+r',F}&= \SI{'+ str(cp_f)+r'}{} \\ ')
    fd.write("\n"+r'	c_{pe,'+ str(einflussflaeche)+r',G}&=\SI{'+ str(cp_g)+r'}{}    \\')
    if vereinfachtes_verfahren == 'Vereinfachtes Verfahren gemäß ÖNORM B 1991-1-4, Abschnitt 9.2.3.1':


        cp_h_druck=cpe_dach[2]
        cp_i_druck=cpe_dach[4]
        cp_h_sog=cpe_dach[3]
        cp_i_sog=cpe_dach[5]
        fd.write("\n"+r'c_{pe,'+ str(einflussflaeche)+r',H}&=\SI{'+ str(cp_h_druck)+r'}{}   \\')
        fd.write("\n"+r'	c_{pe,'+ str(einflussflaeche)+r',H}&=\SI{'+ str(cp_h_sog)+r'}{} \\ ')
        fd.write("\n"+r'	c_{pe,'+ str(einflussflaeche)+r',I}&=\SI{'+ str(cp_i_druck)+r'}{} \\ ')
        fd.write("\n"+r'	c_{pe,'+ str(einflussflaeche)+r',I}&=\SI{'+ str(cp_i_sog)+r'}{}  ')
    else:

        cp_h=cpe_dach[2]
        cp_i=abs(cpe_dach[3])
        fd.write("\n"+r'c_{pe,'+ str(einflussflaeche)+r',H}&=\SI{'+ str(cp_h)+r'}{}   \\')
        fd.write("\n"+r'	c_{pe,'+ str(einflussflaeche)+r',I}&=\SI{\pm'+ str(cp_i)+r'}{}  ')
        if art_traufenbereich=="mansardenartig abgeschrägter Traufbereich":


            cp_auf_mans_sog=cpe_dach[5]
            cp_auf_mans_druck=cpe_dach[6]

            fd.write("\n"+r'\\ c_{pe,'+ str(einflussflaeche)+r',Mansarde}&=\SI{'+ str(cp_auf_mans_druck)+r'}{}   \\')
            fd.write("\n"+r' c_{pe,'+ str(einflussflaeche)+r',Mansarde}&=\SI{'+ str(cp_auf_mans_sog)+r'}{}   ')
        else:
            print('keine Mansarden')
    fd.write("\n"+r'		\end{aligned}		$')



def aussenwinddruck(self,arg_latex,aussenwinddruck_dach,einflussflaeche,fd):


    ergebnisse_berechnung=arg_latex['ergebnisse_berechnung']

    wa_f=aussenwinddruck_dach[0]
    wa_g=aussenwinddruck_dach[1]

    vereinfachtes_verfahren = self.flachdach.some_field


    art_traufenbereich = self.flachdach.art_traufenbereich
    fd.write("\n"+r'		$\begin{aligned}[t]')
    fd.write("\n"+r'		w_{e,'+ str(einflussflaeche)+r',F}&= \SI{'+ str(wa_f)+r'}{\kilo\newton\per\square\meter} \\')
    fd.write("\n"+r'	w_{e,'+ str(einflussflaeche)+r',G}&=\SI{'+ str(wa_g)+r'}{\kilo\newton\per\square\meter}  \\')
    if vereinfachtes_verfahren == 'Vereinfachtes Verfahren gemäß ÖNORM B 1991-1-4, Abschnitt 9.2.3.1':
        wa_h_druck=aussenwinddruck_dach[2]
        wa_i_druck=aussenwinddruck_dach[4]
        wa_h_sog=aussenwinddruck_dach[3]
        wa_i_sog=aussenwinddruck_dach[5]
        fd.write("\n"+r'		w_{e,'+ str(einflussflaeche)+r',H}&=\SI{'+ str(wa_h_druck)+r'}{\kilo\newton\per\square\meter}  \\')
        fd.write("\n"+r'		w_{e,'+ str(einflussflaeche)+r',H}&=\SI{'+ str(wa_h_sog)+r'}{\kilo\newton\per\square\meter} \\')
        fd.write("\n"+r'		w_{e,'+ str(einflussflaeche)+r',I}&=\SI{'+ str(wa_i_druck)+r'}{\kilo\newton\per\square\meter} \\')
        fd.write("\n"+r'		w_{e,'+ str(einflussflaeche)+r',I}&=\SI{'+ str(wa_i_sog)+r'}{\kilo\newton\per\square\meter} \\')
    else:

        wa_h=aussenwinddruck_dach[2]
        wa_i=abs(aussenwinddruck_dach[3])
        fd.write("\n"+r'		w_{e,'+ str(einflussflaeche)+r',H}&=\SI{'+ str(wa_h)+r'}{\kilo\newton\per\square\meter}  \\')
        fd.write("\n"+r'		w_{e,'+ str(einflussflaeche)+r',I}&=\SI{\pm'+ str(wa_i)+r'}{\kilo\newton\per\square\meter} ')
        if art_traufenbereich=="mansardenartig abgeschrägter Traufbereich":
            wa_auf_mans_sog=aussenwinddruck_dach[5]
            wa_auf_mans_druck=aussenwinddruck_dach[6]
            fd.write("\n"+r'	\\	w_{e,'+ str(einflussflaeche)+r',Mansarde}&=\SI{'+ str(wa_auf_mans_druck)+r'}{\kilo\newton\per\square\meter}  \\')
            fd.write("\n"+r'		w_{e,'+ str(einflussflaeche)+r',Mansarde}&=\SI{'+ str(wa_auf_mans_sog)+r'}{\kilo\newton\per\square\meter} ')
        else:
            print('Fehler in Latex mansardenartige we werte, Flachdächer')
    fd.write("\n"+r'		\end{aligned}		$')
def innendruckbeiwerte(self,arg_latex,fd):

    ergebnisse_berechnung=arg_latex['ergebnisse_berechnung']

    ergebnisse_waende=ergebnisse_berechnung['ergebnisse_waende']

    cpi=ergebnisse_waende['cpi']
    windrichtung=['Norden','Osten','Süden','Westen']
    some_field_radio2 = self.flachdach.some_field_radio2

    fd.write("\n"+r'$	\begin{aligned}[t]')
    if some_field_radio2=='Innendruckbeiwerte mittels empfohlener Werte nach Abschnitt 9.2.10':
        cpi_druck=cpi[0]
        cpi_sog=cpi[1]
        fd.write("\n"+r'c_{pi,Druck}&=\SI{'+ str(cpi_druck)+r'}{}   \\')
        fd.write("\n"+r'c_{pi,Sog}&=\SI{'+ str(cpi_sog)+r'}{}   ')
    elif some_field_radio2=='Innendruckbeiwerte mittels dominanter Fläche nach Abschnitt 7.2.9':
        for ind, element in enumerate(cpi):
            fd.write("\n"+r'c_{pi,'+ windrichtung[ind]+r'}&=\SI{'+ str(element)+r'}{}   \\')

    fd.write("\n"+r'		\end{aligned}		$')

def innenwinddruck(self,arg_latex,fd):

    ergebnisse_berechnung=arg_latex['ergebnisse_berechnung']
    some_field_radio2 = self.flachdach.some_field_radio2
    ergebnisse_waende=ergebnisse_berechnung['ergebnisse_waende']
    innendruck=ergebnisse_waende['innendruck']
    windrichtung=['Norden','Osten','Süden','Westen']


    fd.write("\n"+r'	$	\begin{aligned}[t]')
    if some_field_radio2=='Innendruckbeiwerte mittels empfohlener Werte nach Abschnitt 9.2.10':
        wi_druck=innendruck[0]
        wi_sog=innendruck[1]
        fd.write("\n"+r'w_{i}&=\SI{'+ str(wi_druck)+r'}{}   \\')
        fd.write("\n"+r'w_{i}&=\SI{'+ str(wi_sog)+r'}{}   ')
    elif some_field_radio2=='Innendruckbeiwerte mittels dominanter Fläche nach Abschnitt 7.2.9':
        for ind, element in enumerate(innendruck):
            fd.write("\n"+r'w_{i,'+ windrichtung[ind]+r'}&=\SI{'+ str(element)+r'}{}   \\')

    fd.write("\n"+r'		\end{aligned}		$')

def ueberlagerter_winddruck(self,arg_latex,fd):
    ergebnisse_berechnung=arg_latex['ergebnisse_berechnung']
    ergebnisse_ueberlagerung_dach=ergebnisse_berechnung['ergebnisse_ueberlagerung_dach']



    w_f=ergebnisse_ueberlagerung_dach[0][0]
    w_g=ergebnisse_ueberlagerung_dach[0][1]

    vereinfachtes_verfahren = self.flachdach.some_field
    art_traufenbereich = self.flachdach.art_traufenbereich
    fd.write("\n"+r'		$\begin{aligned}[t]')
    fd.write("\n"+r'		w_{F}&= \SI{'+ str(w_f)+r'}{\kilo\newton\per\square\meter} \\')
    fd.write("\n"+r'	w_{G}&=\SI{'+ str(w_g)+r'}{\kilo\newton\per\square\meter}  \\')
    if vereinfachtes_verfahren == 'Vereinfachtes Verfahren gemäß ÖNORM B 1991-1-4, Abschnitt 9.2.3.1':
        w_h_druck=ergebnisse_ueberlagerung_dach[0][2]
        w_i_druck=ergebnisse_ueberlagerung_dach[0][4]
        w_h_sog=ergebnisse_ueberlagerung_dach[0][3]
        w_i_sog=ergebnisse_ueberlagerung_dach[0][5]
        fd.write("\n"+r'		w_{H}&=\SI{'+ str(w_h_druck)+r'}{\kilo\newton\per\square\meter}  \\')
        fd.write("\n"+r'		w_{H}&=\SI{'+ str(w_h_sog)+r'}{\kilo\newton\per\square\meter} \\')
        fd.write("\n"+r'		w_{I}&=\SI{'+ str(w_i_druck)+r'}{\kilo\newton\per\square\meter} \\')
        fd.write("\n"+r'		w_{I}&=\SI{'+ str(w_i_sog)+r'}{\kilo\newton\per\square\meter} ')
    else:
        w_h=ergebnisse_ueberlagerung_dach[0][2]
        w_i_druck=ergebnisse_ueberlagerung_dach[0][3]
        w_i_sog=ergebnisse_ueberlagerung_dach[0][4]
        fd.write("\n"+r'		w_{H}&=\SI{'+ str(w_h)+r'}{\kilo\newton\per\square\meter}  \\')
        fd.write("\n"+r'		w_{I}&=\SI{'+ str(w_i_druck)+r'}{\kilo\newton\per\square\meter} \\')
        fd.write("\n"+r'		w_{I}&=\SI{'+ str(w_i_sog)+r'}{\kilo\newton\per\square\meter} ')
        if art_traufenbereich=="mansardenartig abgeschrägter Traufbereich":
            w_auf_mans_sog=ergebnisse_ueberlagerung_dach[0][6]
            w_auf_mans_druck=ergebnisse_ueberlagerung_dach[0][5]
            fd.write("\n"+r'	\\	w_{Mansarde}&=\SI{'+ str(w_auf_mans_sog)+r'}{\kilo\newton\per\square\meter}  \\')
            fd.write("\n"+r'		w_{Mansarde}&=\SI{'+ str(w_auf_mans_druck)+r'}{\kilo\newton\per\square\meter} ')
        else:
            print('Fehler in Latex mansardenartige we werte, Flachdächer')
    fd.write("\n"+r'		\end{aligned}		$')

def ueberlagerter_winddruck_norden(self,arg_latex,fd):
    ergebnisse_berechnung=arg_latex['ergebnisse_berechnung']
    ergebnisse_ueberlagerung_dach=ergebnisse_berechnung['ergebnisse_ueberlagerung_dach']
    vereinfachtes_verfahren = self.flachdach.some_field
    art_traufenbereich = self.flachdach.art_traufenbereich

    fd.write("\n"+r'		$\begin{aligned}[t]')
    if vereinfachtes_verfahren == 'Vereinfachtes Verfahren gemäß ÖNORM B 1991-1-4, Abschnitt 9.2.3.1':
        bezeichnung=['F','G','H','H','I','I']
        fd.write("\n"+r'		w_{I,x}&=\SI{'+ str(w_i_sog_x)+r'}{\kilo\newton\per\square\meter} \\')
    else:
        bezeichnung=['F','G','H','I','I']
        if art_traufenbereich=="mansardenartig abgeschrägter Traufbereich":
            bezeichnung=['F','G','H','I','I','Mansarde','Mansarde']
    for ind, element in enumerate(ergebnisse_ueberlagerung_dach[0]):
        fd.write("\n"+r'w_{'+ bezeichnung[ind]+r'}&=\spann{'+ str(element)+r'}  \\')
    fd.write("\n"+r'		\end{aligned}		$')

def ueberlagerter_winddruck_ost_sued_west(self,arg_latex,fd):
    ergebnisse_berechnung=arg_latex['ergebnisse_berechnung']
    ergebnisse_ueberlagerung_dach=ergebnisse_berechnung['ergebnisse_ueberlagerung_dach']
    vereinfachtes_verfahren = self.flachdach.some_field
    art_traufenbereich = self.flachdach.art_traufenbereich

    if vereinfachtes_verfahren == 'Vereinfachtes Verfahren gemäß ÖNORM B 1991-1-4, Abschnitt 9.2.3.1':
        bezeichnung=['F','G','H','H','I','I']
        fd.write("\n"+r'		w_{I,x}&=\SI{'+ str(w_i_sog_x)+r'}{\kilo\newton\per\square\meter} \\')
    else:
        bezeichnung=['F','G','H','I','I']
        if art_traufenbereich=="mansardenartig abgeschrägter Traufbereich":
            bezeichnung=['F','G','H','I','I','Mansarde','Mansarde']

    for ind_windrichtung, element_Windrichtung in enumerate([1,2,3]):
        fd.write("\n"+r'		$\begin{aligned}[t]')
        for ind, element in enumerate(ergebnisse_ueberlagerung_dach[element_Windrichtung]):
            fd.write("\n"+r'w_{'+ bezeichnung[ind]+r'}&=\spann{'+ str(element)+r'}  \\')
        fd.write("\n"+r'		\end{aligned}		$')
        if element_Windrichtung != 3:
            fd.write("\n"+r'		&		')


def reibung_latex(self,arg_latex,fd):
    waende_beruecksichtigen=self.flachdach.waende_beruecksichtigen
    ergebnisse_berechnung =  arg_latex['ergebnisse_berechnung']
    ergebnisse_waende=ergebnisse_berechnung['ergebnisse_waende']
    w_cfr_dach=ergebnisse_berechnung['w_cfr_dach']
    reibung_vernachlaessigt=ergebnisse_berechnung['reibung_vernachlaessigt']
    reibbeiwert_dach=self.flachdach.reibbeiwert_dach
    reibbeiwert_waende=self.flachdach.reibbeiwert_waende

    w_cfr_wand=ergebnisse_waende['w_cfr_wand']

    fd.write("\n"+r'		$\begin{aligned}[t]')
    fd.write("\n"+r'c_{fr,Dach}&=\num{'+ str(reibbeiwert_dach)+r'}  \\')
    fd.write("\n"+r'w_{fr,Dach}&=\spann{'+ str(w_cfr_dach)+r'}  \\')
    if waende_beruecksichtigen== True:
        fd.write("\n"+r'c_{fr,Wände}&=\num{'+ str(reibbeiwert_waende)+r'}  \\')
        fd.write("\n"+r'w_{fr,Wände}&=\spann{'+ str(w_cfr_wand)+r'}  \\')
    fd.write("\n"+r'		\end{aligned}		$')






def nur_aussendruckergebnisse_flachdach(self,arg_latex,filename):

    ergebnisse_berechnung =  arg_latex['ergebnisse_berechnung']
    sonstige_werte_berechnet=ergebnisse_berechnung['geometrische_werte_flachdach']
    anteil_f_und_g_x = sonstige_werte_berechnet['anteil_f_und_g_sued']
    anteil_f_und_g_y = sonstige_werte_berechnet['anteil_f_und_g_west']
    reibung_beruecksichtigen=self.flachdach.reibung_beruecksichtigen
    reibung_vernachlaessigt=ergebnisse_berechnung['reibung_vernachlaessigt']
    cpe_dach=ergebnisse_berechnung['cpe_dach']
    aussenwinddruck_dach=ergebnisse_berechnung['aussenwinddruck_dach']
    with io.open(filename,'w', encoding="UTF8") as fd:
        #Margin
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
        fd.write("\n"+r' $\NSOWarrow$ & Ergebnisse für alle Windrichtungen')
        fd.write("\n"+r'\\')
        reibung_margin_tab(self,reibung_beruecksichtigen,fd)
        fd.write("\n"+r'\end{tabular}')
        fd.write("\n"+r'\vspace{3 mm}')
        fd.write("\n"+r'\\')
        reibung_margin_vernachlaessigen(self,reibung_vernachlaessigt,fd)
        if anteil_f_und_g_x < 0.2 and anteil_f_und_g_y >= 0.2:
            fd.write("\n"+r'Bei der Windrichtung aus Westen dürfen die Randzonen F und G gemäß ÖNORM EN 1991-1-4 vernachlässigt werden.')
        elif anteil_f_und_g_x >= 0.2 and anteil_f_und_g_y < 0.2:
            fd.write("\n"+r'Bei der Windrichtung aus Süden dürfen die Randzonen F und G gemäß ÖNORM EN 1991-1-4 vernachlässigt werden.')
        elif anteil_f_und_g_x < 0.2 and anteil_f_und_g_y < 0.2:
            fd.write("\n"+r'Die Randzonen F und G dürfen gemäß ÖNORM EN 1991-1-4 vernachlässigt werden.')
        else:
            print('Randbereiche dürfen nicht vernachlässigt werden')
        fd.write("\n"+r'\switchcolumn')


        fd.write("\n"+r'\begin{table}[H]')
        fd.write("\n"+r'\centering')
        if reibung_beruecksichtigen==True:
            fd.write("\n"+r'	\begin{tabularx}{1\columnwidth}{ B{1} B{1} B{1} }')
        else:
            fd.write("\n"+r'	\begin{tabularx}{1\columnwidth}{ B{1} B{1}  }')
        fd.write("\n"+r'\rowcolor{Gray}	')
        if reibung_beruecksichtigen==True:
            fd.write("\n"+r'	\textbf{Außendruckbeiwerte $c_{pe,10}$ \NSOWarrow} & \textbf{Außenwinddruck $w_{e,10}$ \NSOWarrow} & \textbf{Reibung} \\')
        else:
            fd.write("\n"+r'	\textbf{Außendruckbeiwerte $c_{pe,10}$ \NSOWarrow} & \textbf{Außenwinddruck $w_{e,10}$ \NSOWarrow} \\')
        aussendruckbeiwerte(self,arg_latex,cpe_dach,10,fd)
        fd.write("\n"+r'	&')
        aussenwinddruck(self,arg_latex,aussenwinddruck_dach,10,fd)
        if reibung_beruecksichtigen==True:
            fd.write("\n"+r'	&')
            reibung_latex(self,arg_latex,fd)

        fd.write("\n"+r'\end{tabularx}')
        fd.write("\n"+r'\end{table}')







def aussendruck_und_innendruckergebnisse_flachdach(self,arg_latex,filename):

    some_field_radio2 = self.flachdach.some_field_radio2
    reibung_beruecksichtigen=self.flachdach.reibung_beruecksichtigen
    ergebnisse_berechnung =  arg_latex['ergebnisse_berechnung']
    sonstige_werte_berechnet=ergebnisse_berechnung['geometrische_werte_flachdach']
    anteil_f_und_g_x = sonstige_werte_berechnet['anteil_f_und_g_sued']
    anteil_f_und_g_y = sonstige_werte_berechnet['anteil_f_und_g_west']
    reibung_vernachlaessigt=ergebnisse_berechnung['reibung_vernachlaessigt']
    cpe_dach=ergebnisse_berechnung['cpe_dach']
    aussenwinddruck_dach=ergebnisse_berechnung['aussenwinddruck_dach']
    with io.open(filename,'w', encoding="UTF8") as fd:

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
        if some_field_radio2 == 'Innendruckbeiwerte mittels dominanter Fläche nach Abschnitt 7.2.9':
            fd.write("\n"+r' $\downarrow$ & Wind aus Norden')
            fd.write("\n"+r'\\')
            fd.write("\n"+r' $\leftarrow$ & Wind aus Osten')
            fd.write("\n"+r'\\')
            fd.write("\n"+r' $\uparrow$ & Wind aus Süden')
            fd.write("\n"+r'\\')
            fd.write("\n"+r' $\rightarrow$ & Wind aus Westen')
            fd.write("\n"+r'\\')
        reibung_margin_tab(self,reibung_beruecksichtigen,fd)
        fd.write("\n"+r'\end{tabular}')
        fd.write("\n"+r'\vspace{3 mm}')
        fd.write("\n"+r'\\')
        reibung_margin_vernachlaessigen(self,reibung_vernachlaessigt,fd)
        if anteil_f_und_g_x < 0.2 and anteil_f_und_g_y >= 0.2:
            fd.write("\n"+r'Bei der Windrichtung aus Norden und Süden dürfen die Randzonen F und G gemäß ÖNORM EN 1991-1-4 vernachlässigt werden.')
        elif anteil_f_und_g_x >= 0.2 and anteil_f_und_g_y < 0.2:
            fd.write("\n"+r'Bei der Windrichtung aus Osten und Westen dürfen die Randzonen F und G gemäß ÖNORM EN 1991-1-4 vernachlässigt werden.')
        elif anteil_f_und_g_x < 0.2 and anteil_f_und_g_y < 0.2:
            fd.write("\n"+r'Die Randzonen F und G dürfen gemäß ÖNORM EN 1991-1-4 vernachlässigt werden.')
        else:
            print('Randbereiche dürfen nicht vernachlässigt werden')
        fd.write("\n"+r'\switchcolumn')


        #Ergebnisse
        fd.write("\n"+r'\begin{table}[H]')
        fd.write("\n"+r'	\begin{tabularx}{1\columnwidth}{ B{1} B{1} B{1} }')
        fd.write("\n"+r'\rowcolor{Gray}	')
        if some_field_radio2 == 'Innendruckbeiwerte mittels dominanter Fläche nach Abschnitt 7.2.9':
            fd.write("\n"+r'	\textbf{Außendruckbeiwert $c_{pe,10}$ \NSOWarrow} & \textbf{Innendruckbeiwert} & ')
            if reibung_beruecksichtigen==True:
                fd.write("\n"+r'\textbf{Reibung} \\')
            else:
                fd.write("\n"+r'\textbf{} \\')

        else:
            fd.write("\n"+r'	\textbf{Außendruckbeiwerte $c_{pe,10}$ \NSOWarrow} & \textbf{Innendruckbeiwerte \NSOWarrow} & ')
            if reibung_beruecksichtigen==True:
                fd.write("\n"+r'\textbf{Reibung} \\')
            else:
                fd.write("\n"+r'\textbf{} \\')
        aussendruckbeiwerte(self,arg_latex,cpe_dach,10,fd)
        fd.write("\n"+r'	&')
        innendruckbeiwerte(self,arg_latex,fd)
        fd.write("\n"+r'	& ')
        if reibung_beruecksichtigen==True:
            reibung_latex(self,arg_latex,fd)
        fd.write("\n"+r'\end{tabularx}')
        fd.write("\n"+r'\end{table}')
        fd.write("\n"+r'\begin{table}[H]')
        fd.write("\n"+r'	\begin{tabularx}{1\columnwidth}{ B{1} B{1} B{1} }')
        fd.write("\n"+r'\rowcolor{Gray}	')
        if some_field_radio2 == 'Innendruckbeiwerte mittels dominanter Fläche nach Abschnitt 7.2.9':
            fd.write("\n"+r'	\textbf{Außenwinddruck $w_{e,10}$ \NSOWarrow} & \textbf{Innenwinddruck \NSOWarrow} & \textbf{überlagerter Winddruck $\downarrow$} \\')
        else:
            fd.write("\n"+r' 	\textbf{Außenwinddruck $w_{e,10}$ \NSOWarrow} & \textbf{Innenwinddruck \NSOWarrow} & \textbf{überlagerter Winddruck \NSOWarrow} \\')
        aussenwinddruck(self,arg_latex,aussenwinddruck_dach,10,fd)
        fd.write("\n"+r'	&')

        innenwinddruck(self,arg_latex,fd)
        fd.write("\n"+r'	&')
        if some_field_radio2 == 'Innendruckbeiwerte mittels dominanter Fläche nach Abschnitt 7.2.9':
            ueberlagerter_winddruck_norden(self,arg_latex,fd)
            fd.write("\n"+r'\end{tabularx}')
            fd.write("\n"+r'\end{table}')
            fd.write("\n"+r'\begin{table}[H]')
            fd.write("\n"+r'	\begin{tabularx}{1\columnwidth}{ B{1} B{1} B{1} }')
            fd.write("\n"+r'\rowcolor{Gray}	')
            fd.write("\n"+r'	\textbf{Überlagerter Winddruck $\leftarrow$} & \textbf{Überlagerter Winddruck $\uparrow $} & \textbf{Überlagerter Winddruck $\rightarrow$} \\')
            ueberlagerter_winddruck_ost_sued_west(self,arg_latex,fd)
        else:
            ueberlagerter_winddruck(self,arg_latex,fd)


        fd.write("\n"+r'\end{tabularx}')
        fd.write("\n"+r'\end{table}')


def nur_aussendruckergebnisse_flachdach_ohne_cp(self,arg_latex,filename):

    ergebnisse_berechnung =  arg_latex['ergebnisse_berechnung']
    sonstige_werte_berechnet=ergebnisse_berechnung['geometrische_werte_flachdach']
    anteil_f_und_g_x = sonstige_werte_berechnet['anteil_f_und_g_sued']
    anteil_f_und_g_y = sonstige_werte_berechnet['anteil_f_und_g_west']
    reibung_beruecksichtigen=self.flachdach.reibung_beruecksichtigen
    reibung_vernachlaessigt=ergebnisse_berechnung['reibung_vernachlaessigt']
    aussenwinddruck_dach=ergebnisse_berechnung['aussenwinddruck_dach']
    with io.open(filename,'w', encoding="UTF8") as fd:
        #Margin
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
        fd.write("\n"+r' $\NSOWarrow$ & Ergebnisse für alle Windrichtungen')
        fd.write("\n"+r'\\')
        reibung_margin_tab(self,reibung_beruecksichtigen,fd)
        fd.write("\n"+r'\end{tabular}')
        fd.write("\n"+r'\vspace{3 mm}')
        fd.write("\n"+r'\\')
        reibung_margin_vernachlaessigen(self,reibung_vernachlaessigt,fd)
        if anteil_f_und_g_x < 0.2 and anteil_f_und_g_y >= 0.2:
            fd.write("\n"+r'Bei der Windrichtung aus Westen dürfen die Randzonen F und G gemäß ÖNORM EN 1991-1-4 vernachlässigt werden.')
        elif anteil_f_und_g_x >= 0.2 and anteil_f_und_g_y < 0.2:
            fd.write("\n"+r'Bei der Windrichtung aus Süden dürfen die Randzonen F und G gemäß ÖNORM EN 1991-1-4 vernachlässigt werden.')
        elif anteil_f_und_g_x < 0.2 and anteil_f_und_g_y < 0.2:
            fd.write("\n"+r'Die Randzonen F und G dürfen gemäß ÖNORM EN 1991-1-4 vernachlässigt werden.')
        else:
            print('Randbereiche dürfen nicht vernachlässigt werden')
        fd.write("\n"+r'\switchcolumn')


        fd.write("\n"+r'\begin{table}[H]')
        fd.write("\n"+r'\centering')
        if reibung_beruecksichtigen==True:
            fd.write("\n"+r'	\begin{tabularx}{1\columnwidth}{ B{1} B{1}  }')
        else:
            fd.write("\n"+r'	\begin{tabularx}{1\columnwidth}{ B{1}  }')
        fd.write("\n"+r'\rowcolor{Gray}	')
        if reibung_beruecksichtigen==True:
            fd.write("\n"+r'	  \textbf{Außenwinddruck $w_{e,10}$ \NSOWarrow} & \textbf{Reibung} \\')
        else:
            fd.write("\n"+r'	 \textbf{Außenwinddruck $w_{e,10}$ \NSOWarrow} \\')
        aussenwinddruck(self,arg_latex,aussenwinddruck_dach,10,fd)
        if reibung_beruecksichtigen==True:
            fd.write("\n"+r'	&')
            reibung_latex(self,arg_latex,fd)
        fd.write("\n"+r'\end{tabularx}')
        fd.write("\n"+r'\end{table}')


def aussendruck_und_innendruckergebnisse_flachdach_ohne_cp(self,arg_latex,filename):

    some_field_radio2 = self.flachdach.some_field_radio2
    reibung_beruecksichtigen=self.flachdach.reibung_beruecksichtigen
    ergebnisse_berechnung =  arg_latex['ergebnisse_berechnung']
    sonstige_werte_berechnet=ergebnisse_berechnung['geometrische_werte_flachdach']
    anteil_f_und_g_x = sonstige_werte_berechnet['anteil_f_und_g_sued']
    anteil_f_und_g_y = sonstige_werte_berechnet['anteil_f_und_g_west']
    reibung_vernachlaessigt=ergebnisse_berechnung['reibung_vernachlaessigt']
    aussenwinddruck_dach=ergebnisse_berechnung['aussenwinddruck_dach']
    with io.open(filename,'w', encoding="UTF8") as fd:

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
        if some_field_radio2 == 'Innendruckbeiwerte mittels dominanter Fläche nach Abschnitt 7.2.9':
            fd.write("\n"+r' $\downarrow$ & Wind aus Norden')
            fd.write("\n"+r'\\')
            fd.write("\n"+r' $\leftarrow$ & Wind aus Osten')
            fd.write("\n"+r'\\')
            fd.write("\n"+r' $\uparrow$ & Wind aus Süden')
            fd.write("\n"+r'\\')
            fd.write("\n"+r' $\rightarrow$ & Wind aus Westen')
            fd.write("\n"+r'\\')
        reibung_margin_tab(self,reibung_beruecksichtigen,fd)
        fd.write("\n"+r'\end{tabular}')
        fd.write("\n"+r'\vspace{3 mm}')
        fd.write("\n"+r'\\')
        reibung_margin_vernachlaessigen(self,reibung_vernachlaessigt,fd)
        if anteil_f_und_g_x < 0.2 and anteil_f_und_g_y >= 0.2:
            fd.write("\n"+r'Bei der Windrichtung aus Norden und Süden dürfen die Randzonen F und G gemäß ÖNORM B 1991-1-4 vernachlässigt werden.')
        elif anteil_f_und_g_x >= 0.2 and anteil_f_und_g_y < 0.2:
            fd.write("\n"+r'Bei der Windrichtung aus Osten und Westen dürfen die Randzonen F und G gemäß ÖNORM B 1991-1-4 vernachlässigt werden.')
        elif anteil_f_und_g_x < 0.2 and anteil_f_und_g_y < 0.2:
            fd.write("\n"+r'Die Randzonen F und G dürfen gemäß ÖNORM B 1991-1-4 vernachlässigt werden.')
        else:
            print('Randbereiche dürfen nicht vernachlässigt werden')
        fd.write("\n"+r'\switchcolumn')


        #Ergebnisse
        if reibung_beruecksichtigen==True:
            fd.write("\n"+r'\begin{table}[H]')
            fd.write("\n"+r'	\begin{tabularx}{1\columnwidth}{ B{1}  }')
            fd.write("\n"+r'\rowcolor{Gray}	')
            fd.write("\n"+r'\textbf{Reibung} \\')
            reibung_latex(self,arg_latex,fd)
            fd.write("\n"+r'\end{tabularx}')
            fd.write("\n"+r'\end{table}')
        fd.write("\n"+r'\begin{table}[H]')
        fd.write("\n"+r'	\begin{tabularx}{1\columnwidth}{ B{1} B{1} B{1} }')
        fd.write("\n"+r'\rowcolor{Gray}	')
        if some_field_radio2 == 'Innendruckbeiwerte mittels dominanter Fläche nach Abschnitt 7.2.9':
            fd.write("\n"+r'	\textbf{Außenwinddruck $w_{e,10}$ \NSOWarrow} & \textbf{Innenwinddruck \NSOWarrow} & \textbf{überlagerter Winddruck $\downarrow$} \\')
        else:
            fd.write("\n"+r' 	\textbf{Außenwinddruck $w_{e,10}$ \NSOWarrow} & \textbf{Innenwinddruck \NSOWarrow} & \textbf{überlagerter Winddruck \NSOWarrow} \\')
        aussenwinddruck(self,arg_latex,aussenwinddruck_dach,10,fd)
        fd.write("\n"+r'	&')

        innenwinddruck(self,arg_latex,fd)
        fd.write("\n"+r'	&')
        if some_field_radio2 == 'Innendruckbeiwerte mittels dominanter Fläche nach Abschnitt 7.2.9':
            ueberlagerter_winddruck_norden(self,arg_latex,fd)
            fd.write("\n"+r'\end{tabularx}')
            fd.write("\n"+r'\end{table}')
            fd.write("\n"+r'\begin{table}[H]')
            fd.write("\n"+r'	\begin{tabularx}{1\columnwidth}{ B{1} B{1} B{1} }')
            fd.write("\n"+r'\rowcolor{Gray}	')
            fd.write("\n"+r'	\textbf{Überlagerter Winddruck $\leftarrow$} & \textbf{Überlagerter Winddruck $\uparrow $} & \textbf{überlagerter Winddruck $\rightarrow$} \\')
            ueberlagerter_winddruck_ost_sued_west(self,arg_latex,fd)
        else:
            ueberlagerter_winddruck(self,arg_latex,fd)
        fd.write("\n"+r'\end{tabularx}')
        fd.write("\n"+r'\end{table}')
