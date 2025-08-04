from django.contrib import admin

from main.models import TelegramUser

@admin.register(TelegramUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'first_name', 'group', 'created_at')
    search_fields = ('user_id', 'group')
