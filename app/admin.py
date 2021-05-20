from django.contrib.auth.models import Group,User
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib.admin import AdminSite
from .models import Header,ContactUs, Train

class TrainerAdmin(ImportExportModelAdmin):
    list_display = ('topic','time','user_name')
    ordering=["-id"]
admin.site.register(Train,TrainerAdmin)
admin.site.register(Header)
admin.site.register(ContactUs)
