from django.contrib import admin

# Register your models here.
from .models import producer , production

admin.site.register(producer)
admin.site.register(production)