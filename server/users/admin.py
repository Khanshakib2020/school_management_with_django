from django.contrib import admin
from django.contrib.auth.hashers import make_password
from users.models import Users, Roles

# Register your models here.
class RolesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class UsersAdmin(admin.ModelAdmin):
    list_display = ('rollnumber', 'firstname', 'lastname', 'role_id')
    def save_model(self, request, obj, form, change):
        # Hash the password before saving the user
        obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)

admin.site.register(Roles, RolesAdmin)
admin.site.register(Users, UsersAdmin)