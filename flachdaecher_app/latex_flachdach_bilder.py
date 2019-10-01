import os
import io

def bilder_flachdach(self,arg_latex,filename):


    ergebnisse_berechnung =  arg_latex['ergebnisse_berechnung']

    art_traufenbereich = self.flachdach.art_traufenbereich
    hoehe = self.flachdach.hoehe
    hoehe_attika = self.flachdach.hoehe_attika
    radius = self.flachdach.radius
    alpha = self.flachdach.alpha
    laenge_west = self.flachdach.breite_x
    laenge_sued = self.flachdach.breite_y
    vereinfachtes_verfahren = self.flachdach.some_field

    sonstige_werte_berechnet=ergebnisse_berechnung['geometrische_werte_flachdach']
    lf_sued=sonstige_werte_berechnet['lf_sued']
    lg_sued=sonstige_werte_berechnet['lg_sued']
    bf_sued=sonstige_werte_berechnet['bf_sued']
    bh_sued=sonstige_werte_berechnet['bh_sued']
    bi_sued=sonstige_werte_berechnet['bi_sued']
    lf_west=sonstige_werte_berechnet['lf_west']
    lg_west=sonstige_werte_berechnet['lg_west']
    bf_west=sonstige_werte_berechnet['bf_west']
    bh_west=sonstige_werte_berechnet['bh_west']
    bi_west=sonstige_werte_berechnet['bi_west']
    # für die tikz zeichnung Größe kann so vareiert werden

    if laenge_sued > laenge_west:
        laenge_sued_latex=4.5
        scalefaktor=laenge_sued_latex/float(laenge_sued)
        laenge_west_latex=float(laenge_west)*scalefaktor

        lf_sued_latex=lf_sued*scalefaktor
        lg_sued_latex=lg_sued*scalefaktor
        bf_sued_latex=bf_sued*scalefaktor
        bh_sued_latex=bh_sued*scalefaktor


        lf_west_latex=lf_west*scalefaktor
        lg_west_latex=lg_west*scalefaktor
        bf_west_latex=bf_west*scalefaktor
        bh_west_latex=bh_west*scalefaktor


    elif laenge_sued <= laenge_west:
        laenge_west_latex=3.0
        scalefaktor=laenge_west_latex/float(laenge_west)
        laenge_sued_latex=float(laenge_sued)*scalefaktor

        lf_sued_latex=lf_sued*scalefaktor
        lg_sued_latex=lg_sued*scalefaktor
        bf_sued_latex=bf_sued*scalefaktor
        bh_sued_latex=bh_sued*scalefaktor


        lf_west_latex=lf_west*scalefaktor
        lg_west_latex=lg_west*scalefaktor
        bf_west_latex=bf_west*scalefaktor
        bh_west_latex=bh_west*scalefaktor




    with io.open(filename,'w', encoding="UTF8") as fd:
        ###############
        #Ansicht
        lange_ansicht=4
        h_tikz=1.0
        fd.write("\n"+r'\tikzset{')
        fd.write("\n"+r'flachdachAnsicht/.pic = {')
        fd.write("\n"+r'\node[coordinate] at (0,0) (na) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(lange_ansicht)+r',0) (nb) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(lange_ansicht)+r','+ str(h_tikz)+r') (nc) {};')
        fd.write("\n"+r'\node[coordinate] at (0,'+ str(h_tikz)+r') (nd) {};')

        #Überschrift
        if art_traufenbereich=="mit Attika" and vereinfachtes_verfahren=='Verfahren gemäß ÖNORM EN 1991-1-4, Abschnitt 7.2.3':
            fd.write("\n"+r'\node[anchor=west] at (-1,'+ str(h_tikz+1)+r')  {\Large{Ansicht Traufenbereich}};')
        else:
            fd.write("\n"+r'\node[anchor=west] at (-1,'+ str(h_tikz+0.5)+r')  {\Large{Ansicht Traufenbereich}};')

        #Boden
        fd.write("\n"+r'\draw[line width=0.35mm] (na) -- +(-0.5,0);')
        fd.write("\n"+r'\draw[line width=0.35mm] (nb) -- +(0.5,0);')
        fd.write("\n"+r'\draw[line width=0.35mm] (na) -- (nb);')
        fd.write("\n"+r'\fill[pattern,pattern= north east lines] ($(na)-(0.5,0)$) rectangle ($(nb)+(0.5,-0.3)$);')
        if art_traufenbereich=="scharfkantiger Traufbereich" or vereinfachtes_verfahren == 'Vereinfachtes Verfahren gemäß ÖNORM B 1991-1-4, Abschnitt 9.2.3.1':
            fd.write("\n"+r'\draw[line width=0.25mm] (na) -- (nb) -- (nc) -- (nd) -- cycle;')
        elif art_traufenbereich=="mit Attika" and vereinfachtes_verfahren=='Verfahren gemäß ÖNORM EN 1991-1-4, Abschnitt 7.2.3':
            fd.write("\n"+r'\draw[line width=0.25mm] (na) -- (nb) -- (nc) -- (nd) -- cycle;')
            fd.write("\n"+r'\draw[line width=0.25mm] (nd) -- +(0,0.5);')
            fd.write("\n"+r'\draw[line width=0.25mm] (nc) -- +(0,0.5);')
            fd.write("\n"+r'\node[coordinate] at ($(nd)+(0,0.5)$) (nat) {};')
            fd.write("\n"+r'\DimlineV[nd][nat][-0.7][\num{'+ str(hoehe_attika)+r'}]')
        elif art_traufenbereich=="abgerundeter Traufbereich" and vereinfachtes_verfahren=='Verfahren gemäß ÖNORM EN 1991-1-4, Abschnitt 7.2.3':
            fd.write("\n"+r'\node[coordinate] at ($(nd)-(0,0.5)$) (nda) {};')
            fd.write("\n"+r'\node[coordinate] at ($(nd)+(0.5,0.0)$) (ndc) {};')
            fd.write("\n"+r'\node[coordinate] at ($(nc)-(0,0.5)$) (ncb) {};')
            fd.write("\n"+r'\node[coordinate] at ($(nc)-(0.5,0.0)$) (ncd) {};')
            fd.write("\n"+r'\draw[line width=0.25mm] (na) -- (nb) -- (ncb);')
            fd.write("\n"+r'\draw[line width=0.25mm]  (ncd) -- (ndc);')
            fd.write("\n"+r'\draw[line width=0.25mm]  (nda) -- (na);')
            #Rundung links
            fd.write("\n"+r'\draw[line width=0.25mm] (nda)  arc[radius = 5mm, start angle= 180, end angle= 90];')
            fd.write("\n"+r'\draw[->] ($(nda)+(0.5,0)$) node[above,rotate=-45]{\tiny{\num{'+ str(radius)+r'}}} -- +(135:0.5) ;')
            #Rundung rechts
            fd.write("\n"+r'\draw[line width=0.25mm] (ncb)  arc[radius = 5mm, start angle= 0, end angle= 90];')
            fd.write("\n"+r'\draw[->] ($(ncb)-(0.5,0)$) node[above,rotate=45]{\tiny{\num{'+ str(radius)+r'}}} -- +(45:0.5) ;')
        elif art_traufenbereich=="mansardenartig abgeschrägter Traufbereich" and vereinfachtes_verfahren=='Verfahren gemäß ÖNORM EN 1991-1-4, Abschnitt 7.2.3':
            fd.write("\n"+r'\node[coordinate] at ($(nd)-(0,0.3)$) (nda) {};')
            fd.write("\n"+r'\node[coordinate] at ($(nd)+(0.8,0.0)$) (ndc) {};')
            fd.write("\n"+r'\node[coordinate] at ($(nc)-(0,0.3)$) (ncb) {};')
            fd.write("\n"+r'\node[coordinate] at ($(nc)-(0.8,0.0)$) (ncd) {};')
            fd.write("\n"+r'\draw[line width=0.25mm] (na) -- (nb) -- (ncb);')
            fd.write("\n"+r'\draw[line width=0.25mm]  (ncd) -- (ndc);')
            fd.write("\n"+r'\draw[line width=0.25mm]  (nda) -- (na);')
            #Schräge
            fd.write("\n"+r'\draw[line width=0.25mm]  (nda) -- (ndc);')
            fd.write("\n"+r'\draw[line width=0.25mm]  (ncd) -- (ncb);')
            fd.write("\n"+r'\draw[line width=0.13mm]  (nd) -- ($(ndc)-(0.2,0)$);')
            #Winkelbemassung rechts
            fd.write("\n"+r'\draw[line width=0.13mm]  (nc) -- ($(ncd)+(0.2,0)$);')
            fd.write("\n"+r'\tkzMarkAngle[size=.5](ncb,ncd,nc)')
            fd.write("\n"+r'\tkzLabelAngle[pos=0.9](ncb,ncd,nc){\tiny{\num{'+ str(alpha)+r'}}}')
            #Winkelbemassung links
            fd.write("\n"+r'\draw[line width=0.13mm]  (nd) -- ($(ndc)-(0.2,0)$);')
            fd.write("\n"+r'\tkzMarkAngle[size=.5](nd,ndc,nda)')
            fd.write("\n"+r'\tkzLabelAngle[pos=-0.9](nd,ndc,nda){\tiny{\num{'+ str(alpha)+r'}}}')



        #Bemasung
        #fd.write("\n"+r'\DimlineH[($(na)-(0.0,1.0)$)][($(nb)-(0.0,1.0)$)][\num{'+ str(laenge_west)+r'}]')
        fd.write("\n"+r'\DimlineV[na][nd][-0.7][\num{'+ str(hoehe)+r'}]')

        fd.write("\n"+r'}}')


        ####################
        #Grundriss Wind aus Süden
        fd.write("\n"+r'\tikzset{')
        fd.write("\n"+r'flachdachSued/.pic = {')
        fd.write("\n"+r'\node[coordinate] at (0,0) (na) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(laenge_sued_latex)+r',0) (nb) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(laenge_sued_latex)+r','+ str(laenge_west_latex)+r') (nc) {};')
        fd.write("\n"+r'\node[coordinate] at (0,'+ str(laenge_west_latex)+r') (nd) {};')
        fd.write("\n"+r'\node[coordinate] at (0,'+ str(bf_sued_latex)+r') (ne) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(lf_sued_latex)+r','+ str(bf_sued_latex)+r') (nf) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(laenge_sued_latex- lf_sued_latex)+r','+str( bf_sued_latex)+r') (ng) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(laenge_sued_latex)+r','+str( bf_sued_latex)+r') (nh) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(lf_sued_latex)+r',0) (ni) {};')
        fd.write("\n"+r'\node[coordinate] at ('+str(laenge_sued_latex- lf_sued_latex)+r',0) (nj) {};')
        fd.write("\n"+r'\node[coordinate] at (0,'+str(bf_sued_latex+bh_sued_latex)+r') (nk) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(laenge_sued_latex)+r','+ str(bf_sued_latex+bh_sued_latex)+r') (nl) {};')
        #Umrandungslinien
        fd.write("\n"+r'\draw[line width=0.25mm] (na) -- (nb) -- (nc) -- (nd) -- cycle;')
        #Horizontale F G
        fd.write("\n"+r'\draw (ne) -- (nh);')
        #Horizontale H zwischen I
        if bi_sued >0:
            fd.write("\n"+r'\draw (nk) -- (nl);')
        #Vertikale zwischen F und G
        fd.write("\n"+r'\draw (nf) -- (ni);')
        #Vertikale zwischen G und F
        fd.write("\n"+r'\draw (ng) -- (nj);')
        #Vertikale Bemasungslinien
        fd.write("\n"+r'\DimlineV[na][ne][-0.5][\num{'+ str(bf_sued)+r'}]')
        if bi_sued <=0:
            fd.write("\n"+r'\DimlineV[ne][nd][-0.5][\num{'+ str(bh_sued)+r'}]')
        else:
            fd.write("\n"+r'\DimlineV[ne][nk][-0.5][\num{'+ str(bh_sued)+r'}]')
            fd.write("\n"+r'\DimlineV[nk][nd][-0.5][\num{'+ str(bi_sued)+r'}] ')
        fd.write("\n"+r'\DimlineV[na][nd][-1][\num{'+ str(laenge_west)+r'}] ')
        #Horizontale Bemasungslinien
        fd.write("\n"+r'\DimlineH[na][ni]['+ str(laenge_west_latex + 0.5) +r'][\num{'+ str(lf_sued)+r'}] ')
        fd.write("\n"+r'\DimlineH[ni][nj]['+ str(laenge_west_latex + 0.5) +r'][\num{'+ str(lg_sued)+r'}] ')
        fd.write("\n"+r'\DimlineH[nj][nb]['+ str(laenge_west_latex + 0.5) +r'][\num{'+ str(lf_sued)+r'}]')
        fd.write("\n"+r'\DimlineH[na][nb]['+ str(laenge_west_latex + 1) +r'][\num{'+ str(laenge_sued)+r'}] ')
        #Flächenbezeichnung
        fd.write("\n"+r'\node[between=na and nf]  {\normalsize{F}};')
        fd.write("\n"+r'\node[between=ni and ng]  {\normalsize{G}};')
        fd.write("\n"+r'\node[between=nj and nh]  {\normalsize{F}};')
        fd.write("\n"+r'\node[between=ne and nl]  {\normalsize{H}};')
        if bi_sued >0:
            fd.write("\n"+r'\node[between=nk and nc]  {\normalsize{I}};')

        #Himmelsrichtungen
        fd.write("\n"+r'\node[between=nd and nc, above ]  {Norden};')
        fd.write("\n"+r'\node[between=nb and nc, below ,rotate=90]  {Osten};')
        fd.write("\n"+r'\node[between=na and nb, below ]  {Süden};')
        fd.write("\n"+r'\node[between=na and nd, above ,rotate=90]  {Westen};')

        #Pfeile für die Windrichtung
        fd.write("\n"+r'\pic at ('+ str(laenge_sued_latex/2)+r',-0.7) {windrichtung};')
        fd.write("\n"+r'}}')

        #############################
        #Grundriss Wind aus Westen
        fd.write("\n"+r'\tikzset{')
        fd.write("\n"+r'flachdachWest/.pic = {')
        fd.write("\n"+r'\node[coordinate] at (0,0) (na) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(laenge_sued_latex)+r',0) (nb) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(laenge_sued_latex)+r','+ str(laenge_west_latex)+r') (nc) {};')
        fd.write("\n"+r'\node[coordinate] at (0,'+ str(laenge_west_latex)+r') (nd) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(bf_west_latex)+r','+ str(laenge_west_latex)+r') (ne) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(bf_west_latex)+r','+ str(laenge_west_latex-lf_west_latex)+r') (nf) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(bf_west_latex)+r','+str( lf_west_latex)+r') (ng) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(bf_west_latex)+r',0) (nh) {};')
        fd.write("\n"+r'\node[coordinate] at (0,'+ str(laenge_west_latex-lf_west_latex)+r') (ni) {};')
        fd.write("\n"+r'\node[coordinate] at (0,'+ str(lf_west_latex)+r') (nj) {};')
        fd.write("\n"+r'\node[coordinate] at ('+str(bh_west_latex+bf_west_latex)+r','+str(laenge_west_latex)+r') (nk) {};')
        fd.write("\n"+r'\node[coordinate] at ('+ str(bh_west_latex+bf_west_latex)+r',0) (nl) {};')
        #Umrandungslinien
        fd.write("\n"+r'\draw[line width=0.25mm] (na) -- (nb) -- (nc) -- (nd) -- cycle;')
        #Horizontale F G
        fd.write("\n"+r'\draw (ne) -- (nh);')
        #Horizontale H zwischen I
        if bi_west >0:
            fd.write("\n"+r'\draw (nk) -- (nl);')
        #Vertikale zwischen F und G
        fd.write("\n"+r'\draw (nf) -- (ni);')
        #Vertikale zwischen G und F
        fd.write("\n"+r'\draw (ng) -- (nj);')
        #Vertikale Bemasungslinien
        fd.write("\n"+r'\DimlineV[na][nj]['+ str(laenge_sued_latex + 0.9) +r'][\num{'+ str(lf_west)+r'}]')
        fd.write("\n"+r'\DimlineV[nj][ni]['+ str(laenge_sued_latex + 0.9) +r'][\num{'+ str(lg_west)+r'}]')
        fd.write("\n"+r'\DimlineV[ni][nd]['+ str(laenge_sued_latex + 0.9) +r'][\num{'+ str(lf_west)+r'}] ')
        fd.write("\n"+r'\DimlineV[nb][nc][1.4][\num{'+ str(laenge_west)+r'}] ')
        #Horizontale Bemasungslinien
        fd.write("\n"+r'\DimlineH[na][nh]['+ str(laenge_west_latex + 0.5) +r'][\num{'+ str(bf_west)+r'}] ')
        if bi_west <=0:
            fd.write("\n"+r'\DimlineH[nh][nb]['+ str(laenge_west_latex + 0.5) +r'][\num{'+ str(bh_west)+r'}] ')
        else:
            fd.write("\n"+r'\DimlineH[nh][nl]['+ str(laenge_west_latex + 0.5) +r'][\num{'+ str(bh_west)+r'}] ')
            fd.write("\n"+r'\DimlineH[nl][nb]['+ str(laenge_west_latex + 0.5) +r'][\num{'+ str(bi_west)+r'}] ')
        fd.write("\n"+r'\DimlineH[na][nb]['+ str(laenge_west_latex + 1) +r'][\num{'+ str(laenge_sued)+r'}] ')
        #Flächenbezeichnung
        fd.write("\n"+r'\node[between=nd and nf]  {\normalsize{F}};')
        fd.write("\n"+r'\node[between=ni and ng]  {\normalsize{G}};')
        fd.write("\n"+r'\node[between=nj and nh]  {\normalsize{F}};')
        if bi_west >0:
            fd.write("\n"+r'\node[between=ne and nl]  {\normalsize{H}};')
            fd.write("\n"+r'\node[between=nk and nb]  {\normalsize{I}};')
        else:
            fd.write("\n"+r'\node[between=ne and nb]  {\normalsize{H}};')

        #Himmelsrichtungen
        fd.write("\n"+r'\node[between=nd and nc, above ]  {Norden};')
        fd.write("\n"+r'\node[between=nb and nc, below ,rotate=90]  {Osten};')
        fd.write("\n"+r'\node[between=na and nb, below ]  {Süden};')
        fd.write("\n"+r'\node[between=na and nd, above ,rotate=90]  {Westen};')

        #Pfeile für die Windrichtung
        fd.write("\n"+r'\pic[rotate=-90,,transform shape] at (-0.7,'+ str(laenge_west_latex/2)+r') {windrichtung};')
        fd.write("\n"+r'}}')


        ##Margin
        fd.write("\n"+r'\switchcolumn*')
        fd.write("\n"+r'\begin{figure}[H]')
        fd.write("\n"+r'\centering')
        fd.write("\n"+r'\begin{tikzpicture}')
        fd.write("\n"+r' \pic[scale=1,fill=black,text=black] at (0,0) {compass};')
        fd.write("\n"+r'\end{tikzpicture}')
        fd.write("\n"+r'\end{figure}')
        fd.write("\n"+r'alle Werte in $[m]$')
        fd.write("\n"+r'\switchcolumn')
        ##############
        ####Bild zusammenfügen
        fd.write("\n"+r'\begin{figure}[H]')
        fd.write("\n"+r'\centering')
        fd.write("\n"+r'\begin{tikzpicture}')
        #Ansicht einfügen
        fd.write("\n"+r'\pic at (0,'+ str(laenge_west_latex+2.5)+r') {flachdachAnsicht};')
        #Grundriss Flachdach wind von Süden
        fd.write("\n"+r'\node[anchor=west] at (-1,'+ str(laenge_west_latex+1.7)+r')  {\Large{Dachdraufsicht}};')
        fd.write("\n"+r'\pic at (0,0) {flachdachSued};')
        #Grundriss Flachdach wind von Westen
        fd.write("\n"+r'\pic at (7.5,0) {flachdachWest};')
        fd.write("\n"+r'\end{tikzpicture}')
        fd.write("\n"+r'\end{figure}')
