from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from portfolio_app.models import User, Education, Experience, Skills, Projects, SocialMedia


@admin.register(User)
class MyUserAdmin(UserAdmin):
    list_display = ("username", "first_name", "last_name", "birth_date")
    search_fields = ("first_name", "last_name", "about", "information")


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("institution", "field_of_study", "degree", "start_date", "end_date")
    search_fields = ("institution", "field_of_study", "degree")
    list_filter = ("start_date", "end_date")


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("company", "profession", "start_date", "end_date")
    search_fields = ("company", "profession")
    list_filter = ("start_date", "end_date")


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "owner")
    search_fields = ("name", "description")
    exclude = ('owner',)

    def save_model(self, request, obj, form, change):
        if not obj.owner:
            obj.owner = request.user
        super().save_model(request, obj, form, change)


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ("name", "date", "media")
    search_fields = ("name", "description")
    list_filter = ("date",)
    filter_horizontal = ("skills",)


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("name", "media")
    search_fields = ("name", "description")
