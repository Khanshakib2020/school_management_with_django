from django.contrib import admin
from subjects.models import Subjects


# Register your models here.
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Subjects, SubjectsAdmin)
