from django.contrib import admin
from comments import models


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    pass