import os
from pylatex import Document, Section, Subsection, Command,Figure,TikZ, TikZNode, TikZDraw, TikZCoordinate, TikZUserPath, TikZOptions,Package
from pylatex.utils import italic, NoEscape
from latex import build_pdf

from gesamt_pdf_app.models import GesamtPdf
from django.forms.models import model_to_dict


def standortparameter_pultdach(self, doc,arg_latex):


    bundesland = self.pultdach.projekt.bundesland
    ort = self.pultdach.projekt.ort
    gelaendekategorie = self.pultdach.projekt.gelaendekategorie
    basiswinddruck = self.pultdach.projekt.basiswinddruck
    windgeschwindigkeit = self.pultdach.projekt.windgeschwindigkeit
    seehoehe = self.pultdach.projekt.seehoehe

    hoehe = self.pultdach.hoehe
    dachneigung = self.pultdach.dachneigung
    eingaben_pdfbearbeiten_titel = arg_latex['eingaben_pdfbearbeiten_titel']


    abminderungsfaktor = self.pultdach.projekt.abminderungsfaktor
    winddruck_benutzerdefiniert = self.pultdach.projekt.winddruck_benutzerdefiniert
    seehoehe_benutzerdefiniert = self.pultdach.projekt.seehoehe_benutzerdefiniert
    vereinfachtes_verfahren = self.pultdach.verfahren_wahl

    ergebnisse_pultdach=arg_latex['ergebnisse_pultdach']





    qp=round(ergebnisse_pultdach['qp'], 2)
    bezugshoehe=hoehe


    if bool(eingaben_pdfbearbeiten_titel) == True:

        if len(eingaben_pdfbearbeiten_titel['titel']) != 0:
            titel = eingaben_pdfbearbeiten_titel['titel']
            doc.append(NoEscape(r'\section*{'+ str(titel)+r'}'))

        if len(eingaben_pdfbearbeiten_titel['untertitel']) !=0:
            untertitel = eingaben_pdfbearbeiten_titel['untertitel']

            doc.append(NoEscape(r'\subsection*{'+ str(untertitel)+r'}'))
        if len(eingaben_pdfbearbeiten_titel['untertitel2']) !=0:
            untertitel2 = eingaben_pdfbearbeiten_titel['untertitel2']

            doc.append(NoEscape(r'\subsection*{'+ str(untertitel2)+r'}'))

    else:
        titel = self.pultdach.projekt.projekt_name
        untertitel = self.pultdach.bautteil_name.bautteil_name
        untertitel2 = self.pultdach.user.company


        doc.append(NoEscape(r'\section*{'+ str(titel)+r'}'))
        doc.append(NoEscape(r'\subsection*{'+ str(untertitel)+r' -- '+'Pultdach'+r'}'))
        doc.append(NoEscape(r'\subsection*{'+ str(untertitel2)+r'}'))


    if vereinfachtes_verfahren == 'Vereinfachtes Verfahren gemäß ÖNORM B 1991-1-4, Abschnitt 9.2.4.1':
        doc.append(NoEscape(r'Die Berechnung erfolgt mit dem Vereinfachten Verfahren gemäß ÖNORM B 1991-1-4, Abschnitt 9.2.4.1 Pultdächer.'))
    else:
        doc.append(NoEscape(r'Die Berechnung erfolgt gemäß ÖNORM EN/B 1991-1-4 Abschnitt 7.2.4 Pultdächer.'))
    doc.append(NoEscape(r'\subsubsection*{Standortparameter}'))
    doc.append(NoEscape(r'\begin{table}[h]'))
    doc.append(NoEscape(r'\centering'))
    doc.append(NoEscape(r'\begin{tabular}{R{3.5cm}  L{3.5cm} R{1.5cm}  @{ }L{2.0cm} @{ \dots} L{5.25cm}}'))
    doc.append(NoEscape(r'Bundesland:& '+ str(bundesland)+r' & $ z_{e}=$&$\SI{'+ str(bezugshoehe)+r'}{\meter}$ &  Bezugshöhe \\ '))
    doc.append(NoEscape(r'Ort:& '+ str(ort)+r'& $ v_{b,0}=$&$\SI{'+ str(windgeschwindigkeit)+r'}{\meter\per\second}$ & Basiswindgeschwindigkeit \\ '))
    doc.append(NoEscape(r'Geländekategorie:& ' + str(gelaendekategorie)+r'& $q_{b,0}=$&$\SI{'+ str(basiswinddruck)+r'}{\kilo\newton\per\square\meter} $ & Basisgeschwindigkeitsdruck'))
    if winddruck_benutzerdefiniert ==True:
         doc.append(NoEscape(r'(vom Benutzer definiert)'))
    doc.append(NoEscape(r'\\ & & $q_p =$&$\SI{'+ str(qp)+ r'}{\kilo\newton\per\square\meter}$ & Spitzengeschwindigkeitsdruck '))
    doc.append(NoEscape(r'\\ & & $H =$&$\SI{'+ str(seehoehe)+r'}{\meter} $&  Seehöhe '))
    if seehoehe_benutzerdefiniert ==True:
         doc.append(NoEscape(r'(vom Benutzer definiert)'))
    doc.append(NoEscape(r'\\ & & $f_s =$&$\SI{'+ str(abminderungsfaktor)+r'}{}$ &    Abminderungsfaktor für Basiswindgeschwindigkeitsdrücke '))
    doc.append(NoEscape(r'\end{tabular}'))
    doc.append(NoEscape(r'\end{table}'))

