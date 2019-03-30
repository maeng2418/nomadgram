from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers

class ListAllImages(APIView):

    # �������κ��� ��û�� ����.
    def get(self, request, format=None):
        all_images =models.Image.objects.all() # �𵨾��� ��� ������Ʈ ������.
        
        serializer = serializers.ImageSerializer(all_images, many=True) # serializer�� �ϳ��� ����ϹǷ� many=True�� �����ؼ� ��� ���� �����´�.
        
        return Response(data=serializer.data) # �������� ��ȯ�� ������Ʈ ��ȯ.