import os
import io
from itertools import islice
import numpy as np
from gesamt_pdf_app.reibung import reibung_margin_vernachlaessigen
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
    einflussflaeche=latex_waende_list['einflussflaeche']
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
        fd.write("\n"+r'	\textbf{Außenwinddruck $w_{e,10}$ $\updownarrow$} &  \textbf{Außenwinddruck $w_{e,10}$ $\leftrightarrow$}\\')
        aussendruck(self,arg_latex,fd)
        fd.write("\n"+r'\end{tabularx}')
        fd.write("\n"+r'\end{table}')
        fd.write("\n"+r'\begin{table}[H]')
        fd.write("\n"+r'	\begin{tabularx}{1\columnwidth}{ B{1} B{1} }')
        fd.write("\n"+r'\rowcolor{Gray}	')
        fd.write("\n"+r'	\textbf{Außenwinddruck $w_{e,'+ str(einflussflaeche)+r'}$ $\updownarrow$} &  \textbf{Außenwinddruck $w_{e,'+  str(einflussflaeche)+r'}$ $\leftrightarrow$}\\')
        aussendruck_A(self,arg_latex,fd,einflussflaeche)

        fd.write("\n"+r'\end{tabularx}')
        fd.write("\n"+r'\end{table}')
        fd.write("\n"+r'\begin{table}[H]')
        fd.write("\n"+r'	\begin{tabularx}{1\columnwidth}{ B{1} B{1} }')
        fd.write("\n"+r'\rowcolor{Gray}	')
        fd.write("\n"+r'	\textbf{Außenwinddruck $w_{e,1}$ $\updownarrow$} &  \textbf{Außenwinddruck $w_{e,1}$ $\leftrightarrow$}\\')
        aussendruck_1(self,arg_latex,fd)


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
                    fd.write("\n"+r'w_{e,10,'+ beschriftung[ind_a]+r'}&=\spann{'+ str(ausenwindruecke_d[ind_list][0])+r'}   \\')
                else:
                    for ind_d, element_d in enumerate(ausenwindruecke_d[ind_list]):
                        fd.write("\n"+r'w_{e,10,'+ beschriftung[ind_a]+ str(ind_d+1)+r'}&=\spann{'+ str(element_d)+r'}   \\')
            elif ind_a ==2 and element_a ==0:
                print('keine Fläche c')
            else:
                fd.write("\n"+r'w_{e,10,'+ beschriftung[ind_a]+r'}&=\spann{'+ str(element_a)+r'}   \\')
        fd.write("\n"+r'		\end{aligned}		$')
        if ind_list != (len(ausenwindruecke_a_b_c_e)-1):
            fd.write("\n"+r'		&		')

def aussendruck_1(self,arg_latex,fd):
    ergebnisse_berechnung=arg_latex['ergebnisse_berechnung']
    ergebnisse_waende=ergebnisse_berechnung['ergebnisse_waende']
    ausenwindruecke_d=ergebnisse_waende['ausenwindruecke_1_d']
    ausenwindruecke_a_b_c_e=ergebnisse_waende['ausenwindruecke_1_a_b_c_e']
    beschriftung=['A','B','C','D','E']
    for ind_list, element_list in enumerate(ausenwindruecke_a_b_c_e):
        fd.write("\n"+r'$	\begin{aligned}[t]')
        for ind_a, element_a in enumerate(ausenwindruecke_a_b_c_e[ind_list]):
            if ind_a == 3:
                if len(ausenwindruecke_d[ind_list]) == 1:
                    fd.write("\n"+r'w_{e,1,'+ beschriftung[ind_a]+r'}&=\spann{'+ str(ausenwindruecke_d[ind_list][0])+r'}   \\')
                else:
                    for ind_d, element_d in enumerate(ausenwindruecke_d[ind_list]):
                        fd.write("\n"+r'w_{e,1,'+ beschriftung[ind_a]+ str(ind_d+1)+r'}&=\spann{'+ str(element_d)+r'}   \\')
            elif ind_a ==2 and element_a ==0:
                print('keine Fläche c')
            else:
                fd.write("\n"+r'w_{e,1,'+ beschriftung[ind_a]+r'}&=\spann{'+ str(element_a)+r'}   \\')
        fd.write("\n"+r'		\end{aligned}		$')
        if ind_list != (len(ausenwindruecke_a_b_c_e)-1):
            fd.write("\n"+r'		&		')

