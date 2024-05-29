from django.db import models

# Create your models here.


class Funko(models.Model):
    name = models.CharField(max_length=128)
    number = models.IntegerField()
    collection = models.CharField(max_length=128)
    is_backlight = models.BooleanField(default=False)
    # user_id

    def __str__(self):
        return f'{self.number} - {self.name}'


class User(models.Model):
    name = models.CharField(max_length=128)
    funkos = models.ManyToManyField(Funko, blank=True)

    def str(self):
        return self.name


class Pokemon(models.Model):
    name = models.CharField(max_length=128)
    number = models.IntegerField()
    type = models.CharField(max_length=128)
    subtype = models.CharField(max_length=128)
    level = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} - {self.number} '


class Athlete(models.Model):
    name = models.CharField(max_length=128)
    sport_type = models.CharField(max_length=128)
    nationality = models.CharField(max_length=128)
    gender = models.CharField(max_length=16)

    def __str__(self):
        return f'{self.name} '
