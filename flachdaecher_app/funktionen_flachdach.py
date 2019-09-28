import numpy as np
from scipy.interpolate import interp1d,Rbf

def scharfkantiger_traufbereich():

	cp_f=-1.8
	cp_g=-1.2
	cp_h=-0.7
	cp_i_sog=-0.2
	cp_i_druck=0.2
	cpe=[cp_f,cp_g,cp_h,cp_i_sog,cp_i_druck]


	return cpe

def mit_attika(hp_zu_h):
	cp_auf_mans_druck = 0
	cp_auf_mans_sog = 0
	cp_i_sog=-0.2
	cp_i_druck=0.2

	if hp_zu_h < 0.1:
		attika_f  = np.array([-1.6,-1.4,-1.2])
		attika_g  = np.array([-1.1,-0.9,-0.8])
		attika_hp_zu_h  = np.array([0.025,0.05,0.1])
		interpolation_f = interp1d(attika_hp_zu_h, attika_f)
		interpolation_g = interp1d(attika_hp_zu_h, attika_g)
		cp_f=float(interpolation_f(hp_zu_h))
		cp_g=float(interpolation_g(hp_zu_h))
		cp_h  = -0.7

	elif hp_zu_h >= 0.1:
		cp_f=-1.1
		cp_g=-0.8
		cp_h=-0.7
	else:
		print("Fehler in Freistehenden Wände mit Attika")

	cpe=[cp_f,cp_g,cp_h,cp_i_sog,cp_i_druck]

	return cpe

def abgerundeter_traufbereich(r_zu_h):
	cp_auf_mans_druck = 0
	cp_auf_mans_sog = 0
	cp_i_sog=-0.2
	cp_i_druck=0.2
	if r_zu_h < 0.2:
		rund_f  = np.array([-1.0,-0.7,-0.5]) #Vektor mit allen f Werten
		rund_g  = np.array([-1.2,-0.8,-0.5])
		rund_h  = np.array([-0.4,-0.3,-0.3])
		rund_r_zu_h  = np.array([0.05,0.1,0.2]) # Vektor mit den verhältnissen
		interpolation_f = interp1d(rund_r_zu_h,rund_f) # interpolationsfunktion
		interpolation_g = interp1d(rund_r_zu_h,rund_g)
		interpolation_h = interp1d(rund_r_zu_h,rund_h)
		cp_f=float(interpolation_f(r_zu_h))	# gibt interpolierten wert aus
		cp_g=float(interpolation_g(r_zu_h))
		cp_h=float(interpolation_h(r_zu_h))


	elif r_zu_h >= 0.2:
		cp_f=-0.5
		cp_g=-0.5
		cp_h=-0.3
	else:
		print("Fehler in Freistehenden Wände mit Attika")

	cpe=[cp_f,cp_g,cp_h,cp_i_sog,cp_i_druck]

	return cpe

def mansarde(alpha):
	mans_f  = np.array([-1.0,-1.2,-1.3,-1.8])
	mans_g  = np.array([-1.0,-1.3,-1.3,-1.2])
	mans_h  = np.array([-0.3,-0.4,-0.5,-0.7])
	mans_alpha  = np.array([30,45,60,90])
	interpolation_f = interp1d(mans_alpha, mans_f)
	interpolation_g = interp1d(mans_alpha, mans_g)
	interpolation_h = interp1d(mans_alpha, mans_h)
	cp_f=float(interpolation_f(alpha))
	cp_g=float(interpolation_g(alpha))
	cp_h  =float(interpolation_h(alpha))
	auf_mans_sog=np.array([-0.5,0,0.7,0.8])
	auf_mans_druck=np.array([0.7,0.7,0.7,0.8])
	auf_mans_alpha = np.array([30,45,60,75])
	auf_mans_interpolation_sog=interp1d(mans_alpha, auf_mans_sog)
	auf_mans_interpolation_druck=interp1d(mans_alpha, auf_mans_druck)
	cp_auf_mans_sog=float(auf_mans_interpolation_sog(alpha))
	cp_auf_mans_druck=float(auf_mans_interpolation_druck(alpha))

	cp_i_sog=-0.2
	cp_i_druck=0.2

	cpe=[cp_f,cp_g,cp_h,cp_i_sog,cp_i_druck,cp_auf_mans_druck,cp_auf_mans_sog]

	return cpe

def sonstige_werte_berechnen(self, hoehe):
	b_sued = float(self.flachdach.breite_x)
	b_west = float(self.flachdach.breite_y)
	#Wind aus x richtung
	e_sued=min(b_west,2*hoehe)
	lf_sued=e_sued/4
	lg_sued=b_west-2*lf_sued
	bf_sued=e_sued/10
	bh_sued=e_sued/2-bf_sued
	bi_sued=b_sued-e_sued/2
	if bh_sued + bf_sued > b_sued:
		print("Die berechnete Breite für die Fläche H ist größer als die vorh Breite!")
		bh_sued = b_sued-bf_sued
		print("Die Fläche I existiert im Lastfall Wind in X nicht!")
		bi_sued = 0

	#Wind aus y richtung
	e_west=min(b_sued,2*hoehe)
	lf_west=e_west/4
	lg_west=b_sued-2*lf_west
	bf_west=e_west/10
	bh_west=e_west/2-bf_west
	bi_west=b_west-e_west/2
	if bh_west + bf_west > b_west:
		print("Die berechnete Breite für die Fläche H ist größer als die vorh Breite!")
		bh_west = b_west-bf_west
		print("Die Fläche I existiert im Lastfall Wind in X nicht!")
		bi_west = 0


	anteil_f_und_g_sued = 0
	anteil_f_und_g_west = 0

	sonstige_werte_berechnet={


	'lf_sued':lf_sued,
	'lg_sued':lg_sued,
	'bf_sued':bf_sued,
	'bh_sued':bh_sued,
	'bi_sued':bi_sued,
	'lf_west':lf_west,
	'lg_west':lg_west,
	'bf_west':bf_west,
	'bh_west':bh_west,
	'bi_west':bi_west,
	'anteil_f_und_g_sued':anteil_f_und_g_sued,
	'anteil_f_und_g_west':anteil_f_und_g_west,

	}

	return sonstige_werte_berechnet
