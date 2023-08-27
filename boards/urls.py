from django.urls import path

from boards import views

app_name = "boards"
urlpatterns = [
    # ex: /boards
    path("", views.index, name="index"),
    # ex: /boards/1
    path("/<int:post_id>", views.detail, name="detail"),
]
