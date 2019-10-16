from gesamt_pdf_app.latexbasisfunktionen import *
from gesamt_pdf_app.standortparameter import standortparameter_schnee
from gesamt_pdf_app.kopfzeile import *
from .latex_satteldach_schnee import ergebnisse_angaben_satteldach_schnee, bilder_satteldach_schnee
import os.path as path
from account_app.models import User
from django.shortcuts import get_object_or_404
#Standard Ausdruckprotokoll_Flachdach


def satteldach_schnee_pdferzeugen(self, arg_latex):

    #identifikationsnummern
    user_id = str(self.request.user.id)
    pk_bauteil =self.kwargs['pk']
    pk_projekt = str(self.kwargs['my'])

    #Ordner erstellen für das zuküftige Pdf
    BASE_DIR = os.path.dirname(os.path.abspath(path.join(__file__ ,"../")))
    media_path = BASE_DIR +'/media/satteldach_schnee/' + user_id #Bauteil ordner in Media
    if not os.path.exists(media_path):
        os.makedirs(media_path)

    ###############################
    #Deiteipfade an denen die tex dateien erzeugt werden #############################

    #Standortparameter
    path_standortparameter = BASE_DIR +'/media/pdf_bearbeiten/' + user_id+'/standortparameter_schnee'+pk_projekt+'.tex'

    #Gesammtausdruckprotokoll
    my_path_ausdruckprotokoll =  media_path +'/Ausdruckprotokoll_Satteldach_Schnee'+str(pk_bauteil)+'.tex'

    #Satteldach Schnee
    my_path_ergebnisse=media_path +'/ergebnisse_satteldach_schnee'+str(pk_bauteil)+'.tex'
    my_path_bilder=media_path +'/bilder_satteldach_schnee'+str(pk_bauteil)+'.tex'


    #### Eingabewerte für benützte funktionen ########################

    #Argument fürs Wasserzeichen
    user_has_free_account = self.request.user.is_free


    #Kopfzeile eingaben
    user = get_object_or_404(User,email=self.request.user)
    logo_kopfzeile = None

    if user.logo_kopfzeile:
        logo_kopfzeile = user.logo_kopfzeile.url
    kopfzeile_eingeben_list={'projekt': self.satteldach_schnee.projekt,
                    'bautteil_name':self.satteldach_schnee.bautteil_name,
                    'bemessungsart_wind_schnee':self.satteldach_schnee.bautteil_name.bemessungsart_wind_schnee,
                    'company':user.company,
                    'logo_kopfzeile':logo_kopfzeile
                        }


    ##### Tex dateien erstellen  ##############################

    #Standortparameter
    standortparameter_schnee(self,arg_latex,path_standortparameter)

    #Satteldch Schnee
    ergebnisse_angaben_satteldach_schnee(self,arg_latex,my_path_ergebnisse)
    bilder_satteldach_schnee(self,arg_latex,my_path_bilder)



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
        input_latex(fd,my_path_ergebnisse)
        input_latex(fd,my_path_bilder)


        fd.write("\n"+r'\end{paracol}')
        fd.write("\n"+r'\end{document}')

    #Compiling to pdf

    compiling(self,media_path,my_path_ausdruckprotokoll)
