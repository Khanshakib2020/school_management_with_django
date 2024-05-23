from rest_framework import serializers
from users.models import Roles, Users



class RolesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'



class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


