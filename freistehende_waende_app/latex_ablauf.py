from .latexfreistehendewaende import*
import os.path as path
from gesamt_pdf_app.standortparameter import standortparameter
from gesamt_pdf_app.latexbasisfunktionen import *
from gesamt_pdf_app.models import GesamtPdf
from django.forms.models import model_to_dict
from gesamt_pdf_app.kopfzeile import *


#from pylatex.base_classes import LatexObject,Container


def freistehende_waende_pdferzeugen(self, arg_latex):
    #Eingabewerte und ergebnisse von Allgemeine EIngaben
    eingaben_pdfbearbeiten = arg_latex['eingaben_pdfbearbeiten']




    user_has_free_account = arg_latex['user_has_free_account']

        ### Pfade der tex dateien
    #Argumente fürs Lates (Wasserzeichen)
    user_id = str(self.request.user.id)

    #Ordner erstellen für das zuküftige Pdf
    BASE_DIR = os.path.dirname(os.path.abspath(path.join(__file__ ,"../")))
    media_path = BASE_DIR +'/media/freistehende_waende/' + user_id
    if not os.path.exists(media_path):
        os.makedirs(media_path)

    pk_freistehende_waende =self.kwargs['pk']
    pk_projekt = str(self.kwargs['my'])
    path_standortparameter = BASE_DIR +'/media/pdf_bearbeiten/' + user_id+'/standortparameter'+pk_projekt+'.tex'

    my_path_ausdruckprotokoll =  media_path +'/Ausdruckprotokoll_Freistehende_Waende'+str(pk_freistehende_waende)+'.tex'
    # hier wird der Speicherort und dateiname für die einzelnen latexteile bestimmt
    # du kannst auch gerne einen unterordner pro projekt oder latexteil machen


    output_geometrische_angaben_freistehende_waende = media_path +'/output_geometrische_angaben_freistehende_waende'+str(pk_freistehende_waende)+'.tex'
    output_ergebnisse_freistehende_waende = media_path +'/output_ergebnisse_freistehende_waende'+str(pk_freistehende_waende)+'.tex'
    output_bilder_freistehende_waende = media_path +'/output_bilder_freistehende_waende'+str(pk_freistehende_waende)+'.tex'

    margin_ergebnisse = os.path.join(os.path.dirname(__file__), 'static','freistehende_waende_app','ausdruckprotokoll','margin_ergebnisse.tex')


    ##### Tex dateien erstellen
    standortparameter(self,arg_latex,path_standortparameter)
    geometrische_angaben_freistehende_waende(self,arg_latex,output_geometrische_angaben_freistehende_waende)
    ergebnisse_freistehende_waende_latex(self,arg_latex,output_ergebnisse_freistehende_waende)
    bilder_freistehende_waende(self, arg_latex,output_bilder_freistehende_waende)

    with io.open(my_path_ausdruckprotokoll,'w', encoding="UTF8") as fd:

        preamble_static_latex(self,fd)
        if user_has_free_account:
            latexwasserzeichen(fd)
        kopfundfusszeile(fd,arg_latex)

        fd.write("\n"+r'\begin{document}')
        beginn_latex_format(fd)

        input_latex(fd,path_standortparameter)
        input_latex(fd,output_geometrische_angaben_freistehende_waende)
        input_latex(fd,margin_ergebnisse)
        input_latex(fd,output_ergebnisse_freistehende_waende)
        input_latex(fd,output_bilder_freistehende_waende)

        fd.write("\n"+r'\end{paracol}')
        fd.write("\n"+r'\end{document}')

    compiling(self,media_path,my_path_ausdruckprotokoll)
    #subprocess.check_call(['pdflatex','-output-format=dvi', my_path_ausdruckprotokoll])
