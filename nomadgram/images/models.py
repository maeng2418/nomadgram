from django.db import models
from nomadgram.users import models as user_models

# Create your models here.
class TimeStampedModel(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True) # ó�� �����Ǿ������� �ڵ����� ��¥ �߰�
    updated_at = models.DateTimeField(auto_now=True) # ���� ����ɶ����� �ڵ����� ���ΰ�ħ
    class Meta:
        abstract = True # �����ͺ��̽��� �������� ����.(�����ͺ��̽��� ������� ����.)

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