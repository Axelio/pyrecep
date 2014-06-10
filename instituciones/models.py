# *-* coding: utf-8 *-*
from django.db import models

class Institucion(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.TextField(blank=True,
        verbose_name=u'dirección')
    
    class Meta:
        db_table = 'institucion'
        verbose_name = u'institución'
        verbose_name_plural = u'instituciones'

    def __unicode__(self):
        return u'%s' % (self.nombre)
