from django.urls import path, include
from .views import *
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static



urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', Logout_user, name='logout'),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)