# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm



class poblacion(models.Model):
    nombre = models.CharField(max_length=100)
    ci=models.IntegerField()
    usuario=models.ForeignKey(User,unique=True)
    def __unicode__(self):
        return self.nombre

class encargadoemp(models.Model):
    nombre = models.CharField(max_length=100)
    SHIRT_SIZES = (
        ('activo', 'activo'),
        ('DeBaja', 'DeBaja'),
    )
    estado = models.CharField(max_length=20, choices=SHIRT_SIZES)
    usuario=models.ForeignKey(User,unique=True)
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
    usuario=models.ForeignKey(User,unique=True)
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
    nombreproyecto = models.CharField(max_length=100)
    nombreempresa = models.CharField(max_length=100)
    fechainicio = models.DateTimeField(auto_now_add=True)
    fechaconclucion = models.DateTimeField(auto_now_add=True)
    fecharegistro = models.DateTimeField(auto_now_add=True)
    costo=models.IntegerField()
    estadoproyecto = models.CharField(max_length=20, choices=SHIRT_SIZES)

    coordenadas = models.CharField(max_length=100)

    lat=models.CharField(max_length=50)
    lng=models.CharField(max_length=50)



    encargadoemp = models.ForeignKey(encargadoemp,unique=True)
    encargadopref = models.ForeignKey(encargadopref)
    tipoproyecto = models.ForeignKey(tipoproyecto)
    def __unicode__(self):
        return self.nombreproyecto






class informesemanal(models.Model):
    imagen = models.ImageField(upload_to='proyectos', verbose_name='Imágen')
    comentario = models.TextField(max_length=100)
    fechapublicacion = models.DateTimeField(auto_now_add=True)
    avanceobra = models.IntegerField()
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





#------------------------------------------------------------

class Ubicacion(models.Model):

    nombreproyecto = models.CharField(max_length=100)

    lat=models.CharField(max_length=50)
    lng=models.CharField(max_length=50)

    encargadopref = models.ForeignKey(encargadopref)


    def __unicode__ (self):
        return self.nombreproyecto


class UbicacionForm(ModelForm):
    class Meta:
        model=Ubicacion

        


