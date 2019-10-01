from .latexbasisfunktionen import *
from django.shortcuts import get_object_or_404
from freistehende_waende_app.models import FreistehendeWaende
from flachdaecher_app.models import FlachdachModel
from anzeigetafeln_app.models import AnzeigetafelnModel
from.standortparameter import *
import os.path as path
from .models import GesamtPdf
from gesamt_pdf_app.kopfzeile import *
from account_app.models import User
from django.shortcuts import get_object_or_404


#Diese Funktion soll den Ablauf für das Gesamtpdf sein
def gesamt_pdf_erzeugen(self, arg_latex):
    #hier sollen die Standortparameter in das GEsamtpdf geschrieben werden
    #get_standortparameter(self, arg_latex)
    #in 'eingaben_pdfbearbeiten' sind die eingabe werte: Kurz/LangVersion,
    eingaben_pdfbearbeiten_object = get_object_or_404(GesamtPdf, projekt_id=self.kwargs['my'])

    # Infos zum app
    flachdach_app_wahl =eingaben_pdfbearbeiten_object.flachdach_app_wahl
    freistehendewaende_app_wahl = eingaben_pdfbearbeiten_object.freistehendewaende_app_wahl
    anzeigetafeln_app_wahl=eingaben_pdfbearbeiten_object.anzeigetafeln_app_wahl
    kurz_lang_version=eingaben_pdfbearbeiten_object.kurz_lang_version

    #identifikationsnummern
    user_id = str(self.request.user.id)
    pk_projekt = str(self.kwargs['my'])

    #Pfad zum Ordner wo das Ausdruckprotokoll sein soll
    BASE_DIR = os.path.dirname(os.path.abspath(path.join(__file__ ,"../")))
    media_path = BASE_DIR +'/media/pdf_bearbeiten/' + user_id
    if not os.path.exists(media_path):
        os.makedirs(media_path)

    ##### #Deiteipfade an denen die tex dateien erzeugt werden #############################

    #Standortparameter
    path_standortparameter = BASE_DIR +'/media/pdf_bearbeiten/' + user_id+'/standortparameter'+pk_projekt+'.tex'

    #Gesammtausdruckprotokoll
    my_path_ausdruckprotokoll =  media_path +'/FullPDF_'+str(self.kwargs['pk'])+'.tex'


    ########## Latex wird erzeugt ###############
    with io.open(my_path_ausdruckprotokoll,'w', encoding="UTF8") as fd:
        #### Pramble ########
        preamble_static_latex(self,fd)
        #Wasserzeichen
        user_has_free_account = arg_latex['user_has_free_account']
        if user_has_free_account:
            latexwasserzeichen(fd)

        #Kopfzeile eingaben
        kopfzeilen_art_wahl=eingaben_pdfbearbeiten_object.kopfzeilen_art_wahl
        user = get_object_or_404(User,email=self.request.user)
        logo_kopfzeile = None
        if user.logo_kopfzeile:
            logo_kopfzeile = user.logo_kopfzeile.url


        kopfzeile_eingeben_list={'projekt': eingaben_pdfbearbeiten_object.projekt.projekt_name,
                        'company':user.company,
                        'logo_kopfzeile':logo_kopfzeile
                            }

        if kopfzeilen_art_wahl=='kopfzeile 1':
            kopfundfusszeile_gesamt_links(fd,kopfzeile_eingeben_list,arg_latex)
        if kopfzeilen_art_wahl=='kopfzeile 2':
            kopfundfusszeile_gesamt_rechts(fd,kopfzeile_eingeben_list,arg_latex)

        #####Hauptdokument beginnt hir ####
        fd.write("\n"+r'\begin{document}')
        beginn_latex_format(fd)
        #Standortparameter werden eingefügt
        input_latex(fd,path_standortparameter)

        #### Die Bauteile werden eingefügt ####

        #Flachdach
        for element in flachdach_app_wahl.all():

            liste_flachdach = get_object_or_404(FlachdachModel.objects.filter(user=self.request.user, id = str(element.id)))
            my_path_geometrische_angaben = BASE_DIR +'/media/flachdach/' + user_id +'/output_geometrische_angaben_flachdach'+str(element.id)+'.tex'
            my_path_ergebnisse = BASE_DIR +'/media/flachdach/' + user_id +'/output_ergebnisse_flachdach'+str(element.id)+'.tex'
            my_path_ergebnisse_ohne_cp = BASE_DIR +'/media/flachdach/' + user_id +'/output_ergebnisse_flachdach_ohne_cp'+str(element.id)+'.tex'
            my_path_bilder = BASE_DIR +'/media/flachdach/' + user_id +'/output_bilder_flachdach'+str(element.id)+'.tex'
            my_path_cpe_waende =  BASE_DIR +'/media/flachdach/' + user_id  +'/output_cpe_waende'+str(element.id)+'.tex'
            my_path_ergebnisse_waende =  BASE_DIR +'/media/flachdach/' + user_id  +'/output_ergebnisse_waende'+str(element.id)+'.tex'
            input_latex(fd,my_path_geometrische_angaben)
            if kurz_lang_version=='langversion':
                input_latex(fd,my_path_ergebnisse)
            else:
                input_latex(fd,my_path_ergebnisse_ohne_cp)
            if os.path.exists(my_path_ergebnisse_waende):
                if kurz_lang_version=='langversion':
                    input_latex(fd,my_path_cpe_waende)
                input_latex(fd,my_path_ergebnisse_waende)
            input_latex(fd,my_path_bilder)

        #Freistehende Wände
        for element in freistehendewaende_app_wahl.all():

            liste_freistehende_waende = get_object_or_404(FreistehendeWaende.objects.filter(user=self.request.user, id = str(element.id)))
            my_path_geometrische_angaben = BASE_DIR +'/media/freistehende_waende/' + user_id +'/output_geometrische_angaben_freistehende_waende'+str(element.id)+'.tex'
            my_path_margin_ergebnisse = BASE_DIR+"/freistehende_waende_app/static/freistehende_waende_app/ausdruckprotokoll/margin_ergebnisse.tex"
            my_path_ergebnisse = BASE_DIR +'/media/freistehende_waende/' + user_id +'/output_ergebnisse_freistehende_waende'+str(element.id)+'.tex'
            my_path_bilder = BASE_DIR +'/media/freistehende_waende/' + user_id +'/output_bilder_freistehende_waende'+str(element.id)+'.tex'

            input_latex(fd,my_path_geometrische_angaben)
            input_latex(fd,my_path_margin_ergebnisse)
            input_latex(fd,my_path_ergebnisse)
            input_latex(fd,my_path_bilder)

        #Anzeigetafeln
        for element in anzeigetafeln_app_wahl.all():
            liste_anzeigetafeln = get_object_or_404(AnzeigetafelnModel.objects.filter(user=self.request.user, id = str(element.id)))
            my_path_geometrische_angaben = BASE_DIR +'/media/anzeigetafeln/' + user_id +'/output_geometrische_angaben_anzeigetafeln'+str(element.id)+'.tex'
            my_path_bilder = BASE_DIR +'/media/anzeigetafeln/' + user_id +'/output_bilder_anzeigetafeln'+str(element.id)+'.tex'
            input_latex(fd,my_path_geometrische_angaben)
            input_latex(fd,my_path_bilder)



        #Das Dokument endet hier
        fd.write("\n"+r'\end{paracol}')
        fd.write("\n"+r'\end{document}')

    # zum PDF compilieren
    compiling(self,media_path,my_path_ausdruckprotokoll)

    return














    # if user_has_free_account:
    #     latexwasserzeichen(doc)








    #
    # doc.generate_pdf(foldername, clean_tex=False)
