from rest_framework import serializers
from . import models
class ImageSerializer(serializers.ModelSerializer):

    # Meta class is extra information
    class Meta:
        model = models.Image
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):

    image = ImageSerializer()

    # Meta class is extra information
    class Meta:
        model = models.Like
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    image = ImageSerializer()
    
    # Meta class is extra information
    class Meta:
        model = models.Comment
        fields = '__all__'