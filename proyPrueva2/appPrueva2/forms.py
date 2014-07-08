from django.forms import ModelForm
from django import forms
from appPrueva2.models import *


class comentarioForm(forms.Form):

        #o tambien
        #nombre=forms.CharField(required=True)
    comentar=forms.CharField(widget=forms.Textarea)
    #usuario=forms.InlineForeignKeyField()

class poblacionForm(forms.Form):

    nombre=forms.CharField(required=True)
    ci=forms.CharField(required=True)
    email=forms.EmailField(required=True)


class tipoproyForm(forms.Form):
    nombre=forms.CharField(required=True)

#SHIRT_SIZES = (
#        ('en_ejecucion', 'en_ejecucion'),
#        ('Terminado', 'Terminado'),
#        ('Postergado', 'Postergado'),
#    )
class regencprefForm(forms.Form):
    nombre=forms.CharField(required=True)


    #telefono=forms.CharField()
SHIRT_SIZES = (
        ('en_ejecucion', 'en_ejecucion'),
        ('Terminado', 'Terminado'),
        ('Postergado', 'Postergado'),
    )
class regproyectoForm(ModelForm):
    class Meta():
		model=proyecto
		fields=["nombreproyecto","nombreempresa","lat","lng","costo","estadoproyecto","tipoproyecto"]

#class regproyectoForm(forms.Form):

    #nombre = forms.CharField(max_length=100)
    #nombreempresa = forms.CharField(max_length=100)
    #fechainicio = forms.DateTimeField()
    #fechaconclucion = forms.DateTimeField()

    #costo=forms.FloatField()
    #estado = forms.CharField()
    #coordenadas=forms.CharField(max_length=100)

    #tipoproyecto = forms.ModelChoiceField(queryset=tipoproyecto.objects.all())


class regencempForm(ModelForm):
    class Meta():
        model=encargadoemp
        fields=["nombre","estado"]


class informesemanalForm(ModelForm):
    class Meta():
        model = informesemanal
        fields=["imagen","comentario","avanceobra"]


#******esto no pasarles
class operacionesProyecto(ModelForm):
    class Meta():
        model = proyecto
        fields=["nombreproyecto","nombreempresa","costo","estadoproyecto"]



