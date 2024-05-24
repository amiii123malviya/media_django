from django.urls import *
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('register/',register,name='register'),

]