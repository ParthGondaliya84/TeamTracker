from rest_framework import serializers
from apps.user.models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    retype_password = serializers.CharField(write_only=True)    
    
    class Meta:
        model = CustomUser
        fields = [ 'email' , 'first_name' , 'last_name'  , 'password' , 'retype_password' ]
        
    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email alredy in use")
        return value
    
    
    def validate(self , value):
        if value['password'] != value['retype_password']:
            raise serializers.ValidationError({"Password" : " password did not match !!"})
        return value
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        return user
    
    
class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)
