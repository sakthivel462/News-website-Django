from django.urls import path

from news import settings
from . import views
from django.conf.urls.static import static


urlpatterns =[
    path('', views.news, name="news"),
    path('news/<str:pk>/', views.new,name="single-news"),
    path('New/', views.new_news, name='new-news'),
    path('category/<str:tag_name>/', views.news_by_tag, name='news-by-tag'), 
    path('magazine/', views.magazine_page, name='magazine_page'),
    path('magazine/<str:pk>/', views.single_magazine, name="single-mag")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
