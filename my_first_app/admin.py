from django.contrib import admin
from .models import EasyLevel, MediumLevel, HardLevel
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(EasyLevel)
admin.site.register(MediumLevel)
admin.site.register(HardLevel)


#
