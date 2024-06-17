from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=128)
    number = models.IntegerField()
    type = models.CharField(max_length=128)
    # subtype = models.CharField(max_length=128, default='-')
    level = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id} - {self.name} '

# Create your models here.
