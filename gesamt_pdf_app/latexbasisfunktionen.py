import os
import io
import subprocess
import os.path as path



def latexwasserzeichen(fd):


    fd.write("\n"+r'\usepackage{draftwatermark}')
    fd.write("\n"+r'\SetWatermarkText{Demoversion}')
    fd.write("\n"+r'\SetWatermarkScale{1}')
    fd.write("\n"+r'\SetWatermarkColor[rgb]{0.8,0,0}')
    fd.write("\n"+r'\SetWatermarkAngle{50}')


def preamble_static_latex(self,fd):
    BASE_DIR = os.path.dirname(os.path.abspath(path.join(__file__ ,"../")))
    #D:\Desktop\accountneu\gesamt_pdf_app\static\gesamt_pdf_app\preamble
    #muss als aller erstes stehen
    preamble_filename_python=BASE_DIR+"/gesamt_pdf_app/static/gesamt_pdf_app/preamble/preamble"
    preamble_filename_latex=preamble_filename_python.replace("\\", "/")
    fd.write(r'%&'+preamble_filename_latex)
    #fd.write("\n"+r'%&latex')
    fd.write("\n"+r'\csname endofdump\endcsname') #Bestimmt das ende der Statischen Preamble
    fd.write("\n"+r'\pdfcompresslevel=0') #Macht das compilieren schneller erzeugt jedoch ein größeres pdf
    fd.write("\n"+r'\pdfobjcompresslevel=0') #Macht das compilieren schneller erzeugt jedoch ein größeres pdf
    fd.write("\n"+r'\setlength\intextsep{2.0mm}')





def beginn_latex_format(fd,):
    #Steht direct nach beginn Document
    #eigene Tabellenart für tabularx
    fd.write("\n"+r'\newcolumntype{D}[1]{>{\setlength\hsize{#1\hsize}\raggedleft\arraybackslash}X}') #rechtsbündig
    fd.write("\n"+r'\newcolumntype{B}[1]{>{\setlength\hsize{#1\hsize}\centering\arraybackslash}X}')#centriert
    fd.write("\n"+r'\newcolumntype{A}[1]{>{\setlength\hsize{#1\hsize}\raggedright\arraybackslash}X}') #Linksbündig
    fd.write("\n"+r'\AddToShipoutPicture{\BackgroundStructure}') # Set the background of each page to that specified above in the header information section
    fd.write("\n"+r'\begin{paracol}{2}') #Teilt das document in zwei spalten








def kopfundfusszeile_einzeln(fd,arg_latex):
    fd.write("\n"+r'\fancyhead[L]{\begin{tabular}{l r | l r}')
    fd.write("\n"+r'	\textbf{Projekt}') # eintrag 1
    fd.write("\n"+r' &  &')
    fd.write("\n"+r'\textbf{Seite} & \thepage') # eintrag 2 Seitenzahl
    fd.write("\n"+r'\\[-4pt]')
    fd.write("\n"+r'\textbf{Bauteil}   & Wand') #eintrag 3 Bauteil
    fd.write("\n"+r'&')
    fd.write("\n"+r'\textbf{Datum} & \today') # eintrag 4 Datum
    fd.write("\n"+r'\\[-4pt]')
    fd.write("\n"+r'\textbf{Bauteilart} & Freistehende Wand') # eintrag 5 Bauteilart
    fd.write("\n"+r'&')
    fd.write("\n"+r'\textbf{Firma} & Musterman GMBH')  # eintrag 6 Bauteilart
    fd.write("\n"+r'\\[-4pt]')
    fd.write("\n"+r'&  &')#eintrag 7 nichts
    fd.write("\n"+r'\textbf{Bearbeiter} & James Smith')#eintrag 8 Bearbeiter
    fd.write("\n"+r'\end{tabular}}')

