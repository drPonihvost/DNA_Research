from django.contrib import admin
from .models import *

class ResearchAdmin(admin.ModelAdmin):
    list_display = ('id', )


admin.site.register(Research)
admin.site.register(Person)


