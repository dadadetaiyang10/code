from django.urls import re_path

from booktest import views

urlpatterns = [
    re_path(r"^books/$", views.BookInfoViewSet.as_view(
        {"get": "list"}
    )),
    re_path(r"^books/(?P<pk>\d+)/$", views.BookInfoViewSet.as_view(
        {"get": "retrieve"}
    )),
]
