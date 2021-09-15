from django.contrib import admin

# from .models.Greetings import Greeting
from .models import User

# Register your models here.

# admin.site.register(Greeting)
# admin.site.register(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = (
        "pk",
        "username",
        "email",
    )
    list_display_links = (
        "pk",
        "username",
        "email",
    )

    search_fields = [
        "email",
        "username",
        "first_name",
        "list_name",
    ]

    list_filter = [
        "is_active",
        "is_staff",
        "date_joined",
        # "modified",
    ]

    readonly_fields = [
        "fecha_registro",
        # "modified",
    ]
