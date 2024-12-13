from django.contrib import admin
from django.contrib.auth import get_user_model

from accounts.models import Portfolio, UserSkill, Relation, Employer

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


@admin.register(Relation)
class RelationAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user')


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name')