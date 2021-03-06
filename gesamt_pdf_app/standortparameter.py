from django.shortcuts import get_object_or_404
import io
from core.models import allgEingaben

# UTF8 brauche ich für umlate
# with macht das file automatisch wieder zu





def standortparameter(self,arg_latex,filename):
    #gibt mir alle objekte aus aus dem Model: allgEingaben(standortparameter) je Projekt
    allgeingaben = get_object_or_404(allgEingaben.objects.filter(id=self.kwargs['my']))


    bundesland = allgeingaben.bundesland
    ort = allgeingaben.ort
    gelaendekategorie = allgeingaben.gelaendekategorie
    basiswinddruck = allgeingaben.basiswinddruck
    windgeschwindigkeit = allgeingaben.windgeschwindigkeit
    seehoehe = allgeingaben.seehoehe
    abminderungsfaktor = allgeingaben.abminderungsfaktor
    winddruck_benutzerdefiniert = allgeingaben.winddruck_benutzerdefiniert
    seehoehe_benutzerdefiniert = allgeingaben.seehoehe_benutzerdefiniert
    with io.open(filename,'w', encoding="UTF8") as fd:
         fd.write("\n"+r'\switchcolumn*')
         fd.write("\n"+r'\vspace{-0.3cm}')
         fd.write("\n"+r'\scriptsize')
         fd.write("\n"+r'\begin{tabular}{ r @{\dots} L{2.8cm} }')
         fd.write("\n"+r'$v_{b,0}$ &  Basiswind- geschwindigkeit')
         fd.write("\n"+r'\\')
         fd.write("\n"+r'$q_{b,0}$ &  Basisgeschwin- digkeitsdruck')
         if winddruck_benutzerdefiniert ==True:
                  fd.write("\n"+r'(vom Benutzer definiert)')
         fd.write("\n"+r'\\')
         fd.write("\n"+r'$H$ &  Seehöhe')
         if seehoehe_benutzerdefiniert ==True:
                  fd.write("\n"+r'(vom Benutzer definiert)')
         fd.write("\n"+r'\\')
         fd.write("\n"+r'$f_s$ &  Abminderungsfaktor für Basiswindgeschwindigkeitsdrücke')
         fd.write("\n"+r'\\')
         fd.write("\n"+r'\end{tabular}')
         fd.write("\n"+r'\switchcolumn')

         fd.write("\n"+r'\vspace{-0.5cm}')
         fd.write("\n"+r'\begin{table}[H]')
         fd.write("\n"+r'\centering')
         fd.write("\n"+r'\begin{tabularx}{1\columnwidth}{B{1.24} B{0.88} B{0.88}}')
         fd.write("\n"+r'\rowcolor{Gray}	')
         fd.write("\n"+r'\multicolumn{3}{c}{\rule{0mm}{5mm} \Large{\textbf{Standortparameter}}} \\')
         fd.write("\n"+r'\begin{tabular}[t]{R{2.875cm}  L{2.875cm}}')
         fd.write("\n"+r'Bundesland:& '+ str(bundesland))
         fd.write("\n"+r'\\')
         fd.write("\n"+r'Ort:& '+ str(ort))
         fd.write("\n"+r'\\')
         fd.write("\n"+r'Geländekategorie:& ' + str(gelaendekategorie))
         fd.write("\n"+r'\end{tabular}')
         fd.write("\n"+r'&')
         fd.write("\n"+r'$	\begin{aligned}[t]')
         fd.write("\n"+r'v_{b,0}&=\SI{'+ str(windgeschwindigkeit)+r'}{\meter\per\second}')
         fd.write("\n"+r'\\')
         fd.write("\n"+r'q_{b,0}&=\spann{'+ str(basiswinddruck)+r'}')
         fd.write("\n"+r'\end{aligned}$')
         fd.write("\n"+r'&')
         fd.write("\n"+r'$	\begin{aligned}[t]')
         fd.write("\n"+r'H &=\lang{'+ str(seehoehe)+r'}')
         fd.write("\n"+r'\\')
         fd.write("\n"+r'f_s &=\num{'+ str(abminderungsfaktor)+r'}')
         fd.write("\n"+r'\end{aligned}$')
         fd.write("\n"+r'\end{tabularx}')
         fd.write("\n"+r'\end{table}')


