from django.contrib import admin
from django.contrib.admin import display

from jobs.models import Project, Budget, File, ProjectFile, UserBid, ProjectSkill, Skill


class ProjectFileInline(admin.TabularInline):
    model = ProjectFile


class UserBidInline(admin.TabularInline):
    model = UserBid


class ProjectSkillInline(admin.TabularInline):
    model = ProjectSkill


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'expire_time', 'status']
    inlines = [ProjectFileInline, UserBidInline, ProjectSkillInline]

    @display(description='user')
    def get_user(self, obj):
        return obj.user.username


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ['title', 'min_price', 'max_price',]


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['title']
