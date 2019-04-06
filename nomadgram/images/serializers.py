from rest_framework import serializers
from . import models
from nomadgram.users import models as user_models

class FeedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = user_models.User
        fields = (
            'username', # In models.py name is declared but we are extending from AbstractUser and that one has username
            'profile_image'
        )
class LikeSerializer(serializers.ModelSerializer):

    # Meta class is extra information
    class Meta:
        model = models.Like
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    
    creator = FeedUserSerializer()
    # Meta class is extra information
    class Meta:
        model = models.Comment
        fields = (
            'id',
            'message',
            'creator'
        )

class ImageSerializer(serializers.ModelSerializer):

    # Bring inside Object instead of the ID
    comments = CommentSerializer(many=True)
    creator = FeedUserSerializer()

    # Meta class is extra information
    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'comments', # Letter use lower name of model.
            'like_count',
            'creator'
        )