from django.contrib import admin
from portfolio_app.models import User, Education, Experience, Skills, Projects, SocialMedia


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "birth_date")
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
    list_display = ("name", "description")
    search_fields = ("name", "description")


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
