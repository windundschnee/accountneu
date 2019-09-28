from .latexpultdach_EN import *
from .latexpultdach_NA import nur_aussendruck_na, aussendruck_und_innendruck_na
#Standard Ausdruckprotokoll_pultdach
from gesamt_pdf_app.latexbasisfunktionen import *

def pultdach_pdferzeugen(self, arg_latex):
    #Eingabewerte und ergebnisse von Allgemeine EIngaben

    eingaben_pdfbearbeiten = arg_latex['eingaben_pdfbearbeiten']
    user_has_free_account = arg_latex['user_has_free_account']

    doc = Document('pultdach_latex')

    latexlang(doc,arg_latex)

    latexpackage(doc, arg_latex)
    latexseitenstiel(doc, arg_latex)
    if bool(eingaben_pdfbearbeiten) == True:
        kopfundfusszeile(doc,arg_latex)
    else:
        kopfundfusszeile_ohne_formatierung(doc,arg_latex)

    if user_has_free_account:
        latexwasserzeichen(doc)


    standortparameter_pultdach(self,doc,arg_latex)
    geometrische_angaben_pultdach(self,doc,arg_latex)

    if self.pultdach.verfahren_wahl == 'Verfahren gemäß ÖNORM EN 1991-1-4, Abschnitt 7.2.4':
        if self.pultdach.innendruck == True:
            nur_aussendruck(self, doc, arg_latex)
            aussendruck_und_innendruck(self, doc, arg_latex)
        else:
            nur_aussendruck(self, doc,arg_latex)

    else:
        if self.pultdach.innendruck == True:
            nur_aussendruck_na(self, doc, arg_latex)
            aussendruck_und_innendruck_na(self, doc, arg_latex)
        else:
            nur_aussendruck_na(self, doc,arg_latex)



    #bilder_lang(self,doc,arg_latex)



    foldername=arg_latex['foldername']



    doc.generate_pdf(foldername, clean_tex=False)

#Standard Ausdruckprotokoll_pultdach


def pultdach_pdferzeugen_kurzversion(self, arg_latex):
    #Eingabewerte und ergebnisse von Allgemeine EIngaben

    eingaben_pdfbearbeiten = arg_latex['eingaben_pdfbearbeiten']
    user_has_free_account = arg_latex['user_has_free_account']

    doc = Document('pultdach_latex')

    latexkurz(doc,arg_latex)

    latexpackage(doc, arg_latex)
    latexseitenstiel(doc, arg_latex)
    if bool(eingaben_pdfbearbeiten) == True:
        kopfundfusszeile(doc,arg_latex)
    else:
        # Standartwersion wenn pdf lehr ist und überschrift lehr ist
        kopfundfusszeile_ohne_formatierung(doc,arg_latex)

    if user_has_free_account:
        latexwasserzeichen(doc)


    standortparameter_pultdach(self,doc,arg_latex)
    geometrische_angaben_pultdach(self,doc,arg_latex)

    if self.pultdach.innendruck == True:
        aussendruck_und_innendruck(self, doc,arg_latex)
    else:
        nur_aussendruck(self, doc,arg_latex)

    bilder_kurz(self,doc,arg_latex)



    foldername=arg_latex['foldername']



    doc.generate_pdf(foldername, clean_tex=False)
