from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterAPIView.as_view(), name='api-register'),
    path('login/', views.LoginAPIView.as_view(), name='api-login'),
    path('profile/', views.ProfileAPIView.as_view(), name='api-profile'),
    path('follow/<int:user_id>', views.follow_user, name='api-follow'),
    path('unfollow/<int:user_id>/', views.unfollow_user, name='api-unfollow'),
]
