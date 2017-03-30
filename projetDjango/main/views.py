from django.shortcuts import render
from django.http import HttpResponse
from models import *

from django.shortcuts import redirect
# Create your views here.

# A FAIRE

# 5 - Revoir le design du formulaire d'inscription

# 6 - Faire le tri sur les fonctions JS et les fonctions PYTHON + URLS

# 13 - Bonjour + prenom plutot que Bonjour + identifiant

# 15 - Ajouter mdp a la famille

idGlobal = ""
ajouterPersonneAFamille = False
nombrePartenaireInconnu = -2

def home(request):
	return render(request, "index.html", {})

def indexUtilisateur(request):
	global idGlobal
	u = Utilisateur.objects.get(identifiant=idGlobal)
	p = Personne.objects.get(id=int(u.idPersonne.id))

	# Famille
	if (p.famille == -1):
		famille = "Rejoindre une famille"
		pere = "Pas de pere"
		mere = "Pas de mere"
	else:
		famille = "Famille : "+str(Famille.objects.get(id=p.famille))
		if (p.pere == -1):
			pere = "<a href='ajouterPereMere'>Ajouter un pere</a>"
		if (p.mere == -1):
			mere = "<a href='ajouterPereMere'>Ajouter une mere</a>"

	if (p.pere != -1):
		pere = "<b>Pere : </b>"+str(Personne.objects.get(id=p.pere))
	if (p.mere != -1):
		mere = "<b>Mere : </b>"+str(Personne.objects.get(id=p.mere))

		
	return render(request, "indexUtilisateur_bloc.html", 
	{'identifiant':u.identifiant, 'nom':p.nom, 'prenom':p.prenom,
	'nationalite':p.nationalite, 'genre': p.genre, 
	'lieux':p.lieux,'ddn':p.ddn, 'ddm':p.ddm, 'ddd':p.ddd,
	'famille':famille, 'pere':pere, 'mere':mere})

def homeTemplateBis(request):
	global idGlobal
	if idGlobal == "":
		return render(request, "index.html", {})
	else:
		u = Utilisateur.objects.get(identifiant=idGlobal)
		p = Personne.objects.get(id=int(u.idPersonne.id))

		# Famille
		if (p.famille == -1):
			famille = "Rejoindre une famille"
			pere = "Pas de pere"
			mere = "Pas de mere"
		else:
			famille = "Famille : "+str(Famille.objects.get(id=p.famille))
			if (p.pere == -1):
				pere = "<a href='ajouterPereMere'>Ajouter un pere</a>"
			if (p.mere == -1):
				mere = "<a href='ajouterPereMere'>Ajouter une mere</a>"

		if (p.pere != -1):
			pere = "<b>Pere : </b>"+str(Personne.objects.get(id=p.pere))
		if (p.mere != -1):
			mere = "<b>Mere : </b>"+str(Personne.objects.get(id=p.mere))

		return render(request, "indexUtilisateur_bloc.html", 
		{'identifiant':u.identifiant, 'nom':p.nom, 'prenom':p.prenom,
		'nationalite':p.nationalite, 'genre': p.genre, 
		'lieux':p.lieux,'ddn':p.ddn, 'ddm':p.ddm, 'ddd':p.ddd,
		'famille':famille, 'pere':pere, 'mere':mere})

