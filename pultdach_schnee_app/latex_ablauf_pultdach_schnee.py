from gesamt_pdf_app.latexbasisfunktionen import *
from gesamt_pdf_app.standortparameter import standortparameter_schnee
from gesamt_pdf_app.kopfzeile import *
import os.path as path
from account_app.models import User
from django.shortcuts import get_object_or_404
from .latex_pultdach_schnee import ergebnisse_angaben_pultdach_schnee, bilder_pultdach_schnee

#Standard Ausdruckprotokoll_Flachdach


def pultdach_schnee_pdferzeugen(self, arg_latex):
    #Eingabewerte und ergebnisse von Allgemeine EIngaben


        ### Pfade der tex dateien
    #Argumente fürs Lates (Wasserzeichen)
    user_id = str(self.request.user.id)
    #Ordner erstellen für das zuküftige Pdf
    BASE_DIR = os.path.dirname(os.path.abspath(path.join(__file__ ,"../")))
    media_path = BASE_DIR +'/media/pultdach_schnee/' + user_id
    if not os.path.exists(media_path):
        os.makedirs(media_path)

    pk_bauteil =self.kwargs['pk']
    pk_projekt = str(self.kwargs['my'])

    user_has_free_account = self.request.user.is_free

    path_standortparameter = BASE_DIR +'/media/pdf_bearbeiten/' + user_id+'/standortparameter_schnee'+pk_projekt+'.tex'

    my_path_ausdruckprotokoll =  media_path +'/Ausdruckprotokoll_Pultdach_Schnee'+str(pk_bauteil)+'.tex'
    my_path_ergebnisse=media_path +'/ergebnisse_pultdach_schnee'+str(pk_bauteil)+'.tex'
    my_path_bilder=media_path +'/bilder_pultdach_schnee'+str(pk_bauteil)+'.tex'
    # hier wird der Speicherort und dateiname für die einzelnen latexteile bestimmt






    ##### Tex dateien erstellen
    standortparameter_schnee(self,arg_latex,path_standortparameter)
    ergebnisse_angaben_pultdach_schnee(self,arg_latex,my_path_ergebnisse)
    bilder_pultdach_schnee(self,arg_latex,my_path_bilder)


    #Kopfzeile eingaben
    user = get_object_or_404(User,email=self.request.user)
    logo_kopfzeile = None

    if user.logo_kopfzeile:
        logo_kopfzeile = user.logo_kopfzeile.url
    kopfzeile_eingeben_list={'projekt': self.pultdach_schnee.projekt,
                    'bautteil_name':self.pultdach_schnee.bautteil_name,
                    'bemessungsart_wind_schnee':self.pultdach_schnee.bautteil_name.bemessungsart_wind_schnee,
                    'company':user.company,
                    'logo_kopfzeile':logo_kopfzeile
                        }

    # gesammt tex datei erstellen

    with io.open(my_path_ausdruckprotokoll,'w', encoding="UTF8") as fd:

        preamble_static_latex(self,fd)
        if user_has_free_account:
            latexwasserzeichen(fd)
        kopfundfusszeile_einzeln(fd,kopfzeile_eingeben_list,arg_latex)


        fd.write("\n"+r'\begin{document}')
        beginn_latex_format(fd)
            ####Tex datein in ein document einfügen
        input_latex(fd,path_standortparameter)
        input_latex(fd,my_path_ergebnisse)
        input_latex(fd,my_path_bilder)


        fd.write("\n"+r'\end{paracol}')
        fd.write("\n"+r'\end{document}')

    #Compiling to pdf

    compiling(self,media_path,my_path_ausdruckprotokoll)
