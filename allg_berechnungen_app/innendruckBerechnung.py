
from scipy import interpolate
import numpy as np


def innendruckbeiwert_diagramm(mu,h_zu_d):
	if mu <= 0.33:
		cpi_1=0.35
	#beide schräg
	elif 0.33 < mu<0.9:
		cpi_hd_25  = np.array([0.35,-0.3])
		mu_hd_25  = np.array([0.33,0.9])
		interpolation_hd_25 = interpolate.interp1d(mu_hd_25, cpi_hd_25)
		wert_hd_25=interpolation_hd_25(mu)
		cpi_hd_1  = np.array([0.35,-0.5])
		mu_hd_1  = np.array([0.33,0.95])
		hd_array=np.array([0.25,1])
		interpolation_hd_1 = interpolate.interp1d(mu_hd_1, cpi_hd_1)
		wert_hd_1=interpolation_hd_1(mu)
		if h_zu_d<=0.25:
			cpi_1=wert_hd_25
		elif h_zu_d>=1:
			cpi_1=wert_hd_1
		elif 0.25<h_zu_d<1:
			dazwischen=np.array([wert_hd_25,wert_hd_1])
			interpolation_beide = interpolate.interp1d(hd_array, dazwischen)
			cpi_1=interpolation_beide(h_zu_d)
		else:
			print("Fehler beim innendruckbeiwert mue kleiner 0,9")
	# h/d<=0,25 ist gerade
	elif 0.9 <= mu < 0.95:
		wert_hd_25=-0.3
		cpi_hd_1  = np.array([0.35,-0.5])
		mu_hd_1  = np.array([0.33,0.95])
		hd_array=np.array([0.25,1])
		interpolation_hd_1 = interpolate.interp1d(mu_hd_1, cpi_hd_1)
		wert_hd_1=interpolation_hd_1(mu)
		if h_zu_d<=0.25:
			cpi_1=wert_hd_25
		elif h_zu_d>=1:
			cpi_1=wert_hd_1
		elif 0.25<h_zu_d<1:
			dazwischen=np.array([wert_hd_25,wert_hd_1])
			interpolation_beide = interpolate.interp1d(hd_array, dazwischen)
			cpi_1=interpolation_beide(h_zu_d)
		else:
			print("Fehler beim innendruckbeiwert <0,9  mu < 0,95")
	# beide sind gerade
	elif mu >= 0.95 :
			wert_hd_25=-0.3
			hd_array=np.array([0.25,1])
			wert_hd_1=-0.5
			if h_zu_d<=0.25:
				cpi_1=wert_hd_25
			elif h_zu_d>=1:
				cpi_1=wert_hd_1
			elif 0.25<h_zu_d<1:
				dazwischen=np.array([wert_hd_25,wert_hd_1])
				interpolation_beide = interpolate.interp1d(hd_array, dazwischen)
				cpi_1=interpolation_beide(h_zu_d)
			else:
				print("Fehler beim innendruckbeiwert   mu > 0,95")
	else:
		cpi_1=0
		print("es sind keine öffnungen ausgewählt und mü ist unendlich oder sonnst ein fehler")

	return cpi_1

def innendruck_berechnung_empfohlen(self, qp):
	cpi=np.array([0.2,-0.3])
	wi=cpi*qp
	gibt_es_eine_dominante_seite=False
	index_dominante_seite=False

	list_innendruck={	'wi':wi.tolist(),
						'cpi':cpi.tolist(),
						'gibt_es_eine_dominante_seite':gibt_es_eine_dominante_seite,
						'index_dominante_seite':index_dominante_seite,
						}
	return list_innendruck

