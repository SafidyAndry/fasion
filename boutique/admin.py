from django.contrib import admin
from .models import Produit, ContactMessage


@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'couleurs', 'tailles', 'disponible', 'date_ajout')
    list_filter = ('disponible', 'couleurs', 'tailles')
    search_fields = ('nom', 'description')
    list_editable = ('disponible',)
    date_hierarchy = 'date_ajout'
    fieldsets = (
        ('Informations générales', {
            'fields': ('nom', 'description', 'prix', 'image')
        }),
        ('Variantes', {
            'fields': ('couleurs', 'tailles')
        }),
        ('Statut', {
            'fields': ('disponible',)
        }),
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'sujet', 'date_envoi', 'lu')
    list_filter = ('lu', 'date_envoi')
    search_fields = ('nom', 'email', 'sujet', 'message')
    list_editable = ('lu',)
    readonly_fields = ('nom', 'email', 'sujet', 'message', 'date_envoi')
    date_hierarchy = 'date_envoi'


admin.site.site_header = 'Mademoiselle Fashion — Administration'
admin.site.site_title = 'Mademoiselle Fashion'
admin.site.index_title = 'Gestion de la boutique'
