from django.urls import path

from .views import home, news_by_category, news_detail


urlpatterns = [
    path('', home, name='home'),
    path('category/<int:category_id>/', news_by_category, name="news_by_category"),
    path('news/<int:pk>/', news_detail, name='news_detail'),
]