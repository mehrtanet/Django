from django.urls import path
from Account  import views 


app_name = 'account'

urlpatterns = [
    path('login/', views.login_view , name='login'), 
    path('logout/', views.logout_view , name='logout'), 
    path('me/', views.profile_view , name='profile'), 
    path('signup/', views.signup_view , name='signup'), 
    
]
