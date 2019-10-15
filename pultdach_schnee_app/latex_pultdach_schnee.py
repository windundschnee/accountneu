import os
import io







def ergebnisse_angaben_pultdach_schnee(self,arg_latex,filename):

    bauteilname = self.pultdach_schnee.bautteil_name.bautteil_name
    ergebnisse_pultdach_schnee=arg_latex['ergebnisse_pultdach_schnee']
    mue_1=ergebnisse_pultdach_schnee['mue_1']
    neigung=ergebnisse_pultdach_schnee['neigung']
    gesamtschneelast=ergebnisse_pultdach_schnee['gesamtschneelast_rounded']

    with io.open(filename,'w', encoding="UTF8") as fd:
        #Beschreibung in Margin
        fd.write("\n"+r'\switchcolumn*')
        fd.write("\n"+r'\begin{tabular}{ r @{\dots} L{2.8cm} }')
        fd.write("\n"+r'$\alpha$ & Neigungswinkel des Dachs  ')
        fd.write("\n"+r'\\')
        fd.write("\n"+r'$\mu$ & Formbeiwert  ')
        fd.write("\n"+r'\\')
        fd.write("\n"+r'$s$ & Schneelast auf dem Dach  ')
        fd.write("\n"+r'\end{tabular}')
        fd.write("\n"+r'\switchcolumn')

        #####geometrische geometrische_angaben_Pultdach Schnee
        fd.write("\n"+r'\begin{table}[H]')
        fd.write("\n"+r'\centering')
        fd.write("\n"+r'\begin{tabularx}{1\columnwidth}{B{1} B{1} B{1} }')
        fd.write("\n"+r'\rowcolor{Gray}	')
        fd.write("\n"+r'\multicolumn{3}{c}{  \rule{0mm}{5mm} \Large{\textbf{'+ str(bauteilname) +r' -- Schneellast auf Pultdach }}} \\')
        fd.write("\n"+r'		$\begin{aligned}[t]')
        fd.write("\n"+r'		\alpha & =\ang{'+ str(neigung)+r'}')
        fd.write("\n"+r'		\\')

        fd.write("\n"+r'		\end{aligned}$')
        fd.write("\n"+r'	&')
        fd.write("\n"+r'		$\begin{aligned}[t]')
        fd.write("\n"+r'		\mu_1 & ='+ str(mue_1)+r'')
        fd.write("\n"+r'		\\')

        fd.write("\n"+r'		\end{aligned}$')
        fd.write("\n"+r'	&')
        fd.write("\n"+r'		$\begin{aligned}[t]')
        fd.write("\n"+r'		s & =\spann{'+  str(gesamtschneelast)+r'}')

        fd.write("\n"+r'		\end{aligned}$')

        fd.write("\n"+r'\end{tabularx}')
        fd.write("\n"+r'\end{table}')


def bilder_pultdach_schnee(self,arg_latex,filename):
    ergebnisse_pultdach_schnee=arg_latex['ergebnisse_pultdach_schnee']
    neigung=ergebnisse_pultdach_schnee['neigung']
    gesamtschneelast=ergebnisse_pultdach_schnee['gesamtschneelast_rounded']
    hoehe_1=1
    hoehe_2=1.8
    breite=3
    with io.open(filename,'w', encoding="UTF8") as fd:
        ##Margin
        fd.write("\n"+r'\switchcolumn*')
        fd.write("\n"+r'alle Werte in $[m]$')
        fd.write("\n"+r'\switchcolumn')
        ##############
        ####Bild zusammenfügen
        fd.write("\n"+r'\begin{figure}[H]')
        fd.write("\n"+r'\centering')
        fd.write("\n"+r'\begin{tikzpicture}')
        #nodes
        fd.write("\n"+r'\node[coordinate] at (0,0) (na) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(breite)+r',0) (nb) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(breite)+r','+ str(hoehe_2)+r') (nc) {};')
        fd.write("\n"+r'\node[coordinate] at (0,'+ str(hoehe_1)+r') (nd) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(breite+2)+r','+ str(hoehe_1)+r') (ndc) {};')

        #Boden
        fd.write("\n"+r'\draw[line width=0.35mm] (na) -- +(-0.5,0);')
        fd.write("\n"+r'\draw[line width=0.35mm] (nb) -- +(0.5,0);')
        fd.write("\n"+r'\draw[line width=0.35mm] (na) -- (nb);')
        fd.write("\n"+r'\fill[pattern,pattern= north east lines] ($(na)-(0.5,0)$) rectangle ($(nb)+(0.5,-0.3)$);')

        #Gebäude
        fd.write("\n"+r'\draw[line width=0.25mm]  (na) -- (nb) -- (nc) -- (nd) -- cycle;')

        #Winkelbemassung links
        fd.write("\n"+r'\draw[dashed, line width=0.13mm]  (nd) -- +(1.6,0);')
        fd.write("\n"+r'\tkzMarkAngle[size=1.4cm](ndc,nd,nc)')
        fd.write("\n"+r'\tkzLabelAngle[pos=1.7](ndc,nd,nc){\tiny{\num{'+ str(neigung)+r'}}}')

        fd.write("\n"+r'\def\lastschnee[#1][#2][#3][#4]{')
        fd.write("\n"+r'\filldraw[fill=gray!30, draw=black, line width=0.13mm]  #1 -- #2 -- ($#2 + (0,#3)$) -- ($#1 + (0,#3)$) --cycle ;')

        fd.write("\n"+r'\node[above] at ($($#1 + (0,#3)$)!0.5!($#2 + (0,#3)$)$) {#4};')

        fd.write("\n"+r'}')

        fd.write("\n"+r'\lastschnee[($(nd)+(0,1.3)$)][($(nc)+(0,0.5)$)][0.5][\spann{'+ str(gesamtschneelast)+r'}]')




        fd.write("\n"+r'\end{tikzpicture}')
        fd.write("\n"+r'\end{figure}')
