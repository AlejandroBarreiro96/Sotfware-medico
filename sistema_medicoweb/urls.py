from django.urls import path

from sistema_medicoweb import views
urlpatterns = [
 
    path('', views.home, name="Home"),
    path('servicio', views.servicio, name="Servicios"),
    path('blog', views.blog, name="Blog"),
    path('contacto', views.blog, name="Contacto"),
    path('login', views.contacto, name="Login"),
]
