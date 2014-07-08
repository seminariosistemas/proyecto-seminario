from appPrueva2.models import *
from appPrueva2.forms import *
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404,redirect
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from datetime import *
from django.db import models
from django.forms import *





from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from django.template.context import RequestContext
from django.http.response import HttpResponseRedirect
from models import *
from django.contrib.auth.models import User
from forms import *
from django.core.mail import EmailMessage
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required

from django.db.models import Q
import os
import pdb
import datetime
import csv


def base(request):
    return render_to_response('base.html',context_instance=RequestContext(request))

def inicio(request):
    comentarios=comentario.objects.all()
    return render_to_response('inicio.html',{'comentarios':comentarios})




def ingresar(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/')
    if request.method=='POST':
        formulario=AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario=request.POST['username']
            clave=request.POST['password']
            acceso=authenticate(username=usuario,password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request,acceso)

                    return HttpResponseRedirect('/')
                else:
                    return render_to_response('noactivo.html',context_instance=RequestContext(request))
            else:
                return render_to_response('nousuario.html',context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('ingresar.html',{'formulario':formulario},context_instance=RequestContext(request))





@login_required(login_url='/ingresar')
def privadousuario(request):
    usuario=request.user
    return render_to_response('privadousuariocomun.html',{'usuario':usuario},context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')




def mostrar_proyectos(request):
    tipoproyect=tipoproyecto.objects.all()
    proyect=proyecto.objects.all()
    return render_to_response('mostrarproyectos.html',{'tipoproyecto':tipoproyect,'proyecto':proyect},context_instance=RequestContext(request))





def detalle_proyecto(request,id_proyecto):
    dato=get_object_or_404(proyecto,pk=id_proyecto)
    comentarios=comentario.objects.filter(proyecto=dato)

    informes=informesemanal.objects.filter(proyecto=dato)

    if request.user.is_authenticated():
        if request.method=="POST":
            form=comentarioForm(request.POST)
            if form.is_valid:
                texto=request.POST["comentar"]
                u=request.user
  
                p=comentario(comentar =texto,
                             usuario=u,
                             proyecto=dato,
                            )
                p.save()
                url='/proyecto/'+str(dato.id)
                return HttpResponseRedirect(url)
        else:

            form = comentarioForm()

    return render_to_response("proyecto.html",{"informes":informes,"formul":form,"proyecto":dato,"comentarios":comentarios},context_instance=RequestContext(request))



def nuevo_comentario(request):
    if request.user.is_authenticated():

        if request.method=="POST":
            form=comentarioForm(request.POST)
            if form.is_valid:

                texto=request.POST["comentar"]
                u=request.user

                p=comentario(comentar =texto,
                             usuario=u,
                            )
                p.save()

                return HttpResponseRedirect('/')
        else:
            form = comentarioForm()
        return render_to_response('nuevocomentario.html',{'formulario':form}, RequestContext(request))
    else:
        return HttpResponseRedirect("/")



def reg_poblacion(request):
    if request.method=='POST':
        formulario=UserCreationForm(request.POST)
        formulario2=poblacionForm(request.POST)
        if formulario.is_valid() and formulario2.is_valid():
            formulario.save()
            usuario=request.POST['username']
            nombre=request.POST['nombre']
            ci=request.POST['ci']
            email=request.POST['email']
            u=User.objects.get(username=usuario)
            u.email=email
            u.save()
            poblacion.objects.create(nombre=nombre,ci=ci,usuario=u)
            return render_to_response('mensaje.html',context_instance=RequestContext(request))
    else:
        formulario=UserCreationForm()
        formulario2=poblacionForm()
    return render_to_response("regpoblacion.html",{'formulario':formulario,'formulario2':formulario2},context_instance=RequestContext(request))

def reg_tipoproy(request):
    if request.user.is_authenticated():
        if request.method=="POST":
            form=comentarioForm(request.POST)
            if form.is_valid:
                texto=request.POST["nombre"]
                a=request.user
                x=a.id
                u=encargadopref.objects.get(usuario=x)


                p=tipoproyecto(nombre =texto,
                               encargadopref=u,
                               )
                p.save()

                return render_to_response('mensajetipo.html',context_instance=RequestContext(request))
        else:
            form = tipoproyForm()
        return render_to_response('regtipoproy.html',{'formulario':form}, RequestContext(request))
    else:
        return HttpResponseRedirect("/")





def reg_encpref(request):
    if request.method=='POST':
        formulario=UserCreationForm(request.POST)
        formulario2=regencprefForm(request.POST)
        if formulario.is_valid() and formulario2.is_valid():
            formulario.save()


            usuario=request.POST['username']

            u=User.objects.get(username=usuario)

            uss=request.POST['nombre']


            encargadopref.objects.create(nombre=uss,estado="Activo",usuario=u)
            return render_to_response('mensajeenc.html',context_instance=RequestContext(request))
    else:
        formulario=UserCreationForm()
        formulario2=regencprefForm()

    return render_to_response("reg_encpref.html",{'formulario':formulario,'formulario2':formulario2},context_instance=RequestContext(request))




def reg_proyecto(request):
    if request.method=='POST':
        formulario=regproyectoForm(request.POST)
        if formulario.is_valid():

            a=request.user
            x=a.id
            u=encargadopref.objects.get(usuario=x)

            

            v=encargadopref.objects.get(id=1)

            p=proyecto(
                nombre = formulario.cleaned_data["nombre"],
                nombreempresa = formulario.cleaned_data["nombreempresa"],

                costo=formulario.cleaned_data["costo"],
                estado = formulario.cleaned_data["estado"],
                coordenadas=formulario.cleaned_data["coordenadas"],
                encargadopref = u,
                tipoproyecto = formulario.cleaned_data["tipoproyecto"],
                )

            p.save()
            return render_to_response('mensajeproy.html',context_instance=RequestContext(request))
    else:
        formulario=regproyectoForm()
    return render_to_response("regproyecto.html",{'formulario':formulario,},context_instance=RequestContext(request))













