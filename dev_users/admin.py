from django.contrib import admin
from .models import Profile,Skill,Message
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ['name','subject','is_read','created']

class SkillAdmin(admin.ModelAdmin):
    list_display = ['owner','name','description','created']
    list_filter = ['owner']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','name','email']
    list_filter =  ['user']

admin.site.register(Message,MessageAdmin)
admin.site.register(Skill,SkillAdmin)
admin.site.register(Profile,ProfileAdmin)
