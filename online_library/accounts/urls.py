from django.urls import path
from .views import signup, custom_logout

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("logout/", custom_logout, name="custom_logout"),
]