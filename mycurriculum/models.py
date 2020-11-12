
from django.db import models
import datetime
from django.utils import timezone


class Descripciones(models.Model):
	habilidad=models.CharField(max_length=25)
	pub_date = models.DateTimeField('date published')
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	def __str__(self):
		return self.habilidad

class Contexto(models.Model):
	descripciones= models.ForeignKey(Descripciones, on_delete=models.CASCADE)
	descrip_habilidad=models.TextField()
	def __str__(self):
		return self.descrip_habilidad

# Create your models here.
