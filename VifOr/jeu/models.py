from django.db import models
class Game(models.Model):
    taille_map= models.IntegerField()
    nbr_tour=models.IntegerField()
    timeout_tour=models.IntegerField()
    demarrer_partie=models.BooleanField()
# Create your models here.
