from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Member)
admin.site.register(Network)
admin.site.register(Cluster)
admin.site.register(Machinery)
admin.site.register(ProductionPerPhase)
