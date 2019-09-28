from .latexflachdach import geometrische_angaben_flachdach, bilder_flachdach, aussendruck_und_innendruckergebnisse_flachdach, nur_aussendruckergebnisse_flachdach, aussendruck_und_innendruckergebnisse_flachdach_ohne_cp, nur_aussendruckergebnisse_flachdach_ohne_cp
from gesamt_pdf_app.latexbasisfunktionen import *
from gesamt_pdf_app.standortparameter import standortparameter
import os.path as path

from waende_app.latex_waende import latex_waende_ergebniss, bilder_waende, aussendruckbeiwerte_waende
#Standard Ausdruckprotokoll_Flachdach


def flachdach_pdferzeugen(self, arg_latex):
    #Eingabewerte und ergebnisse von Allgemeine EIngaben


        ### Pfade der tex dateien
    #Argumente fürs Lates (Wasserzeichen)
    user_id = str(self.request.user.id)

    #Ordner erstellen für das zuküftige Pdf
    BASE_DIR = os.path.dirname(os.path.abspath(path.join(__file__ ,"../")))
    media_path = BASE_DIR +'/media/flachdach/' + user_id
    if not os.path.exists(media_path):
        os.makedirs(media_path)

    pk_flachdach =self.kwargs['pk']
    pk_projekt = str(self.kwargs['my'])

    user_has_free_account = self.request.user.is_free

    path_standortparameter = BASE_DIR +'/media/pdf_bearbeiten/' + user_id+'/standortparameter'+pk_projekt+'.tex'

    my_path_ausdruckprotokoll =  media_path +'/Ausdruckprotokoll_Flachdach'+str(pk_flachdach)+'.tex'
    # hier wird der Speicherort und dateiname für die einzelnen latexteile bestimmt
    # du kannst auch gerne einen unterordner pro projekt oder latexteil machen
    # output_standortparameter =  media_path +'/output_standortparameter'+str(pk_flachdach)+'.tex'
    output_ergebnisse_flachdach =  media_path +'/output_ergebnisse_flachdach'+str(pk_flachdach)+'.tex'
    output_ergebnisse_flachdach_ohne_cp =  media_path +'/output_ergebnisse_flachdach_ohne_cp'+str(pk_flachdach)+'.tex'
    output_geometrische_angaben_flachdach = media_path +'/output_geometrische_angaben_flachdach'+str(pk_flachdach)+'.tex'
    output_bilder_flachdach = media_path +'/output_bilder_flachdach'+str(pk_flachdach)+'.tex'



    latex_waende_list={
                        'innendruck_verfahren_wahl': self.flachdach.some_field_radio2,
                        'reibung_beruecksichtigen':self.flachdach.reibung_beruecksichtigen,
                        'innendruck_beruecksichtigen':self.flachdach.innendruck,
                        'fehlende_korrelation_beruecksichtigen':self.flachdach.fehlende_korrelation_beruecksichtigen,
                        'breite_sued':self.flachdach.breite_x,
                        'breite_west':self.flachdach.breite_y,
                        'anzahl_streifen':int(self.flachdach.anzahl_streifen)


                        }
    print(self.flachdach.anzahl_streifen)
    print(self.flachdach.anzahl_streifen)
    print(self.flachdach.anzahl_streifen)
    print(self.flachdach.anzahl_streifen)
    print(self.flachdach.anzahl_streifen)


    ##### Tex dateien erstellen
    standortparameter(self,arg_latex,path_standortparameter)
    geometrische_angaben_flachdach(self,arg_latex,output_geometrische_angaben_flachdach)
    bilder_flachdach(self,arg_latex,output_bilder_flachdach)

    #Wände
    my_path_cpe_waende =  media_path +'/output_cpe_waende'+str(pk_flachdach)+'.tex'
    my_path_ergebnisse_waende =  media_path +'/output_ergebnisse_waende'+str(pk_flachdach)+'.tex'
    my_path_bilder_waende =  media_path +'/output_bilder_waende'+str(pk_flachdach)+'.tex'
    if self.flachdach.waende_beruecksichtigen == True:
        aussendruckbeiwerte_waende(self,arg_latex,my_path_cpe_waende)
        latex_waende_ergebniss(self,arg_latex,latex_waende_list,my_path_ergebnisse_waende)
        bilder_waende(self,arg_latex,latex_waende_list,my_path_bilder_waende)
    elif os.path.exists(my_path_ergebnisse_waende):
        os.remove(my_path_cpe_waende)
        os.remove(my_path_ergebnisse_waende)
        os.remove(my_path_bilder_waende)
    #margin_ergebnisse(output_margin_ergebnisse)

    if self.flachdach.innendruck == True:
        aussendruck_und_innendruckergebnisse_flachdach(self,arg_latex,output_ergebnisse_flachdach)
        aussendruck_und_innendruckergebnisse_flachdach_ohne_cp(self,arg_latex,output_ergebnisse_flachdach_ohne_cp)
    else:
        nur_aussendruckergebnisse_flachdach(self,arg_latex,output_ergebnisse_flachdach)
        nur_aussendruckergebnisse_flachdach_ohne_cp(self,arg_latex,output_ergebnisse_flachdach_ohne_cp)

    # gesammt tex datei erstellen

    with io.open(my_path_ausdruckprotokoll,'w', encoding="UTF8") as fd:

        preamble_static_latex(self,fd)
        if user_has_free_account:
            latexwasserzeichen(fd)
        kopfundfusszeile_1(fd,arg_latex)
        print('es macht das ausdruckprotokoll')
        print(my_path_ausdruckprotokoll)

        fd.write("\n"+r'\begin{document}')
        beginn_latex_format(fd)
            ####Tex datein in ein document einfügen
        input_latex(fd,path_standortparameter)
        input_latex(fd,output_geometrische_angaben_flachdach)
        #input_latex(doc,margin_ergebnisse)
        input_latex(fd,output_ergebnisse_flachdach)
        if self.flachdach.waende_beruecksichtigen == True:
            input_latex(fd,my_path_cpe_waende)
            input_latex(fd,my_path_ergebnisse_waende)
        input_latex(fd,output_bilder_flachdach)
        if self.flachdach.waende_beruecksichtigen == True:
            input_latex(fd,my_path_bilder_waende)
        # if self.flachdach.waende_beruecksichtigen == True:
        #     input_latex(fd,my_path_bilder_waende)

        fd.write("\n"+r'\end{paracol}')
        fd.write("\n"+r'\end{document}')

    #Compiling to pdf

    compiling(self,media_path,my_path_ausdruckprotokoll)
        #batchmode unterdrückt die fehlermeldungen und macht es schneller
