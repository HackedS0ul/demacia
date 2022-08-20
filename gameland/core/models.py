from distutils.command.upload import upload
from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=120)
    class_name = models.CharField(max_length=100)
    attack_damage = models.IntegerField()
    ability_damage = models.IntegerField()
    armor = models.IntegerField()
    image = models.ImageField(upload_to='character', null=True)
