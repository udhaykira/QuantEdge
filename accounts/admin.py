from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = (
        'created_at',
        'updated_at',
        'id',
        'username',
        'email',
        'phone_number',
        'is_verified',
        'is_staff'
    )

    search_fields = (
        'username',
        'phone_number',
        'email'
    )

    list_filter = (
        'is_verified',
        'is_staff',
        'is_superuser'
    )

    ordering = (
        '-created_at',
    )

    list_per_page = 10

    readonly_fields = (
        'created_at',
        'updated_at'
    )