def geometrische_angaben_pultdach(self,doc,arg_latex):
    hoehe = self.pultdach.hoehe
    dachneigung = self.pultdach.dachneigung
    breite_x = self.pultdach.breite_x
    breite_y = self.pultdach.breite_y
    vereinfachtes_verfahren = self.pultdach.verfahren_wahl


    doc.append(NoEscape(r'\subsubsection*{Geometrische Angaben}'))
    doc.append(NoEscape(r'\begin{table}[h]'))
    doc.append(NoEscape(r'\centering'))
    doc.append(NoEscape(r'\begin{tabular}{R{1.5cm}  @{ }L{2.0cm} @{ \dots} L{3.14cm}  R{1.5cm}  @{ }L{2.0cm} @{ \dots} L{5.25cm}}'))
    doc.append(NoEscape(r'$h =$&\SI{'+ str(hoehe)+r'}{\meter}  &  Höhe &'))
    doc.append(NoEscape(r'$b_x =$&$\SI{'+ str(breite_x)+r'}{\meter}$  &	 Breite in +X \\'))
    doc.append(NoEscape(r'$\alpha=$&$\ang{'+ str(dachneigung)+r'}$  & Dachneigung &'))
    doc.append(NoEscape(r'$b_y =$&$\SI{'+ str(breite_y)+r'}{\meter}$ & Breite in +Y '))
    doc.append(NoEscape(r'\end{tabular}'))
    doc.append(NoEscape(r'\end{table}'))

