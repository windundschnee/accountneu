from scipy.interpolate import interp1d,Rbf
import numpy as np

def innendruck_berechnung(self, innendruck_liste):


	qp = innendruck_liste['qp']
	innendruck_cpi = innendruck_liste['innendruck_cpi']
	flaechenparameter_mue = innendruck_liste['flaechenparameter_mue']
	basiswinddruck_gewählt = innendruck_liste['basiswinddruck_gewählt']
	breite_x = innendruck_liste['breite_x']
	breite_y = innendruck_liste['breite_y']
	hoehe = innendruck_liste['hoehe']
	innendruck_verfahren_wahl = innendruck_liste['innendruck_verfahren_wahl']
	#Eingabewerte als Dict
	if innendruck_cpi == None:
		cpi_eingabe = 0
	else:
		cpi_eingabe = float(innendruck_cpi)
	    #Eingabewerte einzeln
	if flaechenparameter_mue == None:
		flaechenparameter_mue = 0
	else:
		flaechenparameter_mue= float(flaechenparameter_mue)

	basiswinddruck_gewählt = float(basiswinddruck_gewählt)
	bx = float(breite_x)
	by = float(breite_y)

	h = float(hoehe)
	#was ist ddddddddddddddddddddddddddddddd


	innendruck_verfahren_wahl =innendruck_verfahren_wahl


	if innendruck_verfahren_wahl == 'Innendruckbeiwerte mittels Flächenparameter nach Abschnitt 7.2.9':
		h_zu_bx=h/bx
		h_zu_by=h/by
		cpi_1_x=innendruckbeiwert_diagramm(flaechenparameter_mue,h_zu_bx)
		cpi_1_y=innendruckbeiwert_diagramm(flaechenparameter_mue,h_zu_by)
		wi_f_x=cpi_1_x * qp
		wi_f_y=cpi_1_y * qp
		cpi_druck=0
		wi_druck=0
		cpi_sog=0
		wi_sog=0

		list_innendruck={	'cpi_druck':cpi_druck,
							'cpi_sog':cpi_sog,
							'wi_druck':wi_druck,
							'wi_sog':wi_sog,
							'cpi_1_y':cpi_1_y,
							'cpi_1_x':cpi_1_x,
							'wi_f_x':wi_f_x,
							'wi_f_y':wi_f_y,
							}

	elif innendruck_verfahren_wahl == 'Innendruckbeiwerte mittels dominanter Fläche nach Abschnitt 7.2.9':
		cpi_druck=cpi_eingabe
		wi_druck=cpi_eingabe * qp
		cpi_sog=0
		wi_sog=0
		cpi_1_y=0
		cpi_1_x=0
		wi_f_x=0
		wi_f_y=0


		list_innendruck={	'cpi_druck':cpi_druck,
							'cpi_sog':cpi_sog,
							'wi_druck':wi_druck,
							'wi_sog':wi_sog,
							'cpi_1_y':cpi_1_y,
							'cpi_1_x':cpi_1_x,
							'wi_f_x':wi_f_x,
							'wi_f_y':wi_f_y
							}



	elif innendruck_verfahren_wahl =='Innendruckbeiwerte mittels empfohlener Werte nach Abschnitt 9.2.10':
		cpi_1_y=0
		cpi_1_x=0
		wi_f_x=0
		wi_f_y=0
		cpi_sog=-0.3
		cpi_druck=0.2
		wi_sog=cpi_sog * qp
		wi_druck=cpi_druck * qp
		list_innendruck={	'cpi_druck':cpi_druck,
							'cpi_sog':cpi_sog,
							'wi_druck':wi_druck,
							'wi_sog':wi_sog,
							'cpi_1_y':cpi_1_y,
							'cpi_1_x':cpi_1_x,
							'wi_f_x':wi_f_x,
							'wi_f_y':wi_f_y
							}
	return list_innendruck


def innendruckbeiwert_diagramm(mu,h_zu_d):
	#beide schräg
	if mu<0.9:
		cpi_hd_25  = np.array([0.35,-0.3])
		mu_hd_25  = np.array([0.33,0.9])
		interpolation_hd_25 = interp1d(mu_hd_25, cpi_hd_25)
		wert_hd_25=interpolation_hd_25(mu)
		cpi_hd_1  = np.array([0.35,-0.5])
		mu_hd_1  = np.array([0.33,0.95])
		hd_array=np.array([0.25,1])
		interpolation_hd_1 = interp1d(mu_hd_1, cpi_hd_1)
		wert_hd_1=interpolation_hd_1(mu)
		if h_zu_d<=0.25:
			cpi_1=wert_hd_25
		elif h_zu_d>=1:
			cpi_1=wert_hd_1
		elif 0.25<h_zu_d<1:
			dazwischen=np.array([wert_hd_25,wert_hd_1])
			interpolation_beide = interp1d(hd_array, dazwischen)
			cpi_1=interpolation_beide(h_zu_d)
		else:
			print("Fehler beim innendruckbeiwert mue kleiner 0,9")
	# h/d<=0,25 ist gerade
	elif 0.9 <= mu < 0.95:
		wert_hd_25=-0.3
		cpi_hd_1  = np.array([0.35,-0.5])
		mu_hd_1  = np.array([0.33,0.95])
		hd_array=np.array([0.25,1])
		interpolation_hd_1 = interp1d(mu_hd_1, cpi_hd_1)
		wert_hd_1=interpolation_hd_1(mu)
		if h_zu_d<=0.25:
			cpi_1=wert_hd_25
		elif h_zu_d>=1:
			cpi_1=wert_hd_1
		elif 0.25<h_zu_d<1:
			dazwischen=np.array([wert_hd_25,wert_hd_1])
			interpolation_beide = interp1d(hd_array, dazwischen)
			cpi_1=interpolation_beide(h_zu_d)
		else:
			print("Fehler beim innendruckbeiwert <0,9  mu < 0,95")
	# beide sind gerade
	elif mu >= 0.95:
			wert_hd_25=-0.3
			hd_array=np.array([0.25,1])
			wert_hd_1=-0.5
			if h_zu_d<=0.25:
				cpi_1=wert_hd_25
			elif h_zu_d>=1:
				cpi_1=wert_hd_1
			elif 0.25<h_zu_d<1:
				dazwischen=np.array([wert_hd_25,wert_hd_1])
				interpolation_beide = interp1d(hd_array, dazwischen)
				cpi_1=interpolation_beide(h_zu_d)
			else:
				print("Fehler beim innendruckbeiwert   mu > 0,95")
	else:
		print("Fehler im diagramm innendruckbeiwert")

	return cpi_1
