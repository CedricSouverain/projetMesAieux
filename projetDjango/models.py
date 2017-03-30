from django.db import models


# CharField(max_length=100)
# TextField(null=True) Pas de limite de taille
# null = True signifie que le champ n'est pas obligatoire

class Personne(models.Model):
	prenom = models.CharField(max_length=30)
	nom = models.CharField(max_length=30)
	
	def __str__(self):
		return self.prenom

		