import os
from pylatex import Document, Section, Subsection, Command,Figure,TikZ, TikZNode, TikZDraw, TikZCoordinate, TikZUserPath, TikZOptions,Package
from pylatex.utils import italic, NoEscape
from latex import build_pdf

from gesamt_pdf_app.models import GesamtPdf
from django.forms.models import model_to_dict



def nur_aussendruck_na(self,doc,arg_latex):


    ergebnisse_pultdach =  arg_latex['ergebnisse_pultdach']
    ergebnisse_we_gerundet=ergebnisse_pultdach['ergebnisse_we_gerundet']


    we_f_und_g_neg_ergebnis = ergebnisse_we_gerundet['we_f_und_g_neg_ergebnis']
    we_f_und_g_pos_ergebnis = ergebnisse_we_gerundet['we_f_und_g_pos_ergebnis']
    we_h_und_i_neg_ergebnis = ergebnisse_we_gerundet['we_h_und_i_neg_ergebnis']
    we_h_und_i_pos_ergebnis = ergebnisse_we_gerundet['we_h_und_i_pos_ergebnis']


    ergebnisse_cpe_gerundet = ergebnisse_pultdach['ergebnisse_cpe_gerundet']


    cpe_f_und_g_neg_ergebnis = ergebnisse_cpe_gerundet['cpe_f_und_g_neg_ergebnis']
    cpe_f_und_g_pos_ergebnis = ergebnisse_cpe_gerundet['cpe_f_und_g_pos_ergebnis']
    cpe_h_und_i_neg_ergebnis = ergebnisse_cpe_gerundet['cpe_h_und_i_neg_ergebnis']
    cpe_h_und_i_pos_ergebnis = ergebnisse_cpe_gerundet['cpe_h_und_i_pos_ergebnis']





    doc.append(NoEscape(r'\subsubsection*{Außendruckbeiwerte}'))
    doc.append(NoEscape(r'\begin{table}[hb]'))
    doc.append(NoEscape(r'	\begin{tabular}{ C{.3\textwidth}  C{.3\textwidth} C{.3\textwidth}}'))


    doc.append(NoEscape(r'	$	\begin{aligned}'))
    doc.append(NoEscape(r'	c_{pe,F}&= \SI{'+ str(cpe_f_und_g_pos_ergebnis)+r'}{} \\ '))
    doc.append(NoEscape(r'	c_{pe,F}&= \SI{'+ str(cpe_f_und_g_neg_ergebnis)+r'}{} \\ '))
    doc.append(NoEscape(r'	c_{pe,G}&=\SI{'+ str(cpe_f_und_g_pos_ergebnis)+r'}{}    \\'))
    doc.append(NoEscape(r'	c_{pe,G}&=\SI{'+ str(cpe_f_und_g_neg_ergebnis)+r'}{}    \\'))
    doc.append(NoEscape(r'c_{pe,H}&=\SI{'+ str(cpe_h_und_i_pos_ergebnis)+r'}{}   \\'))
    doc.append(NoEscape(r'c_{pe,H}&=\SI{'+ str(cpe_h_und_i_neg_ergebnis)+r'}{}   \\'))
    doc.append(NoEscape(r'c_{pe,I}&=\SI{'+ str(cpe_h_und_i_pos_ergebnis)+r'}{}   \\'))
    doc.append(NoEscape(r'c_{pe,I}&=\SI{'+ str(cpe_h_und_i_neg_ergebnis)+r'}{}   \\'))



    doc.append(NoEscape(r'		\end{aligned}		$'))
    ##################################
    doc.append(NoEscape(r'	&'))

    doc.append(NoEscape(r'		$\begin{aligned}'))

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
    doc.append(NoEscape(r'\subsubsection*{Außenwinddruck}'))

    doc.append(NoEscape(r'\begin{table}[h!]'))
    doc.append(NoEscape(r'	\begin{tabular}{ C{.3\textwidth}  C{.3\textwidth} C{.3\textwidth}}'))


    doc.append(NoEscape(r'	$	\begin{aligned}'))
    doc.append(NoEscape(r'	w_{e,F}&= \SI{'+ str(we_f_und_g_pos_ergebnis)+r'}{\kilo\newton\per\square\meter} \\ '))
    doc.append(NoEscape(r'	w_{e,F}&= \SI{'+ str(we_f_und_g_neg_ergebnis)+r'}{\kilo\newton\per\square\meter} \\ '))
    doc.append(NoEscape(r'	w_{e,G}&=\SI{'+ str(we_f_und_g_pos_ergebnis)+r'}{\kilo\newton\per\square\meter}    \\'))
    doc.append(NoEscape(r'	w_{e,G}&=\SI{'+ str(we_f_und_g_neg_ergebnis)+r'}{\kilo\newton\per\square\meter}    \\'))
    doc.append(NoEscape(r'w_{e,H}&=\SI{'+ str(we_h_und_i_pos_ergebnis)+r'}{\kilo\newton\per\square\meter}   \\'))
    doc.append(NoEscape(r'w_{e,H}&=\SI{'+ str(we_h_und_i_neg_ergebnis)+r'}{\kilo\newton\per\square\meter}   \\'))
    doc.append(NoEscape(r'w_{e,I}&=\SI{'+ str(we_h_und_i_pos_ergebnis)+r'}{\kilo\newton\per\square\meter}   \\'))
    doc.append(NoEscape(r'w_{e,I}&=\SI{'+ str(we_h_und_i_neg_ergebnis)+r'}{\kilo\newton\per\square\meter}   \\'))



    doc.append(NoEscape(r'		\end{aligned}		$'))
    ##################################
    doc.append(NoEscape(r'	&'))

    doc.append(NoEscape(r'		$\begin{aligned}'))

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


    if self.pultdach.innendruck == False:
        doc.append(NoEscape(r'In den Ergebnissen stehen alle positiven Werte für Winddruck und die Negativen für Windsog. '))
    doc.append(NoEscape(r'\noindent'))

