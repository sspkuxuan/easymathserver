from django.contrib import admin
from .models import PinInformation,PinUser

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(PinInformation,)
admin.site.register(PinUser,)
