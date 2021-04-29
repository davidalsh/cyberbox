from django.contrib import admin

from main.models import ProgrammingLanguages, WorkingPlace, UserProfile


@admin.register(ProgrammingLanguages)
class ProgrammingLanguagesAdmin(admin.ModelAdmin):
    list_display = ("id", "title",)
    list_display_links = ("id", "title",)


@admin.register(WorkingPlace)
class WorkingPlaceAdmin(admin.ModelAdmin):
    list_display = ("id", "title",)
    list_display_links = ("id", "title",)
    list_filter = ("title",)
    search_fields = ("title",)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user",)
    list_display_links = ("user",)
    list_filter = ("programming_languages", "working_place",)
    search_fields = ("title", "about", )
    readonly_fields = ("avatar",)
