from .models import Task
from django.contrib.auth.models import User
from rest_framework import serializers

#username:mytask, password:task123

class TheUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password']
    def create(self, validated_data):
        # Use Django's create_user method which handles password hashing
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        
class TaskSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    class Meta:
        model = Task
        fields = ['id', 'user', 'task_name', 'task', 'task_status']

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()