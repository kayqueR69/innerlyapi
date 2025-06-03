from rest_framework.decorators import api_view
from innerlyapp.models import Usuario, Registro
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from innerlyapp.controllers.usuarioFunctions import *

@api_view(['GET'])
def getRegistros(request):

    registros = list(Registro.objects.values())

    return JsonResponse(registros, safe=False)

@api_view(['GET'])
def getRegistrosByUser(request, idUsuario):
    
    registros = list(Registro.objects.filter(idUsuario=idUsuario).values())

    if not registros:
        return JsonResponse({'mensagem' : 'usuario não encontrado'})

    return JsonResponse(registros, safe=False)



@api_view(['GET'])
def getRegistro(request, idRegistro):

    try:
        registro = model_to_dict(Registro.objects.get(id=idRegistro))
    except Exception as e:
        return JsonResponse({'mensagem' : 'registro não encontrado'})

    return JsonResponse(registro)