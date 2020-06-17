from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path('index/', views.index, name = "index"),
    path('<int:person_pk>/past_life/', views.past_life, name = "past_life"),
]