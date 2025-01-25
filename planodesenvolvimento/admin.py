from django.contrib import admin
from .models import Planu, DettaluPlano


class DettaluPlanoInline(admin.TabularInline):
    model = DettaluPlano
    extra = 1  # Number of empty forms to display
    exclude = ('user_created', 'is_deleted', 'date_created', 'date_modified')  # Exclude BaseModel fields


@admin.register(Planu)
class PlanuAdmin(admin.ModelAdmin):
    list_display = ('nome', 'deskrisaun', 'contact')
    inlines = [DettaluPlanoInline]
    exclude = ('user_created', 'is_deleted', 'date_created', 'date_modified')  # Exclude BaseModel fields


# @admin.register(DettaluPlano)
class DettaluPlanoAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'planu')  # Display relevant fields
    exclude = ('user_created', 'is_deleted', 'date_created', 'date_modified')  # Exclude BaseModel fields
