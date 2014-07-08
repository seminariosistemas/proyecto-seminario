from django.forms import ModelForm
from django import forms
from appPrueva2.models import *

class comentarioForm(forms.Form):

    comentar=forms.CharField(widget=forms.Textarea)
 
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
        fields=["nombreproyecto","nombreempresa","lat","lng","costo","estadoproyecto","tipoproyecto"]


class regencempForm(ModelForm):
    class Meta():
		model=encargadoemp
		fields=["nombre","estado"]


class informesemanalForm(ModelForm):
    class Meta():
        model = informesemanal
        fields=["imagen","comentario","avanceobra"]











class operacionesProyecto(ModelForm):
    class Meta():
        model = proyecto
        fields=["nombreproyecto","nombreempresa","costo","estadoproyecto"]


class operacionesProyecto1(ModelForm):
    class Meta():
        model = proyecto
        fields=["estadoproyecto"]

class editarProyectoForm(ModelForm):
    class Meta():
        model = proyecto
        fields=["nombreproyecto","nombreempresa","costo","estadoproyecto"]


class editarUsuarioForm(ModelForm):
    class Meta():
        model = User
        fields=["username"]