def aussendruck_A(self,arg_latex,fd,einflussflaeche):
    ergebnisse_berechnung=arg_latex['ergebnisse_berechnung']
    ergebnisse_waende=ergebnisse_berechnung['ergebnisse_waende']
    ausenwindruecke_d=ergebnisse_waende['ausenwindruecke_A_d']
    ausenwindruecke_a_b_c_e=ergebnisse_waende['ausenwindruecke_A_a_b_c_e']
    beschriftung=['A','B','C','D','E']

    for ind_list, element_list in enumerate(ausenwindruecke_a_b_c_e):
        fd.write("\n"+r'$	\begin{aligned}[t]')
        for ind_a, element_a in enumerate(ausenwindruecke_a_b_c_e[ind_list]):
            if ind_a == 3:
                if len(ausenwindruecke_d[ind_list]) == 1:
                    fd.write("\n"+r'w_{e,'+ str(einflussflaeche)+r','+ beschriftung[ind_a]+r'}&=\spann{'+ str(ausenwindruecke_d[ind_list][0])+r'}   \\')
                else:
                    for ind_d, element_d in enumerate(ausenwindruecke_d[ind_list]):
                        fd.write("\n"+r'w_{e,'+ str(einflussflaeche)+r','+ beschriftung[ind_a]+ str(ind_d+1)+r'}&=\spann{'+ str(element_d)+r'}   \\')
            elif ind_a ==2 and element_a ==0:
                print('keine Fläche c')
            else:
                fd.write("\n"+r'w_{e,'+ str(einflussflaeche)+r','+ beschriftung[ind_a]+r'}&=\spann{'+ str(element_a)+r'}   \\')
        fd.write("\n"+r'		\end{aligned}		$')
        if ind_list != (len(ausenwindruecke_a_b_c_e)-1):
            fd.write("\n"+r'		&		')


def aussendruckbeiwerte_waende(self,arg_latex,latex_waende_list,filename):
    ergebnisse_berechnung=arg_latex['ergebnisse_berechnung']
    ergebnisse_waende=ergebnisse_berechnung['ergebnisse_waende']
    cpe=ergebnisse_waende['cpe']
    beschriftung=['A','B','C','D','E']
    einflussflaeche=latex_waende_list['einflussflaeche']
    with io.open(filename,'w', encoding="UTF8") as fd:
        #Einflussfläche 10
        fd.write("\n"+r'\begin{table}[H]')
        fd.write("\n"+r'	\begin{tabularx}{1\columnwidth}{ B{1} B{1}  }')
        fd.write("\n"+r'\rowcolor{Gray}	')
        fd.write("\n"+r'	\textbf{Außendruckbeiwert $c_{pe,10}$ $\updownarrow$} &  \textbf{Außendruckbeiwert $c_{pe,10}$ $\leftrightarrow$} \\')
        for ind_list, element_list in enumerate(cpe):
            fd.write("\n"+r'$	\begin{aligned}[t]')
            for ind_a, element_a in enumerate(cpe[ind_list]):
                if ind_a ==2 and element_a==0:
                    print('keine Fläche c')
                else:
                    fd.write("\n"+r'c_{pe,10,'+ beschriftung[ind_a]+r'}&=\num{'+ str(element_a)+r'}   \\')
            fd.write("\n"+r'		\end{aligned}		$')
            if ind_list != (len(cpe)-1):
                fd.write("\n"+r'		&		')
        fd.write("\n"+r'\end{tabularx}')
        fd.write("\n"+r'\end{table}')

        #Einflussfläche A
        cpe=ergebnisse_waende['cpe_A']
        fd.write("\n"+r'\begin{table}[H]')
        fd.write("\n"+r'	\begin{tabularx}{1\columnwidth}{ B{1} B{1}  }')
        fd.write("\n"+r'\rowcolor{Gray}	')
        fd.write("\n"+r'	\textbf{Außendruckbeiwert $c_{pe,'+ str(einflussflaeche)+r'}$ $\updownarrow$} &  \textbf{Außendruckbeiwert $c_{pe,'+ str(einflussflaeche)+r'}$ $\leftrightarrow$} \\')
        for ind_list, element_list in enumerate(cpe):
            fd.write("\n"+r'$	\begin{aligned}[t]')
            for ind_a, element_a in enumerate(cpe[ind_list]):
                if ind_a ==2 and element_a==0:
                    print('keine Fläche c')
                else:
                    fd.write("\n"+r'c_{pe,'+ str(einflussflaeche)+r','+ beschriftung[ind_a]+r'}&=\num{'+ str(element_a)+r'}   \\')
            fd.write("\n"+r'		\end{aligned}		$')
            if ind_list != (len(cpe)-1):
                fd.write("\n"+r'		&		')
        fd.write("\n"+r'\end{tabularx}')
        fd.write("\n"+r'\end{table}')

        #Einflussfläche 1
        cpe=ergebnisse_waende['cpe_1']
        fd.write("\n"+r'\begin{table}[H]')
        fd.write("\n"+r'	\begin{tabularx}{1\columnwidth}{ B{1} B{1}  }')
        fd.write("\n"+r'\rowcolor{Gray}	')
        fd.write("\n"+r'	\textbf{Außendruckbeiwert $c_{pe,1}$ $\updownarrow$} &  \textbf{Außendruckbeiwert $c_{pe,1}$ $\leftrightarrow$} \\')
        for ind_list, element_list in enumerate(cpe):
            fd.write("\n"+r'$	\begin{aligned}[t]')
            for ind_a, element_a in enumerate(cpe[ind_list]):
                if ind_a ==2 and element_a==0:
                    print('keine Fläche c')
                else:
                    fd.write("\n"+r'c_{pe,1,'+ beschriftung[ind_a]+r'}&=\num{'+ str(element_a)+r'}   \\')
            fd.write("\n"+r'		\end{aligned}		$')
            if ind_list != (len(cpe)-1):
                fd.write("\n"+r'		&		')
        fd.write("\n"+r'\end{tabularx}')
        fd.write("\n"+r'\end{table}')



