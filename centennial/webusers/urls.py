from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

# app url patterns
urlpatterns = [
    path('register/',views.register_view,name='register'),
    path('profile/',views.profile_view,name='profile'),
    path('profile/edit',views.profile_update_view,name='profile-update'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('pw-reset/',LoginView.as_view(),name='password_reset'), # TODO create pw reset
]
