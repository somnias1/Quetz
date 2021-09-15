from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# from rest_framework.views import APIView

from ..serializers import UserLoginSerializer, UserSerializer, UserSignUpSerializer

from ..models import User
from datetime import date

# from cerberus import Validator


class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer

    @action(detail=False, methods=["post"])
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()

        data = {"user": UserSerializer(user).data, "access_token": token}
        data["user"]["last_login"] = date.today()

        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["post"])
    def signup(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserSerializer(user).data
        # print(date(data["fecha_nacimiento"]).year)
        # edad = date(year=data["fecha_nacimiento"]) - date(year).today()

        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["get"])
    def watch(self, request):
        serializer = UserSerializer()
        specificuser = serializer.get_specific_user(data=request.data)
        # print(specificuser)
        return Response(specificuser, status=status.HTTP_200_OK)
