from django.db import models


# Create your models here.
class Brend(models.Model):
    name = models.CharField(max_length=20)
    # img = models.CharField(max_length=100)
    img = models.FileField(upload_to='static/img-brend/')
    code = models.TextField()
