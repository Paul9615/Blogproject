from django.db import models

# Create your models here.


class Portfolio(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=225)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title