# CONNEXION
def submitConnexion(request):
	global idGlobal
	identi = idGlobal

	if identi == "": # Personne venant de la page home
		identi = request.POST.get("identifiant","")
		mdp = request.POST.get("password","")

		if Utilisateur.objects.filter(identifiant=identi, mdp=mdp).exists():
			u = Utilisateur.objects.get(identifiant=identi)
			p = Personne.objects.get(id=int(u.idPersonne.id))

			# Famille
			if (p.famille == -1):
				famille = "Rejoindre une famille"
				pere = "Pas de pere"
				mere = "Pas de mere"
			else:
				famille = "Famille : "+str(Famille.objects.get(id=p.famille))
				if (p.pere == -1):
					pere = "<a href='ajouterPereMere'>Ajouter un pere</a>"
				if (p.mere == -1):
					mere = "<a href='ajouterPereMere'>Ajouter une mere</a>"

			if (p.pere != -1):
				pere = "<b>Pere : </b>"+str(Personne.objects.get(id=p.pere))
			if (p.mere != -1):
				mere = "<b>Mere : </b>"+str(Personne.objects.get(id=p.mere))

	   		idGlobal = identi

			return render(request, "indexUtilisateur_bloc.html", 
			{'identifiant':identi, 'nom':p.nom, 'prenom':p.prenom,
			'nationalite':p.nationalite, 'genre': p.genre, 'lieux':p.lieux,
			'ddn':p.ddn, 'ddm':p.ddm, 'ddd':p.ddd,
			'famille':famille, 'pere':pere, 'mere':mere})

			# Inverser les deux cas, Erreur sur identifiant avant erreur sur mdp
		elif Utilisateur.objects.filter(identifiant=identi).exists():
			msgJs = "alert('Mot de passe incorrect !');"
			return render(request, "index.html", 
			{'alertJs':msgJs})

		else:
			msgJs = """alert("L'Utilisateur n'existe pas !");"""
			return render(request, "index.html", 
			{'alertJs':msgJs})


	else: # Si actualisation
		u = Utilisateur.objects.get(identifiant=identi)
		p = Personne.objects.get(id=int(u.idPersonne.id))

		# Famille
		if (p.famille == -1):
			famille = "Rejoindre une famille"
			pere = "Pas de pere"
			mere = "Pas de mere"
		else:
			famille = "Famille : "+str(Famille.objects.get(id=p.famille))
			if (p.pere == -1):
				pere = "<a href='ajouterPereMere'>Ajouter un pere</a>"
			if (p.mere == -1):
				mere = "<a href='ajouterPereMere'>Ajouter une mere</a>"

		if (p.pere != -1):
			pere = "<b>Pere : </b>"+str(Personne.objects.get(id=p.pere))
		if (p.mere != -1):
			mere = "<b>Mere : </b>"+str(Personne.objects.get(id=p.mere))


		return render(request, "indexUtilisateur_bloc.html", 
			{'identifiant':identi, 'nom':p.nom, 'prenom':p.prenom,
			'nationalite':p.nationalite, 'genre': p.genre, 'lieux':p.lieux,
			'ddn':p.ddn, 'ddm':p.ddm, 'ddd':p.ddd,
			'famille':famille,'pere':pere,'mere':mere})


# DECONNEXION
def deconnexion(request):
	global idGlobal
	idGlobal = ""
	return render(request, "index.html", {})

# INSCRIPTION
def inscription(request):
	return render(request, "templateBisFinaliserInscription_bloc.html", {})

def validerInscription(request):
	identi = request.POST.get("identifiant","")
	mail = request.POST.get("mail","")
	mdp1 = request.POST.get("password1","")
	mdp2 = request.POST.get("password2","")

	nom = request.POST.get("nom","")
	prenom = request.POST.get("prenom","")
	nationalite = request.POST.get("nationalite","")
	genre = request.POST.get("genre","")
	lieux = request.POST.get("lieux","")
	ddn = request.POST.get("ddn","")
	ddm = request.POST.get("ddm","")
	ddd = request.POST.get("ddd","")



	if Utilisateur.objects.filter(identifiant=identi).exists():	# Utilisateur existe deja
		msgJs = """alert("Cet identifiant existe deja !");"""
		return render(request, "templateBisFinaliserInscription_bloc.html", 
			{'alertJs':msgJs})


	else: # Si le nom d'identifiant est libre
		if mdp1 != mdp2:
			msgJs = """alert("Les deux MDP sont differents !");"""
			return render(request, "templateBisFinaliserInscription_bloc.html", 
			{'alertJs':msgJs})


		else: #Creer Utilisateur + Personne
			np = Personne(prenom=prenom,nom=nom,genre=genre, nationalite=nationalite,lieux=lieux,ddn=ddn,ddm=ddm,ddd=ddd)
			np.save()

			nu = Utilisateur(identifiant=identi,mdp=mdp1,mail=mail,idPersonne=np)
			nu.save()

			global idGlobal
			idGlobal = identi

			#Famille
			famille = "Rejoindre une famille"
			pere = "Pas de pere"
			mere = "Pas de mere"

			return render(request, "indexUtilisateur_bloc.html", 
				{'identifiant':identi, 'nom':nom, 'prenom':prenom,
				'nationalite':nationalite, 'genre':genre, 'lieux':lieux,
				'ddn':ddn, 'ddm':ddm, 'ddd':ddd,
				'famille':famille, 'pere':pere, 'mere':mere})


