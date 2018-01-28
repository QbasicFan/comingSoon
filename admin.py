from django.contrib import admin

# Register your models here.

from .models import mainImage , comingDate , eMail , background

admin.site.register(mainImage)
admin.site.register(comingDate)
admin.site.register(eMail)
admin.site.register(background)