def nur_aussendruck(self,doc,arg_latex):


    ergebnisse_pultdach =  arg_latex['ergebnisse_pultdach']
    ergebnisse_we_gerundet=ergebnisse_pultdach['ergebnisse_we_gerundet']

    we_f_neg_0_ergebnis = ergebnisse_we_gerundet['we_f_neg_0_ergebnis']
    we_g_neg_0_ergebnis = ergebnisse_we_gerundet['we_g_neg_0_ergebnis']
    we_h_neg_0_ergebnis = ergebnisse_we_gerundet['we_h_neg_0_ergebnis']
    we_f_pos_0_ergebnis = ergebnisse_we_gerundet['we_f_pos_0_ergebnis']
    we_g_pos_0_ergebnis = ergebnisse_we_gerundet['we_g_pos_0_ergebnis']
    we_h_pos_0_ergebnis = ergebnisse_we_gerundet['we_h_pos_0_ergebnis']

    we_f_neg_180_ergebnis = ergebnisse_we_gerundet['we_f_neg_180_ergebnis']
    we_g_neg_180_ergebnis = ergebnisse_we_gerundet['we_g_neg_180_ergebnis']
    we_h_neg_180_ergebnis = ergebnisse_we_gerundet['we_h_neg_180_ergebnis']

    we_f_hoch_neg_90_ergebnis = ergebnisse_we_gerundet['we_f_hoch_neg_90_ergebnis']
    we_f_tief_neg_90_ergebnis = ergebnisse_we_gerundet['we_f_tief_neg_90_ergebnis']

    we_g_neg_90_ergebnis = ergebnisse_we_gerundet['we_g_neg_90_ergebnis']
    we_h_neg_90_ergebnis = ergebnisse_we_gerundet['we_h_neg_90_ergebnis']
    we_i_neg_90_ergebnis = ergebnisse_we_gerundet['we_i_neg_90_ergebnis']

    ergebnisse_cpe_gerundet = ergebnisse_pultdach['ergebnisse_cpe_gerundet']

    cpe_f_neg_0_ergebnis = ergebnisse_cpe_gerundet['cpe_f_neg_0_ergebnis']
    cpe_g_neg_0_ergebnis = ergebnisse_cpe_gerundet['cpe_g_neg_0_ergebnis']
    cpe_h_neg_0_ergebnis = ergebnisse_cpe_gerundet['cpe_h_neg_0_ergebnis']
    cpe_f_pos_0_ergebnis = ergebnisse_cpe_gerundet['cpe_f_pos_0_ergebnis']
    cpe_g_pos_0_ergebnis = ergebnisse_cpe_gerundet['cpe_g_pos_0_ergebnis']
    cpe_h_pos_0_ergebnis = ergebnisse_cpe_gerundet['cpe_h_pos_0_ergebnis']

    cpe_f_neg_180_ergebnis = ergebnisse_cpe_gerundet['cpe_f_neg_180_ergebnis']
    cpe_g_neg_180_ergebnis = ergebnisse_cpe_gerundet['cpe_g_neg_180_ergebnis']
    cpe_h_neg_180_ergebnis = ergebnisse_cpe_gerundet['cpe_h_neg_180_ergebnis']

    cpe_f_hoch_neg_90_ergebnis = ergebnisse_cpe_gerundet['cpe_f_hoch_neg_90_ergebnis']
    cpe_f_tief_neg_90_ergebnis = ergebnisse_cpe_gerundet['cpe_f_tief_neg_90_ergebnis']

    cpe_g_neg_90_ergebnis = ergebnisse_cpe_gerundet['cpe_g_neg_90_ergebnis']
    cpe_h_neg_90_ergebnis = ergebnisse_cpe_gerundet['cpe_h_neg_90_ergebnis']
    cpe_i_neg_90_ergebnis = ergebnisse_cpe_gerundet['cpe_i_neg_90_ergebnis']



    doc.append(NoEscape(r'\subsubsection*{Außendruckbeiwerte}'))
    doc.append(NoEscape(r'\begin{table}[hb]'))
    doc.append(NoEscape(r'	\begin{tabular}{ C{.3\textwidth}  C{.3\textwidth} C{.3\textwidth}}'))
    doc.append(NoEscape(r'	$\theta = \ang{0}$ & $\theta = \ang{90}$ & $\theta = \ang{180}$ \\'))

    doc.append(NoEscape(r'	$	\begin{aligned}'))
    doc.append(NoEscape(r'	c_{pe,F}&= \SI{'+ str(cpe_f_pos_0_ergebnis)+r'}{} \\ '))
    doc.append(NoEscape(r'	c_{pe,F}&= \SI{'+ str(cpe_f_neg_0_ergebnis)+r'}{} \\ '))
    doc.append(NoEscape(r'	c_{pe,G}&=\SI{'+ str(cpe_g_pos_0_ergebnis)+r'}{}    \\'))
    doc.append(NoEscape(r'	c_{pe,G}&=\SI{'+ str(cpe_g_neg_0_ergebnis)+r'}{}    \\'))
    doc.append(NoEscape(r'c_{pe,H}&=\SI{'+ str(cpe_h_pos_0_ergebnis)+r'}{}   \\'))
    doc.append(NoEscape(r'c_{pe,H}&=\SI{'+ str(cpe_h_neg_0_ergebnis)+r'}{}   \\'))



    doc.append(NoEscape(r'		\end{aligned}		$'))
    ##################################
    doc.append(NoEscape(r'	&'))

    doc.append(NoEscape(r'		$\begin{aligned}'))
    doc.append(NoEscape(r'		c_{pe,F,Hoch}&= \SI{'+ str(cpe_f_hoch_neg_90_ergebnis)+r'}{} \\'))
    doc.append(NoEscape(r'		c_{pe,F,Tief}&= \SI{'+ str(cpe_f_tief_neg_90_ergebnis)+r'}{} \\'))
    doc.append(NoEscape(r'	    c_{pe,G}&=\SI{'+ str(cpe_g_neg_90_ergebnis)+r'}{}  \\'))
    doc.append(NoEscape(r'		c_{pe,H}&=\SI{'+ str(cpe_h_neg_90_ergebnis)+r'}{}  \\'))
    doc.append(NoEscape(r'		c_{pe,I}&=\SI{'+ str(cpe_i_neg_90_ergebnis)+r'}{} \\'))
    doc.append(NoEscape(r'		\end{aligned}		$'))
    ####################################
    doc.append(NoEscape(r'	&'))
