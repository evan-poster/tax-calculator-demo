from django.contrib import admin

from .models import State, Town

# Register your models here.
admin.site.register(State)
admin.site.register(Town)