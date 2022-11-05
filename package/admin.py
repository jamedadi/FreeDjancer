from django.contrib import admin

from package.models import Package


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['title', 'bids', 'price']