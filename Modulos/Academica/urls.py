from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [

    path('', views.home),
    path('FormularioContacto/', views.FormularioContacto),
    path('Contactar/', views.Contactar),
    path('RegistroCupo/', views.RegistroCupo),
    path('EliminarCurso/<codigo>', views.EliminarCurso),
    path('EdicionCurso/<codigo>', views.EdicionCurso),
    path('EditarCurso/', views.EditarCurso),

]