# AJOUT PERSONNE
def pageAjouterPersonne(request):
	return render(request, "templateBisAjouterPersonne_bloc.html", {})

def ajouterPersonne(request):
	nom = request.POST.get("nom","")
	prenom = request.POST.get("prenom","")
	nationalite = request.POST.get("nationalite","")
	genre = request.POST.get("genre","")
	lieux = request.POST.get("lieux","")
	ddn = request.POST.get("ddn","")
	ddm = request.POST.get("ddm","")
	ddd = request.POST.get("ddd","")

	global idGlobal
	global ajouterPersonneAFamille
	u = Utilisateur.objects.get(identifiant=idGlobal)
	p = Personne.objects.get(id=int(u.idPersonne.id))

	if ajouterPersonneAFamille:
		np = Personne(prenom=prenom,nom=nom,genre=genre, 
			nationalite=nationalite,lieux=lieux,ddn=ddn,
			ddm=ddm,ddd=ddd,famille=p.famille)
	else:
		np = Personne(prenom=prenom,nom=nom,genre=genre, 
			nationalite=nationalite,lieux=lieux,ddn=ddn,
			ddm=ddm,ddd=ddd)
	np.save()

	

	# Famille
	if (p.famille == -1):
		famille = "Rejoindre une famille"
		pere = "Pas de pere"
		mere = "Pas de mere"
	else:
		famille = "Famille : "+str(Famille.objects.get(id=p.famille))
		if (p.pere == -1):
			pere = "<a href='ajouterPereMere'>Ajouter un pere</a>"
		if (p.mere == -1):
			mere = "<a href='ajouterPereMere'>Ajouter une mere</a>"

	if (p.pere != -1):
		pere = "<b>Pere : </b>"+str(Personne.objects.get(id=p.pere))
	if (p.mere != -1):
		mere = "<b>Mere : </b>"+str(Personne.objects.get(id=p.mere))

	return render(request, "indexUtilisateur_bloc.html", 
	{'identifiant':u.identifiant, 'nom':p.nom, 'prenom':p.prenom,
	'nationalite':p.nationalite, 'genre': p.genre, 
	'lieux':p.lieux,'ddn':p.ddn, 'ddm':p.ddm, 'ddd':p.ddd,
	'famille':famille, 'pere':pere, 'mere':mere})

def rechercherPersonne(request):
	nom = request.POST.get("nom","")
	prenom = request.POST.get("prenom","")
	genre = request.POST.get("genre","")
	nationalite = request.POST.get("nationalite","")
	lieux = request.POST.get("lieux","")
	ddn = request.POST.get("ddn","")
	ddm = request.POST.get("ddm","")
	ddd = request.POST.get("ddd","")

	p = Personne.objects.all()

	if nom != "":
		p = p.filter(nom=nom)
	if prenom != "":
		p = p.filter(prenom=prenom)
	if genre != "":
		p = p.filter(genre=genre)
	if nationalite != "":
		p = p.filter(nationalite=nationalite)
	if lieux != "":
		p = p.filter(lieux=lieux)
	if ddn != "":
		p = p.filter(ddn=ddn)
	if ddm != "":
		p = p.filter(ddm=ddm)
	if ddd != "":
		p = p.filter(ddd=ddd)

	valeur = "<i>Cliquez sur une personne pour avoir ses informations personnelles</i><br/><br/>"

	for i in range(0,len(p)):
		valeur += "<a href='afficherDonneesPerso/"+str(p[i].id)+"'>"+str(p[i])+" "+str(p[i].nom)+"</a><br/>"

	return render(request, "templateBisRechercherPersonne.html", 
		{'droite_resultat':valeur})


