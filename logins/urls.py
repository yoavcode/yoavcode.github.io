from . import views
from django.urls import path

app_name = "logins"
urlpatterns = [
    path('', views.register, name='login')
]