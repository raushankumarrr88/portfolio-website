from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from portfolio_app.models import User, Education, Experience, Skills, Projects, SocialMedia


@admin.register(User)
class MyUserAdmin(UserAdmin):
    list_display = ("username", "first_name", "last_name", "birth_date")
    search_fields = ("first_name", "last_name", "about", "information")


@admin.register(Education)
class EducationAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("institution", "field_of_study", "degree", "start_date", "end_date", "order")
    list_editable = ("order",)


@admin.register(Experience)
class ExperienceAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("company", "profession", "start_date", "end_date", "order")
    list_editable = ("order",)


@admin.register(Skills)
class SkillsAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("name", "description", "owner", "order")
    search_fields = ("name", "description")
    exclude = ("owner",)
    list_editable = ("order",)

    def save_model(self, request, obj, form, change):
        if not obj.owner:
            obj.owner = request.user
        super().save_model(request, obj, form, change)


@admin.register(Projects)
class ProjectsAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("name", "date", "media", "order")
    search_fields = ("name", "description")
    list_filter = ("date",)
    filter_horizontal = ("skills",)
    list_editable = ("order",)


@admin.register(SocialMedia)
class SocialMediaAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("name", "media", "order")
    list_editable = ("order",)
