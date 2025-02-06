from django.contrib import admin
from .models import Notecreate




class NotecreateAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'user','created_at')
    list_filter = ('user', 'created_at')
admin.site.register(Notecreate, NotecreateAdmin)





