from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..serializers import UserLoginSerializer, UserSerializer, UserSignUpSerializer

from ..models import User
from datetime import date, timedelta, datetime

# Serializador general para usuarios
class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer

    # Acción a realizar, login
    @action(detail=False, methods=["post"])
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {"user": UserSerializer(user).data, "access_token": token}

        # Cambia la última vez que inició sesión
        data["user"]["last_login"] = datetime.today()

        # Lee la edad del usuario que inicia sesión con el fin de validar
        # Si ya es mayor de edad en caso de que no lo fuera
        dob = datetime.strptime(data["user"]["fecha_nacimiento"], "%Y-%m-%d").date()
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
            # Si no existe el usuario o si no se proporcionó un usuario
            not request.GET.get("username")
            or not User.objects.filter(
                username=self.request.GET.get("username")
            ).exists()
        ):
            return Response(
                {"Error": "Username inválido"}, status=status.HTTP_400_BAD_REQUEST
            )
        serializer = UserSerializer()
        specificuser = serializer.get_specific_user(request.GET["username"])
        return Response(specificuser.data, status=status.HTTP_200_OK)
