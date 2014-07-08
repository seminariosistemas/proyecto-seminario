from django.conf.urls import patterns, include, url

from django.contrib import admin


from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from appPrueva2.views import *



admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','appPrueva2.views.inicio'),
    url(r'^ingresar/$', 'appPrueva2.views.ingresar'),
    url(r'^cerrarsesion/$', 'appPrueva2.views.cerrar'),
    url(r'^privadousuario/$', 'appPrueva2.views.privadousuario'),
    url(r'^privadoencempresa/$', 'appPrueva2.views.privadoencempresa'),
    url(r'^privadoencprefectra/$', 'appPrueva2.views.privadoencprefectura'),
    url(r'^privadoadministrador/$', 'appPrueva2.views.privadoadministrador'),
    url(r'^comentar/$', 'appPrueva2.views.nuevo_comentario'),
    url(r'^mostrarproyectos/$', 'appPrueva2.views.mostrar_proyectos'),
    url(r'^proyecto/(?P<id_proyecto>\d+)$','appPrueva2.views.detalle_proyecto'),
    url(r'^registropoblacion/$','appPrueva2.views.reg_poblacion'),
    url(r'^registrotipo/$','appPrueva2.views.reg_tipoproy'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
    url(r'^registroencargadop/$','appPrueva2.views.reg_encpref'),
    url(r'^registroproyecto/$','appPrueva2.views.reg_proyecto'),
    url(r'^registroinforme/$','appPrueva2.views.reg_infsemanal'),
    url(r'^buscar/$','appPrueva2.views.buscar'),
    url(r'^registradoexito/$','appPrueva2.views.registroexit'),


     url(r'^operacionesproyectos/$','appPrueva2.views.operacionesproyecto'),
    url(r'^dardebajaproyecto/$','appPrueva2.views.dardebajaproyecto'),
    url(r'^coords/save/$', 'appPrueva2.views.coords_save'),
    url(r'^editarpro/(?P<id_proyecto>\d+)$','appPrueva2.views.editarproyecto'),
    url(r'^mostrarmapa/$', 'appPrueva2.views.mostrarmapa'),




)
