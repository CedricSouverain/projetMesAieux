from django.db import models

# https://docs.djangoproject.com/en/dev/ref/models/querysets

# python manage.py makemigrations
# python manage.py migrate
# python manage.py shell



# from main.models import maClasse
# mavariable = maClasse(prenom="mavaleur", nom="mavaleur")
# mavariable.prenom
# mavariable.nom
# mavariable.prenom = "changementDePrenom"
# mavariable.nom = "changementDeNom"
# mavariable.save()
# mavariable.delete()

# maClasse.objects.all()
# a = maClasse.objects.get(nom="souverain")
# a.delete()


# CharField(max_length=100)
# TextField(null=True) Pas de limite de taille
# null = True signifie que le champ n'est pas obligatoire



# Suppression Personne -> Suppression Utilisateur
# Creer personne avant Utilisateur
class Personne(models.Model):
	prenom = models.CharField(max_length=30, default="")
	nom = models.CharField(max_length=30, default="")
	genre = models.CharField(max_length=10, default="")
	nationalite = models.CharField(max_length=30, default="")
	lieux = models.CharField(max_length=30, default="")
	ddn = models.CharField(max_length=30, default="")
	ddm = models.CharField(max_length=30, blank =True, default="")
	ddd = models.CharField(max_length=30, blank =True, default="")
	famille = models.IntegerField(default=-1)
	pere = models.IntegerField(default=-1)
	mere = models.IntegerField(default=-1)
	mari = models.IntegerField(default=-1)
	
	def __str__(self):
		return self.prenom


class Document(models.Model):
	titre = models.CharField(max_length=30, default="")
	typeDocument = models.CharField(max_length=10, default="")
	description = models.CharField(max_length=30, default="")
	source = models.CharField(max_length=30, default="")

	annee = models.CharField(max_length=4, default="")
	motsClefs = models.CharField(max_length=30, default="")
	nomPl = models.CharField(max_length=30, default="")
	prenomPl = models.CharField(max_length=30, default="")

	def __str__(self):
		return self.titre


class Famille(models.Model):
	nom = models.CharField(max_length=30)

	def __str__(self):
		return self.nom


class Utilisateur(models.Model):
	identifiant = models.CharField(max_length=30, primary_key=True)
	mdp = models.CharField(max_length=30)
	mail = models.CharField(max_length=30)
	idPersonne = models.ForeignKey(Personne, on_delete=models.CASCADE, null=False)

	def __str__(self):
		return self.identifiant

		