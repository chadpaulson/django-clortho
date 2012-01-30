from django.contrib import admin
from clortho.models import Keymaster


class KeymasterAdmin(admin.ModelAdmin):
    list_display = ('user', 'service', 'key')
    search_fields = ['user__username', 'user__first_name',
                     'user__last_name']
    ordering = ('id',)


admin.site.register(Keymaster, KeymasterAdmin)
