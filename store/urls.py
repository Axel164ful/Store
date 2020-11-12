from django.urls import path

from . import views
app_name='store'
urlpatterns = [
    path('<int:numero_id>/', views.storevw, name='storevw'),
]