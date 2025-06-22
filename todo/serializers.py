from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'  # Or list them: ['id', 'title', 'description', 'completed', 'created_at', 'user']
        read_only_fields = ['user', 'created_at']

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,required=True,style={"input_type":"password"})
    class Meta:
        model=User
        fields=['username','email','password']
    def create(self,validated_data):
        user=User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user