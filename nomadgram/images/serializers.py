from rest_framework import serializers
from . import models

class LikeSerializer(serializers.ModelSerializer):

    # Meta class is extra information
    class Meta:
        model = models.Like
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    
    # Meta class is extra information
    class Meta:
        model = models.Comment
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):

    # Bring inside Object instead of the ID
    comment_set = CommentSerializer(many=True)
    like_set = LikeSerializer(many=True)

    # Meta class is extra information
    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'comment_set', # Letter use lower name of model.
            'like_set'
        )