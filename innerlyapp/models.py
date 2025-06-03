from django.db import models

# Create your models here.

class Usuario(models.Model):

    nome = models.CharField(max_length=255)
    dataNascimento = models.DateField()
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    contato = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nome
