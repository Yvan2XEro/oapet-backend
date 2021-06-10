from djoser.serializers import UserCreateSerializer
from .models import *


class UserCreateSeriliser(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'phone', 'password')

class TeacherCreateSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        model = Teacher
        fields = ('email', 'username', 'first_name', 'last_name', 'phone', 'password', 'teacher_matricule')
