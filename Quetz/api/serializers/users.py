from django.contrib.auth import password_validation, authenticate
from django.core.validators import RegexValidator, FileExtensionValidator

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

from ..models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:

        model = User

        fields = [
            "username",
            "last_login",
            "email",
            "fecha_registro",
            "fecha_nacimiento",
            "institucion_educativa",
            "idiomas",
            "ubicacion",
            "facebookurl",
            "twitterurl",
            "youtubeurl",
            "adulto",
            "foto_perfil",
        ]

    def get_users(self):
        return UserSerializer(User.objects.all(), many=True).data

    def get_specific_user(self, validate_data):
        infouser = User.objects.filter(username=validate_data)[0]
        return UserSerializer(infouser)


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=8, max_length=86)
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        usuario = authenticate(username=data["username"], password=data["password"])
        if not usuario:
            raise serializers.ValidationError("Credenciales incorrectas")

        self.context["username"] = usuario
        return data

    def create(self, data):
        token, created = Token.objects.get_or_create(user=self.context["username"])
        return self.context["username"], token.key


class UserSignUpSerializer(serializers.Serializer):
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)
    fecha_nacimiento = serializers.DateField()
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    def validate(self, data):
        passwrd = data["password"]
        passwrd_conf = data["password_confirmation"]
        if passwrd != passwrd_conf:
            raise serializers.ValidationError("La contraseña no coincide")
        password_validation.validate_password(passwrd)
        return data

    def create(self, data):
        data.pop("password_confirmation")
        user = User.objects.create_user(**data)
        return user
