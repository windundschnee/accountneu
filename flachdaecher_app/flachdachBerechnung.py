from scipy.interpolate import interp1d,Rbf
import numpy as np
from allg_berechnungen_app.qp_berechnen import qp_berechnen
from waende_app.winddruck_waende_berechnung_ablauf import winddruck_waende_berechnung_ablauf
from allg_berechnungen_app.algemeine_berechnungsfunktionen import windruck_berechnen, ueberlagerung_empfohlen, ueberlagerung_EN, liste_runden,cpe_zwischen_1_und_10
from flachdaecher_app.funktionen_flachdach import *
from allg_berechnungen_app.reibung import reibung_vernachlaessigen,reibung


def flachdach_berechnung_ablauf(self):
	gelaendekategorie = self.flachdach.projekt.gelaendekategorie

	art_traufenbereich = self.flachdach.art_traufenbereich
	hoehe = float(self.flachdach.hoehe)
	b_sued = float(self.flachdach.breite_x)
	b_west = float(self.flachdach.breite_y)
	anzahl_streifen=int(self.flachdach.anzahl_streifen)
	innendruck_verfahren_wahl = self.flachdach.some_field_radio2
	fehlende_korrelation_beruecksichtigen=self.flachdach.fehlende_korrelation_beruecksichtigen
	reibung_beruecksichtigen=self.flachdach.reibung_beruecksichtigen
	reibbeiwert_dach=self.flachdach.reibbeiwert_dach
	reibbeiwert_waende=self.flachdach.reibbeiwert_waende
	oeffnung_nord_flaeche=self.flachdach.oeffnung_nord_flaeche
	oeffnung_ost_flaeche=self.flachdach.oeffnung_ost_flaeche
	oeffnung_sued_flaeche=self.flachdach.oeffnung_sued_flaeche
	oeffnung_west_flaeche=self.flachdach.oeffnung_west_flaeche
	vereinfachtes_verfahren = self.flachdach.some_field
	einflussflaeche=float(5)


	if vereinfachtes_verfahren=='Verfahren gemäß ÖNORM EN 1991-1-4, Abschnitt 7.2.3':
		#cpe werte und Höhe berechnen
		#scharfkantiger Traufenbereich
		if art_traufenbereich=="scharfkantiger Traufbereich":
			cpe_dach = scharfkantiger_traufbereich()
			cpe_dach_1 = scharfkantiger_traufbereich_1()
			hoehe_qp=hoehe


		#mit Attika
		elif art_traufenbereich=="mit Attika":
			hoehe_attika = float(self.flachdach.hoehe_attika)
			hp_zu_h = hoehe_attika/hoehe
			cpe_dach = mit_attika(hp_zu_h)
			cpe_dach_1 = mit_attika_1(hp_zu_h)
			hoehe_qp = hoehe + hoehe_attika

		#abgerundeter Traufenbereich
		elif art_traufenbereich=="abgerundeter Traufbereich":
			radius = float(self.flachdach.radius)
			r_zu_h = radius/hoehe
			cpe_dach = abgerundeter_traufbereich(r_zu_h)
			cpe_dach_1 = abgerundeter_traufbereich_1(r_zu_h)
			hoehe_qp=hoehe

		#mansadenartiger Traufenbereich
		elif art_traufenbereich=="mansardenartig abgeschrägter Traufbereich":
			alpha = float(self.flachdach.alpha)
			cpe_dach = mansarde(alpha)
			cpe_dach_1 = mansarde_1(alpha)
			hoehe_qp=hoehe

		else:
			print("Fehler in der Flachdachberechnung")

	else:
		#Beiwerte nach Önorm
		cp_f=-1.8
		cp_g=-1.8
		cp_h_druck=0.2
		cp_i_druck=0.2
		cp_h_sog=-0.7
		cp_i_sog=-0.7

		cp_f_1=-2.5
		cp_g_1=-2.0
		cp_h_druck_1=0.2
		cp_i_druck_1=0.2
		cp_h_sog_1=-1.2
		cp_i_sog_1=-1.2

		cpe_dach=[cp_f,cp_g,cp_h_druck,cp_h_sog,cp_i_druck,cp_i_sog]
		cpe_dach_1=[cp_f_1,cp_g_1,cp_h_druck_1,cp_h_sog_1,cp_i_druck_1,cp_i_sog_1]
		hoehe_qp=hoehe
	#cpe mit einflussfläche zwischen 10 und 1
	cpe_dach_A=cpe_zwischen_1_und_10(self,cpe_dach,cpe_dach_1,einflussflaeche)


	#qp berechnen

	qp = qp_berechnen(self, hoehe_qp)

	#aussenwindrücke berechnen
	aussenwinddruck_dach=windruck_berechnen(self,qp,cpe_dach)
	aussenwinddruck_dach_1=windruck_berechnen(self,qp,cpe_dach_1)
	aussenwinddruck_dach_A=windruck_berechnen(self,qp,cpe_dach_A)


	#Berechnung der Wände und des Innendrucks

	eingaben_waende_berechnung = {'hoehe':hoehe_qp,
						'b_sued':b_sued,
						'b_west':b_west,
						'anzahl_streifen':anzahl_streifen,
						'qp':qp,
						'innendruck_verfahren_wahl':innendruck_verfahren_wahl,
						'fehlende_korrelation_beruecksichtigen':fehlende_korrelation_beruecksichtigen,
						'reibbeiwert_waende':reibbeiwert_waende,
						'reibung_beruecksichtigen':reibung_beruecksichtigen,
						'oeffnung_nord_flaeche':oeffnung_nord_flaeche,
						'oeffnung_ost_flaeche':oeffnung_ost_flaeche,
						'oeffnung_sued_flaeche':oeffnung_sued_flaeche,
						'oeffnung_west_flaeche':oeffnung_west_flaeche,
						'einflussflaeche':einflussflaeche,
						}

	ergebnisse_waende=winddruck_waende_berechnung_ablauf(self,eingaben_waende_berechnung)


	#Überlagerung Aussen mit innendruck Flachdach
	innendruck=ergebnisse_waende['innendruck']




	if innendruck_verfahren_wahl == 'Innendruckbeiwerte mittels dominanter Fläche nach Abschnitt 7.2.9':
		ergebnisse_ueberlagerung_dach=[]
		for ind in range(len(innendruck)):
			ueberlagert=ueberlagerung_EN(self,innendruck[ind],aussenwinddruck_dach)
			ergebnisse_ueberlagerung_dach.append(ueberlagert)
	# innendruck_verfahren_wahl =='Innendruckbeiwerte mittels empfohlener Werte nach Abschnitt 9.2.10':
	else:
		ergebnisse_ueberlagerung_dach=[ueberlagerung_empfohlen(self,innendruck,aussenwinddruck_dach)]

	#Geometrische Werte Flachdach
	geometrische_werte_flachdach=sonstige_werte_berechnen(self, hoehe_qp)


	#Darf reibung vernachlässigt werden
	reibung_vernachlaessigen_nord_sued=reibung_vernachlaessigen(self,b_sued,b_west,hoehe)
	reibung_vernachlaessigen_ost_west=reibung_vernachlaessigen(self,b_west,b_sued,hoehe)
	if reibung_beruecksichtigen==True:
		w_cfr_dach=reibung(self,qp,reibbeiwert_dach)
	else:
		w_cfr_dach=False
	reibung_vernachlaessigt=[reibung_vernachlaessigen_nord_sued,reibung_vernachlaessigen_ost_west]

	ergebnisse_flachdach={
	'ergebnisse_waende':ergebnisse_waende,
	'ergebnisse_ueberlagerung_dach':ergebnisse_ueberlagerung_dach,
	'aussenwinddruck_dach':aussenwinddruck_dach,
	'aussenwinddruck_dach_1':aussenwinddruck_dach_1,
	'aussenwinddruck_dach_A':aussenwinddruck_dach_A,
	'cpe_dach':cpe_dach,
	'cpe_dach_1':cpe_dach_1,
	'cpe_dach_A':cpe_dach_A,
	'geometrische_werte_flachdach':geometrische_werte_flachdach,
	'w_cfr_dach':w_cfr_dach,
	'reibung_vernachlaessigt':reibung_vernachlaessigt,
	'qp':qp
											}
	print(ergebnisse_flachdach)
	print(liste_runden(ergebnisse_flachdach))

	return liste_runden(ergebnisse_flachdach)
