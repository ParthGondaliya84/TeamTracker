from rest_framework import serializers
from apps.user.models import TeamUser, UserProfileInfo
from apps.base.serializers import BaseSerialzers


class UserRegistrationSerializer(BaseSerialzers):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta(BaseSerialzers.Meta):
        model = TeamUser
        fields = [
            'email', 'user_role', 'first_name', 'last_name',
            'gender', 'password', 'password2'
        ]

    def validate_email(self, value):
        if TeamUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use")
        return value

    def validate(self, value):
        if value['password'] != value['password2']:
            raise serializers.ValidationError({
                "password": "Passwords do not match!"
            })
        return value

    def create(self, validated_data):
        user = TeamUser.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            gender=validated_data['gender'],
            user_role=validated_data['user_role'],
            password=validated_data['password']
        )
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamUser
        fields = ["first_name", "last_name"]


class UserProfileInfoSerializer(BaseSerialzers):
    user = UserSerializer()

    class Meta:
        model = UserProfileInfo
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", None)

        if user_data:
            user_serializer = UserSerializer(
                instance.user, data=user_data, partial=True
            )
            if user_serializer.is_valid():
                user_serializer.save()
            else:
                raise serializers.ValidationError(user_serializer.errors)

        return super().update(instance, validated_data)
