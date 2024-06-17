from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login),
    path('signup/', views.signup),
    path('test-view/', views.TestView),
    path('logout/', views.logout),
]