# DOCUMENTS
# Fonction appele lorsque la personne actionne le bouton Rechercher
# dans le formulaire.
def rechercherDocument(request):
	# On recupere les champs du formulaire et on les enregistre
	# dans des varibales
	titre = request.POST.get("titre","")
	typeDocument = request.POST.get("typeDocument","")
	anneeDocument = request.POST.get("anneeDocument","")
	motsClefs = request.POST.get("motsClefs","")
	nomPl = request.POST.get("nomPl","")
	prenomPl = request.POST.get("prenomPl","")

	# On prend tout les Documents enregistre dans la base de donnees
	d = Document.objects.all()

	# Si le titre a ete mentionne, on applique le filtre
	if titre != "":
		# On prend seulement les documents qui ont le titre mentionne
		d = d.filter(titre=titre)
	# Si le type du document a ete mentionne, on applique le filtre
	if typeDocument != "":
		d = d.filter(typeDocument=typeDocument)
	if anneeDocument != "":
		d = d.filter(annee=anneeDocument)
	if motsClefs != "":
		d = d.filter(motsClefs=motsClefs)
	if nomPl != "":
		d = d.filter(nomPl=nomPl)
	if prenomPl != "":
		d = d.filter(prenomPl=prenomPl)

	# valeur est la varibale enregistrant le contenu que l'on va
	# renvoyer au template
	valeur = "<i>Cliquez sur un document pour avoir ses informations personnelles</i><br/><br/>"

	# On parcours la liste d contenant tous les documents correspondants 
	# a la recherche effectuee
	for i in range(0,len(d)):
		# On specifie qu'il s'agit d'un lien avec la balise HTML <a></a>
		valeur += "<a href='affichageDocument/"+str(d[i].id)+"'>"+str(d[i])+"</a><br/>"

	# On redirige l'utilisateur vers la page ou il pourra
	# visualiser les resultats, effectuer une seconde recherche
	# ou avoir plus d'informations sur le ou les documents qu'il recherche
	return render(request, "templateBisRechercherDocument.html", 
		{'droite_resultat':valeur})

# Fonction appelee lorsque l'utilisateur clique sur un document
# On passe en parametre la clef de document pour savoir quel
# document cela concerne
def affichageDocument(request,idDocument):
	# On recupere le document correspondant a l'id passe en parametre
	d  = Document.objects.get(id=idDocument)	
	# On extrait les attributs du document dans des variables
	titre = d.titre
	typeDocument = d.typeDocument
	description = d.description
	source = d.source
	anneeDocument = d.annee
	motsClefs = d.motsClefs
	nomPl = d.nomPl
	prenomPl = d.prenomPl


	# Si le document est une image, alors on affiche l'image
	if typeDocument == "image":
		fichierDocument = "<img src='/my_app/img/"+source+"' height='42' width='42'>"
	else:
		fichierDocument = ""

	return render(request, "templateBisAffichageDocument.html", 
		{'titre': titre, 'annee': anneeDocument,
		 'description': description,
		 'nompl': nomPl, 'prenompl': prenomPl, 'motsClefs': motsClefs,
		 'document': fichierDocument })
	# return redirect('/indexUtilisateur')

def pageAjouterDocument(request):
	return render(request, "templateBisAjouterDocument_bloc.html", {})

def ajouterDocument(request):
	titre = request.POST.get("titre","")
	annee = request.POST.get("annee","")
	typeDocument = request.POST.get("typeDocument","")
	source = request.POST.get("source","")
	description = request.POST.get("description","")
	nomPl = request.POST.get("nompl","")
	prenomPl = request.POST.get("prenompl","")
	motsclefs = request.POST.get("motsclefs","")

	d = Document(titre=titre, typeDocument=typeDocument,
		description=description, source=source, annee=annee,
		motsClefs=motsclefs, nomPl=nomPl, prenomPl=prenomPl)
	d.save()

	return indexUtilisateur(request)


	# return render(request, "templateBisAjouterDocument_bloc.html", {})

