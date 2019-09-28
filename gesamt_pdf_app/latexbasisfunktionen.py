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
