# *-* coding: utf-8 *-*
from django.db import models
from personas.models import Persona
from instituciones.models import Institucion

class Visita(models.Model):
    persona = models.ForeignKey(Persona)
    institucion = models.ForeignKey(Institucion,
        verbose_name=u'institución')
    proyecto = models.CharField(max_length=50, blank=True)
    observacion = models.TextField(blank=True, verbose_name=u'observación')
    fecha = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'visita'

    def __unicode__(self):
        return u'%s - %s' % (self.persona, self.institucion)