#######################
    doc.append(NoEscape(r'		$\begin{aligned}'))
    doc.append(NoEscape(r'	     c_{pe,F}&= \SI{'+ str(cpe_f_neg_180_ergebnis)+r'}{} \\ '))
    doc.append(NoEscape(r'	     c_{pe,G}&=\SI{'+ str(cpe_g_neg_180_ergebnis)+r'}{}    \\'))
    doc.append(NoEscape(r'      c_{pe,H}&=\SI{'+ str(cpe_h_neg_180_ergebnis)+r'}{}   \\'))
    doc.append(NoEscape(r'		\end{aligned}		$'))
######################################
    #aussenwinddruck(self,doc,arg_latex)
    doc.append(NoEscape(r'\end{tabular}'))
    doc.append(NoEscape(r'\end{table}'))
    doc.append(NoEscape(r'\subsubsection*{Außenwinddruck}'))

    doc.append(NoEscape(r'\begin{table}[h!]'))
    doc.append(NoEscape(r'	\begin{tabular}{ C{.3\textwidth}  C{.3\textwidth} C{.3\textwidth}}'))
    doc.append(NoEscape(r'	$\theta = \ang{0}$ & $\theta = \ang{90}$ & $\theta = \ang{180}$ \\'))

    doc.append(NoEscape(r'	$	\begin{aligned}'))
    doc.append(NoEscape(r'	w_{e,F}&= \SI{'+ str(we_f_pos_0_ergebnis)+r'}{\kilo\newton\per\square\meter} \\ '))
    doc.append(NoEscape(r'	w_{e,F}&= \SI{'+ str(we_f_neg_0_ergebnis)+r'}{\kilo\newton\per\square\meter} \\ '))
    doc.append(NoEscape(r'	w_{e,G}&=\SI{'+ str(we_g_pos_0_ergebnis)+r'}{\kilo\newton\per\square\meter}    \\'))
    doc.append(NoEscape(r'	w_{e,G}&=\SI{'+ str(we_g_neg_0_ergebnis)+r'}{\kilo\newton\per\square\meter}    \\'))
    doc.append(NoEscape(r'w_{e,H}&=\SI{'+ str(we_h_pos_0_ergebnis)+r'}{\kilo\newton\per\square\meter}   \\'))
    doc.append(NoEscape(r'w_{e,H}&=\SI{'+ str(we_h_neg_0_ergebnis)+r'}{\kilo\newton\per\square\meter}   \\'))



    doc.append(NoEscape(r'		\end{aligned}		$'))
    ##################################
    doc.append(NoEscape(r'	&'))

    doc.append(NoEscape(r'		$\begin{aligned}'))
    doc.append(NoEscape(r'		w_{e,F,Hoch}&= \SI{'+ str(we_f_hoch_neg_90_ergebnis)+r'}{\kilo\newton\per\square\meter} \\'))
    doc.append(NoEscape(r'		w_{e,F,Tief}&= \SI{'+ str(we_f_tief_neg_90_ergebnis)+r'}{\kilo\newton\per\square\meter} \\'))
    doc.append(NoEscape(r'	    w_{e,G}&=\SI{'+ str(we_g_neg_90_ergebnis)+r'}{\kilo\newton\per\square\meter}  \\'))
    doc.append(NoEscape(r'		w_{e,H}&=\SI{'+ str(we_h_neg_90_ergebnis)+r'}{\kilo\newton\per\square\meter}  \\'))
    doc.append(NoEscape(r'		w_{e,I}&=\SI{'+ str(we_i_neg_90_ergebnis)+r'}{\kilo\newton\per\square\meter} \\'))
    doc.append(NoEscape(r'		\end{aligned}		$'))
    ####################################
    doc.append(NoEscape(r'	&'))
