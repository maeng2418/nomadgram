from rest_framework import serializers
from . import models
class ImageSerializer(serializers.Serializer):

    # Meta class is extra information
    class Meta:
        model = models.Image
        fields = '__all__'

class LikeSerializer(serializers.Serializer):

    # Meta class is extra information
    class Meta:
        model = models.Like
        fields = '__all__'

class CommentSerializer(serializers.Serializer):

    # Meta class is extra information
    class Meta:
        model = models.Comment
        fields = '__all__'