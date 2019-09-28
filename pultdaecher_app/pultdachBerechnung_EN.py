from scipy.interpolate import interp1d,Rbf
import numpy as np
from .innendruckBerechnung import innendruck_berechnung

def pultdach_berechnung_en(self):
	gelaendekategorie = self.pultdach.projekt.gelaendekategorie

	basiswinddruck_gewählt =float(self.pultdach.projekt.basiswinddruck)

	hoehe = float(self.pultdach.hoehe)
	qp = qp_berechnen(self, hoehe)
	dachneigung = float(self.pultdach.dachneigung)
	breite_x = float(self.pultdach.breite_x)
	breite_y = float(self.pultdach.breite_y)

	neigungswinkel_list = [5, 15, 30, 45, 60, 75]
	cpe_f_neg_0 = [-1.7, -0.9, -0.5, 0, 0, 0]
	cpe_g_neg_0 = [-1.2, -0.8, -0.5, 0, 0, 0]
	cpe_h_neg_0 = [-0.6, -0.3, -0.2, 0, 0, 0]

	cp_f_pos_0 = [0, 0.2, 0.7, 0.7, 0.7, 0.8]
	cp_g_pos_0 = [0, 0.2, 0.7, 0.7, 0.7, 0.8]
	cp_h_pos_0 = [0, 0.2, 0.4, 0.6, 0.7, 0.8]

	cpe_f_neg_0_ergebnis = np.interp(dachneigung, neigungswinkel_list, cpe_f_neg_0)
	cpe_g_neg_0_ergebnis = np.interp(dachneigung, neigungswinkel_list, cpe_g_neg_0)
	cpe_h_neg_0_ergebnis = np.interp(dachneigung, neigungswinkel_list, cpe_h_neg_0)

	cpe_f_pos_0_ergebnis = np.interp(dachneigung, neigungswinkel_list, cp_f_pos_0)
	cpe_g_pos_0_ergebnis = np.interp(dachneigung, neigungswinkel_list, cp_g_pos_0)
	cpe_h_pos_0_ergebnis = np.interp(dachneigung, neigungswinkel_list, cp_h_pos_0)


	cpe_f_neg_180 = [-2.3, -2.5, -1.1, -0.6, -0.5, -0.5]
	cpe_g_neg_180 = [-1.3, -1.3, -0.8, -0.5, -0.5, -0.5]
	cp_h_neg_180 = [-0.8, -0.9, -0.8, -0.7, -0.5, -0.5]

	cpe_f_neg_180_ergebnis = np.interp(dachneigung, neigungswinkel_list, cpe_f_neg_180)
	cpe_g_neg_180_ergebnis = np.interp(dachneigung, neigungswinkel_list, cpe_g_neg_180)
	cpe_h_neg_180_ergebnis = np.interp(dachneigung, neigungswinkel_list, cp_h_neg_180)

	cpe_f_hoch_neg_90 = [-2.1, -2.4, -2.1, -1.5, -1.2, -1.2]
	cpe_f_tief_neg_90 = [-2.1, -1.6, -1.3, -1.3, -1.2, -1.2]
	cpe_g_neg_90 = [-1.8, -1.9, -1.5, -1.4, -1.2, -1.2]
	cpe_h_neg_90 = [-0.6, -0.8, -1, -1, -1, -1]
	cpe_i_neg_90 = [-0.5, -0.7, -0.8, -0.9, -0.7, -0.5]

	cpe_f_hoch_neg_90_ergebnis = np.interp(dachneigung, neigungswinkel_list, cpe_f_hoch_neg_90)
	cpe_f_tief_neg_90_ergebnis = np.interp(dachneigung, neigungswinkel_list, cpe_f_tief_neg_90)
	cpe_g_neg_90_ergebnis = np.interp(dachneigung, neigungswinkel_list, cpe_g_neg_90)
	cpe_h_neg_90_ergebnis = np.interp(dachneigung, neigungswinkel_list, cpe_h_neg_90)
	cpe_i_neg_90_ergebnis = np.interp(dachneigung, neigungswinkel_list, cpe_i_neg_90)

	ergebnisse_cpe_werte = {'cpe_f_neg_0_ergebnis':cpe_f_neg_0_ergebnis,
							'cpe_g_neg_0_ergebnis':cpe_g_neg_0_ergebnis,
							'cpe_h_neg_0_ergebnis':cpe_h_neg_0_ergebnis,
							'cpe_f_pos_0_ergebnis':cpe_f_pos_0_ergebnis,
							'cpe_g_pos_0_ergebnis':cpe_g_pos_0_ergebnis,
							'cpe_h_pos_0_ergebnis':cpe_h_pos_0_ergebnis,
							'cpe_f_neg_180_ergebnis':cpe_f_neg_180_ergebnis,
							'cpe_g_neg_180_ergebnis':cpe_g_neg_180_ergebnis,
							'cpe_h_neg_180_ergebnis':cpe_h_neg_180_ergebnis,
							'cpe_f_hoch_neg_90_ergebnis':cpe_f_hoch_neg_90_ergebnis,
							'cpe_f_tief_neg_90_ergebnis':cpe_f_tief_neg_90_ergebnis,
							'cpe_g_neg_90_ergebnis':cpe_g_neg_90_ergebnis,
							'cpe_h_neg_90_ergebnis':cpe_h_neg_90_ergebnis,
							'cpe_i_neg_90_ergebnis':cpe_i_neg_90_ergebnis,
							}
	#we Werte
	we_f_neg_0_ergebnis = qp * cpe_f_neg_0_ergebnis
	we_g_neg_0_ergebnis = qp * cpe_g_neg_0_ergebnis
	we_h_neg_0_ergebnis = qp * cpe_h_neg_0_ergebnis

	we_f_pos_0_ergebnis = qp * cpe_f_pos_0_ergebnis
	we_g_pos_0_ergebnis = qp * cpe_g_pos_0_ergebnis
	we_h_pos_0_ergebnis = qp * cpe_h_pos_0_ergebnis

	we_f_neg_180_ergebnis = qp * cpe_f_neg_180_ergebnis
	we_g_neg_180_ergebnis = qp * cpe_g_neg_180_ergebnis
	we_h_neg_180_ergebnis = qp * cpe_h_neg_180_ergebnis

	we_f_hoch_neg_90_ergebnis = qp * cpe_f_hoch_neg_90_ergebnis
	we_f_tief_neg_90_ergebnis = qp * cpe_f_tief_neg_90_ergebnis
	we_g_neg_90_ergebnis = qp * cpe_g_neg_90_ergebnis
	we_h_neg_90_ergebnis = qp * cpe_h_neg_90_ergebnis
	we_i_neg_90_ergebnis = qp * cpe_i_neg_90_ergebnis


	ergebnisse_we_werte = {'we_f_neg_0_ergebnis':we_f_neg_0_ergebnis,
							'we_g_neg_0_ergebnis':we_g_neg_0_ergebnis,
							'we_h_neg_0_ergebnis':we_h_neg_0_ergebnis,
							'we_f_pos_0_ergebnis':we_f_pos_0_ergebnis,
							'we_g_pos_0_ergebnis':we_g_pos_0_ergebnis,
							'we_h_pos_0_ergebnis':we_h_pos_0_ergebnis,
							'we_f_neg_180_ergebnis':we_f_neg_180_ergebnis,
							'we_g_neg_180_ergebnis':we_g_neg_180_ergebnis,
							'we_h_neg_180_ergebnis':we_h_neg_180_ergebnis,
							'we_f_hoch_neg_90_ergebnis':we_f_hoch_neg_90_ergebnis,
							'we_f_tief_neg_90_ergebnis':we_f_tief_neg_90_ergebnis,
							'we_g_neg_90_ergebnis':we_g_neg_90_ergebnis,
							'we_h_neg_90_ergebnis':we_h_neg_90_ergebnis,
							'we_i_neg_90_ergebnis':we_i_neg_90_ergebnis,
							}




	ergebnisse_cpe_gerundet = liste_runden(ergebnisse_cpe_werte)
	ergebnisse_we_gerundet = liste_runden(ergebnisse_we_werte)
	#print(ergebnisse_gerundet)

	sonstige_werte_berechnet=sonstige_werte_berechnen(self, hoehe)
	#print(sonstige_werte_berechnet)
	sonstige_werte_berechnet_gerundet=liste_runden(sonstige_werte_berechnet)
	innendruck_cpi= self.pultdach.innendruck_cpi
	flaechenparameter_mue = self.pultdach.flaechenparameter_mue
	innendruck_verfahren_wahl = self.pultdach.innendruck_verfahren_wahl
	innendruck_liste = {'innendruck_cpi':innendruck_cpi,
						'flaechenparameter_mue':flaechenparameter_mue,
						'basiswinddruck_gewählt':basiswinddruck_gewählt,
						'innendruck_verfahren_wahl':innendruck_verfahren_wahl,
						'hoehe':hoehe,
						'breite_x':breite_x,
						'breite_y':breite_y,
						'qp':qp,}


	if self.pultdach.innendruck == True:


		innendruck_berechnen =innendruck_berechnung(self, innendruck_liste)
		innendruck_berechnen_gerundet = liste_runden(innendruck_berechnen)

		ueberlagerungs_list={
								'ergebnisse_cpe_werte':ergebnisse_cpe_werte,
								'innendruck_berechnen':innendruck_berechnen,}

		endergebnisse_ueberlagert = ueberlagerung_pultdach_en(self, ueberlagerungs_list, qp)

		endergebnisse_ueberlagert_gerundet = liste_runden(endergebnisse_ueberlagert)
		#hier funktionert das runden nicht ganz richtig!!!!!!!!!!!!


		alle_berechneten_werte_endlist={	'qp':qp,
											'ergebnisse_cpe_gerundet':ergebnisse_cpe_gerundet,
											'ergebnisse_we_gerundet':ergebnisse_we_gerundet,
											'innendruck_berechnen_gerundet':innendruck_berechnen_gerundet,
											'endergebnisse_ueberlagert_gerundet':endergebnisse_ueberlagert_gerundet,
											'sonstige_werte_berechnet_gerundet':sonstige_werte_berechnet_gerundet,

								}


	else:





		alle_berechneten_werte_endlist={	'qp':qp,
											'ergebnisse_cpe_gerundet':ergebnisse_cpe_gerundet,
											'ergebnisse_we_gerundet':ergebnisse_we_gerundet,
											'sonstige_werte_berechnet_gerundet':sonstige_werte_berechnet_gerundet,

											}



	return alle_berechneten_werte_endlist



