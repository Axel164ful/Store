

from django.shortcuts import get_object_or_404, render
from datetime import datetime
from django.http import HttpResponse
from .models import Descripciones, Contexto
# 
def first(request, salida_id):
	
	lista_habilidad = Descripciones.objects.order_by('pub_date')[:5]
	
	salida2 = get_object_or_404(Descripciones, pk=salida_id)#Este diccionario recibe toda la lista  del modelo "descripciones dependiendo de la id ", adicional tambien recibe todos los objetos relacionados en caso de no existir manda error
	
	hora=datetime.now()

	return render(request, 'mycurriculum/index.html', {'salida2':salida2, 'lista_habilidad':lista_habilidad, 'hora':hora}) 

