from django.urls import path
from.import views

urlpatterns = [

    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
]
# normal comment
# ! exclamation comment
# ? question comment
# // strike through comment