from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path("relate/",views.relate,name="relate"),
    path("extension/",views.extension,name="extension"),
]