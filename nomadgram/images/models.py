from django.db import models
from nomadgram.users import models as user_models

# Create your models here.
class TimeStampedModel(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True) # Add the time automatically, when they were generated first.
    updated_at = models.DateTimeField(auto_now=True) # Refresh the time automatically, when they saved.
    class Meta:

        abstract = True # Don't make database (It doesn't connect with DB)

class Image(TimeStampedModel):

    """ Image Model """

    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return 'User:{} - Image Caption:{}'.format(self.location, self.caption)

class Comment(TimeStampedModel):

    """ Comment Model """

    message = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, null=True, on_delete=models.CASCADE, related_name='comments')

class Like(TimeStampedModel):

    """ Like Model """

    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, null=True, on_delete=models.CASCADE, related_name='likes')