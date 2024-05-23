from django.db import models
from classes.models import Classes
from subjects.models import Subjects
import uuid


# ------------------- Role Model --------------------

class Roles(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.name


class Users(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, null=True, choices=(('Male', 'Male'),('Female', 'Female')))
    rollnumber = models.SmallIntegerField(null=True, blank=True)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=150)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True, editable=True)
    is_staff = models.BooleanField(default=False)

    role_id = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True)
    class_id = models.ManyToManyField(Classes, blank=True)
    subject_id = models.ManyToManyField(Subjects, blank=True)

    def __str__(self) -> str:
        return self.username