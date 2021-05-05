from django.db import models


class Superhero(models.Model):
    name = models.CharField(max_length=20)
    alter_ego_name = models.CharField(max_length=20)
    primary_ability = models.CharField(max_length=20)
    secondary_ability = models.CharField(max_length=20)
    catchphrase = models.CharField(max_length=50)

    def __str__(self):
        return self.name
