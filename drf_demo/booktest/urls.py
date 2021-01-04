from django.urls import re_path

from booktest import views

urlpatterns = [
    re_path(r"^books/$", views.BookListView.as_view()),
    re_path(r"^books/(?P<pk>\d+)/$", views.BookDetailView.as_view()),
]
