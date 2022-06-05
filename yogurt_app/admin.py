from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(Yogurt)
admin.site.register(City)
admin.site.register(Order)