def standortparameter_schnee(self,arg_latex,filename):
    #gibt mir alle objekte aus aus dem Model: allgEingaben(standortparameter) je Projekt
    allgeingaben = get_object_or_404(allgEingaben.objects.filter(id=self.kwargs['my']))


    bundesland = allgeingaben.bundesland
    ort = allgeingaben.ort
    gelaendekategorie = allgeingaben.gelaendekategorie
    basiswinddruck = allgeingaben.basiswinddruck
    windgeschwindigkeit = allgeingaben.windgeschwindigkeit
    seehoehe = allgeingaben.seehoehe
    abminderungsfaktor = allgeingaben.abminderungsfaktor
    winddruck_benutzerdefiniert = allgeingaben.winddruck_benutzerdefiniert
    seehoehe_benutzerdefiniert = allgeingaben.seehoehe_benutzerdefiniert
    schneelast= allgeingaben.schneelast
    schneelast_benutzerdefiniert= allgeingaben.schneelast_benutzerdefiniert
    schneelastzone=allgeingaben.schneelastzone
    with io.open(filename,'w', encoding="UTF8") as fd:
         fd.write("\n"+r'\switchcolumn*')
         fd.write("\n"+r'\vspace{-0.3cm}')
         fd.write("\n"+r'\scriptsize')
         fd.write("\n"+r'\begin{tabular}{ r @{\dots} L{2.8cm} }')
         fd.write("\n"+r'$H$ &  Seehöhe')
         if seehoehe_benutzerdefiniert ==True:
                  fd.write("\n"+r'(vom Benutzer definiert)')
         fd.write("\n"+r'\\')
         fd.write("\n"+r'$s_k$ &  charakteristischer Wert der Schneelast auf dem Boden')
         if schneelast_benutzerdefiniert ==True:
                  fd.write("\n"+r'(vom Benutzer definiert)')
         fd.write("\n"+r'\\')
         fd.write("\n"+r'\end{tabular}')
         fd.write("\n"+r'\switchcolumn')

         fd.write("\n"+r'\vspace{-0.5cm}')
         fd.write("\n"+r'\begin{table}[H]')
         fd.write("\n"+r'\centering')
         fd.write("\n"+r'\begin{tabularx}{1\columnwidth}{B{1.0} B{1}}')
         fd.write("\n"+r'\rowcolor{Gray}	')
         fd.write("\n"+r'\multicolumn{2}{c}{\rule{0mm}{5mm} \Large{\textbf{Standortparameter}}} \\')
         fd.write("\n"+r'\begin{tabular}[t]{R{2.875cm}  L{2.875cm}}')
         fd.write("\n"+r'Bundesland:& '+ str(bundesland))
         fd.write("\n"+r'\\')
         fd.write("\n"+r'Ort:& '+ str(ort))
         fd.write("\n"+r'\\')
         fd.write("\n"+r'Schneelastzone:& ' + str(schneelastzone))
         fd.write("\n"+r'\end{tabular}')
         fd.write("\n"+r'&')
         fd.write("\n"+r'$	\begin{aligned}[t]')
         fd.write("\n"+r'H &=\lang{'+ str(seehoehe)+r'}')
         fd.write("\n"+r'\\')
         fd.write("\n"+r's_{k}&=\spann{'+ str(schneelast)+r'}')
         fd.write("\n"+r'\end{aligned}$')
         fd.write("\n"+r'\end{tabularx}')
         fd.write("\n"+r'\end{table}')

