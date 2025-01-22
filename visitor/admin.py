from django.contrib import admin
from django.utils.html import format_html
from django.urls import path
from django.shortcuts import render
from log.models import LogEntry

from .models import AnnualPlan, Author, Noticia, Atividade, Eventu, Missa, Aunsiu, Atendimentu, Attachment

class MyAdminSite(admin.AdminSite):
    site_header = 'My Custom Admin'
    site_title = 'My Admin'
    index_title = 'Dashboard'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_view(self.dashboard_view)),
        ]
        return custom_urls + urls

    def dashboard_view(self, request):
        # Calculate your custom counts here
        return render(request, 'visitor/dashboard.html')

class AttachmentInline(admin.TabularInline):
    model = Attachment
    extra = 1
    max_num = 5  # Adjust the maximum number of files if needed
    fields = ('file',)


class NoticiaAdmin(admin.ModelAdmin):
    readonly_fields = ('is_deleted', 'date_created', 'date_modified', 'image_tag')
    list_display = ('image_tag', 'title', 'date_published', 'edit_link', 'delete_link')
    inlines = [AttachmentInline]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj is None:
            form.base_fields.pop('user_created', None)
        return form

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user_created = request.user
        super().save_model(request, obj, form, change)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
        return 'No Image'
    image_tag.short_description = 'Image'

    def edit_link(self, obj):
        return format_html('<a href="{}">Edit</a>', obj.get_admin_url())
    edit_link.short_description = 'Edit'
    
    def delete_link(self, obj):
        return format_html('<a href="{}">Delete</a>', obj.get_admin_url())
    delete_link.short_description = 'Delete'

class AtividadeAdmin(admin.ModelAdmin):
    readonly_fields = ('is_deleted', 'date_created', 'date_modified', 'image_tag')
    list_display = ('name', 'date', 'image_tag', 'edit_link', 'delete_link')
    inlines = [AttachmentInline]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj is None:
            form.base_fields.pop('user_created', None)
        return form

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user_created = request.user
        super().save_model(request, obj, form, change)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="40" height="40" />', obj.image.url)
        return 'No Image'
    image_tag.short_description = 'Image'

    def edit_link(self, obj):
        return format_html('<a href="{}">Edit</a>', obj.get_admin_url())
    edit_link.short_description = 'Edit'
    
    def delete_link(self, obj):
        return format_html('<a href="{}">Delete</a>', obj.get_admin_url())
    delete_link.short_description = 'Delete'

class EventuAdmin(admin.ModelAdmin):
    readonly_fields = ('is_deleted', 'date_created', 'date_modified', 'image_tag')
    list_display = ('name', 'date', 'image_tag', 'edit_link', 'delete_link')
    inlines = [AttachmentInline]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj is None:
            form.base_fields.pop('user_created', None)
        return form

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user_created = request.user
        super().save_model(request, obj, form, change)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
        return 'No Image'
    image_tag.short_description = 'Image'

    def edit_link(self, obj):
        return format_html('<a href="{}">Edit</a>', obj.get_admin_url())
    edit_link.short_description = 'Edit'
    
    def delete_link(self, obj):
        return format_html('<a href="{}">Delete</a>', obj.get_admin_url())
    delete_link.short_description = 'Delete'

class MissaAdmin(admin.ModelAdmin):
    readonly_fields = ('is_deleted', 'date_created', 'date_modified', 'image_tag')
    list_display = ('title', 'priest', 'image_tag', 'edit_link', 'delete_link')
    inlines = [AttachmentInline]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj is None:
            form.base_fields.pop('user_created', None)
        return form

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user_created = request.user
        super().save_model(request, obj, form, change)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" />', obj.image.url)
        return 'No Image'
    image_tag.short_description = 'Image'

    def edit_link(self, obj):
        return format_html('<a href="{}">Edit</a>', obj.get_admin_url())
    edit_link.short_description = 'Edit'
    
    def delete_link(self, obj):
        return format_html('<a href="{}">Delete</a>', obj.get_admin_url())
    delete_link.short_description = 'Delete'

