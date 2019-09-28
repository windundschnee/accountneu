import os
import os.path as path

def kopfundfusszeile_einzeln(fd,arg_latex):
    fd.write("\n"+r'\fancyhead[L]{\begin{tabular}{l r | l r}')
    fd.write("\n"+r'	\textbf{Projekt}') # eintrag 1
    fd.write("\n"+r' &  &')
    fd.write("\n"+r'\textbf{Seite} & \thepage') # eintrag 2 Seitenzahl
    fd.write("\n"+r'\\[-4pt]')
    fd.write("\n"+r'\textbf{Bauteil}   & Wand') #eintrag 3 Bauteil
    fd.write("\n"+r'&')
    fd.write("\n"+r'\textbf{Datum} & \today') # eintrag 4 Datum
    fd.write("\n"+r'\\[-4pt]')
    fd.write("\n"+r'\textbf{Bauteilart} & Freistehende Wand') # eintrag 5 Bauteilart
    fd.write("\n"+r'&')
    fd.write("\n"+r'\textbf{Firma} & Musterman GMBH')  # eintrag 6 Bauteilart
    fd.write("\n"+r'\\[-4pt]')
    fd.write("\n"+r'&  &')#eintrag 7 nichts
    fd.write("\n"+r'\textbf{Bearbeiter} & James Smith')#eintrag 8 Bearbeiter
    fd.write("\n"+r'\end{tabular}}')

def kopfundfusszeile(fd,arg_latex):
    fd.write("\n"+r'\fancyhead[L]{\begin{tabular}{l r | l r}')
    fd.write("\n"+r'	\textbf{Projekt}') # eintrag 1
    fd.write("\n"+r' &  &')
    fd.write("\n"+r'\textbf{Seite} & \thepage') # eintrag 2 Seitenzahl
    fd.write("\n"+r'\\[-4pt]')
    fd.write("\n"+r'\textbf{Bauteil}   & Wand') #eintrag 3 Bauteil
    fd.write("\n"+r'&')
    fd.write("\n"+r'\textbf{Datum} & \today') # eintrag 4 Datum
    fd.write("\n"+r'\\[-4pt]')
    fd.write("\n"+r'\textbf{Bauteilart} & Freistehende Wand') # eintrag 5 Bauteilart
    fd.write("\n"+r'&')
    fd.write("\n"+r'\textbf{Firma} & Musterman GMBH')  # eintrag 6 Bauteilart
    fd.write("\n"+r'\\[-4pt]')
    fd.write("\n"+r'&  &')#eintrag 7 nichts
    fd.write("\n"+r'\textbf{Bearbeiter} & James Smith')#eintrag 8 Bearbeiter
    fd.write("\n"+r'\end{tabular}}')

def kopfundfusszeile_1(fd,arg_latex):
    fd.write("\n"+r'\fancyhead[L]{\begin{tabular}{l r | l r}')
    fd.write("\n"+r'	\textbf{Projekt}') # eintrag 1
    fd.write("\n"+r' & Beispielprojekt &')
    fd.write("\n"+r'\textbf{Seite} & \thepage') # eintrag 2 Seitenzahl
    fd.write("\n"+r'\\[-4pt]')
    fd.write("\n"+r'\textbf{Firma}   & Musterman GMBH') #eintrag 3 Bauteil
    fd.write("\n"+r'&')
    fd.write("\n"+r'\textbf{Datum} & \today') # eintrag 4 Datum
    fd.write("\n"+r'\\[-4pt]')
    fd.write("\n"+r'\textbf{Bearbeiter} & James Smith') # eintrag 5 Bauteilart
    fd.write("\n"+r'\end{tabular}}')
