from django.contrib import admin
from django.contrib.admin import display

from jobs.models import Project, Budget


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'expire_time', 'status']

    @display(description='user')
    def get_user(self, obj):
        return obj.user.username


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ['title', 'min_price', 'max_price',]