def aussendruck_und_innendruck_na(self,doc,arg_latex):

    innendruck_verfahren_wahl = self.pultdach.innendruck_verfahren_wahl
    #innendruck_berechnen_gerundet
    #
    ergebnisse_pultdach =  arg_latex['ergebnisse_pultdach']
    sonstige_werte_berechnet=ergebnisse_pultdach['sonstige_werte_berechnet_gerundet']
    innendruck_berechnen_gerundet = ergebnisse_pultdach['innendruck_berechnen_gerundet']

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
    cp_f_und_g_druck_ges = endergebnisse_ueberlagert_gerundet['cp_f_und_g_druck_ges']
    cp_h_und_i_druck_ges = endergebnisse_ueberlagert_gerundet['cp_h_und_i_druck_ges']

    cp_f_und_g_sog_ges = endergebnisse_ueberlagert_gerundet['cp_f_und_g_sog_ges']
    cp_h_und_i_sog_ges = endergebnisse_ueberlagert_gerundet['cp_h_und_i_sog_ges']

    w_f_und_g_druck_ges = endergebnisse_ueberlagert_gerundet['w_f_und_g_druck_ges']
    w_h_und_i_druck_ges = endergebnisse_ueberlagert_gerundet['w_h_und_i_druck_ges']

    w_f_und_g_sog_ges = endergebnisse_ueberlagert_gerundet['w_f_und_g_sog_ges']
    w_h_und_i_sog_ges = endergebnisse_ueberlagert_gerundet['w_h_und_i_sog_ges']



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
    if self.pultdach.verfahren_wahl =='Vereinfachtes Verfahren gemäß ÖNORM B 1991-1-4, Abschnitt 9.2.4.1':
        doc.append(NoEscape(r'	\text{Es wird mit dem betragsmäßig größerem Wert überlagert.} \\ '))
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

    doc.append(NoEscape(r'	$	\begin{aligned}'))
    doc.append(NoEscape(r'	    w_{F}&= \SI{'+ str(w_f_und_g_druck_ges)+r'}{\kilo\newton\per\square\meter} \\ '))
    doc.append(NoEscape(r'	    w_{F}&= \SI{'+ str(w_f_und_g_sog_ges)+r'}{\kilo\newton\per\square\meter} \\ '))
    doc.append(NoEscape(r'	    w_{G}&=\SI{'+ str(w_f_und_g_druck_ges)+r'}{\kilo\newton\per\square\meter}    \\'))
    doc.append(NoEscape(r'	    w_{G}&=\SI{'+ str(w_f_und_g_sog_ges)+r'}{\kilo\newton\per\square\meter}    \\'))
    doc.append(NoEscape(r'      w_{H}&=\SI{'+ str(w_h_und_i_druck_ges)+r'}{\kilo\newton\per\square\meter}   \\'))
    doc.append(NoEscape(r'      w_{H}&=\SI{'+ str(w_h_und_i_sog_ges)+r'}{\kilo\newton\per\square\meter}   \\'))
    doc.append(NoEscape(r'		w_{I}&=\SI{'+ str(w_h_und_i_druck_ges)+r'}{\kilo\newton\per\square\meter} \\'))
    doc.append(NoEscape(r'		w_{I}&=\SI{'+ str(w_h_und_i_sog_ges)+r'}{\kilo\newton\per\square\meter} \\'))
    doc.append(NoEscape(r'		\end{aligned}		$'))
    ##################################
    doc.append(NoEscape(r'	&'))
    doc.append(NoEscape(r'		$\begin{aligned}'))

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
    doc.append(NoEscape(r'\noindent'))
    doc.append(NoEscape(r'In den Ergebnissen stehen alle positiven Werte für Winddruck und die Negativen für Windsog. '))
