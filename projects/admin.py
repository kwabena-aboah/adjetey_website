from django.contrib import admin
from . models import Project, Contact


class ProjectAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', 'image',)
	list_filter = ('title',)
	search_fields = ('title',)

admin.site.register(Project, ProjectAdmin)


class ContactForm(admin.ModelAdmin):
	list_display = ('name', 'email', 'message',)
	search_fields = ('name', 'email',)

admin.site.register(Contact, ContactForm)
