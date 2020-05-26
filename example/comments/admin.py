from django.contrib import admin
from .models import CommentModel


@admin.register(CommentModel)
class CustomUserAdmin(admin.ModelAdmin):
    pass
