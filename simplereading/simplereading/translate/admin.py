from django.contrib import admin

from .models import History
from .models import Simple
from .models import Original

admin.site.register(History)
admin.site.register(Simple)
admin.site.register(Original)
