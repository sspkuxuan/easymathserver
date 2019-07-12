from django.contrib import admin
from .models import QuestionLib, UserAnswer, MathUser,ErrorAnswer,ErrorT


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(QuestionLib,UserProfileAdmin)
admin.site.register(UserAnswer,)
admin.site.register(MathUser,)
admin.site.register(ErrorAnswer,)
admin.site.register(ErrorT,)