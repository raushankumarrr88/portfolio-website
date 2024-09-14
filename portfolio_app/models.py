from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    information = models.TextField(null=True, blank=True)
    cv = models.TextField(null=True, blank=True)


class Education(models.Model):
    institution = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    degree = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_educations")


class Experience(models.Model):
    company = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    location = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_experiences")


class Skills(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_skills")


class Projects(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_projects")
    experience = models.ForeignKey(
        Experience, on_delete=models.CASCADE, null=True, blank=True, related_name="project_experiences"
    )
    skills = models.ManyToManyField(Skills, blank=True, related_name="project_skills")
    date = models.DateField(null=True, blank=True)
    media = models.URLField(null=True, blank=True)


class SocialMedia(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_social_media")
    media = models.URLField(null=True, blank=True)
