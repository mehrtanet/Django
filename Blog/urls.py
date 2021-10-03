from django.urls import path
from Blog  import views 


app_name = 'blog'

urlpatterns = [
path('', views.home_view , name='home'), 
path('post/', views.post_view , name='post'), 
path('detailpost/<str:slug>/', views.post_detail_view , name='detailpost'), 
]