#######################
    doc.append(NoEscape(r'		$\begin{aligned}'))
    doc.append(NoEscape(r'	     w_{e,F}&= \SI{'+ str(we_f_neg_180_ergebnis)+r'}{\kilo\newton\per\square\meter} \\ '))
    doc.append(NoEscape(r'	     w_{e,G}&=\SI{'+ str(we_g_neg_180_ergebnis)+r'}{\kilo\newton\per\square\meter}    \\'))
    doc.append(NoEscape(r'      w_{e,H}&=\SI{'+ str(we_h_neg_180_ergebnis)+r'}{\kilo\newton\per\square\meter}   \\'))
    doc.append(NoEscape(r'		\end{aligned}		$'))
######################################
    #aussenwinddruck(self,doc,arg_latex)
    doc.append(NoEscape(r'\end{tabular}'))
    doc.append(NoEscape(r'\end{table}'))


    if self.pultdach.innendruck == False:
        doc.append(NoEscape(r'In den Ergebnissen stehen alle positiven Werte für Winddruck und die Negativen für Windsog. '))
    doc.append(NoEscape(r'\noindent'))

def aussendruck_und_innendruck(self,doc,arg_latex):

    innendruck_verfahren_wahl = self.pultdach.innendruck_verfahren_wahl
    #innendruck_berechnen_gerundet
    #
    ergebnisse_pultdach =  arg_latex['ergebnisse_pultdach']
    sonstige_werte_berechnet=ergebnisse_pultdach['sonstige_werte_berechnet_gerundet']
    innendruck_berechnen_gerundet = ergebnisse_pultdach['innendruck_berechnen_gerundet']
    print(innendruck_berechnen_gerundet)
    cpi_druck = innendruck_berechnen_gerundet['cpi_druck']
    cpi_sog = innendruck_berechnen_gerundet['cpi_sog']
    wi_druck = innendruck_berechnen_gerundet['wi_druck']
    wi_sog = innendruck_berechnen_gerundet['wi_sog']

    cpi_1_y = innendruck_berechnen_gerundet['cpi_1_y']
    cpi_1_x = innendruck_berechnen_gerundet['cpi_1_x']
    wi_f_y = innendruck_berechnen_gerundet['wi_f_y']
    wi_f_x = innendruck_berechnen_gerundet['wi_f_x']
    endergebnisse_ueberlagert_gerundet = ergebnisse_pultdach['endergebnisse_ueberlagert_gerundet']
    #print(endergebnisse_ueberlagert_gerundet)
    wf_druck_0_ges = endergebnisse_ueberlagert_gerundet['wf_druck_0_ges']
    wg_druck_0_ges = endergebnisse_ueberlagert_gerundet['wg_druck_0_ges']
    wh_druck_0_ges = endergebnisse_ueberlagert_gerundet['wh_druck_0_ges']

    wf_sog_0_ges = endergebnisse_ueberlagert_gerundet['wf_sog_0_ges']

    wg_sog_0_ges = endergebnisse_ueberlagert_gerundet['wg_sog_0_ges']
    wh_sog_0_ges = endergebnisse_ueberlagert_gerundet['wh_sog_0_ges']

    wf_sog_180_ges = endergebnisse_ueberlagert_gerundet['wf_sog_180_ges']
    wg_sog_180_ges = endergebnisse_ueberlagert_gerundet['wg_sog_180_ges']
    wh_sog_180_ges = endergebnisse_ueberlagert_gerundet['wh_sog_180_ges']

    wf_hoch_sog_90_ges = endergebnisse_ueberlagert_gerundet['wf_hoch_sog_90_ges']
    wf_tief_sog_90_ges = endergebnisse_ueberlagert_gerundet['wf_tief_sog_90_ges']

    wg_sog_90_ges = endergebnisse_ueberlagert_gerundet['wg_sog_90_ges']
    wh_sog_90_ges = endergebnisse_ueberlagert_gerundet['wh_sog_90_ges']
    wi_sog_90_ges = endergebnisse_ueberlagert_gerundet['wi_sog_90_ges']


    doc.append(NoEscape(r'\subsubsection*{Innendruckbeiwerte}'))
    doc.append(NoEscape(r'\begin{table}[h!]'))
    doc.append(NoEscape(r'	\begin{tabular}{ C{.3\textwidth}  C{.3\textwidth} C{.3\textwidth}}'))
    doc.append(NoEscape(r'	$	\begin{aligned}'))
    if innendruck_verfahren_wahl == 'Innendruckbeiwerte mittels empfohlener Werte nach Abschnitt 9.2.10':
        doc.append(NoEscape(r'	c_{pi}&= \SI{'+ str(cpi_druck)+r'}{} \\ '))
        doc.append(NoEscape(r'	c_{pi}&= \SI{'+ str(cpi_sog)+r'}{} \\ '))

    elif innendruck_verfahren_wahl == 'Innendruckbeiwerte mittels dominanter Fläche nach Abschnitt 7.2.9':
        doc.append(NoEscape(r'	c_{pi}&= \SI{'+ str(cpi_druck)+r'}{} \\ '))
    elif innendruck_verfahren_wahl == 'Innendruckbeiwerte mittels Flächenparameter nach Abschnitt 7.2.9':
        doc.append(NoEscape(r'	c_{pi,y}&= \SI{'+ str(cpi_1_y)+r'}{} \\ '))
        doc.append(NoEscape(r'	c_{pi,x}&= \SI{'+ str(cpi_1_x)+r'}{} \\ '))



    doc.append(NoEscape(r'		\end{aligned}		$'))
    ##################################
    doc.append(NoEscape(r'	&'))
    doc.append(NoEscape(r'		$\begin{aligned}'))
    if innendruck_verfahren_wahl == 'Innendruckbeiwerte mittels empfohlener Werte nach Abschnitt 9.2.10':
        doc.append(NoEscape(r'	w_{i}&= \SI{'+ str(wi_druck)+r'}{\kilo\newton\per\square\meter} \\ '))
        doc.append(NoEscape(r'	w_{i}&= \SI{'+ str(wi_sog)+r'}{\kilo\newton\per\square\meter} \\ '))
    elif innendruck_verfahren_wahl == 'Innendruckbeiwerte mittels dominanter Fläche nach Abschnitt 7.2.9':
        doc.append(NoEscape(r'	w_{i}&= \SI{'+ str(wi_druck)+r'}{\kilo\newton\per\square\meter} \\ '))
    elif innendruck_verfahren_wahl == 'Innendruckbeiwerte mittels Flächenparameter nach Abschnitt 7.2.9':
        doc.append(NoEscape(r'	w_{i,y}&= \SI{'+ str(wi_f_y)+r'}{\kilo\newton\per\square\meter} \\ '))
        doc.append(NoEscape(r'	w_{i,x}&= \SI{'+ str(wi_f_x)+r'}{\kilo\newton\per\square\meter} \\ '))
    doc.append(NoEscape(r'		\end{aligned}		$'))
    ####################################
    doc.append(NoEscape(r'	&'))