def innendruck_berechnung_EN(self, innendruck_eingaben_liste):
	oeffnung_nord_flaeche=float(innendruck_eingaben_liste['oeffnung_nord_flaeche'])
	oeffnung_ost_flaeche=float(innendruck_eingaben_liste['oeffnung_ost_flaeche'])
	oeffnung_sued_flaeche=float(innendruck_eingaben_liste['oeffnung_sued_flaeche'])
	oeffnung_west_flaeche=float(innendruck_eingaben_liste['oeffnung_west_flaeche'])
	oeffnungen_flaeche=[oeffnung_nord_flaeche,oeffnung_ost_flaeche,oeffnung_sued_flaeche,oeffnung_west_flaeche]
	qp = innendruck_eingaben_liste['qp']
	b_sued = float(innendruck_eingaben_liste['b_sued'])
	b_west = float(innendruck_eingaben_liste['b_west'])
	cpe_nord_sued=innendruck_eingaben_liste['cpe_nord_sued']
	cpe_ost_west=innendruck_eingaben_liste['cpe_ost_west']
	hoehe = float(innendruck_eingaben_liste['hoehe'])
	innendruck_verfahren_wahl = innendruck_eingaben_liste['innendruck_verfahren_wahl']
	# h /d verhältnisse
	h_zu_b_sued=hoehe/b_sued
	h_zu_b_west=hoehe/b_west
	#Öffnungsverhältnisse festlegen und überprüfen ob es eine Dominante seite gibt
	oeffnung_verhaeltnis=[]
	lage_dominante_seite=[]
	for ind in range(len(oeffnungen_flaeche)):
		eine_seite=oeffnungen_flaeche[ind]
		alle_anderen_seiten=np.delete(oeffnungen_flaeche, ind, axis=0)
		verhaeltnis=eine_seite / np.sum(alle_anderen_seiten)
		oeffnung_verhaeltnis.append(verhaeltnis)
		if verhaeltnis > 2:
			lage_dominante_seite.append(1)
		else:
			lage_dominante_seite.append(0)

	if 1 in lage_dominante_seite:
		index_dominante_seite= lage_dominante_seite.index(1)
		gibt_es_eine_dominante_seite=True
	else:
		gibt_es_eine_dominante_seite=False
		index_dominante_seite=False


	# print(oeffnung_verhaeltnis)
	# print(index_dominante_seite)
	# print(lage_dominante_seite)
	# print(oeffnungen_flaeche)
	#
	# print(oeffnungen_flaeche)
	# print(gibt_es_eine_dominante_seite)
	# print(cpe_nord_sued)
	# print(cpe_ost_west)

	if gibt_es_eine_dominante_seite==False:
		# ohne Dominante öffnung
		mue_nord=(oeffnungen_flaeche[1]+oeffnungen_flaeche[2]+oeffnungen_flaeche[3])/np.sum(oeffnungen_flaeche)
		mue_ost=(oeffnungen_flaeche[0]+oeffnungen_flaeche[2]+oeffnungen_flaeche[3])/np.sum(oeffnungen_flaeche)
		mue_sued=(oeffnungen_flaeche[1]+oeffnungen_flaeche[0]+oeffnungen_flaeche[3])/np.sum(oeffnungen_flaeche)
		mue_west=(oeffnungen_flaeche[1]+oeffnungen_flaeche[2]+oeffnungen_flaeche[0])/np.sum(oeffnungen_flaeche)
		# print(mue_nord,mue_ost,mue_sued,mue_west)
		cpi_mue_nord=innendruckbeiwert_diagramm(mue_nord,h_zu_b_sued)
		cpi_mue_sued=innendruckbeiwert_diagramm(mue_sued,h_zu_b_sued)
		cpi_mue_ost=innendruckbeiwert_diagramm(mue_ost,h_zu_b_west)
		cpi_mue_west=innendruckbeiwert_diagramm(mue_west,h_zu_b_west)

		cpi=np.array([cpi_mue_nord,cpi_mue_ost,cpi_mue_sued,cpi_mue_west])
		# print(cpi)
		wi=cpi*qp


	elif gibt_es_eine_dominante_seite==True:
		#Dominante Seite ist im Norden
		if index_dominante_seite == 0:
			cpe_innendruck=[cpe_nord_sued[3],cpe_ost_west[0],cpe_nord_sued[4],cpe_ost_west[0]]
		#Dominante Seite ist im Osten
		elif index_dominante_seite == 1:
			cpe_innendruck=[cpe_nord_sued[0],cpe_ost_west[3],cpe_nord_sued[0],cpe_ost_west[4]]
		#Dominante Seite ist im Süden
		elif index_dominante_seite == 2:
			cpe_innendruck=[cpe_nord_sued[4],cpe_ost_west[0],cpe_nord_sued[3],cpe_ost_west[0]]
		#Dominante Seite ist im Westen
		elif index_dominante_seite == 3:
			cpe_innendruck=[cpe_nord_sued[0],cpe_ost_west[4],cpe_nord_sued[0],cpe_ost_west[3]]

		# berechnet den Foktor mit dem der ausendruck multipliziert wird

		interpolationf_faktor_cpi=interpolate.interp1d(np.array([2,3]), np.array([0.75,0.9]))

		if oeffnung_verhaeltnis[index_dominante_seite]<3:
			faktor_cpi=interpolationf_faktor_cpi(oeffnung_verhaeltnis[index_dominante_seite])
		elif 3 <= oeffnung_verhaeltnis[index_dominante_seite]:
			faktor_cpi=0.9

		cpi= np.asarray(cpe_innendruck)*faktor_cpi

		wi=cpi*qp

	list_innendruck={	'wi':wi.tolist(),
							'cpi':cpi.tolist(),
							'gibt_es_eine_dominante_seite':gibt_es_eine_dominante_seite,
							'index_dominante_seite':index_dominante_seite,
							}
		# print(list_innendruck)


	return list_innendruck
