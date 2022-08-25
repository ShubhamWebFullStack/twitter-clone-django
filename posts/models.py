from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
    class Meta(object):
        db_table = "Post"

    name = models.CharField (
        "Name", blank=False, null=False, default="Anonymous", max_length=60, db_index=True
    )    

    body = models.CharField (
        "Body", blank=False, null=False, default="What's Happening?", max_length=500, db_index=True
    )

    image = CloudinaryField (
        "Post Image", blank=True, null=True
    )

    like_count = models.PositiveIntegerField (
        "Likes", blank=True, null=False, default=0
    )

    created_at = models.DateTimeField (
        "Post Created At", auto_now_add=True
    )

    updated_at = models.DateTimeField (
        "Post Updated At", auto_now=True
    )

    def __str__(self):
        return self.name
