from django.contrib import admin
from clortho.models import Facebook

class FacebookAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'uid', 'url')
    search_fields = ['user__username', 'user__first_name',
                     'user__last_name']
    ordering = ('id',)
    
    def full_name(self, obj):
        """
        Shows Some School @ Some school
        """
        return '%s %s' % (obj.user.first_name, obj.user.last_name)
admin.site.register(Facebook, FacebookAdmin)