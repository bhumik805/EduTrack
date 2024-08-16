from django.urls import path
from .views import home,login,validate,register,add_user,plot,ret,logout

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('validate/', validate, name='validate'),
    path('register/', register, name='register'),
    path('add_user/', add_user, name='add_user'),
    path('plot/<str:p1>/<str:p2>/', plot, name='plot'),
    path('ret/', ret, name='ret'),
    path('logout/', logout, name='logout'),
]