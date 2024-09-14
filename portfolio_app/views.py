from django.shortcuts import render
from django.views.generic import ListView

from portfolio_app.models import Education, Experience, Skills, Projects


def index(request):
    return render(request, "index.html")


class EducationListView(ListView):
    model = Education
    template_name = "education.html"
    context_object_name = "educations"


class ExperienceListView(ListView):
    model = Experience
    template_name = "experience.html"
    context_object_name = "experiences"


class SkillsListView(ListView):
    model = Skills
    template_name = "skills.html"
    context_object_name = "skills"


class ProjectsListView(ListView):
    model = Projects
    template_name = "projects.html"
    context_object_name = "projects"