def afficherDonneesPerso(request,idPersonne):
	global idGlobal
	p = Personne.objects.get(id=idPersonne)
	uPersonne = Utilisateur.objects.filter(idPersonne=idPersonne)

	if len(uPersonne) > 0: # Si cette personne est liee a un utilisateur
		# On ne peut pas modifier ses informations
		if idGlobal=="": #Visiteur
			return render(request, "templateBisVisualiserDonneesPersonneVisiteur.html", 
				{'nom':p.nom, 'prenom':p.prenom, 'genre':p.genre,
				'nationalite': p.nationalite, 'lieux':p.lieux, 'ddn':p.ddn,
				'ddm':p.ddm, 'ddd':p.ddd })
		else:
			return render(request, "templateBisVisualiserDonneesPersonneUtilisateur.html", 
				{'nom':p.nom, 'prenom':p.prenom, 'genre':p.genre,
				'nationalite': p.nationalite, 'lieux':p.lieux, 'ddn':p.ddn,
				'ddm':p.ddm, 'ddd':p.ddd })

	else:
		# On peut modifier ses infos, seulement si on est un Utilisateur
		if idGlobal != "":

			modifDonnees = """<form action='/modifierDonneesPersoDunePersonne/"""+str(idPersonne)+"""'>
							<div class="input-group">
								<input type="submit" name="modiferPerso" value="Modifier ses donnees perso" class="btn wow tada btn-embossed btn-primary">
							</div>
						</form>"""


			famille = ""
			pere = ""
			mere = ""

			if p.famille != -1:
				famille = Famille.objects.get(id=p.famille)
			if p.pere != -1:
				pere = Personne.objects.get(id=p.pere)
			if p.mere != -1:
				mere = Personne.objects.get(id=p.mere)

			modifFamille = """<form action='/modifierDonneesFamilleDunePersonne/"""+str(idPersonne)+"""'>
							<div class="input-group">
								<input type="submit" name="modiferFamille" value="Modifier ses donnees de famille" class="btn wow tada btn-embossed btn-primary">
							</div>
						</form>"""


			return render(request, "templateBisVisualiserDonneesPersonneUtilisateur.html", 
				{'nom':p.nom, 'prenom':p.prenom, 'genre':p.genre,
				'nationalite': p.nationalite, 'lieux':p.lieux, 'ddn':p.ddn,
				'ddm':p.ddm, 'ddd':p.ddd, 'modifierDonneesPerso':modifDonnees,
				'famille':famille, 'modifierFamille':modifFamille,
				'pere':pere, 'mere':mere })

		else: # Meme chose que si ce nest pas un utilisateur 
		# car le visiteur ne peut pas modifier des donnees
			return render(request, "templateBisVisualiserDonneesPersonneVisiteur.html", 
				{'nom':p.nom, 'prenom':p.prenom, 'genre':p.genre,
				'nationalite': p.nationalite, 'lieux':p.lieux, 'ddn':p.ddn,
				'ddm':p.ddm, 'ddd':p.ddd })


def modifierDonneesPersoDunePersonne(request,idPersonne):
	p = Personne.objects.get(id=idPersonne)

	if p.genre == "M":
		body_genre_male = "checked='checked'"
		body_genre_femme = ""
	else:
		body_genre_male = ""
		body_genre_femme = "checked='checked'"
   
	return render(request, "templateBisModifierDonneesPersoExterne_bloc.html", 
		{'prenom':p.prenom, 'nom':p.nom, 'body_genre_male':body_genre_male, 
		'body_genre_femme':body_genre_femme,
		'nationalite':p.nationalite, 'lieux':p.lieux,
		'ddn':p.ddn, 'ddm':p.ddm, 'ddd':p.ddd })

def validerModificationDonneesPersoDunePersonne(request):
	return HttpResponse("Modifier donneees")

def modifierDonneesFamilleDunePersonne(request,idPersonne):
	p = Personne.objects.get(id=idPersonne)
	return HttpResponse("Modifier donneees famille "+str(p))


# DONNEEES PERSO
def modifierDonneesPersonelles(request):
	global idGlobal
	identi = idGlobal

	u = Utilisateur.objects.get(identifiant=identi)
	p = Personne.objects.get(id=u.idPersonne.id)

	if p.genre == "M":
		body_genre_male = "checked='checked'"
		body_genre_femme = ""
	else:
		body_genre_male = ""
		body_genre_femme = "checked='checked'"
   
	return render(request, "templateBisModifierDonneesPerso_bloc.html", 
		{'identifiant':identi, 'mail':u.mail, 'mdp1':u.mdp, 'mdp2':u.mdp,
		'prenom':p.prenom, 'nom':p.nom, 'body_genre_male':body_genre_male, 'body_genre_femme':body_genre_femme,
		'nationalite':p.nationalite, 'lieux':p.lieux,
		'ddn':p.ddn, 'ddm':p.ddm, 'ddd':p.ddd })


