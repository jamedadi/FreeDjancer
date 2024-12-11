from django.contrib import admin
from django.contrib.admin import register

from messaging.models import Chat


@register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'get_participants')
    search_fields = ('participants__username',)
    ordering = ('-created_at',)

    def get_participants(self, obj):
        return ", ".join([user.username for user in obj.participants.all()])
    get_participants.short_description = "Participants"