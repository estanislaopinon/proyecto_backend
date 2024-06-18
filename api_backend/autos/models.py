from django.db import models


class Marca(models.Model):

    nombre = models.CharField(max_length=128)
    # user_id

    def __str__(self):
        return f' {self.nombre}'


class Auto(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=128)
    anio = models.IntegerField()
    color = models.CharField(max_length=20)

    # user_id

    def __str__(self):
        return f' - {self.modelo}'


class Usuario(models.Model):
    nombre = models.CharField(max_length=128)
    autos = models.ManyToManyField(Auto, blank=True)

    def __str__(self):
        return self.nombre


class PropiedadAuto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    fecha_adquisicion = models.DateField()

    def __str__(self):
        return f'{self.usuario.nombre} posee {self.auto.modelo} desde {self.fecha_adquisicion}'
# Create your models here.
