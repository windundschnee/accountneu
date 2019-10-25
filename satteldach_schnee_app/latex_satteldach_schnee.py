import os
import io
from .models import SatteldachSchneeModel



def ergebnisse_angaben_satteldach_schnee(self,arg_latex,filename):

    eingaben_satteldach_schnee = SatteldachSchneeModel.objects.get(pk=self.kwargs['pk'])
    bauteilname = self.satteldach_schnee.bautteil_name.bautteil_name
    ergebnisse_schnee=arg_latex['ergebnisse_schnee']
    mue=ergebnisse_schnee['mue']
    neigung_alpha1=ergebnisse_schnee['neigung_alpha1']
    neigung_alpha2=ergebnisse_schnee['neigung_alpha2']
    gesammtschneelast=ergebnisse_schnee['gesammtschneelast']
    gesammtschneelast_halbe=ergebnisse_schnee['gesammtschneelast_halbe']
    indizes_mue=[r'1(\alpha 1)',r'1(\alpha 2)',r'2(\alpha 1)',r'2(\alpha 2)']

    with io.open(filename,'w', encoding="UTF8") as fd:
        #Beschreibung in Margin
        fd.write("\n"+r'\switchcolumn*')
        fd.write("\n"+r'\begin{tabular}{ r @{\dots} L{2.8cm} }')
        fd.write("\n"+r'$\alpha$ & Neigungswinkel des Dachs  ')
        fd.write("\n"+r'\\')
        fd.write("\n"+r'$\mu$ & Formbeiwert  ')
        fd.write("\n"+r'\\')
        fd.write("\n"+r'$s$ & Schneelast auf dem Dach  ')
        fd.write("\n"+r'\\')
        fd.write("\n"+r'\romannumeral 1 & Fall 1 nichtverwehter Schnee ')
        fd.write("\n"+r'\\')
        fd.write("\n"+r'\romannumeral 2 & Fall 2 verwehter Schnee ')
        fd.write("\n"+r'\\')
        fd.write("\n"+r'\romannumeral 3 & Fall 3 verwehter Schnee ')
        fd.write("\n"+r'\end{tabular}')
        fd.write("\n"+r'\vspace{3 mm}')
        fd.write("\n"+r'\\')
        if eingaben_satteldach_schnee.abrutschen_verhindert == True:
            fd.write("\n"+r'Das Abrutschen des Schnees ist verhindert')

        fd.write("\n"+r'\switchcolumn')

        #####geometrische geometrische_angaben_Pultdach Schnee
        fd.write("\n"+r'\begin{table}[H]')
        fd.write("\n"+r'\centering')
        fd.write("\n"+r'\begin{tabularx}{1\columnwidth}{B{1} B{1} B{1} }')
        fd.write("\n"+r'\rowcolor{Gray}	')
        fd.write("\n"+r'\multicolumn{3}{c}{  \rule{0mm}{5mm} \Large{\textbf{'+ str(bauteilname) +r' -- Schneellast auf Pultdach }}} \\')
        fd.write("\n"+r'		$\begin{aligned}[t]')
        fd.write("\n"+r'		\alpha_1 & =\ang{'+ str(neigung_alpha1)+r'}')
        fd.write("\n"+r'		\\')
        fd.write("\n"+r'		\alpha_2 & =\ang{'+ str(neigung_alpha2)+r'}')
        fd.write("\n"+r'		\\')

        fd.write("\n"+r'		\end{aligned}$')
        fd.write("\n"+r'	&')
        fd.write("\n"+r'		$\begin{aligned}[t]')
        for ind_list, element_list in enumerate(mue):
            fd.write("\n"+r'		\mu_{'+ str(indizes_mue[ind_list])+r'} & =\num{'+ str(element_list)+r'}')
            fd.write("\n"+r'		\\')
        fd.write("\n"+r'		\end{aligned}$')
        fd.write("\n"+r'	&')
        fd.write("\n"+r'		$\begin{aligned}[t]')
        fd.write("\n"+r'		s_{\text{\romannumeral 1}(\alpha 1)} & =\spann{'+  str(gesammtschneelast[0])+r'}')
        fd.write("\n"+r'		\\')
        fd.write("\n"+r'		s_{\text{\romannumeral 1}(\alpha 2)} & =\spann{'+  str(gesammtschneelast[1])+r'}')
        fd.write("\n"+r'		\\')
        fd.write("\n"+r'		s_{\text{\romannumeral 2}(\alpha 1)} & =\spann{'+  str(gesammtschneelast_halbe[2])+r'}')
        fd.write("\n"+r'		\\')
        fd.write("\n"+r'		s_{\text{\romannumeral 2}(\alpha 2)} & =\spann{'+  str(gesammtschneelast[3])+r'}')
        fd.write("\n"+r'		\\')
        fd.write("\n"+r'		s_{\text{\romannumeral 3}(\alpha 1)} & =\spann{'+  str(gesammtschneelast[2])+r'}')
        fd.write("\n"+r'		\\')
        fd.write("\n"+r'		s_{\text{\romannumeral 3}(\alpha 2)} & =\spann{'+  str(gesammtschneelast_halbe[3])+r'}')

        fd.write("\n"+r'		\end{aligned}$')

        fd.write("\n"+r'\end{tabularx}')
        fd.write("\n"+r'\end{table}')


