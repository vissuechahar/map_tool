from django.contrib import admin
from .models import InterfaceType,Interface,Profile,InterfaceDetail,SchemaTable,InterfacefieldDetail



admin.site.register(InterfaceType)

admin.site.register(Interface)

admin.site.register(Profile)

admin.site.register(InterfaceDetail)

admin.site.register(SchemaTable)

admin.site.register(InterfacefieldDetail)