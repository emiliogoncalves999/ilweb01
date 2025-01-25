from django.contrib import admin
from django.utils.html import format_html
from .models import (
    PerfilParoquiaSAJOBRIL,
    Congregacao,
    EskolaCatolico,
    GrupuCategorial,
    ProfessorReligiaoCatolico,
    PadreMadre,
    EisSeminaristaExReligioso,
)

class PerfilParoquiaSAJOBRILAdmin(admin.ModelAdmin):
    exclude = ('user_created', 'is_deleted', 'date_created', 'date_modified')
    list_display = ('visao_geral', 'display_area_geografica', 'display_ecp')

    def display_area_geografica(self, obj):
        if obj.area_geografica:
            return format_html('<img src="{}" width="100" height="auto" />', obj.area_geografica.url)
        return "No Image"
    display_area_geografica.short_description = "Área Geográfica"

    def display_ecp(self, obj):
        if obj.ecp:
            return format_html('<img src="{}" width="100" height="auto" />', obj.ecp.url)
        return "No Image"
    display_ecp.short_description = "ECP Image"

class CongregacaoAdmin(admin.ModelAdmin):
    exclude = ('user_created', 'is_deleted', 'date_created', 'date_modified')
    list_display = ('nome', 'deskrisau', 'display_file_link')

    def display_file_link(self, obj):
        if obj.file:
            return format_html('<a href="{}">Download</a>', obj.file.url)
        return "No File"
    display_file_link.short_description = "File"

class EskolaCatolicoAdmin(admin.ModelAdmin):
    exclude = ('user_created', 'is_deleted', 'date_created', 'date_modified')
    list_display = ('nome', 'deskrisau', 'display_file_link')

    def display_file_link(self, obj):
        if obj.file:
            return format_html('<a href="{}">Download</a>', obj.file.url)
        return "No File"
    display_file_link.short_description = "File"

class GrupuCategorialAdmin(admin.ModelAdmin):
    exclude = ('user_created', 'is_deleted', 'date_created', 'date_modified')
    list_display = ('nome', 'deskrisau', 'display_file_link')

    def display_file_link(self, obj):
        if obj.file:
            return format_html('<a href="{}">Download</a>', obj.file.url)
        return "No File"
    display_file_link.short_description = "File"

class ProfessorReligiaoCatolicoAdmin(admin.ModelAdmin):
    exclude = ('user_created', 'is_deleted', 'date_created', 'date_modified')
    list_display = ('nome', 'fatinserviço','estatuto', 'display_foto')

    def display_foto(self, obj):
        if obj.foto:
            return format_html('<img src="{}" width="100" height="auto" />', obj.foto.url)
        return "No Image"
    display_foto.short_description = "Foto"

class PadreMadreAdmin(admin.ModelAdmin):
    exclude = ('user_created', 'is_deleted', 'date_created', 'date_modified')
    list_display = ('nome', 'tipo', 'fatinnodataordenacao','fatinservico', 'descricao','display_foto')

    def display_foto(self, obj):
        if obj.foto:
            return format_html('<img src="{}" width="100" height="auto" />', obj.foto.url)
        return "No Image"
    display_foto.short_description = "Foto"

class EisSeminaristaExReligiosoAdmin(admin.ModelAdmin):
    exclude = ('user_created', 'is_deleted', 'date_created', 'date_modified')
    list_display = ('nome', 'estadoeivil','contacto','descricao', 'display_foto')

    def display_foto(self, obj):
        if obj.foto:
            return format_html('<img src="{}" width="100" height="auto" />', obj.foto.url)
        return "No Image"
    display_foto.short_description = "Foto"

# Register the admin classes
admin.site.register(PerfilParoquiaSAJOBRIL, PerfilParoquiaSAJOBRILAdmin)
admin.site.register(Congregacao, CongregacaoAdmin)
admin.site.register(EskolaCatolico, EskolaCatolicoAdmin)
admin.site.register(GrupuCategorial, GrupuCategorialAdmin)
admin.site.register(ProfessorReligiaoCatolico, ProfessorReligiaoCatolicoAdmin)
admin.site.register(PadreMadre, PadreMadreAdmin)
admin.site.register(EisSeminaristaExReligioso, EisSeminaristaExReligiosoAdmin)
