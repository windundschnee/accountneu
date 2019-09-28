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
            fd.write("\n"+r'\multicolumn{3}{c}{  \rule{0mm}{5mm} \Large{\textbf{'+ str(bauteilname) +r' -- Wände und Flachdach }}} \\')
        else:
            fd.write("\n"+r'\begin{tabularx}{1\columnwidth}{B{1} B{1}  }')
            fd.write("\n"+r'\rowcolor{Gray}	')
            fd.write("\n"+r'\multicolumn{2}{c}{ \rule{0mm}{5mm} \Large{\textbf{'+ str(bauteilname) +r' -- Wände und Flachdach}}} \\')
        fd.write("\n"+r'		$\begin{aligned}[t]')
        fd.write("\n"+r'		\ell_S & =\lang{'+ str(breite_x)+r'}')
        fd.write("\n"+r'		\\')
        fd.write("\n"+r'		\ell_W & =\lang{'+ str(breite_y)+r'}')
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


def aussendruckbeiwerte(self,arg_latex,fd):

    ergebnisse_berechnung=arg_latex['ergebnisse_berechnung']
    #print(ergebnisse_berechnung)
    cpe_dach=ergebnisse_berechnung['cpe_dach']




    vereinfachtes_verfahren = self.flachdach.some_field


    art_traufenbereich = self.flachdach.art_traufenbereich
    cp_f=cpe_dach[0]
    cp_g=cpe_dach[1]

    fd.write("\n"+r'	$	\begin{aligned}[t]')
    fd.write("\n"+r'	c_{pe,F}&= \SI{'+ str(cp_f)+r'}{} \\ ')
    fd.write("\n"+r'	c_{pe,G}&=\SI{'+ str(cp_g)+r'}{}    \\')
    if vereinfachtes_verfahren == 'Vereinfachtes Verfahren gemäß ÖNORM B 1991-1-4, Abschnitt 9.2.3.1':


        cp_h_druck=cpe_dach[2]
        cp_i_druck=cpe_dach[4]
        cp_h_sog=cpe_dach[3]
        cp_i_sog=cpe_dach[5]
        fd.write("\n"+r'c_{pe,H}&=\SI{'+ str(cp_h_druck)+r'}{}   \\')
        fd.write("\n"+r'	c_{pe,H}&=\SI{'+ str(cp_h_sog)+r'}{} \\ ')
        fd.write("\n"+r'	c_{pe,I}&=\SI{'+ str(cp_i_druck)+r'}{} \\ ')
        fd.write("\n"+r'	c_{pe,I}&=\SI{'+ str(cp_i_sog)+r'}{}  ')
    else:

        cp_h=cpe_dach[2]
        cp_i=abs(cpe_dach[3])
        fd.write("\n"+r'c_{pe,H}&=\SI{'+ str(cp_h)+r'}{}   \\')
        fd.write("\n"+r'	c_{pe,I}&=\SI{\pm'+ str(cp_i)+r'}{}  ')
        if art_traufenbereich=="mansardenartig abgeschrägter Traufbereich":


            cp_auf_mans_sog=cpe_dach[5]
            cp_auf_mans_druck=cpe_dach[6]

            fd.write("\n"+r'\\ c_{pe,Mansarde}&=\SI{'+ str(cp_auf_mans_druck)+r'}{}   \\')
            fd.write("\n"+r' c_{pe,Mansarde}&=\SI{'+ str(cp_auf_mans_sog)+r'}{}   ')
        else:
            print('keine Mansarden')
    fd.write("\n"+r'		\end{aligned}		$')

