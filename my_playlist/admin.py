from django.contrib import admin

# Register your models here.
from .models import My_playlist, Latest

admin.site.register(My_playlist)
admin.site.register(Latest)
