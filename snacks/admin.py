from django.contrib import admin
from .models import Snack
# Register your models here.
  
# admin.register(Snack)
# class AdminSnack(admin.ModelAdmin):
#     list_display= ['name', 'reviewer']
#     search_fields = ['name']
#     list_display_links = ('reviewer',)

admin.site.register(Snack)