def validerModificationDonneesPerso(request):
	global idGlobal
	identi = idGlobal
	u = Utilisateur.objects.get(identifiant=idGlobal)
	p = Personne.objects.get(id=u.idPersonne.id)

	mail = request.POST.get("mail","")
	mdp1 = request.POST.get("password1","")
	mdp2 = request.POST.get("password2","")

	nom = request.POST.get("nom","")
	prenom = request.POST.get("prenom","")
	nationalite = request.POST.get("nationalite","")
	genre = request.POST.get("genre","")
	lieux = request.POST.get("lieux","")
	ddn = request.POST.get("ddn","")
	ddm = request.POST.get("ddm","")
	ddd = request.POST.get("ddd","")

	if mdp1 != mdp2:
		if p.genre == "M":
			body_genre_male = "checked='checked'"
			body_genre_femme = ""
		else:
			body_genre_male = ""
			body_genre_femme = "checked='checked'"
		
		msgJs = "alert('Les deux MDP sont differents !');"

		return render(request, "templateBisModifierDonneesPerso_bloc.html", 
		{'alertJs':msgJs,'identifiant':identi, 'mail':u.mail, 'mdp1':u.mdp, 'mdp2':u.mdp,
		'prenom':p.prenom, 'nom':p.nom, 'body_genre_male':body_genre_male, 'body_genre_femme':body_genre_femme,
		'nationalite':p.nationalite, 'lieux':p.lieux,
		'ddn':p.ddn, 'ddm':p.ddm, 'ddd':p.ddd })



	else: #Modifier Utilisateur + Personne
		p.nom = nom
		p.prenom = prenom
		p.nationalite = nationalite
		p.genre = genre
		p.lieux = lieux
		p.ddn = ddn
		p.ddm = ddm
		p.ddd = ddd
		p.save()

		u.mdp = mdp1
		u.mail = mail
		u.save()

		# Famille
		if (p.famille == -1):
			famille = "Rejoindre une famille"
			pere = "Pas de pere"
			mere = "Pas de mere"
		else:
			famille = "Famille : "+str(Famille.objects.get(id=p.famille))
			if (p.pere == -1):
				pere = "<a href='ajouterPereMere'>Ajouter un pere</a>"
			if (p.mere == -1):
				mere = "<a href='ajouterPereMere'>Ajouter une mere</a>"

		if (p.pere != -1):
			pere = "<b>Pere : </b>"+str(Personne.objects.get(id=p.pere))
		if (p.mere != -1):
			mere = "<b>Mere : </b>"+str(Personne.objects.get(id=p.mere))

		return render(request, "indexUtilisateur_bloc.html", 
			{'identifiant':identi, 'nom':nom, 'prenom':prenom,
				'nationalite':nationalite, 'genre':genre, 'lieux':lieux,
				'ddn':ddn, 'ddm':ddm, 'ddd':ddd,
				'famille':famille, 'pere':pere, 'mere':mere})




# FAMILLE
# Affichage de la page recherche
def pageRechercherFamille(request):
	return render(request, "templateBisRechercherFamille.html", {})


# Affichage du resultat de la recherche famille
def rechercherFamille(request):
	nomFamille = request.POST.get("nomFamille","")
	valeur = ""
	global idGlobal
	commentaire = ""
	u = Utilisateur.objects.get(identifiant=idGlobal)
	pers = Personne.objects.get(id=u.idPersonne.id)
	familleUtilisateur = pers.famille

	if idGlobal=="":
		commentaire = "Cliquez sur une famille pour y rentrer"


	f = Famille.objects.all()
	if nomFamille != "":
		f = f.filter(nom=nomFamille)

	for i in range(0,len(f)): #Pour chaque famille
		if idGlobal!="" and familleUtilisateur==f[i].id:
			valeur += "<a style='font-size:1.5em;' href='rejoindreFamille/"+str(i+1)+"'>"+str(f[i])+"</a><i> (Ma famille)</i> <br/>"
		else:
			valeur += "<a style='font-size:1.5em;' href='rejoindreFamille/"+str(i+1)+"'>"+str(f[i])+"</a><br/>"
		p = Personne.objects.all()
		p = p.filter(famille=f[i].id)
		for j in range(0,len(p)):
			valeur += str(p[j]) + " "+ str(p[j].nom)+", "
		if idGlobal!="" and familleUtilisateur==f[i].id:
			valeur += "<br/><a href='pageAjouterPersonne'>Ajouter une personne a cette famille</a><br/>"
			global ajouterPersonneAFamille
			ajouterPersonneAFamille = True

		valeur += "<br/><br/>"


	return render(request, "templateBisRechercherFamille.html",
		{'droite_resultat':valeur,
		'commentaire':commentaire})


# Ajout de la famille dans la bdd
def ajouterFamille(request):
	nomFamilleAjoute = request.POST.get("nomFamilleAjoute")

	f = Famille(nom=nomFamilleAjoute)
	f.save()
	return render(request, "templateBisRechercherFamille.html", {})


