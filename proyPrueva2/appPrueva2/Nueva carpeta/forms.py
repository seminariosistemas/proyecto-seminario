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



class regencprefForm(forms.Form):
    nombre=forms.CharField(required=True)




SHIRT_SIZES = (
        ('en_ejecucion', 'en_ejecucion'),
        ('Terminado', 'Terminado'),
        ('Postergado', 'Postergado'),
    )
class regproyectoForm(ModelForm):
    class Meta():
		model=proyecto
		fields=["nombre","nombreempresa","coordenadas","costo","estado","tipoproyecto"]

