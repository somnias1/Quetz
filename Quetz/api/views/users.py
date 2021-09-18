from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# from rest_framework.views import APIView

from ..serializers import UserLoginSerializer, UserSerializer, UserSignUpSerializer

from ..models import User
from datetime import date, timedelta, datetime

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
        print(data["user"]["fecha_nacimiento"])
        dob = datetime.strptime(data["user"]["fecha_nacimiento"], "%Y-%m-%d").date()
        print(dob)
        print(type(dob))
        if (date.today() - dob) > timedelta(days=18 * 365):
            data["user"]["adulto"] = True

        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["post"])
    def signup(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserSerializer(user).data

        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["get"])
    def watch(self, request):
        if (
            not request.GET.get("username")
            or not User.objects.filter(
                username=self.request.GET.get("username")
            ).exists()
        ):
            return Response(
                {"Error": "Username inválido"}, status=status.HTTP_400_BAD_REQUEST
            )
        serializer = UserSerializer()
        # print(request.GET["username"])
        specificuser = serializer.get_specific_user(request.GET["username"])
        # print(specificuser)
        return Response(specificuser.data, status=status.HTTP_200_OK)
