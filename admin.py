from django.contrib import admin

# Register your models here.

from .models import comingDate , eMail , frontErrorPage , SBtn , backgroundImage

admin.site.register(comingDate)
admin.site.register(eMail)
admin.site.register(frontErrorPage)
admin.site.register(SBtn)
admin.site.register(backgroundImage)
