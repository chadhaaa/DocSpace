
from django.contrib import admin
from django.urls import path
from apps.core.views import frontpage, signup
from django.contrib.auth import views 
from apps.feed.views import feed 
from apps.feed.api import api_tweet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'), 
    path('signup/', signup, name='signup'), 
    path('logout/', views.LogoutView.as_view(), name= 'logout'), 
    path('login/', views.LoginView.as_view(template_name = 'core/login.html'), name='login'), 

    path('feed/', feed, name = 'feed'), 
    
    path('api/add_tweet/', api_tweet, name = 'api_tweet'), 
]