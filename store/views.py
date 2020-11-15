
from django.shortcuts import get_object_or_404, render
from datetime import datetime
from django.http import HttpResponse
from .models import Servicios, Conte

# 
def storevw(request, numero_id):

	hora=datetime.now()
	lista_serv=Servicios.objects.order_by('pub_date')[:6]
	salida=get_object_or_404(Servicios, pk=numero_id)
	return render(request, 'store/tienda.html', {'lista_serv':lista_serv, 'salida':salida, 'hora':hora} )

def versiones(request):
	return render(request, 'store/versiones.html')
