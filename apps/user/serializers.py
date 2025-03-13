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


class ProfileGeneralInfoSerializer(serializers.ModelSerializer):
    user =serializers.StringRelatedField()
    created_by = serializers.StringRelatedField()
    updated_by = serializers.StringRelatedField()
    
    class Meta:
        model = UserProfileGeneralInfo
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}} 


class CustomUserSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField()
    updated_by = serializers.ReadOnlyField()
    profile = ProfileGeneralInfoSerializer(required=False)

    class Meta:
        model = CustomUser
        fields = ["id", "email", "first_name", "last_name", "profile",
                  "created_by", "updated_by"]
        read_only_fields = ["created_by", "updated_by"]


    def update(self, instance, validated_data):
        validated_data.pop('email', None) 

        profile_data = validated_data.pop('profile', None)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()

        if profile_data:
            try:
                profile_serializer = ProfileGeneralInfoSerializer(instance.profile, data=profile_data, partial=True)
                if profile_serializer.is_valid():
                    profile_serializer.save(updated_by=self.context['request'].user)
            except UserProfileGeneralInfo.DoesNotExist:
                pass

        return super().update(instance, validated_data)