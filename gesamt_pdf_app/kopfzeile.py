import os
import os.path as path

def kopfundfusszeile_einzeln(fd,kopfzeile_eingeben_list,arg_latex):
    BASE_DIR = os.path.dirname(os.path.abspath(path.join(__file__ ,"../")))

    projekt= kopfzeile_eingeben_list['projekt']
    bautteil_name= kopfzeile_eingeben_list['bautteil_name']
    company= kopfzeile_eingeben_list['company']
    logo_kopfzeile= kopfzeile_eingeben_list['logo_kopfzeile']
    bemessungsart_wind_schnee=kopfzeile_eingeben_list['bemessungsart_wind_schnee']


    fd.write("\n"+r'\fancyhead[L]{')
    fd.write("\n"+r'\begin{tabular}{@{}l r | l r@{}}')

    fd.write("\n"+r'\textbf{'+ str(bemessungsart_wind_schnee)+r'} & ') # eintrag 5 Bauteilart
    fd.write("\n"+r'&')
    fd.write("\n"+r'\textbf{Seite} & \thepage') # eintrag 2 Seitenzahl
    fd.write("\n"+r'\\[-4pt]')
    fd.write("\n"+r'	\textbf{Projekt}') # eintrag 1
    fd.write("\n"+r' & '+ str(projekt)+r' &')

    fd.write("\n"+r'\textbf{Datum} & \today') # eintrag 4 Datum
    fd.write("\n"+r'\\[-4pt]')
    fd.write("\n"+r'\textbf{Bauteil}   & '+ str(bautteil_name)+r'') #eintrag 3 Bauteil
    fd.write("\n"+r'&')

    fd.write("\n"+r'\textbf{Firma} & '+ str(company)+r'')  # eintrag 6 Bauteilart
    fd.write("\n"+r'\end{tabular}\hfill')

    if logo_kopfzeile:
        logo_kopfzeile_gesamtpfad=BASE_DIR+logo_kopfzeile
        logo_kopfzeile_latex=logo_kopfzeile_gesamtpfad.replace("\\", "/")
        fd.write("\n"+r'\begin{tabular}{@{}c @{}}')
        fd.write("\n"+r'\includegraphics[height=1.6cm,width=5.0cm]{'+ str(logo_kopfzeile_latex)+r'}')
        fd.write("\n"+r'\end{tabular}')
    fd.write("\n"+r'}')


def kopfundfusszeile_gesamt_rechts(fd,kopfzeile_eingeben_list,arg_latex):
    BASE_DIR = os.path.dirname(os.path.abspath(path.join(__file__ ,"../")))
    projekt= kopfzeile_eingeben_list['projekt']
    company= kopfzeile_eingeben_list['company']
    logo_kopfzeile= kopfzeile_eingeben_list['logo_kopfzeile']

    fd.write("\n"+r'\fancyhead[L]{')
    fd.write("\n"+r'\begin{tabular}{@{}l r | l r@{}}')
    fd.write("\n"+r'	\textbf{Projekt}') # eintrag 1
    fd.write("\n"+r' & '+ str(projekt)+r' &')
    fd.write("\n"+r'\textbf{Seite} & \thepage') # eintrag 2 Seitenzahl
    fd.write("\n"+r'\\[-4pt]')
    fd.write("\n"+r'\textbf{Firma}   & '+ str(company)+r'') #eintrag 3 Bauteil
    fd.write("\n"+r'&')
    fd.write("\n"+r'\textbf{Datum} & \today') # eintrag 4 Datum
    fd.write("\n"+r'\end{tabular}\hfill')

    if logo_kopfzeile:
        logo_kopfzeile_gesamtpfad=BASE_DIR+logo_kopfzeile
        logo_kopfzeile_latex=logo_kopfzeile_gesamtpfad.replace("\\", "/")
        fd.write("\n"+r'\begin{tabular}{@{}c @{}}')
        fd.write("\n"+r'\includegraphics[height=1.6cm,width=5.0cm]{'+ str(logo_kopfzeile_latex)+r'}')
        fd.write("\n"+r'\end{tabular}')
    fd.write("\n"+r'}')


def kopfundfusszeile_gesamt_links(fd,kopfzeile_eingeben_list,arg_latex):
    BASE_DIR = os.path.dirname(os.path.abspath(path.join(__file__ ,"../")))
    projekt= kopfzeile_eingeben_list['projekt']
    company= kopfzeile_eingeben_list['company']
    logo_kopfzeile= kopfzeile_eingeben_list['logo_kopfzeile']

    fd.write("\n"+r'\fancyhead[L]{')
    if logo_kopfzeile:
        logo_kopfzeile_gesamtpfad=BASE_DIR+logo_kopfzeile
        logo_kopfzeile_latex=logo_kopfzeile_gesamtpfad.replace("\\", "/")
        fd.write("\n"+r'\begin{tabular}{@{}c @{}}')
        fd.write("\n"+r'\includegraphics[height=1.4cm,width=5.0cm]{'+ str(logo_kopfzeile_latex)+r'}')
        fd.write("\n"+r'\end{tabular}')

    fd.write("\n"+r'\hfill')


    fd.write("\n"+r'\begin{tabular}{@{}l r | l r@{}}')
    fd.write("\n"+r'	\textbf{Projekt}') # eintrag 1
    fd.write("\n"+r' & '+ str(projekt)+r' &')
    fd.write("\n"+r'\textbf{Seite} & \thepage') # eintrag 2 Seitenzahl
    fd.write("\n"+r'\\[-4pt]')
    fd.write("\n"+r'\textbf{Firma}   & '+ str(company)+r'') #eintrag 3 Bauteil
    fd.write("\n"+r'&')
    fd.write("\n"+r'\textbf{Datum} & \today') # eintrag 4 Datum
    fd.write("\n"+r'\end{tabular}')


    fd.write("\n"+r'}')