def kopfundfusszeile(fd,arg_latex):
    fd.write("\n"+r'\fancyhead[L]{\begin{tabular}{l r | l r}')
    fd.write("\n"+r'	\textbf{Projekt}') # eintrag 1
    fd.write("\n"+r' &  &')
    fd.write("\n"+r'\textbf{Seite} & \thepage/\pageref{LastPage}') # eintrag 2 Seitenzahl
    fd.write("\n"+r'\\[-4pt]')
    fd.write("\n"+r'\textbf{Bauteil}   & Wand') #eintrag 3 Bauteil
    fd.write("\n"+r'&')
    fd.write("\n"+r'\textbf{Datum} & \today') # eintrag 4 Datum
    fd.write("\n"+r'\\[-4pt]')
    fd.write("\n"+r'\textbf{Bauteilart} & Freistehende Wand') # eintrag 5 Bauteilart
    fd.write("\n"+r'&')
    fd.write("\n"+r'\textbf{Firma} & Musterman GMBH')  # eintrag 6 Bauteilart
    fd.write("\n"+r'\\[-4pt]')
    fd.write("\n"+r'&  &')#eintrag 7 nichts
    fd.write("\n"+r'\textbf{Bearbeiter} & James Smith')#eintrag 8 Bearbeiter
    fd.write("\n"+r'\end{tabular}}')

def kopfundfusszeile_1(fd,arg_latex):
    fd.write("\n"+r'\fancyhead[L]{\begin{tabular}{l r | l r}')
    fd.write("\n"+r'	\textbf{Projekt}') # eintrag 1
    fd.write("\n"+r' & Beispielprojekt &')
    fd.write("\n"+r'\textbf{Seite} & \thepage') # eintrag 2 Seitenzahl
    fd.write("\n"+r'\\[-4pt]')
    fd.write("\n"+r'\textbf{Firma}   & Musterman GMBH') #eintrag 3 Bauteil
    fd.write("\n"+r'&')
    fd.write("\n"+r'\textbf{Datum} & \today') # eintrag 4 Datum
    fd.write("\n"+r'\\[-4pt]')
    fd.write("\n"+r'\textbf{Bearbeiter} & James Smith') # eintrag 5 Bauteilart
    fd.write("\n"+r'\end{tabular}}')



def input_latex(fd,dateiname):
    dateiname_latex=dateiname.replace("\\", "/")
    fd.write("\n"+r'\input{'+ dateiname_latex +r'}')

def compiling(self,media_path,my_path_ausdruckprotokoll):
    #batchmode unterdrückt die fehlermeldungen und macht es schneller
    #ohne fehlermeldung
    # subprocess.check_call(['pdflatex','-output-directory',media_path,'-interaction','batchmode', my_path_ausdruckprotokoll])
    #mit fehlermeldung
    subprocess.check_call(['pdflatex','-output-directory',media_path, my_path_ausdruckprotokoll])

    # subprocess.check_call(['pdflatex','-output-directory',media_path, my_path_ausdruckprotokoll], shell=True)


    #subprocess.check_call(['pdflatex','-output-format=dvi', my_path_ausdruckprotokoll])
    #subprocess.check_call(['latex', my_path_ausdruckprotokoll])
    #zum aux datei löschen funktioniert noch nicht
    # my_path_log=my_path_ausdruckprotokoll[:-3]+'log'
    # my_path_aux=my_path_ausdruckprotokoll[:-3]+'aux'
    # os.remove(my_path_log)
    # os.remove(my_path_aux)

def reibung_margin_tab(self,reibung_beruecksichtigen,fd):
    if reibung_beruecksichtigen==True:
        fd.write("\n"+r' $c_{fr}$ & Reibungsbeiwert')
        fd.write("\n"+r'\\')
        fd.write("\n"+r' $w_{fr}$ & Reibungsdruck')
        fd.write("\n"+r'\\')

def reibung_margin_vernachlaessigen(self,reibung_beruecksichtigen,reibung_vernachlaessigt,fd):
    windrichtung=['Norden und Süden', 'Osten und Westen']
    if reibung_beruecksichtigen==True:
        if all(element==True for element in reibung_vernachlaessigt )==True:
            fd.write("\n"+r' Die Reibung darf für alle Windrichtungen vernachlassigt werden. \\')
        else:
            for ind, element in enumerate(reibung_vernachlaessigt):
                if element == True:
                    fd.write("\n"+r' Die Reibung darf für die Windrichtungen '+ windrichtung[ind]+r' vernachlassigt werden. \\')
