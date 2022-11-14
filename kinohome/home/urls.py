from django.urls import path, include
from .views import *
from users.views import *
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.contrib import admin
from django.conf.urls.static import static


urlpatterns = [
    path('', cache_page(860)(Home.as_view()), name='home'),
    path('filter/', Filter_kino.as_view(), name='filter'),
    path('producer/<str:slug>/', cache_page(860)(Get_Producer.as_view()), name='producer'),
    path('author/<str:slug>/', cache_page(860)(Get_Author.as_view()), name='producer'),
    path('scenario/<str:slug>/', cache_page(860)(Get_Scenario.as_view()), name='producer'),
    path('Recommendations/', cache_page(860)(Recommendations.as_view()), name='get_rec'),
    path('category/<str:slug>/', cache_page(860)(PostByCategory.as_view()), name='get_category'),
    path('country/<str:slug>/', cache_page(860)(PostByCountry.as_view()), name='get_country'),
    path('production_year/<str:slug>/', cache_page(860)(PostByProduction_year.as_view()), name='get_production_year'),
    path('kino/<str:slug><int:pk>/', never_cache(GetKino.as_view()), name='get_kino'),
    path('category/', cache_page(860)(Category_kino.as_view()), name='category'),
    path('add_favorite/', add_favorite, name='add_favorite'),
    path('add_emailsub/', add_emailSub, name='add_emailSub'),
    path('search/', Search.as_view(), name='search'),
    path('favorite_kino/', Favorite_kino.as_view(), name='favorite_kino'),
    path('plans_kino/', Plans_kino.as_view(), name='plan_kino'),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)