def aussendruckbeiwerte_waende_A(self,arg_latex,filename):
    ergebnisse_berechnung=arg_latex['ergebnisse_berechnung']
    ergebnisse_waende=ergebnisse_berechnung['ergebnisse_waende']
    cpe=ergebnisse_waende['cpe_1']
    beschriftung=['A','B','C','D','E']
    with io.open(filename,'w', encoding="UTF8") as fd:
        fd.write("\n"+r'\begin{table}[H]')
        fd.write("\n"+r'	\begin{tabularx}{1\columnwidth}{ B{1} B{1}  }')
        fd.write("\n"+r'\rowcolor{Gray}	')
        fd.write("\n"+r'	\textbf{Außendruckbeiwert $c_{pe,A}$ $\updownarrow$} &  \textbf{Außendruckbeiwert $c_{pe,A}$ $\leftrightarrow$} \\')
        for ind_list, element_list in enumerate(cpe):
            fd.write("\n"+r'$	\begin{aligned}[t]')
            for ind_a, element_a in enumerate(cpe[ind_list]):
                if ind_a ==2 and element_a==0:
                    print('keine Fläche c')
                else:
                    fd.write("\n"+r'c_{pe,A,'+ beschriftung[ind_a]+r'}&=\num{'+ str(element_a)+r'}   \\')
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
            fd.write("\n"+r'q_{p,s'+ str(ind_a+1) +r'}&=\spann{'+ str(element_a)+r'}   \\')
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
        fd.write("\n"+r' \textbf{Überlagerter Winddruck $ w_{10} $ $\downarrow$ } & \textbf{Überlagerter Winddruck $ w_{10} $ $\leftarrow$}\\')
    else:
        fd.write("\n"+r' \textbf{Überlagerter Winddruck $ w_{10} $ $\updownarrow$ } & \textbf{Überlagerter Winddruck $ w_{10} $ $\leftrightarrow$}\\')
    for ind_list, element_list in enumerate(ergebnisse_ueberlagerung_a_b_c_e):
        if ind_list == 2:
            fd.write("\n"+r'	 \\ \rule{0mm}{4mm}')
            fd.write("\n"+r'	 \\')
            fd.write("\n"+r'\rowcolor{Gray}	')
            fd.write("\n"+r' \textbf{Überlagerter Winddruck $ w_{10} $ $\uparrow$ } & \textbf{Überlagerter Winddruck $ w_{10} $ $\rightarrow$}\\')
        fd.write("\n"+r'$	\begin{aligned}[t]')
        for ind_a, element_a in enumerate(ergebnisse_ueberlagerung_a_b_c_e[ind_list]):
            if ind_a == 3:
                if len(ergebnisse_ueberlagerung_d[ind_list]) == 1:
                    fd.write("\n"+r'w_{10,'+ beschriftung[ind_a]+r'}&=\spann{'+ str(ergebnisse_ueberlagerung_d[ind_list][0])+r'}   \\')
                else:
                    for ind_d, element_d in enumerate(ergebnisse_ueberlagerung_d[ind_list]):
                        fd.write("\n"+r'w_{10,'+ beschriftung[ind_a]+ str(ind_d+1)+r'}&=\spann{'+ str(element_d)+r'}   \\')
            elif ind_a ==2 and element_a ==innendruck[0]:
                print('keine Fläche c')
            else:
                fd.write("\n"+r'w_{10,'+ beschriftung[ind_a]+r'}&=\spann{'+ str(element_a)+r'}   \\')
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
    einflussflaeche=latex_waende_list['einflussflaeche']

    #Margin
    fd.write("\n"+r'\switchcolumn*')
    fd.write("\n"+r'\begin{tabular}{ r @{ \dots} L{2.8cm} }')
    fd.write("\n"+r' + & Winddruck')
    fd.write("\n"+r'\\')
    fd.write("\n"+r' -- & Windsog')
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
        fd.write("\n"+r'\\')
    fd.write("\n"+r'\multicolumn{2}{l}{  Indizes:} \\')
    fd.write("\n"+r' $e$ & Außen')
    fd.write("\n"+r'\\')
    fd.write("\n"+r' $i$ & Innen')
    fd.write("\n"+r'\\')
    fd.write("\n"+r' $10$ & Einflussfläche $\geq \SI{10}{\square\meter}$')
    fd.write("\n"+r'\\')
    fd.write("\n"+r' $'+ str(einflussflaeche)+r'$ & Einflussfläche $= \SI{'+ str(einflussflaeche)+r'}{\square\meter}$')
    fd.write("\n"+r'\\')
    fd.write("\n"+r' $1$ & Einflussfläche $\leq \SI{1}{\square\meter}$')
    fd.write("\n"+r'\\')
    fd.write("\n"+r' $s$ & Streifen')
    fd.write("\n"+r'\\')
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
