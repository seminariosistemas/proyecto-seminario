# coding=utf-8
from django.db import models
from django.contrib.auth.models import User



class poblacion(models.Model):
    nombre = models.CharField(max_length=100)
    ci=models.IntegerField()
    usuario=models.ForeignKey(User)
    def __unicode__(self):
        return self.nombre

class encargadoemp(models.Model):
    nombre = models.CharField(max_length=100)
    SHIRT_SIZES = (
        ('activo', 'activo'),
        ('viaje', 'viaje'),
    )
    estado = models.CharField(max_length=20, choices=SHIRT_SIZES)
    usuario=models.ForeignKey(User)
    def __unicode__(self):
        return self.nombre


class encargadopref(models.Model):
    nombre = models.CharField(max_length=100)
    opciones = (
        ('Activo', 'Activo'),
        ('DeBaja', 'DeBaja'),
        ('Vacacion', 'Vacacion'),
    )
    estado = models.CharField(max_length=20, choices=opciones)
    usuario=models.ForeignKey(User)
    def __unicode__(self):
        return self.nombre







class tipoproyecto(models.Model):
    nombre = models.CharField(max_length=100)
    encargadopref = models.ForeignKey(encargadopref)
    def __unicode__(self):
        return self.nombre

class proyecto(models.Model):
    SHIRT_SIZES = (
        ('en_ejecucion', 'en_ejecucion'),
        ('Terminado', 'Terminado'),
        ('Postergado', 'Postergado'),
    )
    nombre = models.CharField(max_length=100)
    nombreempresa = models.CharField(max_length=100)
    fechainicio = models.DateTimeField(auto_now=True)
    fechaconclucion = models.DateTimeField(auto_now=True)
    fecharegistro = models.DateTimeField(auto_now_add=True)
    costo=models.FloatField()
    estado = models.CharField(max_length=20, choices=SHIRT_SIZES)
    coordenadas=models.CharField(max_length=100)
    encargadopref = models.ForeignKey(encargadopref)
    tipoproyecto = models.ForeignKey(tipoproyecto)
    def __unicode__(self):
        return self.nombre






class informesemanal(models.Model):
    imagen = models.ImageField(upload_to='proyectos', verbose_name='Imágen')
    comentario = models.TextField(max_length=100)
    fechapublicacion = models.DateTimeField(auto_now_add=True)
    avanceobra = models.FloatField()
    encargadoemp = models.ForeignKey(encargadoemp)
    proyecto = models.ForeignKey(proyecto)
    def __unicode__(self):
		return self.comentario




class comentario(models.Model):
    comentar = models.TextField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User)
    proyecto = models.ForeignKey(proyecto)
    def __unicode__(self):
		return self.comentar

















