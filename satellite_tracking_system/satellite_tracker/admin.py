from django.contrib import admin
from .models import LaunchCountry
from .models import Satellite

# Register your models here.
admin.site.register(LaunchCountry)
admin.site.register(Satellite)
