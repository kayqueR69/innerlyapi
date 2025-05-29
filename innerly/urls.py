from django.contrib import admin
from django.urls import path
from innerlyapp.controllers.usuarioController import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', getUsuarios),
    path('usuarios/usuario/<int:idUsuario>', getUsuario),
    path('usuarios/create', createUsuario),
    path('usuarios/update', updateUsuario),
]
