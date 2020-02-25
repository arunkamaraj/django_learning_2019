from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication  # important
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers
from . import permissions


# Create your views here.
class ProfileApiViewSet(viewsets.ModelViewSet):
    # below both from GenericAPIView class
    serializer_class = serializers.UserProfileSerializers
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UserProfilePermission,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('email', 'name',)  # usually will forget this search fields

    # we can use viewset create method to save / post the user data with
    # encrypted password  here but it also depends on serializer create method


# LoginAPI
class LogInApiViewSet(viewsets.ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self, request):
        return ObtainAuthToken().post(request)


class FeedItemApiViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FeedItemSerializers
    queryset = models.FeedItem.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.OwnFeedPermission, IsAuthenticated) # only to hide the list

    # If we want to restrict even the list add IsAuthedicated


    def perform_create(self, serializer):
        # here the user profile field is from serialzer
        serializer.save(user_profile=self.request.user)
