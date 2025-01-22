from django.contrib import admin
from .models import Planu, DettaluPlano

class DettaluPlanoInline(admin.TabularInline):
    model = DettaluPlano
    extra = 1  # Number of empty forms to display

@admin.register(Planu)
class PlanuAdmin(admin.ModelAdmin):
    list_display = ('nome', 'deskrisaun', 'contact')
    inlines = [DettaluPlanoInline]

# Register DettaluPlano separately if needed, but not displaying it in admin
# @admin.register(DettaluPlano)
class DettaluPlanoAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'planu')  # You can add more fields as necessary
    # If you want to hide it from admin, comment or remove the register line
