from atexit import register
from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class registeradmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('lrn', 'username', 'password1', 'password2','email','contacts','parents','adviser','gradelvl','section','userType'),
        }),
    )
admin.site.register(registration, registeradmin)
admin.site.register(make_announcement)
admin.site.register(studentInfo)