from .latexanzeigetafeln import *
from gesamt_pdf_app.latexbasisfunktionen import *
from gesamt_pdf_app.standortparameter import standortparameter
import os.path as path


#Standard Ausdruckprotokoll_Anzeigetafeln


def anzeigetafeln_pdferzeugen(self, arg_latex):
    #Eingabewerte und ergebnisse von Allgemeine EIngaben


        ### Pfade der tex dateien
    #Argumente fürs Lates (Wasserzeichen)
    user_id = str(self.request.user.id)

    #Ordner erstellen für das zuküftige Pdf
    BASE_DIR = os.path.dirname(os.path.abspath(path.join(__file__ ,"../")))
    media_path = BASE_DIR +'/media/anzeigetafeln/' + user_id
    if not os.path.exists(media_path):
        os.makedirs(media_path)

    pk_flachdach =self.kwargs['pk']
    pk_projekt = str(self.kwargs['my'])

    user_has_free_account = self.request.user.is_free

    path_standortparameter = BASE_DIR +'/media/pdf_bearbeiten/' + user_id+'/standortparameter'+pk_projekt+'.tex'

    my_path_ausdruckprotokoll =  media_path +'/Ausdruckprotokoll_Anzeigetafeln'+str(pk_flachdach)+'.tex'
    # hier wird der Speicherort und dateiname für die einzelnen latexteile bestimmt
    # du kannst auch gerne einen unterordner pro projekt oder latexteil machen
    #output_ergebnisse_anzeigetafeln =  media_path +'/output_ergebnisse_anzeigetafeln'+str(pk_flachdach)+'.tex'
    output_geometrische_angaben_anzeigetafeln = media_path +'/output_geometrische_angaben_anzeigetafeln'+str(pk_flachdach)+'.tex'
    output_bilder_anzeigetafeln = media_path +'/output_bilder_anzeigetafeln'+str(pk_flachdach)+'.tex'




    ##### Tex dateien erstellen
    standortparameter(self,arg_latex,path_standortparameter)
    geometrische_angaben(self,arg_latex,output_geometrische_angaben_anzeigetafeln)
    bilder(self, arg_latex, output_bilder_anzeigetafeln)



    # gesammt tex datei erstellen

    with io.open(my_path_ausdruckprotokoll,'w', encoding="UTF8") as fd:

        preamble_static_latex(self,fd)
        if user_has_free_account:
            latexwasserzeichen(fd)
        kopfundfusszeile_1(fd,arg_latex)


        fd.write("\n"+r'\begin{document}')
        beginn_latex_format(fd)
            ####Tex datein in ein document einfügen
        input_latex(fd,path_standortparameter)
        input_latex(fd,output_geometrische_angaben_anzeigetafeln)
        input_latex(fd,output_bilder_anzeigetafeln)

        fd.write("\n"+r'\end{paracol}')
        fd.write("\n"+r'\end{document}')

    #Compiling to pdf

    compiling(self,media_path,my_path_ausdruckprotokoll)
        #batchmode unterdrückt die fehlermeldungen und macht es schneller
