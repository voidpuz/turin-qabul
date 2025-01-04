from django.contrib import admin

from .models import Admission, Country, Program


@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'program', 'phone_number')
    search_fields = ('first_name', 'last_name', 'phone_number')
    list_filter = ('program', 'gender')
    list_per_page = 50



@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    pass