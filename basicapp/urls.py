from django.urls import path
from . import views

app_name = 'basicapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('relative/',views.relative,name='relative'),
    path('logout/',views.user_logout,name='logout'),
    path('special/',views.special,name='special'),
    path('user_login/',views.user_login,name='user_login'),
]