def aussenwinddruck(self,arg_latex,fd):


    ergebnisse_berechnung=arg_latex['ergebnisse_berechnung']

    aussenwinddruck_dach=ergebnisse_berechnung['aussenwinddruck_dach']

    wa_f=aussenwinddruck_dach[0]
    wa_g=aussenwinddruck_dach[1]

    vereinfachtes_verfahren = self.flachdach.some_field


    art_traufenbereich = self.flachdach.art_traufenbereich
    fd.write("\n"+r'		$\begin{aligned}[t]')
    fd.write("\n"+r'		w_{e,F}&= \SI{'+ str(wa_f)+r'}{\kilo\newton\per\square\meter} \\')
    fd.write("\n"+r'	w_{e,G}&=\SI{'+ str(wa_g)+r'}{\kilo\newton\per\square\meter}  \\')
    if vereinfachtes_verfahren == 'Vereinfachtes Verfahren gemäß ÖNORM B 1991-1-4, Abschnitt 9.2.3.1':
        wa_h_druck=aussenwinddruck_dach[2]
        wa_i_druck=aussenwinddruck_dach[4]
        wa_h_sog=aussenwinddruck_dach[3]
        wa_i_sog=aussenwinddruck_dach[5]
        fd.write("\n"+r'		w_{e,H}&=\SI{'+ str(wa_h_druck)+r'}{\kilo\newton\per\square\meter}  \\')
        fd.write("\n"+r'		w_{e,H}&=\SI{'+ str(wa_h_sog)+r'}{\kilo\newton\per\square\meter} \\')
        fd.write("\n"+r'		w_{e,I}&=\SI{'+ str(wa_i_druck)+r'}{\kilo\newton\per\square\meter} \\')
        fd.write("\n"+r'		w_{e,I}&=\SI{'+ str(wa_i_sog)+r'}{\kilo\newton\per\square\meter} \\')
    else:

        wa_h=aussenwinddruck_dach[2]
        wa_i=abs(aussenwinddruck_dach[3])
        fd.write("\n"+r'		w_{e,H}&=\SI{'+ str(wa_h)+r'}{\kilo\newton\per\square\meter}  \\')
        fd.write("\n"+r'		w_{e,I}&=\SI{\pm'+ str(wa_i)+r'}{\kilo\newton\per\square\meter} ')
        if art_traufenbereich=="mansardenartig abgeschrägter Traufbereich":
            wa_auf_mans_sog=aussenwinddruck_dach[5]
            wa_auf_mans_druck=aussenwinddruck_dach[6]
            fd.write("\n"+r'	\\	w_{e,Mansarde}&=\SI{'+ str(wa_auf_mans_druck)+r'}{\kilo\newton\per\square\meter}  \\')
            fd.write("\n"+r'		w_{e,Mansarde}&=\SI{'+ str(wa_auf_mans_sog)+r'}{\kilo\newton\per\square\meter} ')
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
            fd.write("\n"+r'	\textbf{Außendruckbeiwerte \NSOWarrow} & \textbf{Außenwinddruck \NSOWarrow} & \textbf{Reibung} \\')
        else:
            fd.write("\n"+r'	\textbf{Außendruckbeiwerte \NSOWarrow} & \textbf{Außenwinddruck \NSOWarrow} \\')
        aussendruckbeiwerte(self,arg_latex,fd)
        fd.write("\n"+r'	&')
        aussenwinddruck(self,arg_latex,fd)
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
            fd.write("\n"+r'	\textbf{Außendruckbeiwert \NSOWarrow} & \textbf{Innendruckbeiwert} & ')
            if reibung_beruecksichtigen==True:
                fd.write("\n"+r'\textbf{Reibung} \\')
            else:
                fd.write("\n"+r'\textbf{} \\')

        else:
            fd.write("\n"+r'	\textbf{Außendruckbeiwerte \NSOWarrow} & \textbf{Innendruckbeiwerte \NSOWarrow} & ')
            if reibung_beruecksichtigen==True:
                fd.write("\n"+r'\textbf{Reibung} \\')
            else:
                fd.write("\n"+r'\textbf{} \\')
        aussendruckbeiwerte(self,arg_latex,fd)
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
            fd.write("\n"+r'	\textbf{Außenwinddruck \NSOWarrow} & \textbf{Innenwinddruck \NSOWarrow} & \textbf{überlagerter Winddruck $\downarrow$} \\')
        else:
            fd.write("\n"+r' 	\textbf{Außenwinddruck \NSOWarrow} & \textbf{Innenwinddruck \NSOWarrow} & \textbf{überlagerter Winddruck \NSOWarrow} \\')
        aussenwinddruck(self,arg_latex,fd)
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
            fd.write("\n"+r'	\textbf{überlagerter Winddruck $\leftarrow$} & \textbf{überlagerter Winddruck $\uparrow $} & \textbf{überlagerter Winddruck $\rightarrow$} \\')
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
            fd.write("\n"+r'	  \textbf{Außenwinddruck \NSOWarrow} & \textbf{Reibung} \\')
        else:
            fd.write("\n"+r'	 \textbf{Außenwinddruck \NSOWarrow} \\')
        aussenwinddruck(self,arg_latex,fd)
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
            fd.write("\n"+r'	\textbf{Außenwinddruck \NSOWarrow} & \textbf{Innenwinddruck \NSOWarrow} & \textbf{überlagerter Winddruck $\downarrow$} \\')
        else:
            fd.write("\n"+r' 	\textbf{Außenwinddruck \NSOWarrow} & \textbf{Innenwinddruck \NSOWarrow} & \textbf{überlagerter Winddruck \NSOWarrow} \\')
        aussenwinddruck(self,arg_latex,fd)
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
            fd.write("\n"+r'	\textbf{überlagerter Winddruck $\leftarrow$} & \textbf{überlagerter Winddruck $\uparrow $} & \textbf{überlagerter Winddruck $\rightarrow$} \\')
            ueberlagerter_winddruck_ost_sued_west(self,arg_latex,fd)
        else:
            ueberlagerter_winddruck(self,arg_latex,fd)
        fd.write("\n"+r'\end{tabularx}')
        fd.write("\n"+r'\end{table}')



