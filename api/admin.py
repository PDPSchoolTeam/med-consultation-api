from django.contrib import admin
from api.models import (
    User,
    Doctor,
    News,

)

# admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(News)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'email', 'is_staff')
