from django.urls import path

from portfolio_app.views import (
    index,
    EducationListView,
    ExperienceListView,
    SkillsListView,
    ProjectsListView,
    LanguagesListView
)

urlpatterns = [
    path("", index, name="index"),
    path("educations/", EducationListView.as_view(), name="education"),
    path("experiences/", ExperienceListView.as_view(), name="experience"),
    path("skills/", SkillsListView.as_view(), name="skills"),
    path("projects/", ProjectsListView.as_view(), name="projects"),
    path("languages/", LanguagesListView.as_view(), name="languages"),
]

app_name = "portfolio"
