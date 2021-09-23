
from django.urls import path, include
from . import views

urlpatterns = [
    #path('signup', views.signup, name='signup'),
    path('accounts/login/', views.login, name='login'),
    path('accounts/login_popup/', views.login_popup, name='login_popup'),
    path('logout/', views.logout_view, name='logout'),
]
