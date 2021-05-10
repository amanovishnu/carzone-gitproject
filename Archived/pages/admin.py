from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="20" style="border-radius: 10px" />'.format(object.photo.url))
    
    thumbnail.short_description ='Photo'

    list_display =['id','thumbnail','first_name','last_name','designation','facebook_link','twitter_link','google_link','created_date','photo']
    list_display_links = ['id','first_name','last_name']
    search_fields = ['first_name','last_name']
    list_filter = ['designation']

admin.site.register(Team,TeamAdmin)