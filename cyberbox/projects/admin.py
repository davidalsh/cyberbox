from django.contrib import admin

from projects.models import Projects, ApplyToProjectRequest


@admin.register(Projects)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("title", "max_members", "open",)
    list_display_links = ("title",)
    list_filter = ("programming_languages_are_using", "searching_for_working_place",)
    search_fields = ("title", "description", "programming_languages_are_using",)


@admin.register(ApplyToProjectRequest)
class ApplyToProjectRequestAdmin(admin.ModelAdmin):
    list_display = ("user", "project",)
    list_display_links = ("user",)
    search_fields = ("user",)


