from django.db import models


class Paes(models.Model):
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo


class Carnes(models.Model):
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo


class Opcionais(models.Model):
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo


class Status_burguer(models.Model):
    tipo = models.CharField(max_length=20, default='Solicitado')

    def __str__(self):
        return self.tipo


class Burguers(models.Model):
    cliente = models.CharField(max_length=20)
    paes = models.ForeignKey(Paes, on_delete=models.DO_NOTHING)
    carne = models.ForeignKey(Carnes, on_delete=models.DO_NOTHING)
    opcionais = models.ManyToManyField(Opcionais)
    status_burguer = models.ForeignKey(
        Status_burguer, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.cliente
