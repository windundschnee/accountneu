from core.models import allgEingaben
from django.shortcuts import get_object_or_404

def qp_berechnen(self, z):

    allgeingaben = get_object_or_404(allgEingaben.objects.filter(id=self.kwargs['my']))
    gelaendekategorie = allgeingaben.gelaendekategorie
    basiswinddruck_gewählt = float(allgeingaben.basiswinddruck)


    if gelaendekategorie == "II":
	    qp = basiswinddruck_gewählt * 2.1 * (max(5,z) / 10) ** 0.24
    elif gelaendekategorie == "III":
        qp = basiswinddruck_gewählt * 1.75 * (max(10,z) / 10) ** 0.29
    else:
        qp = basiswinddruck_gewählt * 1.2 * (max(15,z) / 10) ** 0.38
    return qp
