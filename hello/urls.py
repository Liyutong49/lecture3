from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("yutong", views.yutong, name="yutong"),
    path("<str:name>", views.greet, name="greet")
]