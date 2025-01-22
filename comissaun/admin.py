from django.contrib import admin
from .models import Comissaun, PlanuComisaun
from django.utils.html import format_html

class PlanuComisaunInline(admin.TabularInline):
    """
    Inline admin configuration for PlanuComisaun.
    This allows adding and editing Planus directly from the Comissaun admin page.
    """
    model = PlanuComisaun
    extra = 1
    fields = ['title', 'description', 'file', 'year']


@admin.register(Comissaun)
class ComissaunAdmin(admin.ModelAdmin):
    """
    Admin configuration for Comissaun.
    Includes inline editing of PlanuComisaun, a logo preview, and contact information.
    """
    list_display = ('nome', 'deskrisaun', 'contact', 'logo_preview')
    search_fields = ('nome',)
    inlines = [PlanuComisaunInline]
    fields = ['nome', 'deskrisaun', 'logo', 'contact']  # Add logo and contact fields in admin form

    def logo_preview(self, obj):
        """
        Show a small preview of the Comissaun's logo in the admin list view.
        """
        if obj.logo:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.logo.url)
        return "No Logo"

    logo_preview.short_description = "Logo"
