from django.contrib import admin

from .models import Culture


class CultureAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'name',
        'volume',
        'start_date',
        'end_date',
        'test_date',
        'ph_test'
    ]


    list_filter = [
        'username',
        'start_date',
        'end_date',
    ]

admin.site.register(Culture, CultureAdmin)
