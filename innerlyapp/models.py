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
    
class Registro(models.Model):

    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    dataCriacao = models.DateField(unique=True)
    nivelHumor = models.SmallIntegerField()
    anotacao = models.TextField()
    dataString = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if not self.dataString:
            self.dataString = self.dataCriacao.strftime("%d/%m/%Y")
        super().save(*args, **kwargs)

    def toString(self):

        valueNivel = ['muito mal', 'mal', 'mais ou menos', 'bem', 'muito bem']

        return {
            'nomeusuario' : Usuario.objects.get(id=self.idUsuario).nome,
            'data' : self.dataString,
            'valuehumor' : self.nivelHumor,
            'stringhumor' : valueNivel[self.nivelHumor -1],
            'anotacao' : self.anotacao
        }

    def __str__(self):
        return f'{self.dataString} - detalhes'