def bilder_flachdach(self,arg_latex,filename):
    ergebnisse_berechnung =  arg_latex['ergebnisse_berechnung']

    art_traufenbereich = self.flachdach.art_traufenbereich
    hoehe = self.flachdach.hoehe
    hoehe_attika = self.flachdach.hoehe_attika
    radius = self.flachdach.radius
    alpha = self.flachdach.alpha
    breite_x = self.flachdach.breite_x
    breite_y = self.flachdach.breite_y
    vereinfachtes_verfahren = self.flachdach.some_field

    sonstige_werte_berechnet=ergebnisse_berechnung['geometrische_werte_flachdach']
    lf_x=sonstige_werte_berechnet['lf_sued']
    lg_x=sonstige_werte_berechnet['lg_sued']
    bf_x=sonstige_werte_berechnet['bf_sued']
    bh_x=sonstige_werte_berechnet['bh_sued']
    bi_x=sonstige_werte_berechnet['bi_sued']
    lf_y=sonstige_werte_berechnet['lf_west']
    lg_y=sonstige_werte_berechnet['lg_west']
    bf_y=sonstige_werte_berechnet['bf_west']
    bh_y=sonstige_werte_berechnet['bh_west']
    bi_y=sonstige_werte_berechnet['bi_west']
    # für die tikz zeichnung Größe kann so vareiert werden
    ls=3
    lw=4
    e=5

    ew=4
    h_tikz=1.5

    with io.open(filename,'w', encoding="UTF8") as fd:
        ###############
        #Ansicht
        fd.write("\n"+r'\tikzset{')
        fd.write("\n"+r'flachdachAnsicht/.pic = {')
        fd.write("\n"+r'\node[coordinate] at (0,0) (na) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(lw)+r',0) (nb) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(lw)+r','+ str(h_tikz)+r') (nc) {};')
        fd.write("\n"+r'\node[coordinate] at (0,'+ str(h_tikz)+r') (nd) {};')

        #Boden
        fd.write("\n"+r'\draw[line width=0.35mm] (na) -- +(-0.5,0);')
        fd.write("\n"+r'\draw[line width=0.35mm] (nb) -- +(0.5,0);')
        fd.write("\n"+r'\draw[line width=0.35mm] (na) -- (nb);')
        fd.write("\n"+r'\fill[pattern,pattern= north east lines] ($(na)-(0.5,0)$) rectangle ($(nb)+(0.5,-0.3)$);')
        if art_traufenbereich=="scharfkantiger Traufbereich" or vereinfachtes_verfahren == 'Vereinfachtes Verfahren gemäß ÖNORM B 1991-1-4, Abschnitt 9.2.3.1':
            fd.write("\n"+r'\draw[line width=0.25mm] (na) -- (nb) -- (nc) -- (nd) -- cycle;')
        elif art_traufenbereich=="mit Attika" and vereinfachtes_verfahren=='Verfahren gemäß ÖNORM EN 1991-1-4, Abschnitt 7.2.3':
            fd.write("\n"+r'\draw[line width=0.25mm] (na) -- (nb) -- (nc) -- (nd) -- cycle;')
            fd.write("\n"+r'\draw[line width=0.25mm] (nd) -- +(0,0.5);')
            fd.write("\n"+r'\draw[line width=0.25mm] (nc) -- +(0,0.5);')
            fd.write("\n"+r'\node[coordinate] at ($(nd)+(0,0.5)$) (nat) {};')
            fd.write("\n"+r'\DimlineV[nd][nat][-0.7][\num{'+ str(hoehe_attika)+r'}]')
        elif art_traufenbereich=="abgerundeter Traufbereich" and vereinfachtes_verfahren=='Verfahren gemäß ÖNORM EN 1991-1-4, Abschnitt 7.2.3':
            fd.write("\n"+r'\node[coordinate] at ($(nd)-(0,0.5)$) (nda) {};')
            fd.write("\n"+r'\node[coordinate] at ($(nd)+(0.5,0.0)$) (ndc) {};')
            fd.write("\n"+r'\node[coordinate] at ($(nc)-(0,0.5)$) (ncb) {};')
            fd.write("\n"+r'\node[coordinate] at ($(nc)-(0.5,0.0)$) (ncd) {};')
            fd.write("\n"+r'\draw[line width=0.25mm] (na) -- (nb) -- (ncb);')
            fd.write("\n"+r'\draw[line width=0.25mm]  (ncd) -- (ndc);')
            fd.write("\n"+r'\draw[line width=0.25mm]  (nda) -- (na);')
            #Rundung links
            fd.write("\n"+r'\draw[line width=0.25mm] (nda)  arc[radius = 5mm, start angle= 180, end angle= 90];')
            fd.write("\n"+r'\draw[->] ($(nda)+(0.5,0)$) node[above,rotate=-45]{\tiny{\num{'+ str(radius)+r'}}} -- +(135:0.5) ;')
            #Rundung rechts
            fd.write("\n"+r'\draw[line width=0.25mm] (ncb)  arc[radius = 5mm, start angle= 0, end angle= 90];')
            fd.write("\n"+r'\draw[->] ($(ncb)-(0.5,0)$) node[above,rotate=45]{\tiny{\num{'+ str(radius)+r'}}} -- +(45:0.5) ;')
        elif art_traufenbereich=="mansardenartig abgeschrägter Traufbereich" and vereinfachtes_verfahren=='Verfahren gemäß ÖNORM EN 1991-1-4, Abschnitt 7.2.3':
            fd.write("\n"+r'\node[coordinate] at ($(nd)-(0,0.3)$) (nda) {};')
            fd.write("\n"+r'\node[coordinate] at ($(nd)+(0.8,0.0)$) (ndc) {};')
            fd.write("\n"+r'\node[coordinate] at ($(nc)-(0,0.3)$) (ncb) {};')
            fd.write("\n"+r'\node[coordinate] at ($(nc)-(0.8,0.0)$) (ncd) {};')
            fd.write("\n"+r'\draw[line width=0.25mm] (na) -- (nb) -- (ncb);')
            fd.write("\n"+r'\draw[line width=0.25mm]  (ncd) -- (ndc);')
            fd.write("\n"+r'\draw[line width=0.25mm]  (nda) -- (na);')
            #Schräge
            fd.write("\n"+r'\draw[line width=0.25mm]  (nda) -- (ndc);')
            fd.write("\n"+r'\draw[line width=0.25mm]  (ncd) -- (ncb);')
            fd.write("\n"+r'\draw[line width=0.13mm]  (nd) -- ($(ndc)-(0.2,0)$);')
            #Winkelbemassung rechts
            fd.write("\n"+r'\draw[line width=0.13mm]  (nc) -- ($(ncd)+(0.2,0)$);')
            fd.write("\n"+r'\tkzMarkAngle[size=.5](ncb,ncd,nc)')
            fd.write("\n"+r'\tkzLabelAngle[pos=0.9](ncb,ncd,nc){\tiny{\num{'+ str(alpha)+r'}}}')
            #Winkelbemassung links
            fd.write("\n"+r'\draw[line width=0.13mm]  (nd) -- ($(ndc)-(0.2,0)$);')
            fd.write("\n"+r'\tkzMarkAngle[size=.5](nd,ndc,nda)')
            fd.write("\n"+r'\tkzLabelAngle[pos=-0.9](nd,ndc,nda){\tiny{\num{'+ str(alpha)+r'}}}')



        #Bemasung
        #fd.write("\n"+r'\DimlineH[($(na)-(0.0,1.0)$)][($(nb)-(0.0,1.0)$)][\num{'+ str(breite_y)+r'}]')
        fd.write("\n"+r'\DimlineV[na][nd][-0.7][\num{'+ str(hoehe)+r'}]')

        fd.write("\n"+r'}}')


        ####################
        #Grundriss Wind aus Süden
        fd.write("\n"+r'\tikzset{')
        fd.write("\n"+r'flachdachSued/.pic = {')
        fd.write("\n"+r'\node[coordinate] at (0,0) (na) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(lw)+r',0) (nb) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(lw)+r','+ str(ls)+r') (nc) {};')
        fd.write("\n"+r'\node[coordinate] at (0,'+ str(ls)+r') (nd) {};')
        fd.write("\n"+r'\node[coordinate] at (0,'+ str(e / 10)+r') (ne) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(e / 4)+r','+ str(e / 10)+r') (nf) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(lw- e / 4)+r','+str( e / 10)+r') (ng) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(lw)+r','+str( e / 10)+r') (nh) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(e / 4)+r',0) (ni) {};')
        fd.write("\n"+r'\node[coordinate] at ('+str(lw- e / 4)+r',0) (nj) {};')
        fd.write("\n"+r'\node[coordinate] at (0,'+str(e / 2)+r') (nk) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(lw)+r','+ str(e / 2)+r') (nl) {};')
        #Umrandungslinien
        fd.write("\n"+r'\draw[line width=0.25mm] (na) -- (nb) -- (nc) -- (nd) -- cycle;')
        #Horizontale F G
        fd.write("\n"+r'\draw (ne) -- (nh);')
        #Horizontale H zwischen I
        if bi_x >0:
            fd.write("\n"+r'\draw (nk) -- (nl);')
        #Vertikale zwischen F und G
        fd.write("\n"+r'\draw (nf) -- (ni);')
        #Vertikale zwischen G und F
        fd.write("\n"+r'\draw (ng) -- (nj);')
        #Vertikale Bemasungslinien
        fd.write("\n"+r'\DimlineV[nb][nh][0.5][\num{'+ str(bf_x)+r'}]')
        if bi_x <=0:
            fd.write("\n"+r'\DimlineV[nh][nc][0.5][\num{'+ str(bh_x)+r'}]')
        else:
            fd.write("\n"+r'\DimlineV[nh][nl][0.5][\num{'+ str(bh_x)+r'}]')
            fd.write("\n"+r'\DimlineV[nl][nc][0.5][\num{'+ str(bi_x)+r'}] ')
        fd.write("\n"+r'\DimlineV[nb][nc][1][\num{'+ str(breite_x)+r'}] ')
        #Horizontale Bemasungslinien
        fd.write("\n"+r'\DimlineH[na][ni]['+ str(ls + 0.5) +r'][\num{'+ str(lf_x)+r'}] ')
        fd.write("\n"+r'\DimlineH[ni][nj]['+ str(ls + 0.5) +r'][\num{'+ str(lg_x)+r'}] ')
        fd.write("\n"+r'\DimlineH[nj][nb]['+ str(ls + 0.5) +r'][\num{'+ str(lf_x)+r'}]')
        fd.write("\n"+r'\DimlineH[na][nb]['+ str(ls + 1) +r'][\num{'+ str(breite_y)+r'}] ')
        #Flächenbezeichnung
        fd.write("\n"+r'\node[between=na and nf]  {\Large{F}};')
        fd.write("\n"+r'\node[between=ni and ng]  {\Large{G}};')
        fd.write("\n"+r'\node[between=nj and nh]  {\Large{F}};')
        fd.write("\n"+r'\node[between=ne and nl]  {\Large{H}};')
        if bi_x >0:
            fd.write("\n"+r'\node[between=nk and nc]  {\Large{I}};')
        #Pfeile für die Windrichtung
        fd.write("\n"+r'\pic at ('+ str(lw/2)+r',-0.5) {windrichtung};')
        fd.write("\n"+r'}}')

        #############################
        #Grundriss Wind aus Westen
        fd.write("\n"+r'\tikzset{')
        fd.write("\n"+r'flachdachWest/.pic = {')
        fd.write("\n"+r'\node[coordinate] at (0,0) (na) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(lw)+r',0) (nb) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(lw)+r','+ str(ls)+r') (nc) {};')
        fd.write("\n"+r'\node[coordinate] at (0,'+ str(ls)+r') (nd) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(ew / 10)+r','+ str(ls)+r') (ne) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(ew / 10)+r','+ str(ls-ew / 4)+r') (nf) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(ew / 10)+r','+str( ew / 4)+r') (ng) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(ew/10)+r',0) (nh) {};')
        fd.write("\n"+r'\node[coordinate] at (0,'+ str(ls-ew / 4)+r') (ni) {};')
        fd.write("\n"+r'\node[coordinate] at (0,'+ str(ew / 4)+r') (nj) {};')
        fd.write("\n"+r'\node[coordinate] at ('+str(ew / 2)+r','+str(ls)+r') (nk) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(ew/2)+r',0) (nl) {};')
        #Umrandungslinien
        fd.write("\n"+r'\draw[line width=0.25mm] (na) -- (nb) -- (nc) -- (nd) -- cycle;')
        #Horizontale F G
        fd.write("\n"+r'\draw (ne) -- (nh);')
        #Horizontale H zwischen I
        if bi_y >0:
            fd.write("\n"+r'\draw (nk) -- (nl);')
        #Vertikale zwischen F und G
        fd.write("\n"+r'\draw (nf) -- (ni);')
        #Vertikale zwischen G und F
        fd.write("\n"+r'\draw (ng) -- (nj);')
        #Vertikale Bemasungslinien
        fd.write("\n"+r'\DimlineV[na][nj]['+ str(lw + 0.5) +r'][\num{'+ str(lf_y)+r'}]')
        fd.write("\n"+r'\DimlineV[nj][ni]['+ str(lw + 0.5) +r'][\num{'+ str(lg_y)+r'}]')
        fd.write("\n"+r'\DimlineV[ni][nd]['+ str(lw + 0.5) +r'][\num{'+ str(lf_y)+r'}] ')
        fd.write("\n"+r'\DimlineV[nb][nc][1][\num{'+ str(breite_x)+r'}] ')
        #Horizontale Bemasungslinien
        fd.write("\n"+r'\DimlineH[na][nh]['+ str(ls + 0.5) +r'][\num{'+ str(bf_y)+r'}] ')
        if bi_y <=0:
            fd.write("\n"+r'\DimlineH[nh][nb]['+ str(ls + 0.5) +r'][\num{'+ str(bh_y)+r'}] ')
        else:
            fd.write("\n"+r'\DimlineH[nh][nl]['+ str(ls + 0.5) +r'][\num{'+ str(bh_y)+r'}] ')
            fd.write("\n"+r'\DimlineH[nl][nb]['+ str(ls + 0.5) +r'][\num{'+ str(bi_y)+r'}] ')
        fd.write("\n"+r'\DimlineH[na][nb]['+ str(ls + 1) +r'][\num{'+ str(breite_y)+r'}] ')
        #Flächenbezeichnung
        fd.write("\n"+r'\node[between=nd and nf]  {\Large{F}};')
        fd.write("\n"+r'\node[between=ni and ng]  {\Large{G}};')
        fd.write("\n"+r'\node[between=nj and nh]  {\Large{F}};')
        if bi_y >0:
            fd.write("\n"+r'\node[between=ne and nl]  {\Large{H}};')
            fd.write("\n"+r'\node[between=nk and nb]  {\Large{I}};')
        else:
            fd.write("\n"+r'\node[between=ne and nb]  {\Large{H}};')

        #Pfeile für die Windrichtung
        fd.write("\n"+r'\pic[rotate=-90,,transform shape] at (-0.5,'+ str(ls/2)+r') {windrichtung};')
        fd.write("\n"+r'}}')
        ##Margin
        fd.write("\n"+r'\switchcolumn*')
        fd.write("\n"+r'alle Werte in $[m]$')
        #fd.write("\n"+r'\begin{tikzpicture}')
        #fd.write("\n"+r' \pic[scale=1,fill=black,text=black] at (0,0) {compass};')
        #fd.write("\n"+r'\end{tikzpicture}')
        fd.write("\n"+r'\switchcolumn')
        ##############
        ####Bild zusammenfügen
        fd.write("\n"+r'\begin{figure}[H]')
        fd.write("\n"+r'\centering')
        fd.write("\n"+r'\begin{tikzpicture}')
        #Ansicht einfügen
        fd.write("\n"+r'\node[anchor=west] at (-1,8.3)  {\Large{Ansicht Traufenbereich}};')
        fd.write("\n"+r'\pic at (0,5.7) {flachdachAnsicht};')
        #Grundriss Flachdach wind von Süden
        fd.write("\n"+r'\node[anchor=west] at (-1,4.8)  {\Large{Dachdraufsicht}};')
        fd.write("\n"+r'\pic at (0,0) {flachdachSued};')
        #Grundriss Flachdach wind von Westen
        fd.write("\n"+r'\pic at (7.5,0) {flachdachWest};')
        #Windrose einfügen
        fd.write("\n"+r' \pic[scale=1,fill=black,text=black] at (9.5,6.5) {compass};')
        fd.write("\n"+r'\end{tikzpicture}')
        fd.write("\n"+r'\end{figure}')
