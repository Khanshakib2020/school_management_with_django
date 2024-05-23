from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import Users, Roles
from users.serializers import UsersSerializers, RolesSerializers

@api_view()
def hello_dashboard(request):
    roles = Roles.objects.filter(name__in=['Teacher', 'Student'])
    roleIds=[]
    for role in roles:
        roleIds.append(role.id)

    dashboardData={
        'totalEmployees': 0,
        'totalStudents': 0,
        'maleStudents': 0,
        'FemaleStudents': 0,
    }

    totalUsers = Users.objects.filter(role_id__in=roleIds)
    for user in totalUsers:
        if str(user.role_id) == 'Teacher':
            dashboardData['totalEmployees'] +=1

        if str(user.role_id) == 'Student':
            dashboardData['totalStudents'] +=1
        
        if user.gender == 'Male' and str(user.role_id) == 'Student':
            dashboardData['maleStudents'] +=1

        if user.gender == 'Female' and str(user.role_id) == 'Student':
            dashboardData['FemaleStudents'] +=1

    print('dashboardData ==> ', dashboardData)
    return Response({"data": dashboardData})