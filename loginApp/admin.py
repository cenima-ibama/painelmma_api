from django.contrib import admin
from .models import UserPermited, LDAPUser

# Register your models here.

admin.site.register(UserPermited)
admin.site.register(LDAPUser)
