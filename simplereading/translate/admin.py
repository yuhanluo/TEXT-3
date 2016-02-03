from django.contrib import admin

from .models import translation
from .models import Simple
from .models import Original

admin.site.register(translation)
admin.site.register(Simple)
admin.site.register(Original)
