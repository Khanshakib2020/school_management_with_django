from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import Roles, Users
from users.serializers import RolesSerializers, UsersSerializers
from django.contrib.auth.hashers import make_password, check_password
import jwt
import os


# ------------------- User Apis ----------------


# create user
@api_view(['POST'])
def create_user(request):
    existUser = Users.objects.filter(username=request.data['username'])
    if existUser: return Response({'error': 'username already taken!!'}, status=403)
    request.data['password'] = make_password(request.data['password'])
    serializedUser = UsersSerializers(data=request.data)
    if serializedUser.is_valid():
        serializedUser.save()
        return Response({'data': serializedUser.data}, status=201)
    else:
        return Response({'data': serializedUser.data}, status=400)

    

# get by id 
@api_view(['GET'])
def get_user_by_id(request, id):
    user = Users.objects.get(pk=id)
    if user:
        serializedUser = UsersSerializers(user)
        return Response({'data': serializedUser.data}, status=200)
    else:
        return Response({'data': 'user does not exist!!'}, status=400)
    

# get all users
@api_view(['GET'])
def get_all_users(request):
    users = Users.objects.all()
    serializedUsers = UsersSerializers(users, many=True)
    return Response({'data': serializedUsers.data}, status=200)


# User Login 
@api_view(['POST'])
def user_login(request):
    
    username = request.data.get('username')
    password = request.data.get('password')
    
    try:
        user = Users.objects.get(username=username)
        print('user --> ', user.is_staff)
        if not user.is_staff: return Response({'error': 'you are authorized to login!!'}, status=403)
    except Users.DoesNotExist:
        return Response({'error': 'User not found!!'}, status=403)

    password_check = check_password(password, user.password)
    if not password_check: return Response({'data': 'invalid password!!'})

    serializedRole = RolesSerializers(user.role_id)

    payload = {
        'userId': str(user.id),
        'firstname': user.firstname,
        'lastname': user.lastname,
        'username': user.username,
        'roleid': serializedRole['id'].value,
        'rolename': serializedRole['name'].value,
    }
    secretKey = os.getenv('DB_NAME')
    algorithm='HS256'
    
    token = jwt.encode(payload, secretKey, algorithm)
    return Response({'data': token})