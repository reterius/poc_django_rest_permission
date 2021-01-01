from rest_framework.routers import DefaultRouter
from django.urls import path, include

from tweet import views

router = DefaultRouter()
router.register('tweets', views.TweetViewSet, basename='tweet-list')

urlpatterns = [
    path('', include(router.urls)),

]
