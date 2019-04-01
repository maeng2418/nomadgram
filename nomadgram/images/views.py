from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers

class ListAllImages(APIView):

    # request from browser.
    def get(self, request, format=None):
        all_images =models.Image.objects.all() # All elements from Model.
        
        serializer = serializers.ImageSerializer(all_images, many=True) # serializer deals only one. So, Set many=True for getting all data.
        
        return Response(data=serializer.data) # return converted Response.