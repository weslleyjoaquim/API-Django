from django.db import models

class Grupo(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    dataCriacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    sexo = models.CharField(max_length=15)
    email = models.EmailField
    telefone = models.CharField(max_length=20)
    pais = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=255)
    logradouro = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    grupo = models.ForeignKey(Grupo, related_name="Groups", on_delete=models.CASCADE)

    def __str__(self):
        return self.name