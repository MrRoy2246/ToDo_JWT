--------------->Models.py-------------------

from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=400, blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


                then...
.....................migrate and migrations..............

add serializer----------------> we can add manually with serializers.serializer.but here i use serializers.Modelserializer.
then add view urls.
tasks----> createlistapiview also authenticate this.
register---->Createapiview with in serializer because django authomatic check user duplicate etc