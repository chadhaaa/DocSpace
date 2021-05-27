
from django.contrib import admin
from django.conf import settings 
from django.conf.urls.static import static
from django.urls import path
from apps.core.views import frontpage, signup
from django.contrib.auth import views 
from apps.feed.views import feed, search 
from apps.feed.api import api_tweet, api_like
from apps.userProfile.views import userprofile, follow_tweet, unfollow_tweet, followers, follows, edit_profile
from apps.conversation.views import conversations, conversation
from apps.conversation.api import api_add_message

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'), 
    path('signup/', signup, name='signup'), 
    path('logout/', views.LogoutView.as_view(), name= 'logout'), 
    path('login/', views.LoginView.as_view(template_name = 'core/login.html'), name='login'), 

    path('feed/', feed, name = 'feed'), 
    path('search/', search, name = 'search'),
    path('edit_profile/', edit_profile, name = 'edit_profile'), 
    path('u/<str:username>/', userprofile, name='userprofile'), 
    path('u/<str:username>/follow', follow_tweet, name='follow_tweet'), 
    path('u/<str:username>/unfollow', unfollow_tweet, name='unfollow_tweet'),
    path('u/<str:username>/followers', followers, name='followers'), 
    path('u/<str:username>/follows', follows, name='follows'), 
    
    path('api/add_tweett/', api_tweet, name = 'api_tweet'), 
    path('api/add_likee/', api_like, name = 'api_like'), 
    path('api/api_add_message/', api_add_message, name = 'api_add_message'), 

    path('conversations/', conversations, name = 'conversations'),
    path('conversations/<int:user_id>/', conversation, name = 'conversation'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
