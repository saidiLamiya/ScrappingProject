from django.contrib import admin
from .models import Event, Keyword, School, User


from django.utils.html import format_html

# Register your models here.

#admin.site.register(Event)
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    model= admin
    list_display= ('title', 'description')

#admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model= User
    list_display= ('first_name', 'last_name', 'school', 'email')
    search_fields = ('first_name', 'last_name', 'school', 'email')

#admin.site.register(School)
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    pass

#admin.site.register(Keyword)
@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    pass