class AunsiuAdmin(admin.ModelAdmin):
    readonly_fields = ('is_deleted', 'date_created', 'date_modified', 'image_tag')
    list_display = ('title', 'date_published', 'image_tag', 'edit_link', 'delete_link')
    inlines = [AttachmentInline]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj is None:
            form.base_fields.pop('user_created', None)
        return form

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user_created = request.user
        super().save_model(request, obj, form, change)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="30px" />', obj.image.url)
        return 'No Image'
    image_tag.short_description = 'Image'

    def edit_link(self, obj):
        return format_html('<a href="{}">Edit</a>', obj.get_admin_url())
    edit_link.short_description = 'Edit'
    
    def delete_link(self, obj):
        return format_html('<a href="{}">Delete</a>', obj.get_admin_url())
    delete_link.short_description = 'Delete'

class AtendimentuAdmin(admin.ModelAdmin):
    readonly_fields = ('is_deleted', 'date_created', 'date_modified', 'image_tag')
    list_display = ('name', 'date', 'image_tag', 'edit_link', 'delete_link')
    inlines = [AttachmentInline]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj is None:
            form.base_fields.pop('user_created', None)
        return form

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user_created = request.user
        super().save_model(request, obj, form, change)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
        return 'No Image'
    image_tag.short_description = 'Image'

    def edit_link(self, obj):
        return format_html('<a href="{}">Edit</a>', obj.get_admin_url())
    edit_link.short_description = 'Edit'
    
    def delete_link(self, obj):
        return format_html('<a href="{}">Delete</a>', obj.get_admin_url())
    delete_link.short_description = 'Delete'

# class AnnualPlanAdmin(admin.ModelAdmin):
#     readonly_fields = ('is_deleted', 'date_created', 'date_modified')
#     list_display = ('title', 'start_date', 'end_date', 'edit_link', 'delete_link','image_tag')
#     inlines = [AttachmentInline]

#     def get_form(self, request, obj=None, **kwargs):
#         form = super().get_form(request, obj, **kwargs)
#         if obj is None:
#             form.base_fields.pop('user_created', None)
#         return form

#     def save_model(self, request, obj, form, change):
#         if not change:
#             obj.user_created = request.user
#         super().save_model(request, obj, form, change)

#     def image_tag(self, obj):
#         if obj.image:
#             return format_html('<img src="{}" width="40" height="40" />', obj.image.url)
#         return 'No Image'
    
#     image_tag.short_description = 'Image'

#     def edit_link(self, obj):
#         return format_html('<a href="{}">Edit</a>', obj.get_admin_url())
#     edit_link.short_description = 'Edit'
    
#     def delete_link(self, obj):
#         return format_html('<a href="{}">Delete</a>', obj.get_admin_url())
#     delete_link.short_description = 'Delete'


admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Atividade, AtividadeAdmin)
admin.site.register(Eventu, EventuAdmin)
admin.site.register(Missa, MissaAdmin)
admin.site.register(Aunsiu, AunsiuAdmin)
admin.site.register(Atendimentu, AtendimentuAdmin)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('file', 'parent_model_name')  # Display the parent model name

    def parent_model_name(self, obj):
        if obj.annual_plan:
            return f"Annual Plan: {obj.annual_plan}"
        elif obj.noticia:
            return f"Noticia: {obj.noticia}"
        elif obj.atividade:
            return f"Atividade: {obj.atividade}"
        elif obj.eventu:
            return f"Eventu: {obj.eventu}"
        elif obj.missa:
            return f"Missa: {obj.missa}"
        elif obj.aunsiu:
            return f"Aunsiu: {obj.aunsiu}"
        elif obj.atendimentu:
            return f"Atendimentu: {obj.atendimentu}"
        return "No Parent"
    parent_model_name.short_description = 'Parent Model Name'

admin.site.register(Attachment, AttachmentAdmin)

# admin.site.register(AnnualPlan,AnnualPlanAdmin)





class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('action', 'model_name', 'instance_id', 'user', 'timestamp', 'details')
    list_filter = ('action', 'model_name', 'timestamp')
    search_fields = ('model_name', 'instance_id', 'details')
admin.site.register(LogEntry, LogEntryAdmin)