def rejoindreFamille(request,idFamille):
	global idGlobal
	u = Utilisateur.objects.get(identifiant=idGlobal)
	p = Personne.objects.get(id=u.idPersonne.id)
	if (int(idFamille) != p.famille):
		p.famille = idFamille
		p.pere = -1
		p.mere = -1
		p.save()

	return redirect('/indexUtilisateur')

# Ajout des parents
def ajouterPereMere(request):
	global idGlobal
	val = "<option>"

	u = Utilisateur.objects.get(identifiant=idGlobal)

	p = Personne.objects.get(id=u.idPersonne.id)

	pereMere = Personne.objects.all()
	pereMere = pereMere.filter(famille=p.famille).exclude(id=p.id)

	for i in range(0,len(pereMere)):
		val += "<option>"+str(pereMere[i])
	select_pere = val
	select_mere = val

	
	return render(request, "templateBisAjouterPereMere_bloc.html", 
		{'test' : pereMere,
		'contenu_select_pere' : select_pere,
		'contenu_select_mere' : select_mere})

def enregistrerPereMere(request):
	nouv_pere = request.POST.get("pere")
	if nouv_pere != "":
		pere = Personne.objects.get(prenom=nouv_pere)

	nouv_mere = request.POST.get("mere")
	if nouv_mere != "":
		mere = Personne.objects.get(prenom=nouv_mere)

	global idGlobal

	u = Utilisateur.objects.get(identifiant=idGlobal)
	p = Personne.objects.get(id=u.idPersonne.id)

	if nouv_pere != "":
		p.pere = pere.id
	if nouv_mere != "":
		p.mere = mere.id
	p.save()

	return indexUtilisateur(request)

# Arbre
def fct(p,idMari):
	liste_liste = []
	global nombrePartenaireInconnu

	pere_inconnu = p.pere
	mere_inconnu = p.mere

	if (p.pere != -1) and (p.mere !=-1):	# Si la personne a un pere et une mere
		pere = Personne.objects.get(id=p.pere)
		mere = Personne.objects.get(id=p.mere)

		liste_liste_pere = fct(pere,mere.id)
		liste_liste.extend(liste_liste_pere)

		liste_liste_mere = fct(mere,pere.id)
		liste_liste.extend(liste_liste_mere)

	elif p.pere != -1:	# Si elle a un pere
		pere = Personne.objects.get(id=p.pere)

		liste_liste_pere = fct(pere,-1)
		liste_liste.extend(liste_liste_pere)

		# Creation d'une mere inconnue
		liste_liste_mereInconnue = [str(nombrePartenaireInconnu),"","F",
			"-1","-1",str(p.pere)]
		nombrePartenaireInconnu = nombrePartenaireInconnu -1
		liste_liste.append(liste_liste_mereInconnue)
		mere_inconnu = nombrePartenaireInconnu+1

	elif p.mere != -1:	# Si elle a une mere
		mere = Personne.objects.get(id=p.mere)

		liste_liste_mere = fct(mere,-1)
		liste_liste.extend(liste_liste_mere)

		# Creation d'un pere inconnu
		liste_liste_pereInconnue = [str(nombrePartenaireInconnu),"","M",
			"-1","-1",str(p.mere)]
		nombrePartenaireInconnu = nombrePartenaireInconnu -1
		liste_liste.append(liste_liste_pereInconnue)
		pere_inconnu = nombrePartenaireInconnu+1

	if idMari != -1:	# Si la personne a un conjoint annonce dans la bdd
		liste_moi = [str(p.id),str(p.prenom),str(p.genre),
			str(mere_inconnu),str(pere_inconnu),str(idMari)]
	else:				# Pas de conjoint annonce dans la bdd
		liste_moi = [str(p.id),str(p.prenom),str(p.genre),
			str(mere_inconnu),str(pere_inconnu),str(p.id)]

	liste_liste.append(liste_moi)

	return liste_liste


def creerListe():
	global idGlobal
	u = Utilisateur.objects.get(identifiant=idGlobal)
	p = Personne.objects.get(id=u.idPersonne.id)

	global nombrePartenaireInconnu
	nombrePartenaireInconnu = -2

	listePersonne = fct(p,-1) # (Personne, idMari)

	return listePersonne


def visualiserArbre(request):	
	liste = creerListe()

	return render(request, "templateBisArbre.html", 
	 	{'my_data':liste,'titre':"Mon arbre"})