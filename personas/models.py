# *-* coding: utf-8 *-*
from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    direccion = models.TextField(blank=True,
        verbose_name=u'dirección')
    telefono_1 = models.IntegerField()
    telefono_2 = models.IntegerField(blank=True, null=True)
    
    class Meta:
        db_table = 'personas'

    def __unicode__(self):
        return u'%s %s' % (self.nombre, self.apellido)
