from django.urls import path

from boards import views

app_name = "boards"
urlpatterns = [
    # ex: /boards
    path("", views.index, name="index")
]
