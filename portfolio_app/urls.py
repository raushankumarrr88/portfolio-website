from django.urls import path

from portfolio_app.views import index


urlpatterns = [
    path("", index, name="index"),
    ]

app_name = "portfolio"