def sonstige_werte_berechnen(self, hoehe):
	bx = float(self.pultdach.breite_x)
	by = float(self.pultdach.breite_y)
	#Wind aus x richtung
	e_x=min(by,2*hoehe)
	lf_x=e_x/4
	lg_x=by-2*lf_x
	bf_x=e_x/10
	bh_x=e_x/2-bf_x
	bi_x=0

	#Wind aus y richtung aus 90°
	e_y=min(bx,2*hoehe)
	lf_y=e_y/4
	lg_y=bx-2*lf_y
	bf_y=e_y/10
	bh_y=e_y/2-bf_y
	bi_y=by-e_y/2



	sonstige_werte_berechnet={


	'lf_x':lf_x,
	'lg_x':lg_x,
	'bf_x':bf_x,
	'bh_x':bh_x,
	'bi_x':bi_x,
	'lf_y':lf_y,
	'lg_y':lg_y,
	'bf_y':bf_y,
	'bh_y':bh_y,
	'bi_y':bi_y,

	}

	return sonstige_werte_berechnet

def qp_berechnen(self, z):

	gelaendekategorie = self.pultdach.projekt.gelaendekategorie
	basiswinddruck_gewählt = float(self.pultdach.projekt.basiswinddruck)


	if gelaendekategorie == "II":
	    qp = basiswinddruck_gewählt * 2.1 * (max(5,z) / 10) ** 0.24
	elif gelaendekategorie == "III":
	    qp = basiswinddruck_gewählt * 1.75 * (max(10,z) / 10) ** 0.29
	else:
	    qp = basiswinddruck_gewählt * 1.2 * (max(15,z) / 10) ** 0.38
	return qp


