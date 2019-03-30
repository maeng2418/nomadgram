from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers

class ListAllImages(APIView):

    # 브라우저로부터 요청을 받음.
    def get(self, request, format=None):
        all_images =models.Image.objects.all() # 모델안의 모든 엘리멘트 가져옴.
        
        serializer = serializers.ImageSerializer(all_images, many=True) # serializer는 하나만 취급하므로 many=True로 설정해서 모든 것을 가져온다.
        
        return Response(data=serializer.data) # 응답으로 변환된 엘리먼트 반환.