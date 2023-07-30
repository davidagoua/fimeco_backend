from django.contrib import admin
from core import models
# Register your models here.



@admin.register(models.District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['id','nom','slug']


@admin.register(models.Circuit)
class CircuitAdmin(admin.ModelAdmin):
    list_display = ['id','nom','slug','district']


@admin.register(models.EgliseLocal)
class EgliseLocalAdmin(admin.ModelAdmin):
    list_display = ['id','nom']


@admin.register(models.Famille)
class FamilleAdmin(admin.ModelAdmin):
    pass 


@admin.register(models.Membre)
class MembreAdmin(admin.ModelAdmin):
    list_display = ['nom','prenoms','famille','date_naissance'] 


@admin.register(models.SouscriptionIndividu)
class SouscriptionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Paiement)
class PaiementAdmin(admin.ModelAdmin):
    pass
