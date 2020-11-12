from django.db import models



class Servicios(models.Model):
	servidescrip=models.CharField(max_length=35)
	pub_date = models.DateTimeField('date published')
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	def __str__(self):
		return self.servidescrip


class Conte(models.Model):
	servicio= models.ForeignKey(Servicios, on_delete=models.CASCADE)
	descrip_servicio=models.TextField()
	def __str__(self):
		return self.descrip_servicio
# Create your models here.
