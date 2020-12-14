from django.urls import re_path

from bookset import views

urlpatterns = [
    re_path(r"^index/$", views.HeroInfomation.as_view()),
]
