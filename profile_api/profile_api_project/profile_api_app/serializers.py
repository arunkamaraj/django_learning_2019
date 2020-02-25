from rest_framework.serializers import ModelSerializer
from . import models

class UserProfileSerializers(ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        if validated_data:
            user = models.UserProfile(email=validated_data['email'], name=validated_data['name'])
            user.set_password(validated_data['password'])
            user.save()
            return user

class FeedItemSerializers(ModelSerializer):

    class Meta:
        model = models.FeedItem
        fields = ['id', 'user_profile', 'content', 'created_on']
        extra_kwargs = {'user_profile': {'read_only': True}}
