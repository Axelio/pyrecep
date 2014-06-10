from django.contrib import admin
from models import Visita

class VisitaAdmin(admin.ModelAdmin):
    list_display = ('persona', 'institucion',
        'proyecto', 'fecha')
    list_filter = ('institucion', 'proyecto', 'fecha')
admin.site.register(Visita, VisitaAdmin)
