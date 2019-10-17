from .latexflachdach import geometrische_angaben_flachdach,  aussendruck_und_innendruckergebnisse_flachdach, nur_aussendruckergebnisse_flachdach, aussendruck_und_innendruckergebnisse_flachdach_ohne_cp, nur_aussendruckergebnisse_flachdach_ohne_cp
from .latex_flachdach_bilder import bilder_flachdach
from gesamt_pdf_app.latexbasisfunktionen import *
from gesamt_pdf_app.standortparameter import standortparameter
from gesamt_pdf_app.kopfzeile import *
import os.path as path
from account_app.models import User
from django.shortcuts import get_object_or_404
from waende_app.latex_waende import latex_waende_ergebniss,  aussendruckbeiwerte_waende
from waende_app.latex_waende_bilder import bilder_waende
#Standard Ausdruckprotokoll_Flachdach


def flachdach_pdferzeugen(self, arg_latex):

    #identifikationsnummern
    user_id = str(self.request.user.id)
    pk_bauteil =self.kwargs['pk']
    pk_projekt = str(self.kwargs['my'])

    #Ordner erstellen für das zuküftige Pdf
    BASE_DIR = os.path.dirname(os.path.abspath(path.join(__file__ ,"../")))
    media_path = BASE_DIR +'/media/flachdach/' + user_id #Bauteil ordner in Media
    if not os.path.exists(media_path):
        os.makedirs(media_path)

    ###############################
    #Deiteipfade an denen die tex dateien erzeugt werden #############################

    #Standortparameter
    path_standortparameter = BASE_DIR +'/media/pdf_bearbeiten/' + user_id+'/standortparameter'+pk_projekt+'.tex'

    #Gesammtausdruckprotokoll
    my_path_ausdruckprotokoll =  media_path +'/Ausdruckprotokoll_Flachdach'+str(pk_bauteil)+'.tex'

    #Flachdach
    output_ergebnisse_flachdach =  media_path +'/output_ergebnisse_flachdach'+str(pk_bauteil)+'.tex'
    output_ergebnisse_flachdach_ohne_cp =  media_path +'/output_ergebnisse_flachdach_ohne_cp'+str(pk_bauteil)+'.tex'
    output_geometrische_angaben_flachdach = media_path +'/output_geometrische_angaben_flachdach'+str(pk_bauteil)+'.tex'
    output_bilder_flachdach = media_path +'/output_bilder_flachdach'+str(pk_bauteil)+'.tex'
    #Wände
    my_path_cpe_waende =  media_path +'/output_cpe_waende'+str(pk_bauteil)+'.tex'
    my_path_ergebnisse_waende =  media_path +'/output_ergebnisse_waende'+str(pk_bauteil)+'.tex'
    my_path_bilder_waende =  media_path +'/output_bilder_waende'+str(pk_bauteil)+'.tex'


    #### Eingabewerte für benützte funktionen ########################

    #Argument fürs Wasserzeichen
    user_has_free_account = self.request.user.is_free

    #Wände Eingaben
    latex_waende_list={
                        'innendruck_verfahren_wahl': self.flachdach.some_field_radio2,
                        'reibung_beruecksichtigen':self.flachdach.reibung_beruecksichtigen,
                        'innendruck_beruecksichtigen':self.flachdach.innendruck,
                        'fehlende_korrelation_beruecksichtigen':self.flachdach.fehlende_korrelation_beruecksichtigen,
                        'breite_sued':self.flachdach.breite_x,
                        'breite_west':self.flachdach.breite_y,
                        'anzahl_streifen':int(self.flachdach.anzahl_streifen),
                        'einflussflaeche':5
                        }

    #Kopfzeile eingaben
    user = get_object_or_404(User,email=self.request.user)
    logo_kopfzeile = None

    if user.logo_kopfzeile:
        logo_kopfzeile = user.logo_kopfzeile.url
    kopfzeile_eingeben_list={'projekt': self.flachdach.projekt,
                    'bautteil_name':self.flachdach.bautteil_name,
                    'bemessungsart_wind_schnee':self.flachdach.bautteil_name.bemessungsart_wind_schnee,
                    'company':user.company,
                    'logo_kopfzeile':logo_kopfzeile
                        }


    ##### Tex dateien erstellen  ##############################

    #Standortparameter
    standortparameter(self,arg_latex,path_standortparameter)

    #Flachdach
    geometrische_angaben_flachdach(self,arg_latex,output_geometrische_angaben_flachdach)
    bilder_flachdach(self,arg_latex,output_bilder_flachdach)
    if self.flachdach.innendruck == True:
        aussendruck_und_innendruckergebnisse_flachdach(self,arg_latex,output_ergebnisse_flachdach)
        aussendruck_und_innendruckergebnisse_flachdach_ohne_cp(self,arg_latex,output_ergebnisse_flachdach_ohne_cp)
    else:
        nur_aussendruckergebnisse_flachdach(self,arg_latex,output_ergebnisse_flachdach)
        nur_aussendruckergebnisse_flachdach_ohne_cp(self,arg_latex,output_ergebnisse_flachdach_ohne_cp)

    #Wände
    if self.flachdach.waende_beruecksichtigen == True:
        aussendruckbeiwerte_waende(self,arg_latex,latex_waende_list,my_path_cpe_waende)
        latex_waende_ergebniss(self,arg_latex,latex_waende_list,my_path_ergebnisse_waende)
        bilder_waende(self,arg_latex,latex_waende_list,my_path_bilder_waende)
        #Falls bereits wände vorhanden sind werden die dateien gelöscht so werden die Wände nur angezeigt wenn sie da sind
    elif os.path.exists(my_path_ergebnisse_waende):
        os.remove(my_path_cpe_waende)
        os.remove(my_path_cpe_1_waende)
        os.remove(my_path_ergebnisse_waende)
        os.remove(my_path_bilder_waende)



    ########### gesammt tex datei erstellen #########################

    with io.open(my_path_ausdruckprotokoll,'w', encoding="UTF8") as fd:
        #preamble
        preamble_static_latex(self,fd)
        if user_has_free_account:
            latexwasserzeichen(fd)
        kopfundfusszeile_einzeln(fd,kopfzeile_eingeben_list,arg_latex)

        #Hauptdockument
        fd.write("\n"+r'\begin{document}')
        beginn_latex_format(fd)
            ####Tex datein in ein document einfügen
        input_latex(fd,path_standortparameter)
        input_latex(fd,output_geometrische_angaben_flachdach)


        if self.flachdach.waende_beruecksichtigen == True:
            input_latex(fd,my_path_bilder_waende)
        input_latex(fd,output_bilder_flachdach)

        input_latex(fd,output_ergebnisse_flachdach)
        if self.flachdach.waende_beruecksichtigen == True:
            input_latex(fd,my_path_cpe_waende)
            input_latex(fd,my_path_ergebnisse_waende)


        fd.write("\n"+r'\end{paracol}')
        fd.write("\n"+r'\end{document}')

    #Compiling to pdf

    compiling(self,media_path,my_path_ausdruckprotokoll)
