from django.urls import path
from JobPost import views


urlpatterns = [
    path('', views.home, name="home"),
    path('job/<str:slug>', views.job_detail, name="job_detail")
]