from django.contrib import admin
from api.models import (
    User,
    Doctor,
    News,

)

admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(News)
