from django.db import models

class Personne(models.Model):
	prenom = models.CharField(max_length=30)
	nom = models.CharField(max_length=30)
	
	def __str__(self):
		return self.nom

		