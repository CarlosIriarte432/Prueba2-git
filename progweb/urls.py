"""progweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from progweb.settings import TEMPLATES
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('Formulario', TemplateView.as_view(template_name='index.html'), name='index'),
    path('apps.Formulario/', include('apps.Formulario.urls')),
    path('servicios', TemplateView.as_view(template_name='servicios.html'), name='servicios'),
    path('nosotros', TemplateView.as_view(template_name='nosotros.html'), name='nosotros'),
    path('contacto', TemplateView.as_view(template_name='contacto.html'), name='contacto'),
    path('recomendados', TemplateView.as_view(template_name='recomendados.html'), name='recomendados'),
    path('formulario', TemplateView.as_view(template_name='formulario.html'), name='formulario'),
    path('api_tiempo', TemplateView.as_view(template_name='api_tiempo.html'), name='api_tiempo'),

    
    path('', include('apps.Formulario.urls')),
    
    # Login and Logout
    path('login/', LoginView.as_view(redirect_authenticated_user=True,template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='Usuario/logout.html'), name='logout'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]
