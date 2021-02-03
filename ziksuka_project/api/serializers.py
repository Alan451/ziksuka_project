from rest_framework.serializers import ModelSerializer
from .models import Blog
from django.contrib.auth.models import User

class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','first_name','password']

