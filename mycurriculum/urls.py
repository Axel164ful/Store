from django.urls import path

from . import views

app_name= 'curriculums'
urlpatterns = [
    path('<int:salida_id>/', views.first, name='curriculum'),
]