from django.contrib import admin

# Register your models here.
from .models import tmens
from .models import ratingreview

admin.site.register(tmens)
admin.site.register(ratingreview)