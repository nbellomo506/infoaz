from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
from .models import User
from .models import Azienda  # add this
from .models import DatiComune  # add this
from .models import CostoSmaltimento  # add this

class UserAdmin(BaseUserAdmin):
    #visualizzazione dati utente
    list_display = ('email','azienda','titolo','nome','cognome')
    list_filter = ('is_admin',)

    #modifica dati utente
    fieldsets = (
        ("Azienda", {'fields': ('azienda',('ragione_sociale','p_iva'))}),
        ("Dati Generali", {'fields': ('nome', 'cognome','email','email2','titolo','telefono','request_date','verification_code','verified')}),
        ('Permissions', {'fields': ('is_assigned','is_admin', 'is_staff','is_active')}),

    )

    #aggiunta utente
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.register(Azienda) # add this
admin.site.register(DatiComune) # add this
admin.site.register(CostoSmaltimento) # add this