def bilder_satteldach_schnee(self,arg_latex,filename):
    ergebnisse_schnee=arg_latex['ergebnisse_schnee']
    neigung_alpha1=ergebnisse_schnee['neigung_alpha1']
    neigung_alpha2=ergebnisse_schnee['neigung_alpha2']
    gesammtschneelast=ergebnisse_schnee['gesammtschneelast']
    gesammtschneelast_halbe=ergebnisse_schnee['gesammtschneelast_halbe']

    hoehe_1=1
    hoehe_2=1.9
    breite=5
    mitte=2
    if gesammtschneelast[0]==gesammtschneelast[1]:
        h_fall_1_a1=0.5
        h_fall_1_a2=0.5
        h_fall_2_a1=0.35
        h_fall_2_a2=0.7
        h_fall_3_a1=0.7
        h_fall_3_a2=0.35
    else:
        if neigung_alpha1<neigung_alpha2:
            h_fall_1_a1=0.5
            h_fall_1_a2=0.4
        else:
            h_fall_1_a1=0.4
            h_fall_1_a2=0.5
        if gesammtschneelast_halbe[2]<gesammtschneelast[3]:
            h_fall_2_a1=0.4
            h_fall_2_a2=0.6
        else:
            h_fall_2_a1=0.6
            h_fall_2_a2=0.4
        if gesammtschneelast[2]<gesammtschneelast_halbe[3]:
            h_fall_3_a1=0.4
            h_fall_3_a2=0.6
        else:
            h_fall_3_a1=0.6
            h_fall_3_a2=0.4


    with io.open(filename,'w', encoding="UTF8") as fd:
        fd.write("\n"+r'\begin{figure}[H]')
        fd.write("\n"+r'\centering')
        fd.write("\n"+r'\begin{tikzpicture}')
        #nodes
        fd.write("\n"+r'\node[coordinate] at (0,0) (na) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(breite)+r',0) (nb) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(breite)+r','+ str(hoehe_1)+r') (nc) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(breite)+r','+ str(hoehe_2)+r') (nco) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(mitte)+r','+ str(hoehe_2)+r') (nd) {};')
        fd.write("\n"+r'\node[coordinate] at (0,'+ str(hoehe_1)+r') (ne) {};')
        fd.write("\n"+r'\node[coordinate] at (0,'+ str(hoehe_2)+r') (neo) {};')


        #Boden
        fd.write("\n"+r'\draw[line width=0.35mm] (na) -- +(-0.5,0);')
        fd.write("\n"+r'\draw[line width=0.35mm] (nb) -- +(0.5,0);')
        fd.write("\n"+r'\draw[line width=0.35mm] (na) -- (nb);')
        fd.write("\n"+r'\fill[pattern,pattern= north east lines] ($(na)-(0.5,0)$) rectangle ($(nb)+(0.5,-0.3)$);')

        #Gebäude
        fd.write("\n"+r'\draw[line width=0.25mm]  (na) -- (nb) -- (nc) -- (nd) -- (ne) -- cycle;')

        #Winkelbemassung links
        fd.write("\n"+r'\draw[ line width=0.13mm]  (ne) -- +(0.8,0);')
        fd.write("\n"+r'\tkzMarkAngle[size=0.6cm](nc,ne,nd)')
        fd.write("\n"+r'\tkzLabelAngle[pos=1.0](nc,ne,nd){\tiny{\ang{'+ str(neigung_alpha1)+r'}}}')
        #Winkelbemassung rechts
        fd.write("\n"+r'\draw[ line width=0.13mm]  (nc) -- +(-0.8,0);')
        fd.write("\n"+r'\tkzMarkAngle[size=0.6cm](nd,nc,ne)')
        fd.write("\n"+r'\tkzLabelAngle[pos=1.1](nd,nc,ne){\tiny{\ang{'+ str(neigung_alpha2)+r'}}}')
        #Fall 1
        fd.write("\n"+r'\lastschnee[($(neo)+(0,0.3)$)][($(nd)+(0,0.3)$)]['+ str(h_fall_1_a1)+r'][\spann{'+ str(gesammtschneelast[0])+r'}][$\mu_{1(\alpha 1)}$]')
        fd.write("\n"+r'\lastschnee[($(nd)+(0,0.3)$)][($(nco)+(0,0.3)$)]['+ str(h_fall_1_a2)+r'][\spann{'+ str(gesammtschneelast[1])+r'}][$\mu_{1(\alpha 2)}$]')
        fd.write("\n"+r'\node at (-0.7,'+ str(hoehe_2+0.55)+r')  {(\romannumeral 1)};')
        #Fall 2
        fd.write("\n"+r'\lastschnee[($(neo)+(0,1.5)$)][($(nd)+(0,1.5)$)]['+ str(h_fall_2_a1)+r'][\spann{'+ str(gesammtschneelast_halbe[2])+r'}][$0,5\mu_{2(\alpha 1)}$]')
        fd.write("\n"+r'\lastschnee[($(nd)+(0,1.5)$)][($(nco)+(0,1.5)$)]['+ str(h_fall_2_a2)+r'][\spann{'+ str(gesammtschneelast[3])+r'}][$\mu_{2(\alpha 2)}$]')
        fd.write("\n"+r'\node at (-0.7,'+ str(hoehe_2+1.85)+r')  {(\romannumeral 2)};')
        #Fall 3
        fd.write("\n"+r'\lastschnee[($(neo)+(0,2.9)$)][($(nd)+(0,2.9)$)]['+ str(h_fall_3_a1)+r'][\spann{'+ str(gesammtschneelast[2])+r'}][$\mu_{2(\alpha 1)}$]')
        fd.write("\n"+r'\lastschnee[($(nd)+(0,2.9)$)][($(nco)+(0,2.9)$)]['+ str(h_fall_3_a2)+r'][\spann{'+ str(gesammtschneelast_halbe[3])+r'}][$0,5\mu_{2(\alpha 2)}$]')
        fd.write("\n"+r'\node at (-0.7,'+ str(hoehe_2+3.25)+r')  {(\romannumeral 3)};')

        fd.write("\n"+r'\end{tikzpicture}')
        fd.write("\n"+r'\end{figure}')
