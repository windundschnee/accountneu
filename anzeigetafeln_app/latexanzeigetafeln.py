import os
from pylatex import Document, Section, Subsection, Command,Figure,TikZ, TikZNode, TikZDraw, TikZCoordinate, TikZUserPath, TikZOptions,Package
from pylatex.utils import italic, NoEscape
from latex import build_pdf
from gesamt_pdf_app.latexbasisfunktionen import *
from gesamt_pdf_app.models import GesamtPdf
from django.forms.models import model_to_dict
from gesamt_pdf_app.kopfzeile import *


def geometrische_angaben(self,arg_latex,filename):


    hoehe = self.anzeigetafeln.hoehe
    breite = self.anzeigetafeln.breite
    abstand_zum_grund = self.anzeigetafeln.abstand_zum_grund
    bauteilname = self.anzeigetafeln.bautteil_name.bautteil_name

    #ergebnisse Anzeigetafeln
    ergebnisse_berechnung = arg_latex['ergebnisse_anzeigetafeln']
    qp = ergebnisse_berechnung['qp']


    aref = ergebnisse_berechnung['aref']
    abstand_e = ergebnisse_berechnung['abstand_e']
    cf = ergebnisse_berechnung['cf']
    Kraft_f = ergebnisse_berechnung['Kraft_f']

    with io.open(filename,'w', encoding="UTF8") as fd:
        fd.write("\n"+r'\switchcolumn*')
        fd.write("\n"+r'\begin{tabular}{ r @{\dots} L{2.8cm} }')
        fd.write("\n"+r'$h$ & Höhe  ')
        fd.write("\n"+r'\\')
        fd.write("\n"+r'$b$ & Breite  ')
        fd.write("\n"+r'\\')
        fd.write("\n"+r'$z_g$ & Bodenabstand ')
        fd.write("\n"+r'\\')
        fd.write("\n"+r'$A_{ref}$ & Bezugsfläche ')
        fd.write("\n"+r'\\')
        fd.write("\n"+r'$e$ & Ausmitte')
        fd.write("\n"+r'\\')
        fd.write("\n"+r'$q_p$ & Böengeschwin- digkeitsdruck  ')
        fd.write("\n"+r'\\')
        fd.write("\n"+r'$F_w$ & Resultierende Windkraft  ')
        fd.write("\n"+r'\\')
        fd.write("\n"+r'$x_F$ & Kraftangriffspunkt  ')
        fd.write("\n"+r'\\')
        fd.write("\n"+r'\end{tabular}')
        fd.write("\n"+r'\switchcolumn')



        fd.write("\n"+r'\begin{table}[H]')
        fd.write("\n"+r'\centering')
        fd.write("\n"+r'\begin{tabularx}{1\columnwidth}{B{1} B{1} B{1} }')
        fd.write("\n"+r'\rowcolor{Gray}	')
        fd.write("\n"+r'\multicolumn{3}{c}{  \rule{0mm}{5mm} \Large{\textbf{'+ str(bauteilname) +r' -- Anzeigetafel }}} \\')
        fd.write("\n"+r'		$\begin{aligned}[t]')
        fd.write("\n"+r'		h & =\lang{'+ str(hoehe)+r'}')
        fd.write("\n"+r'		\\')
        fd.write("\n"+r'		b & =\lang{'+ str(breite)+r'}')
        fd.write("\n"+r'		\\')
        fd.write("\n"+r'		F_w & =\SI{'+ str(Kraft_f)+r'}{\kilo\newton}')
        fd.write("\n"+r'		\end{aligned}$')
        fd.write("\n"+r'		&')
        fd.write("\n"+r'		$\begin{aligned}[t]')
        fd.write("\n"+r'		A_{ref} & =\SI{'+ str(aref)+r'}{\square\meter}')
        fd.write("\n"+r'		\\')
        fd.write("\n"+r' z_g & =\lang{'+ str(abstand_zum_grund)+r'}')
        fd.write("\n"+r'		\end{aligned}$')
        fd.write("\n"+r'		&')
        fd.write("\n"+r'		$\begin{aligned}[t]')
        fd.write("\n"+r'		e & =\lang{'+ str(abstand_e)+r'}')
        fd.write("\n"+r' \\		q_p & =\spann{'+ str(qp)+r'}')
        fd.write("\n"+r'		\end{aligned}$')
        fd.write("\n"+r'\end{tabularx}')
        fd.write("\n"+r'\end{table}')


