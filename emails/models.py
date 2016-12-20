from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Email(models.Model):
    to_user = models.ForeignKey(User)
    from_user = models.ForeignKey(User)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

