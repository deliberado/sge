"""eventos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from evento.views import home_eventos, home_evento, lista_tipos, create_tipo, salvar_tipo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('eventos/', home_eventos, name='home_eventos'),
    path('tipos/', lista_tipos, name='home_tipos'),
    path('tipos/add', create_tipo, name='create_tipo'),
    path('tipos/salvar', salvar_tipo, name='salvar_tipo'),
    path('eventos/<int:evento_id>/', home_evento, name='home_evento'),
]