def ueberlagerung_pultdach_en(self, ueberlagerungs_list, qp):

	ergebnisse_cpe_werte = ueberlagerungs_list['ergebnisse_cpe_werte']
	innendruck_berechnen = ueberlagerungs_list['innendruck_berechnen']

	verfahren_wahl = self.pultdach.verfahren_wahl
	cpe_f_neg_0_ergebnis=ergebnisse_cpe_werte['cpe_f_neg_0_ergebnis']
	cpe_g_neg_0_ergebnis=ergebnisse_cpe_werte['cpe_g_neg_0_ergebnis']
	cpe_h_neg_0_ergebnis=ergebnisse_cpe_werte['cpe_h_neg_0_ergebnis']
	cpe_f_pos_0_ergebnis=ergebnisse_cpe_werte['cpe_f_pos_0_ergebnis']
	cpe_g_pos_0_ergebnis=ergebnisse_cpe_werte['cpe_g_pos_0_ergebnis']
	cpe_h_pos_0_ergebnis=ergebnisse_cpe_werte['cpe_h_pos_0_ergebnis']

	cpe_f_neg_180_ergebnis=ergebnisse_cpe_werte['cpe_f_neg_180_ergebnis']
	cpe_g_neg_180_ergebnis=ergebnisse_cpe_werte['cpe_g_neg_180_ergebnis']
	cpe_h_neg_180_ergebnis=ergebnisse_cpe_werte['cpe_h_neg_180_ergebnis']


	cpe_f_hoch_neg_90_ergebnis=ergebnisse_cpe_werte['cpe_f_hoch_neg_90_ergebnis']
	cpe_f_tief_neg_90_ergebnis=ergebnisse_cpe_werte['cpe_f_tief_neg_90_ergebnis']
	cpe_g_neg_90_ergebnis=ergebnisse_cpe_werte['cpe_g_neg_90_ergebnis']
	cpe_h_neg_90_ergebnis=ergebnisse_cpe_werte['cpe_h_neg_90_ergebnis']
	cpe_i_neg_90_ergebnis=ergebnisse_cpe_werte['cpe_i_neg_90_ergebnis']

	cpi_druck = innendruck_berechnen['cpi_druck']
	cpi_sog = innendruck_berechnen['cpi_sog']
	wi_druck = innendruck_berechnen['wi_druck']
	wi_sog = innendruck_berechnen['wi_sog']
	cpi_1_x = innendruck_berechnen['cpi_1_x']
	cpi_1_y = innendruck_berechnen['cpi_1_y']
	wi_f_x = innendruck_berechnen['wi_f_x']
	wi_f_y = innendruck_berechnen['wi_f_y']



	innendruck_verfahren_wahl = self.pultdach.innendruck_verfahren_wahl
	if innendruck_verfahren_wahl=="Innendruckbeiwerte mittels empfohlener Werte nach Abschnitt 9.2.10":
		cpf_druck_0_ges = cpi_druck+cpe_f_pos_0_ergebnis
		cpg_druck_0_ges = cpi_druck+cpe_g_pos_0_ergebnis
		cph_druck_0_ges = cpi_druck+cpe_h_pos_0_ergebnis

		cpf_sog_0_ges = cpi_sog+cpe_f_neg_0_ergebnis
		cpg_sog_0_ges = cpi_sog+cpe_g_neg_0_ergebnis
		cph_sog_0_ges = cpi_sog+cpe_h_neg_0_ergebnis

		cpf_sog_180_ges = cpi_sog+cpe_f_neg_180_ergebnis
		cpg_sog_180_ges = cpi_sog+cpe_g_neg_180_ergebnis
		cph_sog_180_ges = cpi_sog+cpe_h_neg_180_ergebnis

		cpf_hoch_sog_90_ges = cpi_sog+cpe_f_hoch_neg_90_ergebnis
		cpf_tief_sog_90_ges = cpi_sog+cpe_f_tief_neg_90_ergebnis
		cpg_sog_90_ges = cpi_sog+cpe_g_neg_90_ergebnis

		cph_sog_90_ges = cpi_sog+cpe_h_neg_90_ergebnis
		cpi_sog_90_ges = cpi_sog+cpe_i_neg_90_ergebnis



	if innendruck_verfahren_wahl == 'Innendruckbeiwerte mittels dominanter Fläche nach Abschnitt 7.2.9':
		if cpi_druck < 0:
			cpf_druck_0_ges = cpe_f_pos_0_ergebnis
			cpg_druck_0_ges = cpe_g_pos_0_ergebnis
			cph_druck_0_ges = cpe_h_pos_0_ergebnis

			cpf_sog_0_ges = -(abs(cpi_druck)-cpe_f_neg_0_ergebnis)
			cpg_sog_0_ges = -(abs(cpi_druck)-cpe_g_neg_0_ergebnis)
			cph_sog_0_ges = -(abs(cpi_druck)-cpe_h_neg_0_ergebnis)

			cpf_sog_180_ges = -(abs(cpi_druck)-cpe_f_neg_180_ergebnis)
			cpg_sog_180_ges = -(abs(cpi_druck)-cpe_g_neg_180_ergebnis)
			cph_sog_180_ges = -(abs(cpi_druck)-cpe_h_neg_180_ergebnis)

			cpf_hoch_sog_90_ges = -(abs(cpi_druck)-cpe_f_hoch_neg_90_ergebnis)
			cpf_tief_sog_90_ges = -(abs(cpi_druck)-cpe_f_tief_neg_90_ergebnis)
			cpg_sog_90_ges = -(abs(cpi_druck)-cpe_g_neg_90_ergebnis)

			cph_sog_90_ges = -(abs(cpi_druck)-cpe_h_neg_90_ergebnis)
			cpi_sog_90_ges = -(abs(cpi_druck)-cpe_i_neg_90_ergebnis)

		elif cpi_druck >= 0:
			cpf_druck_0_ges = cpi_druck+cpe_f_pos_0_ergebnis
			cpg_druck_0_ges = cpi_druck+cpe_g_pos_0_ergebnis
			cph_druck_0_ges = cpi_druck+cpe_h_pos_0_ergebnis

			cpf_sog_0_ges = cpe_f_neg_0_ergebnis
			cpg_sog_0_ges = cpe_g_neg_0_ergebnis
			cph_sog_0_ges = cpe_h_neg_0_ergebnis

			cpf_sog_180_ges = cpe_f_neg_180_ergebnis
			cpg_sog_180_ges = cpe_g_neg_180_ergebnis
			cph_sog_180_ges = cpe_h_neg_180_ergebnis

			cpf_hoch_sog_90_ges = cpe_f_hoch_neg_90_ergebnis
			cpf_tief_sog_90_ges = cpe_f_tief_neg_90_ergebnis
			cpg_sog_90_ges = cpe_g_neg_90_ergebnis

			cph_sog_90_ges = cpe_h_neg_90_ergebnis
			cpi_sog_90_ges = cpe_i_neg_90_ergebnis



	if innendruck_verfahren_wahl == 'Innendruckbeiwerte mittels Flächenparameter nach Abschnitt 7.2.9':
		if cpi_1_y < 0:
			cpf_sog_0_ges = cpi_1_y+cpe_f_neg_0_ergebnis
			cpg_sog_0_ges = cpi_1_y+cpe_g_neg_0_ergebnis
			cph_sog_0_ges = cpi_1_y+cpe_h_neg_0_ergebnis

			cpf_sog_180_ges = cpi_1_y+cpe_f_neg_180_ergebnis
			cpg_sog_180_ges = cpi_1_y+cpe_g_neg_180_ergebnis
			cph_sog_180_ges = cpi_1_y+cpe_h_neg_180_ergebnis

			cpf_druck_0_ges = cpe_f_pos_0_ergebnis
			cpg_druck_0_ges = cpe_g_pos_0_ergebnis
			cph_druck_0_ges = cpe_h_pos_0_ergebnis
		elif cpi_1_y >= 0:
			cpf_sog_0_ges = cpe_f_neg_0_ergebnis
			cpg_sog_0_ges = cpe_g_neg_0_ergebnis
			cph_sog_0_ges = cpe_h_neg_0_ergebnis

			cpf_sog_180_ges = cpe_f_neg_180_ergebnis
			cpg_sog_180_ges = cpe_g_neg_180_ergebnis
			cph_sog_180_ges = cpe_h_neg_180_ergebnis

			cpf_druck_0_ges = cpi_1_y+cpe_f_pos_0_ergebnis
			cpg_druck_0_ges = cpi_1_y+cpe_g_pos_0_ergebnis
			cph_druck_0_ges = cpi_1_y+cpe_h_pos_0_ergebnis
		if cpi_1_x < 0:
			cpf_hoch_sog_90_ges = cpi_1_x+cpe_f_hoch_neg_90_ergebnis
			cpf_tief_sog_90_ges = cpi_1_x+cpe_f_tief_neg_90_ergebnis
			cpg_sog_90_ges = cpi_1_x+cpe_g_neg_90_ergebnis

			cph_sog_90_ges = cpi_1_x+cpe_h_neg_90_ergebnis
			cpi_sog_90_ges = cpi_1_x+cpe_i_neg_90_ergebnis
		elif cpi_1_x >= 0:
			cpf_hoch_sog_90_ges = cpe_f_hoch_neg_90_ergebnis
			cpf_tief_sog_90_ges = cpe_f_tief_neg_90_ergebnis
			cpg_sog_90_ges = cpe_g_neg_90_ergebnis

			cph_sog_90_ges = cpe_h_neg_90_ergebnis
			cpi_sog_90_ges = cpe_i_neg_90_ergebnis


	wf_druck_0_ges = cpf_druck_0_ges*qp
	wg_druck_0_ges = cpg_druck_0_ges*qp
	wh_druck_0_ges = cph_druck_0_ges*qp

	wf_sog_0_ges = cpf_sog_0_ges*qp
	wg_sog_0_ges = cpg_sog_0_ges*qp
	wh_sog_0_ges = cph_sog_0_ges*qp

	wf_sog_180_ges = cpf_sog_180_ges*qp
	wg_sog_180_ges = cpg_sog_180_ges*qp
	wh_sog_180_ges = cph_sog_180_ges*qp

	wf_hoch_sog_90_ges = cpf_hoch_sog_90_ges*qp
	wf_tief_sog_90_ges = cpf_tief_sog_90_ges*qp
	wg_sog_90_ges = cpg_sog_90_ges*qp

	wh_sog_90_ges = cph_sog_90_ges*qp
	wi_sog_90_ges = cpi_sog_90_ges*qp


	list = {'cpf_druck_0_ges':cpf_druck_0_ges,
			'cpg_druck_0_ges':cpg_druck_0_ges,
			'cph_druck_0_ges':cph_druck_0_ges,
			'cpf_sog_0_ges':cpf_sog_0_ges,
			'cpg_sog_0_ges':cpg_sog_0_ges,
			'cph_sog_0_ges':cph_sog_0_ges,
			'cpf_sog_180_ges':cpf_sog_180_ges,
			'cpg_sog_180_ges':cpg_sog_180_ges,
			'cph_sog_180_ges':cph_sog_180_ges,
			'cpf_hoch_sog_90_ges':cpf_hoch_sog_90_ges,
			'cpf_tief_sog_90_ges':cpf_tief_sog_90_ges,
			'cpg_sog_90_ges':cpg_sog_90_ges,
			'cph_sog_90_ges':cph_sog_90_ges,
			'cpi_sog_90_ges':cpi_sog_90_ges,
			'wf_druck_0_ges':wf_druck_0_ges,
			'wg_druck_0_ges':wg_druck_0_ges,
			'wh_druck_0_ges':wh_druck_0_ges,
			'wf_sog_0_ges':wf_sog_0_ges,
			'wg_sog_0_ges':wg_sog_0_ges,
			'wh_sog_0_ges':wh_sog_0_ges,
			'wf_sog_180_ges':wf_sog_180_ges,
			'wg_sog_180_ges':wg_sog_180_ges,
			'wh_sog_180_ges':wh_sog_180_ges,
			'wf_hoch_sog_90_ges':wf_hoch_sog_90_ges,
			'wf_tief_sog_90_ges':wf_tief_sog_90_ges,
			'wg_sog_90_ges':wg_sog_90_ges,
			'wh_sog_90_ges':wh_sog_90_ges,
			'wi_sog_90_ges':wi_sog_90_ges,
			}


	return list


def liste_runden(inputdict):
	for key, value in inputdict.items():
				if isinstance(value,(np.ndarray))==True:
					value_float=float(value)
					value_float_gerundet=round(value_float,2)
					inputdict[key] = value_float_gerundet
				elif isinstance(value,(float))==True:
					newvalue=round(value,2)
					inputdict[key] = newvalue
	return inputdict
