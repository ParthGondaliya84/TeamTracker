from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from apps.user.serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    UserProfileInfoSerializer,
)
from apps.user.models import (
    UserProfileInfo, TeamUser
)
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework import status
from apps.base.views import BaseViewSet
from drf_spectacular.utils import extend_schema
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required


class CustomUserRegisterAPIView(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet):
    queryset = TeamUser.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Account has been created successfull"},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"message": "Error!! to create new user " }
            )


class UserLoginViewSet(viewsets.GenericViewSet):
    serializer_class = UserLoginSerializer

    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def login(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get("email")
            password = serializer.validated_data.get("password")
            user = authenticate(email=email, password=password)

            if user:
                refresh = RefreshToken.for_user(user)
                user_info = {
                    "userid" : user.id,
                    "email" : user.email,
                    "firstname" : user.first_name,
                    "lasttname" : user.last_name,
                    
                    
                }
                return Response(
                    {
                        "login": "Successfully Logged In!",
                        "user": user_info,
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                        
                    },
                    status=status.HTTP_202_ACCEPTED
                )
            else:
                return Response(
                    {"error": "Incorrect email or password!"},
                    status=status.HTTP_401_UNAUTHORIZED
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
    @action(detail=False, methods=["post"], permission_classes=[IsAuthenticated])
    def logout(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get("refresh")
            if not refresh_token:
                return Response(
                    {"error": "Refresh token is required"},
                    status=status.HTTP_400_BAD_REQUEST
                )
                
            if not request.auth:
                return Response(
                    {"error": "Invalid Token in Header"},
                    status=status.HTTP_400_BAD_REQUEST
                    )
        
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {"message": "Logged out successfully"},
                status=status.HTTP_200_OK
            )
        except Exception :
            return Response(
                {"error": "Invalid token" },
                status=status.HTTP_400_BAD_REQUEST
            )

@extend_schema(
    methods=['GET', 'PUT', 'PATCH'],
    parameters=[
        {'name': 'id', 'in': 'path', 'required': True, 'schema': {'type': 'integer'}}
    ]
)
class ProfileGeneralInfoView(BaseViewSet, viewsets.ModelViewSet):
    serializer_class = UserProfileInfoSerializer
    http_method_names = ["get", "put", "patch"]

    def get_queryset(self):
        return UserProfileInfo.objects.filter(user=self.request.user)
