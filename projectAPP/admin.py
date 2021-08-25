from django.contrib import admin
from projectAPP.models import *

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'city']
    list_per_page = 5

admin.site.register(Person, PersonAdmin)
admin.site.register(Country)
admin.site.register(City)