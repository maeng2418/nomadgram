from django.db import models
from nomadgram.users import models as user_models

# Create your models here.
class TimeStampedModel(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True) # 처음 생성되었을때만 자동으로 날짜 추가
    updated_at = models.DateTimeField(auto_now=True) # 모델이 저장될때마다 자동으로 새로고침
    class Meta:
        abstract = True # 데이터베이스를 생성하지 않음.(데이터베이스와 연결되지 않음.)

class Image(TimeStampedModel):

    """ Image Model """
    
    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.CASCADE)

class Comment(TimeStampedModel):

    """ Comment Model """

    message = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, null=True, on_delete=models.CASCADE)

class Like(TimeStampedModel):

    """ Like Model """

    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, null=True, on_delete=models.CASCADE)