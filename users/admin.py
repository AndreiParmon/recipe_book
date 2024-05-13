from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Админ-панель модели профиля
    """
    list_display = ['display_user', 'display_birth', 'preview']
    raw_id_fields = ['user']

    def display_user(self, obj):
        return f"{obj.user}"

    display_user.short_description = 'Автор'

    def display_birth(self, obj):
        return f"{obj.date_birth}"

    display_birth.short_description = 'День рождения'

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.avatar.url}" style="width: 50px; height: auto;" alt="Изображения нет">')

    preview.short_description = 'Аватар'
