from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [
    path('<int:id>',views.job_detail),
    path('<>',views.job_list),
]
