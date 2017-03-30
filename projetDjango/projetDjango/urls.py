"""projetDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import url
from django.contrib import admin
from main import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.home), # Home = fonction dans views.py
    url(r'^homeTemplateBis', views.homeTemplateBis),

    url(r'^submitConnexion', views.submitConnexion), # Lors de la connexion
    url(r'^indexUtilisateur', views.indexUtilisateur),
    url(r'^deconnexion', views.deconnexion),

    url(r'^inscription', views.inscription),
    url(r'^validerInscription', views.validerInscription), 

    url(r'^pageAjouterPersonne', views.pageAjouterPersonne),
    url(r'^ajouterPersonne', views.ajouterPersonne),
    url(r'^rechercherPersonne', views.rechercherPersonne),

    url(r'^rechercherDocument', views.rechercherDocument),
    url(r'^pageAjouterDocument', views.pageAjouterDocument),
    url(r'^ajouterDocument', views.ajouterDocument),
    url(r'^affichageDocument/(?P<idDocument>\d+)$', views.affichageDocument),

    url(r'^modifierDonneesPersonelles', views.modifierDonneesPersonelles),
    url(r'^validerModificationDonneesPerso', views.validerModificationDonneesPerso),
    url(r'^afficherDonneesPerso/(?P<idPersonne>\d+)$',views.afficherDonneesPerso),
    
    url(r'^modifierDonneesFamilleDunePersonne/(?P<idPersonne>\d+)$',views.modifierDonneesFamilleDunePersonne),
    url(r'^validerModificationDonneesPersoDunePersonne', views.validerModificationDonneesPersoDunePersonne),
    url(r'^modifierDonneesPersoDunePersonne/(?P<idPersonne>\d+)$',views.modifierDonneesPersoDunePersonne),


    url(r'^pageRechercherFamille', views.pageRechercherFamille), 
    url(r'^rechercherFamille', views.rechercherFamille),
    url(r'^ajouterFamille', views.ajouterFamille),
    url(r'^rejoindreFamille/(?P<idFamille>\d+)$',views.rejoindreFamille),

    url(r'^ajouterPereMere', views.ajouterPereMere),
    url(r'^enregistrerPereMere', views.enregistrerPereMere),

    url(r'^visualiserArbre', views.visualiserArbre),
    

    



    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, 
    document_root=settings.STATIC_ROOT)