def bilder(self, arg_latex, filename):

    ergebnisse_berechnung = arg_latex['ergebnisse_anzeigetafeln']
    bezugshoehe = ergebnisse_berechnung['bezugshoehe']
    hoehe = self.anzeigetafeln.hoehe
    breite = self.anzeigetafeln.breite
    abstand_zum_grund = self.anzeigetafeln.abstand_zum_grund

    #ergebnisse Anzeigetafeln
    ergebnisse_berechnung = arg_latex['ergebnisse_anzeigetafeln']

    bezugshoehe = ergebnisse_berechnung['bezugshoehe']
    abstand_e = ergebnisse_berechnung['abstand_e']

    #nur zum zeichnen
    h_latex=2
    b_latex=3.5
    z_latex=1.0
    e_latex=0.25*b_latex


    with io.open(filename,'w', encoding="UTF8") as fd:

        ##Margin
        fd.write("\n"+r'\switchcolumn*')
        fd.write("\n"+r'\vspace{3mm}')
        fd.write("\n"+r'alle Werte in $[m]$')
        fd.write("\n"+r'\switchcolumn')

        fd.write("\n"+r'\tikzset{')
        fd.write("\n"+r'markierung/.pic = {')
        fd.write("\n"+r'\draw[line width=0.13mm, dashdotted] (0,0) -- (0.2,0);')
        fd.write("\n"+r'\draw[line width=0.13mm, dashdotted] (0,0) -- (-0.2,0);')
        fd.write("\n"+r'\draw[line width=0.13mm, dashdotted] (0,0) -- (0,-0.2);')
        fd.write("\n"+r'\draw[line width=0.13mm, dashdotted] (0,0) -- (0,0.2);')

        fd.write("\n"+r'}}')

        fd.write("\n"+r'\begin{figure}[H]')
        fd.write("\n"+r'\centering')
        fd.write("\n"+r'\begin{tikzpicture}')
        fd.write("\n"+r'\node[coordinate] at (0,0) (na) {};')
        fd.write("\n"+r'\node[coordinate] at (0,'+ str(-z_latex)+r') (nau) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(b_latex)+r',0) (nb) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(b_latex)+r','+ str(-z_latex)+r') (nbu) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(b_latex)+r','+ str(h_latex)+r') (nc) {};')
        fd.write("\n"+r'\node[coordinate] at (0,'+ str(h_latex)+r') (nd) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(b_latex/2-e_latex)+r','+ str(h_latex/2)+r') (ne1) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(b_latex/2+e_latex)+r','+ str(h_latex/2)+r') (ne2) {};')
        fd.write("\n"+r'\node[coordinate] at (0,'+ str(h_latex/2)+r') (nea) {};')
        fd.write("\n"+r'\node[coordinate] at ($(na)+(0.5,0)$) (ns1o) {};')
        fd.write("\n"+r'\node[coordinate] at ($(nau)+(0.5,0)$) (ns1u) {};')
        fd.write("\n"+r'\node[coordinate] at ($(nb)+(-0.5,0)$) (ns2o) {};')
        fd.write("\n"+r'\node[coordinate] at ($(nbu)+(-0.5,0)$) (ns2u) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(b_latex/2)+r','+ str(h_latex/2)+r') (nm) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(b_latex/2)+r',0) (nmu) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(b_latex/2)+r','+ str(h_latex)+r') (nmo) {};')


        #Umrandungslinie
        fd.write("\n"+r'\draw[line width=0.25mm] (na) -- (nb) -- (nc) -- (nd) -- cycle;')

        #Kraftangriffspunkt
        fd.write("\n"+r'\draw[line width=0.13mm, dashdotted] (ne1) -- (ne2);')
        fd.write("\n"+r'\pic at (ne1) {markierung};')
        fd.write("\n"+r'\pic at (ne2) {markierung};')
        fd.write("\n"+r'\DimlineH[ne1][nm][-0.5][\num{'+ str(abstand_e)+r'}] ')
        fd.write("\n"+r'\DimlineH[nm][ne2][-0.5][\num{'+ str(abstand_e)+r'}] ')
        fd.write("\n"+r'\node at (ne1) [above left] {\scriptsize{$x_F$}};')
        fd.write("\n"+r'\node at (ne2) [above right] {\scriptsize{$x_F$}};')
        #Mittellinie
        fd.write("\n"+r'\draw[line width=0.13mm, dashdotted] (nmu) -- (nmo);')


        #Stützen
        fd.write("\n"+r'\draw[line width=0.25mm] ($(ns1o)+(0.1,0)$) -- ($(ns1u)+(0.1,0)$);')
        fd.write("\n"+r'\draw[line width=0.25mm] ($(ns1o)-(0.1,0)$) -- ($(ns1u)-(0.1,0)$);')

        fd.write("\n"+r'\draw[line width=0.25mm] ($(ns2o)+(0.1,0)$) -- ($(ns2u)+(0.1,0)$);')
        fd.write("\n"+r'\draw[line width=0.25mm] ($(ns2o)-(0.1,0)$) -- ($(ns2u)-(0.1,0)$);')

        #Bemaßung
        fd.write("\n"+r'\DimlineV[nau][na][-0.3][\num{'+ str(abstand_zum_grund)+r'}] ')
        fd.write("\n"+r'\DimlineV[na][nd][-0.3][\num{'+ str(hoehe)+r'}] ')
        fd.write("\n"+r'\DimlineV[nbu]['+ str(b_latex)+r','+ str(h_latex/2)+r'][0.5][\num{'+ str(bezugshoehe)+r'}] ')

        fd.write("\n"+r'\DimlineH[nd][nmo][0.3][\num{'+ str(breite/2)+r'}] ')
        fd.write("\n"+r'\DimlineH[nmo][nc][0.3][\num{'+ str(breite/2)+r'}] ')
        fd.write("\n"+r'\DimlineH[nd][nc][0.8][\num{'+ str(breite)+r'}] ')

        #Boden
        fd.write("\n"+r'\draw[line width=0.35mm] (nau) -- +(-0.5,0);')
        fd.write("\n"+r'\draw[line width=0.35mm] (nbu) -- +(0.5,0);')
        fd.write("\n"+r'\draw[line width=0.35mm] (nau) -- (nbu);')
        fd.write("\n"+r'\fill[pattern,pattern= north east lines] ($(nau)-(0.5,0)$) rectangle ($(nbu)+(0.5,-0.3)$);')


        fd.write("\n"+r'\end{tikzpicture}')
        fd.write("\n"+r'\end{figure}')
