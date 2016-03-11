from django.contrib import admin

from leaflet import admin as leaflet_admin

from . import models


class SSIDAdmin(admin.ModelAdmin):
    pass


class ProjectAdmin(leaflet_admin.LeafletGeoAdmin):
    list_display = ('name', 'is_default')

admin.site.register(models.SSID, SSIDAdmin)
admin.site.register(models.Project, ProjectAdmin)
