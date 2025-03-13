from rest_framework import serializers
from apps.user.models import CustomUser, UserProfileGeneralInfo

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


class CustomUserSerializer(serializers.ModelSerializer):
     
     class Meta:
         model = CustomUser   
         fields = ["first_name", "last_name"] 
         

class BaseSerialzers(serializers.ModelSerializer):
    user =serializers.StringRelatedField(read_only=True)
    created_by = serializers.StringRelatedField(read_only=True)
    updated_by = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        abstract = True
        read_only_fields = ["created_by", "updated_by", "created_at", "updated_at",
                            "is_active", "is_delete"]


class ProfileGeneralInfoSerializer(BaseSerialzers):
     user  = CustomUserSerializer()
     
     class Meta:
        model = UserProfileGeneralInfo
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}
         
         
     def update(self, instance, validated_data):
         user_data = validated_data.pop("user" , None)
         
         if user_data:
             user_serialziers = CustomUserSerializer(instance.user, data=user_data, partial=True)
             
             if user_serialziers.is_valid():
                 user_serialziers.save()
             else:
                 raise serializers.ValidationError(user_serialziers.errors)
         
         return super().update(instance, validated_data)
     