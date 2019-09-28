import numpy as np
import collections


def liste_runden(inputdict):
	#erstes dict wird durchsucht
	for key, value in inputdict.items():
		# wenn es ein weiteres dict gibt dann wird dieses durchsucht ansonst wird die liste geprüft und ob float
		if isinstance(value, collections.abc.Mapping)==True:
			for key, value2 in value.items():
				#Wenn es eine liste ist wird die Liste durchsucht ansonst wenn es eine zahl ist wird diese Gerundet
				if isinstance(value2,list)==True:
					for ind, element in enumerate(value2):
						if isinstance(element,float)==True:
							value2[ind]=round(element,2)
							#Gleich wie zuvor mit unterliste
						elif isinstance(element,list)==True:
							for ind2, element2 in enumerate(element):
								if isinstance(element2,float)==True:
									element[ind2]=round(element2,2)
				elif isinstance(value2,float)==True:
					value[key]=round(value2,2)
				elif isinstance(value2, collections.abc.Mapping)==True:
					for key, value3 in value2.items():
						if isinstance(value3,float)==True:
							value2[key]=round(value3,2)

		elif isinstance(value, list)==True:
			for ind, element in enumerate(value):
				if isinstance(element,float)==True:
					value[ind]=round(element,2)
				elif isinstance(element,list)==True:
					for ind2, element2 in enumerate(element):
						if isinstance(element2,float)==True:
							element[ind2]=round(element2,2)
		elif isinstance(value,float)==True:
			inputdict[key] = round(value,2)



	return inputdict

def ueberlagerung_empfohlen(self,innendruck,aussendruck):
	#Überlagert innendruck aus den empfohlenen werten mit dem Aussendruck
	#Es gibt eine liste in einer liste aus beim indexen muss man daher aufpassen vieleicht gibt es noch eine lösung
	wi_druck=innendruck[1]
	wi_sog=innendruck[0]


	windruck_gesamt=[]
	print(aussendruck)
	print(innendruck)
	for ind, element in enumerate(aussendruck):
		if element > 0:
			w_ges=element+wi_druck
		elif element <= 0:
			w_ges=element+wi_sog
		else:
			print('fehler in for loop überlagerung')
		windruck_gesamt.append(w_ges)
	return windruck_gesamt


def ueberlagerung_EN(self,innendruck,aussendruck):
	#überlagerung innendruck mit den berechneten Werten
	windruck_gesamt=[]
	for ind, element in enumerate(aussendruck):
		if element > 0 and innendruck > 0:
			w_ges=element+innendruck
		elif element <= 0 and innendruck <= 0:
			w_ges=element+innendruck
		else:
			w_ges=element
		windruck_gesamt.append(w_ges)
	return windruck_gesamt

def windruck_berechnen(self,qp,cp):
	#qp ist muss ein float sein und cp eine liste oder float
	winddruck=np.array(cp)*qp
	return winddruck.tolist()
