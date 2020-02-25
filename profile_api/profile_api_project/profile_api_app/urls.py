from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
# for model view set no need basename
router.register('profile-api', views.ProfileApiViewSet)
router.register('login-api', views.LogInApiViewSet, basename='login-api')
router.register('feed-api', views.FeedItemApiViewSet)

urlpatterns = [
    path('', include(router.urls)),
]