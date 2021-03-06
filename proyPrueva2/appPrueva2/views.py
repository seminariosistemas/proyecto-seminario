from appPrueva2.models import *
from appPrueva2.forms import *
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect
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


from django.utils import simplejson
from django.db.models import Q





def inicio(request):
    tipoproyect = tipoproyecto.objects.all()

    proyect = proyecto.objects.filter(Q(estadoproyecto="en_ejecucion")|Q(estadoproyecto="Postergado"))

    form=UbicacionForm()
    ubicaciones =proyecto.objects.all()

    if request.method == 'POST':
        fUbicacion = regproyectoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
    else:
        formulario = regproyectoForm()


    return render_to_response('inicio.html', {'tipoproyecto': tipoproyect, 'proyecto': proyect,'form': formulario,'ubicaciones':ubicaciones},
                              context_instance=RequestContext(request))



def ingresar(request):
    if not request.user.is_anonymous():
        u=request.user.id
        dato=encargadoemp.objects.filter(usuario=u).exists()
        if dato:
            return HttpResponseRedirect('/privadoencempresa')
        else:
            dato=poblacion.objects.filter(usuario=u).exists()
            if dato:
                return HttpResponseRedirect('/privadousuario')
            else:
                dato=encargadopref.objects.filter(usuario=u).exists()
                if dato:
                    return HttpResponseRedirect('/privadoencprefectra')
                else:
                    return HttpResponseRedirect('/privadoadministrador')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    u=request.user.id
                    dato=encargadoemp.objects.filter(usuario=u).exists()
                    if dato:
                        return HttpResponseRedirect('/privadoencempresa')
                    else:
                        dato=poblacion.objects.filter(usuario=u).exists()
                        if dato:
                            return HttpResponseRedirect('/privadousuario')
                        else:
                            dato=encargadopref.objects.filter(usuario=u).exists()
                            if dato:
                                return HttpResponseRedirect('/privadoencprefectra')
                            else:
                                return HttpResponseRedirect('/privadoadministrador')
                else:
                    return render_to_response('noactivo.html', context_instance=RequestContext(request))
            else:
                return render_to_response('nousuario.html', context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('ingresar.html', {'formulario': formulario}, context_instance=RequestContext(request))


@login_required(login_url='/ingresar')
def privadousuario(request):
    usuario = request.user
    return render_to_response('privadousuariocomun.html', {'usuario': usuario},context_instance=RequestContext(request))
@login_required(login_url='/ingresar')
def privadoencempresa(request):
    usuario = request.user
    return render_to_response('privadoencempresa.html', {'usuario': usuario},context_instance=RequestContext(request))
@login_required(login_url='/ingresar')
def privadoencprefectura(request):
    usuario = request.user
    return render_to_response('privadoencpref.html', {'usuario': usuario},context_instance=RequestContext(request))
@login_required(login_url='/ingresar')
def privadoadministrador(request):

    tipoproyect = tipoproyecto.objects.all()
    proyect = proyecto.objects.all()
    usuario = request.user
    return render_to_response('privadoadministrador.html', {'usuario': usuario,'tipoproyecto': tipoproyect, 'proyecto': proyect},context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')
def mostrar_proyectos(request):
    tipoproyect = tipoproyecto.objects.all()
    proyect = proyecto.objects.all()
    return render_to_response('mostrarproyectos.html', {'tipoproyecto': tipoproyect, 'proyecto': proyect},context_instance=RequestContext(request))

def detalle_proyecto(request, id_proyecto):
    dato = get_object_or_404(proyecto, pk=id_proyecto)
    comentarios = comentario.objects.filter(proyecto=dato)
    informes = informesemanal.objects.filter(proyecto=dato)
    avan=informesemanal.objects.filter(proyecto=dato).last()


    if request.method == "POST":
        form = comentarioForm(request.POST)
        if form.is_valid:
            texto = request.POST["comentar"]
            u = request.user
            p = comentario(comentar=texto,
                           usuario=u,
                           proyecto=dato,
            )
            p.save()
            url = '/proyecto/' + str(dato.id)
            return HttpResponseRedirect(url)
    else:
        form = comentarioForm()
    return render_to_response("proyecto.html",{"informes": informes, "formul": form, "proyecto": dato, "comentarios": comentarios,"avanc":avan},context_instance=RequestContext(request))

def nuevo_comentario(request):
    if request.user.is_authenticated():

        if request.method == "POST":
            form = comentarioForm(request.POST)
            if form.is_valid:
                texto = request.POST["comentar"]
                u = request.user
                
                p = comentario(comentar=texto,
                               usuario=u,
                )
                p.save()

                return HttpResponseRedirect('/')
        else:
            form = comentarioForm()
        return render_to_response('nuevocomentario.html', {'formulario': form}, RequestContext(request))
    else:
        return HttpResponseRedirect("/")
def reg_poblacion(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        formulario2 = poblacionForm(request.POST)
        if formulario.is_valid() and formulario2.is_valid():
            formulario.save()
            usuario = request.POST['username']
            nombre = request.POST['nombre']
            ci = request.POST['ci']
            email = request.POST['email']
            u = User.objects.get(username=usuario)
            u.email = email
            u.save()
            poblacion.objects.create(nombre=nombre, ci=ci, usuario=u)
            return HttpResponseRedirect('/registradoexito') 
    else:
        formulario = UserCreationForm()
        formulario2 = poblacionForm()
    return render_to_response("regpoblacion.html", {'formulario': formulario, 'formulario2': formulario2},
                              context_instance=RequestContext(request))
@login_required(login_url='/ingresar')
def reg_tipoproy(request):
    if request.method == "POST":
        form = comentarioForm(request.POST)
        if form.is_valid:
            texto = request.POST["nombre"]
            a = request.user
            x = a.id
            u = encargadopref.objects.get(usuario=x)

            p = tipoproyecto(nombre=texto,
                             encargadopref=u,
            )
            p.save()

            return HttpResponseRedirect('/')
    else:
        form = tipoproyForm()
    return render_to_response('regtipoproy.html', {'formulario': form}, RequestContext(request))
@login_required(login_url='/ingresar')
def reg_encpref(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        formulario2 = regencprefForm(request.POST)
        if formulario.is_valid() and formulario2.is_valid():
            formulario.save()

            usuario = request.POST['username']

            u = User.objects.get(username=usuario)

            uss = request.POST['nombre']

            encargadopref.objects.create(nombre=uss, estado="Activo", usuario=u)
            return HttpResponseRedirect('/registradoexito')
    else:
        formulario = UserCreationForm()
        formulario2 = regencprefForm()

    return render_to_response("reg_encpref.html", {'formulario': formulario, 'formulario2': formulario2},
                              context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def reg_proyecto(request):
    if request.method == 'POST':
        formulario3 = regproyectoForm(request.POST)
        formulario1 = UserCreationForm(request.POST)
        formulario2 = regencempForm(request.POST)
        if formulario1.is_valid() and formulario2.is_valid() and formulario3.is_valid():
            a = request.user
            x = a.id
            u = encargadopref.objects.get(usuario=x)


            formulario1.save()

            yy = request.POST["username"]
            y = User.objects.get(username=yy)
            z = y.id

            p = encargadoemp(
                nombre=formulario2.cleaned_data["nombre"],
                estado=formulario2.cleaned_data["estado"],
                usuario=y,
            )
            p.save()
            z = encargadoemp.objects.get(usuario=z)

            q = proyecto(
                nombreproyecto=formulario3.cleaned_data["nombreproyecto"],
                nombreempresa=formulario3.cleaned_data["nombreempresa"],
                costo=formulario3.cleaned_data["costo"],
                estadoproyecto=formulario3.cleaned_data["estadoproyecto"],

                lng=formulario3.cleaned_data["lng"],
                lat=formulario3.cleaned_data["lat"],

                encargadoemp=z,
                encargadopref=u,
                tipoproyecto=formulario3.cleaned_data["tipoproyecto"],
            )
            q.save()
            return HttpResponseRedirect('/registradoexito')
    else:
        formulario3 = regproyectoForm()
        formulario1 = UserCreationForm()
        formulario2 = regencempForm()
    return render_to_response("regproyecto.html",
                              {'formulario1': formulario1, 'formulario2': formulario2, 'formulario3': formulario3},
                              context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def reg_infsemanal(request):
    a = request.user
    u = encargadoemp.objects.get(usuario=a.id)

    dato =u
    suproyecto=proyecto.objects.get(encargadoemp=u)

    if request.method == 'POST':
        formulario = informesemanalForm(request.POST, request.FILES)
        if formulario.is_valid():
            av=request.POST["avanceobra"]
            im=formulario.cleaned_data["imagen"]
            informesemanal.objects.create(imagen=im,comentario=request.POST["comentario"], avanceobra=av,proyecto=suproyecto)
            return HttpResponseRedirect('/registradoexito')
    else:
        formulario = informesemanalForm()
    return render_to_response("reginforme.html",{'dato': dato,"suproyecto":suproyecto,"formulario":formulario},context_instance=RequestContext(request))

def buscar(request):
    if request.method=="POST":
        texto=request.POST["tbuscar"]
        proy=proyecto.objects.filter(nombreproyecto__contains=texto)
        html="<ul>"
        for i in proy:
            html=html+"<li> <a> <a href='/proyecto/"+str(i.id)+"'>" +str(i.nombreproyecto)+ "</a> </li>"
        html=html+"</ul>"
        return HttpResponse(html)
    else:
        return HttpResponse("NADA")

def registroexit(request):
    return render_to_response("registradoexito.html",context_instance=RequestContext(request))













@login_required(login_url='/ingresar')
def operacionesproyecto(request):
    a = request.user
    u = encargadoemp.objects.get(usuario=a.id)
    proyectos = proyecto.objects.get(encargadoemp=u)
    pro=proyecto.objects.all()
    if request.method == 'POST':
        formulario = operacionesProyecto(request.POST)
        if formulario.is_valid():
            proyecto.objects.filter(id=proyectos.id).update(costo=request.POST["costo"],nombreproyecto=request.POST["nombreproyecto"],nombreempresa=request.POST["nombreempresa"],estadoproyecto=request.POST["estadoproyecto"])
            return HttpResponseRedirect('/registradoexito') 
    else:
        formulario = operacionesProyecto()
    return render_to_response("operacionesproyecto.html", {'formulario': formulario, "proyectos": proyectos,"pro":pro},
                          context_instance=RequestContext(request))

#----------------------------
def coords_save(request):
    if request.method == 'POST':
        fUbicacion = regproyectoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
    else:
        formulario = regproyectoForm()
    return render_to_response("mapa.html", {'form': formulario},context_instance=RequestContext(request))
#-----------------------------
@login_required(login_url='/ingresar')
def dardebajaproyecto(request):
    pro = proyecto.objects.filter(Q(estadoproyecto="en_ejecucion")|Q(estadoproyecto="Postergado"))
    if request.method == 'POST':
        var=proyecto.objects.get(id=request.POST["buscar"])

        proyecto.objects.filter(id=var.id).update(estadoproyecto="Terminado")
        return HttpResponseRedirect('/registradoexito') 
    return render_to_response("darbajaproyecto.html", {"pro":pro},context_instance=RequestContext(request))


@login_required(login_url='/ingresar')
def editarproyecto(request, id_proyecto):
    dato = get_object_or_404(proyecto, pk=id_proyecto)
    if request.method == "POST":
        formulario = editarProyectoForm(request.POST)
        if formulario.is_valid():

            proyecto.objects.filter(id=dato.id).update(costo=request.POST["costo"],nombreproyecto=request.POST["nombreproyecto"],nombreempresa=request.POST["nombreempresa"],estadoproyecto=request.POST["estadoproyecto"])
            return HttpResponseRedirect('/registradoexito') 
    else:
        formulario = editarProyectoForm()
    return render_to_response("editarproyecto.html",{"formulario":formulario,"proyecto": dato}, context_instance=RequestContext(request))














def mostrarmapa(request):
    tipoproyect = tipoproyecto.objects.all()

    proyect = proyecto.objects.filter(Q(estadoproyecto="en_ejecucion")|Q(estadoproyecto="Postergado"))

    form=UbicacionForm()
    ubicaciones =proyecto.objects.all()

    if request.method == 'POST':
        fUbicacion = regproyectoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
    else:
        formulario = regproyectoForm()


    return render_to_response('mostrarmapa.html', {'tipoproyecto': tipoproyect, 'proyecto': proyect,'form': formulario,'ubicaciones':ubicaciones},
                              context_instance=RequestContext(request))