from rest_framework.decorators import api_view
from innerlyapp.models import Usuario
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from innerlyapp.controllers.usuarioFunctions import *

@api_view(['GET'])
def getUsuarios(request):
    
    usuarios = list(Usuario.objects.values())

    return JsonResponse(usuarios, safe=False)

@api_view(['GET'])
def getUsuario(request, idUsuario):

    try:
        usuario = model_to_dict(Usuario.objects.get(id=idUsuario))
    except Exception as e:
        return JsonResponse({'mensagem' : 'usuario  não encontado'})
     
    return JsonResponse(usuario)

@api_view(['POST'])
def createUsuario(request):

    try :

        dadosUsuario = json.loads(request.body)

        usuario = Usuario.objects.create(
            nome=dadosUsuario.get('nome').upper(),
            dataNascimento=dadosUsuario.get('datanascimento'),
            email=dadosUsuario.get('email').lower(),
            senha=dadosUsuario.get('senha')
        )

    except Exception as e: 
        return JsonResponse({'mensagem' : 'erro ao criar usuario', 'criado' : False})
    
    return JsonResponse({'mensagem' : 'usuario criado com sucessor', 'id' : usuario.id, 'criado' : True})

@api_view(['PUT'])
def updateUsuario(request):

    try:

        dadosUsuario = json.loads(request.body)

        modelUsuario = model_to_dict(Usuario.objects.get(id=dadosUsuario['id']))
        modelUsuario = preencheUsuario(dadosUsuario, modelUsuario)

        Usuario.objects.filter(id=modelUsuario['id']).update(**modelUsuario)

    except Exception as e:
        return JsonResponse({'mensagem' : 'erro ao alterar usuario'})
    
    return JsonResponse({'mensagem' : 'usuario alterado com sucesso'})
