from django.contrib import admin
from django.contrib.auth import get_user_model

from accounts.models import Portfolio, UserSkill

User = get_user_model()


class PortfolioInline(admin.TabularInline):
    model = Portfolio


class UserSkillInline(admin.TabularInline):
    model = UserSkill


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['user', 'title']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'get_full_name')

    inlines = [PortfolioInline, UserSkillInline]