from django.contrib import admin

# Register your models here.
from bt.models import Nematoda, Worm, TypesOfWorm, ParametrsWorm, SubTypesOfWorm

admin.site.register(Nematoda)
admin.site.register(TypesOfWorm)
admin.site.register(Worm)
admin.site.register(ParametrsWorm)
admin.site.register(SubTypesOfWorm)