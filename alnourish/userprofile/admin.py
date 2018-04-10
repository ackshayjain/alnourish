from django.contrib import admin

# Register your models here.

from .models import Culture


class CultureAdmin(admin.ModelAdmin):
	list_display = [
	'username',
	'name',
	'volume',
	]


admin.site.register(Culture,CultureAdmin)
from django.contrib import admin

# Register your models here.
