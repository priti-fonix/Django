from django.contrib import admin
from .models import student

# Register your models here.

@admin.register(student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'batch', 'photo')
    list_filter = ('batch', 'age')
    search_fields = ('name', 'batch')
    ordering = ('name',)
