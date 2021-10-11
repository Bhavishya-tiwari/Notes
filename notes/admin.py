from django.contrib import admin
from .models import Notes

# Register your models here.
@admin.register(Notes)
class PostAdmin(admin.ModelAdmin):
    list_display =['fno']