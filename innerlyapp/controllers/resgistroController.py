from rest_framework.decorators import api_view
from innerlyapp.models import Usuario, Registro
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from innerlyapp.controllers.usuarioFunctions import *

