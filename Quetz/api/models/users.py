from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField
from datetime import timedelta, date
from django.utils import timezone


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=86)
    USERNAME_FIELD = "username"
    lista_idiomas = [
        ("en", "Inglés"),
        ("es", "Español"),
        ("fr", "Francés"),
        ("de", "Alemán"),
        ("cn", "Chino"),
        ("jp", "Japonés"),
        ("it", "Italiano"),
        ("pt", "Portugués"),
    ]

    email = models.EmailField(null=False)
    fecha_registro = models.DateField(auto_now=True)
    fecha_nacimiento = models.DateField(null=False)
    institucion_educativa = models.CharField(null=True, max_length=255)
    idiomas = MultiSelectField(
        choices=lista_idiomas,
        max_choices=len(lista_idiomas),
        max_length=len(lista_idiomas),
    )
    ubicacion = models.CharField(null=True, max_length=255)
    facebookurl = models.URLField(null=True)
    instagramurl = models.URLField(null=True)
    twitterurl = models.URLField(null=True)
    youtubeurl = models.URLField(null=True)
    adulto = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["correo"]

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return f"{self.username}"
