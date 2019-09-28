
from .latexbasisfunktionen import *
from django.shortcuts import get_object_or_404
from freistehende_waende_app.models import FreistehendeWaende
#Diese Funktion soll den Ablauf für das Gesamtpdf sein
from flachdaecher_app.models import FlachdachModel
from anzeigetafeln_app.models import AnzeigetafelnModel
import os.path as path
from .models import GesamtPdf


def gesamt_pdf_erzeugen(self, arg_latex):
    #hier sollen die Standortparameter in das GEsamtpdf geschrieben werden
    #get_standortparameter(self, arg_latex)
    #in 'eingaben_pdfbearbeiten' sind die eingabe werte: Kurz/LangVersion,
    eingaben_pdfbearbeiten_object = get_object_or_404(GesamtPdf, projekt_id=self.kwargs['my'])

    print(eingaben_pdfbearbeiten_object)

    
    print(eingaben_pdfbearbeiten_object.flachdach_app_wahl)
    flachdach_app_wahl =eingaben_pdfbearbeiten_object.flachdach_app_wahl
    freistehendewaende_app_wahl = eingaben_pdfbearbeiten_object.freistehendewaende_app_wahl
    anzeigetafeln_app_wahl=eingaben_pdfbearbeiten_object.anzeigetafeln_app_wahl
    kurz_lang_version=eingaben_pdfbearbeiten_object.kurz_lang_version
    BASE_DIR = os.path.dirname(os.path.abspath(path.join(__file__ ,"../")))
    user_id = str(self.request.user.id)
    media_path = BASE_DIR +'/media/pdf_bearbeiten/' + user_id
    pk_projekt = str(self.kwargs['my'])
    path_standortparameter = BASE_DIR +'/media/pdf_bearbeiten/' + user_id+'/standortparameter'+pk_projekt+'.tex'
    if not os.path.exists(media_path):
        os.makedirs(media_path)



    my_path_ausdruckprotokoll =  media_path +'/FullPDF_'+str(self.kwargs['pk'])+'.tex'
    user_has_free_account = arg_latex['user_has_free_account']

    with io.open(my_path_ausdruckprotokoll,'w', encoding="UTF8") as fd:

        preamble_static_latex(self,fd)
        if user_has_free_account:
            latexwasserzeichen(fd)
        kopfundfusszeile(fd,arg_latex)

        fd.write("\n"+r'\begin{document}')
        beginn_latex_format(fd)

        input_latex(fd,path_standortparameter)

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

        for element in anzeigetafeln_app_wahl.all():
            liste_anzeigetafeln = get_object_or_404(AnzeigetafelnModel.objects.filter(user=self.request.user, id = str(element.id)))
            my_path_geometrische_angaben = BASE_DIR +'/media/anzeigetafeln/' + user_id +'/output_geometrische_angaben_anzeigetafeln'+str(element.id)+'.tex'
            my_path_bilder = BASE_DIR +'/media/anzeigetafeln/' + user_id +'/output_bilder_anzeigetafeln'+str(element.id)+'.tex'
            input_latex(fd,my_path_geometrische_angaben)
            input_latex(fd,my_path_bilder)




        fd.write("\n"+r'\end{paracol}')
        fd.write("\n"+r'\end{document}')

    compiling(self,media_path,my_path_ausdruckprotokoll)

    return

    # latexpackage(doc, arg_latex)
    # latexseitenstiel(doc, arg_latex)
    # tikzsets(doc, arg_latex)
    # kopfundfusszeile(doc,arg_latex)













    # if user_has_free_account:
    #     latexwasserzeichen(doc)








    #
    # doc.generate_pdf(foldername, clean_tex=False)
