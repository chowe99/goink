from django.db import models

class Dataset(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


# Create your models here.