def standortparameter_schnee_wind(self,arg_latex,filename):
    #gibt mir alle objekte aus aus dem Model: allgEingaben(standortparameter) je Projekt
    allgeingaben = get_object_or_404(allgEingaben.objects.filter(id=self.kwargs['my']))


    bundesland = allgeingaben.bundesland
    ort = allgeingaben.ort
    gelaendekategorie = allgeingaben.gelaendekategorie
    basiswinddruck = allgeingaben.basiswinddruck
    windgeschwindigkeit = allgeingaben.windgeschwindigkeit
    seehoehe = allgeingaben.seehoehe
    abminderungsfaktor = allgeingaben.abminderungsfaktor
    winddruck_benutzerdefiniert = allgeingaben.winddruck_benutzerdefiniert
    seehoehe_benutzerdefiniert = allgeingaben.seehoehe_benutzerdefiniert
    schneelast= allgeingaben.schneelast
    schneelast_benutzerdefiniert= allgeingaben.schneelast_benutzerdefiniert
    schneelastzone=allgeingaben.schneelastzone
    with io.open(filename,'w', encoding="UTF8") as fd:
         fd.write("\n"+r'\switchcolumn*')
         fd.write("\n"+r'\vspace{-0.3cm}')
         fd.write("\n"+r'\scriptsize')
         fd.write("\n"+r'\begin{tabular}{ r @{\dots} L{2.8cm} }')
         fd.write("\n"+r'$v_{b,0}$ &  Basiswind- geschwindigkeit')
         fd.write("\n"+r'\\')
         fd.write("\n"+r'$q_{b,0}$ &  Basisgeschwin- digkeitsdruck')
         if winddruck_benutzerdefiniert ==True:
                  fd.write("\n"+r'(vom Benutzer definiert)')
         fd.write("\n"+r'\\')
         fd.write("\n"+r'$H$ &  Seehöhe')
         if seehoehe_benutzerdefiniert ==True:
                  fd.write("\n"+r'(vom Benutzer definiert)')
         fd.write("\n"+r'\\')
         fd.write("\n"+r'$s_k$ &  charakteristischer Wert der Schneelast auf dem Boden')
         if schneelast_benutzerdefiniert ==True:
                  fd.write("\n"+r'(vom Benutzer definiert)')
         fd.write("\n"+r'\\')
         fd.write("\n"+r'$f_s$ &  Abminderungsfaktor für Basiswindgeschwindigkeitsdrücke')
         fd.write("\n"+r'\\')
         fd.write("\n"+r'\end{tabular}')
         fd.write("\n"+r'\switchcolumn')

         fd.write("\n"+r'\vspace{-0.5cm}')
         fd.write("\n"+r'\begin{table}[H]')
         fd.write("\n"+r'\centering')
         fd.write("\n"+r'\begin{tabularx}{1\columnwidth}{B{1.24} B{0.88} B{0.88}}')
         fd.write("\n"+r'\rowcolor{Gray}	')
         fd.write("\n"+r'\multicolumn{3}{c}{\rule{0mm}{5mm} \Large{\textbf{Standortparameter}}} \\')
         fd.write("\n"+r'\begin{tabular}[t]{R{2.875cm}  L{2.875cm}}')
         fd.write("\n"+r'Bundesland:& '+ str(bundesland))
         fd.write("\n"+r'\\')
         fd.write("\n"+r'Ort:& '+ str(ort))
         fd.write("\n"+r'\\')
         fd.write("\n"+r'Geländekategorie:& ' + str(gelaendekategorie))
         fd.write("\n"+r'\\')
         fd.write("\n"+r'Schneelastzone:& ' + str(schneelastzone))
         fd.write("\n"+r'\end{tabular}')
         fd.write("\n"+r'&')
         fd.write("\n"+r'$	\begin{aligned}[t]')
         fd.write("\n"+r'v_{b,0}&=\SI{'+ str(windgeschwindigkeit)+r'}{\meter\per\second}')
         fd.write("\n"+r'\\')
         fd.write("\n"+r'q_{b,0}&=\spann{'+ str(basiswinddruck)+r'}')
         fd.write("\n"+r'\\')
         fd.write("\n"+r's_{k}&=\span{'+ str(schneelast)+r'}')
         fd.write("\n"+r'\end{aligned}$')
         fd.write("\n"+r'&')
         fd.write("\n"+r'$	\begin{aligned}[t]')
         fd.write("\n"+r'H &=\lang{'+ str(seehoehe)+r'}')
         fd.write("\n"+r'\\')
         fd.write("\n"+r'f_s &=\num{'+ str(abminderungsfaktor)+r'}')
         fd.write("\n"+r'\end{aligned}$')
         fd.write("\n"+r'\end{tabularx}')
         fd.write("\n"+r'\end{table}')
