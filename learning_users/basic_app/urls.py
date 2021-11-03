from django.urls import path
from . import views

app_name = 'basic_app'

urlpatterns = [
    path('user_login/', views.user_login, name='user_login'),
    path('registration/', views.register, name='register')
]
