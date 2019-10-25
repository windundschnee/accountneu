from .ausenwinddruck_waend_funktionen import aussenwinddruck_waende_berechnung,geometrie_waende
from allg_berechnungen_app.innendruckBerechnung import innendruck_berechnung_empfohlen,innendruck_berechnung_EN
from allg_berechnungen_app.algemeine_berechnungsfunktionen import ueberlagerung_empfohlen, ueberlagerung_EN
from allg_berechnungen_app.reibung import reibung

##Ablauf


def winddruck_waende_berechnung_ablauf(self,eingaben_waende_berechnung):
	einflussflaeche=eingaben_waende_berechnung['einflussflaeche']
	cpe_wahl=eingaben_waende_berechnung['cpe_wahl']
	hoehe = eingaben_waende_berechnung['hoehe']
	b_sued = eingaben_waende_berechnung['b_sued']
	b_west = eingaben_waende_berechnung['b_west']
	anzahl_streifen = eingaben_waende_berechnung['anzahl_streifen']
	qp=eingaben_waende_berechnung['qp']
	innendruck_verfahren_wahl = eingaben_waende_berechnung['innendruck_verfahren_wahl']
	fehlende_korrelation_beruecksichtigen=eingaben_waende_berechnung['fehlende_korrelation_beruecksichtigen']
	reibung_beruecksichtigen=eingaben_waende_berechnung['reibung_beruecksichtigen']


	reibbeiwert_waende=eingaben_waende_berechnung['reibbeiwert_waende']
	oeffnung_nord_flaeche=eingaben_waende_berechnung['oeffnung_nord_flaeche']
	oeffnung_ost_flaeche=eingaben_waende_berechnung['oeffnung_ost_flaeche']
	oeffnung_sued_flaeche=eingaben_waende_berechnung['oeffnung_sued_flaeche']
	oeffnung_west_flaeche=eingaben_waende_berechnung['oeffnung_west_flaeche']
	## Ausendruck Berechnen
	ergebnisse_aussen_nord_sued=aussenwinddruck_waende_berechnung(self,hoehe,b_west,b_sued,anzahl_streifen,fehlende_korrelation_beruecksichtigen,einflussflaeche,cpe_wahl)
	ergebnisse_aussen_ost_west=aussenwinddruck_waende_berechnung(self,hoehe,b_sued,b_west,anzahl_streifen,fehlende_korrelation_beruecksichtigen,einflussflaeche,cpe_wahl)
	ausenwindruecke_d=[ergebnisse_aussen_nord_sued['aussenwinddruck_d'],ergebnisse_aussen_ost_west['aussenwinddruck_d'],ergebnisse_aussen_nord_sued['aussenwinddruck_d'],ergebnisse_aussen_ost_west['aussenwinddruck_d']]
	ausenwindruecke_a_b_c_e=[ergebnisse_aussen_nord_sued['aussenwinddruck_a_b_c_e'],ergebnisse_aussen_ost_west['aussenwinddruck_a_b_c_e'],ergebnisse_aussen_nord_sued['aussenwinddruck_a_b_c_e'],ergebnisse_aussen_ost_west['aussenwinddruck_a_b_c_e']]
	cpe_nord_sued=ergebnisse_aussen_nord_sued['cpe_waende']
	cpe_ost_west=ergebnisse_aussen_ost_west['cpe_waende']

	korrelation_beiwert=[ergebnisse_aussen_nord_sued['korrelation_beiwert'],ergebnisse_aussen_ost_west['korrelation_beiwert']]
	##Innendruck Berechnen
	innendruck_eingaben_liste = {'innendruck_verfahren_wahl':innendruck_verfahren_wahl,
						'hoehe':hoehe,
						'b_sued':b_sued,
						'b_west':b_west,
						'qp':qp,
                        'cpe_ost_west':cpe_ost_west,
                        'cpe_nord_sued':cpe_nord_sued,
                        'oeffnung_nord_flaeche':oeffnung_nord_flaeche,
                        'oeffnung_ost_flaeche':oeffnung_ost_flaeche,
                        'oeffnung_sued_flaeche':oeffnung_sued_flaeche,
                        'oeffnung_west_flaeche':oeffnung_west_flaeche}

	if innendruck_verfahren_wahl == 'Innendruckbeiwerte mittels dominanter Fläche nach Abschnitt 7.2.9':
		ergebnisse_innendruck=innendruck_berechnung_EN(self, innendruck_eingaben_liste)
		#Überlagern
		innendruck=ergebnisse_innendruck['wi']
		ergebnisse_ueberlagerung_d=[]
		ergebnisse_ueberlagerung_a_b_c_e=[]
		for ind in range(len(innendruck)):
			ueberlagert=ueberlagerung_EN(self,innendruck[ind],ausenwindruecke_d[ind])
			ergebnisse_ueberlagerung_d.append(ueberlagert)
		for ind in range(len(innendruck)):
			ueberlagert=ueberlagerung_EN(self,innendruck[ind],ausenwindruecke_a_b_c_e[ind])
			ergebnisse_ueberlagerung_a_b_c_e.append(ueberlagert)

		gibt_es_eine_dominante_seite=ergebnisse_innendruck['gibt_es_eine_dominante_seite']
		#innendruck_verfahren_wahl =='Innendruckbeiwerte mittels empfohlener Werte nach Abschnitt 9.2.10'
	else:
		ergebnisse_innendruck=innendruck_berechnung_empfohlen(self, qp)
		#Überlagern
		innendruck=ergebnisse_innendruck['wi']
		ergebnisse_ueberlagerung_nord_sued_d=ueberlagerung_empfohlen(self,ergebnisse_innendruck['wi'],ergebnisse_aussen_nord_sued['aussenwinddruck_d'])
		ergebnisse_ueberlagerung_nord_sued_a_b_c_e=ueberlagerung_empfohlen(self,ergebnisse_innendruck['wi'],ergebnisse_aussen_nord_sued['aussenwinddruck_a_b_c_e'])
		ergebnisse_ueberlagerung_ost_west_d=ueberlagerung_empfohlen(self,ergebnisse_innendruck['wi'],ergebnisse_aussen_ost_west['aussenwinddruck_d'])
		ergebnisse_ueberlagerung_ost_west_a_b_c_e=ueberlagerung_empfohlen(self,ergebnisse_innendruck['wi'],ergebnisse_aussen_ost_west['aussenwinddruck_a_b_c_e'])
		ergebnisse_ueberlagerung_d=[ergebnisse_ueberlagerung_nord_sued_d,ergebnisse_ueberlagerung_ost_west_d]
		ergebnisse_ueberlagerung_a_b_c_e=[ergebnisse_ueberlagerung_nord_sued_a_b_c_e,ergebnisse_ueberlagerung_ost_west_a_b_c_e]
		gibt_es_eine_dominante_seite='es wird mit empfohlenen werten gerechnet'

	#nur für latex ergebnisse
	qp_waende=[ergebnisse_aussen_nord_sued['qp_waende'],ergebnisse_aussen_ost_west['qp_waende']]
	z_waende=[ergebnisse_aussen_nord_sued['z_hoehe'],ergebnisse_aussen_ost_west['z_hoehe']]
	cpi=ergebnisse_innendruck['cpi']
	index_dominante_seite=ergebnisse_innendruck['index_dominante_seite']



	#Reibung Wand
	if reibung_beruecksichtigen==True:
		w_cfr_wand=reibung(self,qp,reibbeiwert_waende)
	else:
		w_cfr_wand=False

	geometrie_waende_norden=geometrie_waende(self,hoehe,b_west,b_sued)
	geometrie_waende_westen=geometrie_waende(self,hoehe,b_sued,b_west)

	ergebnisse_waende={
                        'ausenwindruecke_d':[ergebnisse_aussen_nord_sued['aussenwinddruck_d'],ergebnisse_aussen_ost_west['aussenwinddruck_d']],
                        'ausenwindruecke_a_b_c_e':[ergebnisse_aussen_nord_sued['aussenwinddruck_a_b_c_e'],ergebnisse_aussen_ost_west['aussenwinddruck_a_b_c_e']],
                        'cpe':[cpe_nord_sued,cpe_ost_west],
                        'qp_waende':qp_waende,
                        'z_waende':z_waende,
                        'innendruck':innendruck,
                        'cpi':cpi,
                        'gibt_es_eine_dominante_seite':gibt_es_eine_dominante_seite,
                        'index_dominante_seite':index_dominante_seite,
                        'korrelation_beiwert':korrelation_beiwert,
                        'w_cfr_wand':w_cfr_wand,
                        'ergebnisse_ueberlagerung_d':ergebnisse_ueberlagerung_d,
                        'ergebnisse_ueberlagerung_a_b_c_e':ergebnisse_ueberlagerung_a_b_c_e,
                        'geometrie_waende_norden':geometrie_waende_norden,
                        'geometrie_waende_westen':geometrie_waende_westen,
                        'hoehe':hoehe,

                        }

	# print(ergebnisse_waende)
	return ergebnisse_waende
