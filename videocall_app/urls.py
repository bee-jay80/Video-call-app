from django.urls import path
from . import views

urlpatterns = [
    path("",views.register,name="register"),
    path("login/",views.login_view,name="login"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("meeting/",views.video_call,name="meeting"),
    path("logout/",views.login_view,name="logout"),
    path("joinroom/",views.join_view,name="joinroom")
]