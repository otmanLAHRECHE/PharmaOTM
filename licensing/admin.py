from django.contrib import admin
from .models import License
# Register your models here.
@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = ('license_type', 'start_date', 'expiry_date', 'is_active')