#######################
    doc.append(NoEscape(r'		$\begin{aligned}'))
    doc.append(NoEscape(r'		\end{aligned}		$'))
######################################
    #aussenwinddruck(self,doc,arg_latex)
    doc.append(NoEscape(r'\end{tabular}'))
    doc.append(NoEscape(r'\end{table}'))
    doc.append(NoEscape(r'\subsubsection*{Überlagerung}'))
    doc.append(NoEscape(r'\begin{table}[h]'))
    doc.append(NoEscape(r'	\begin{tabular}{ C{.3\textwidth}  C{.3\textwidth} C{.3\textwidth}}'))
    doc.append(NoEscape(r'	$\theta = \ang{0}$ & $\theta = \ang{90}$ & $\theta = \ang{180}$ \\'))
    doc.append(NoEscape(r'	$	\begin{aligned}'))
    doc.append(NoEscape(r'	w_{F}&= \SI{'+ str(wf_druck_0_ges)+r'}{\kilo\newton\per\square\meter} \\ '))
    doc.append(NoEscape(r'	w_{F}&= \SI{'+ str(wf_sog_0_ges)+r'}{\kilo\newton\per\square\meter} \\ '))
    doc.append(NoEscape(r'	w_{G}&=\SI{'+ str(wg_druck_0_ges)+r'}{\kilo\newton\per\square\meter}    \\'))
    doc.append(NoEscape(r'	w_{G}&=\SI{'+ str(wg_sog_0_ges)+r'}{\kilo\newton\per\square\meter}    \\'))
    doc.append(NoEscape(r'w_{H}&=\SI{'+ str(wh_druck_0_ges)+r'}{\kilo\newton\per\square\meter}   \\'))
    doc.append(NoEscape(r'w_{H}&=\SI{'+ str(wh_sog_0_ges)+r'}{\kilo\newton\per\square\meter}   \\'))
    doc.append(NoEscape(r'		\end{aligned}		$'))
    ##################################
    doc.append(NoEscape(r'	&'))
    doc.append(NoEscape(r'		$\begin{aligned}'))
    doc.append(NoEscape(r'		w_{F,Hoch}&= \SI{'+ str(wf_hoch_sog_90_ges)+r'}{\kilo\newton\per\square\meter} \\'))
    doc.append(NoEscape(r'		w_{F,Tief}&= \SI{'+ str(wf_tief_sog_90_ges)+r'}{\kilo\newton\per\square\meter} \\'))
    doc.append(NoEscape(r'	    w_{G}&=\SI{'+ str(wg_sog_90_ges)+r'}{\kilo\newton\per\square\meter}  \\'))
    doc.append(NoEscape(r'		w_{H}&=\SI{'+ str(wh_sog_90_ges)+r'}{\kilo\newton\per\square\meter}  \\'))
    doc.append(NoEscape(r'		w_{I}&=\SI{'+ str(wi_sog_90_ges)+r'}{\kilo\newton\per\square\meter} \\'))
    doc.append(NoEscape(r'		\end{aligned}		$'))
    ####################################
    doc.append(NoEscape(r'	&'))
#######################
    doc.append(NoEscape(r'		$\begin{aligned}'))
    doc.append(NoEscape(r'	     w_{F}&= \SI{'+ str(wf_sog_180_ges)+r'}{\kilo\newton\per\square\meter} \\ '))
    doc.append(NoEscape(r'	     w_{G}&=\SI{'+ str(wg_sog_180_ges)+r'}{\kilo\newton\per\square\meter}    \\'))
    doc.append(NoEscape(r'      w_{H}&=\SI{'+ str(wh_sog_180_ges)+r'}{\kilo\newton\per\square\meter}   \\'))
    doc.append(NoEscape(r'		\end{aligned}		$'))
######################################
    #aussenwinddruck(self,doc,arg_latex)
    doc.append(NoEscape(r'\end{tabular}'))
    doc.append(NoEscape(r'\end{table}'))
    doc.append(NoEscape(r'\noindent'))
    doc.append(NoEscape(r'In den Ergebnissen stehen alle positiven Werte für Winddruck und die Negativen für Windsog. '))
