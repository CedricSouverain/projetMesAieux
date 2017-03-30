// Fonction echange entre variable et html
function changerInnerHtmlId(nomId, value) {
	document.getElementById(nomId).innerHTML = value;
}


// Affichage du formulaire
function connexion() {
	var value = "<span onclick='reInitConnexion()' class='glyphicon glyphicon-chevron-up' style='margin-left:160px;'></span><br/><input type='text' class='form-control' name='identifiant' placeholder='Identifiant'><input type='password' class='form-control' name='password' placeholder='Mot de Passe'><input type='submit' value='Connexion' class='btn  btn-lg mybutton_cyano wow fadeIn' data-wow-delay='0.5s'>";
	
	
	changerInnerHtmlId("connexion", value);
}
// Re-initialisation de l'espace connexion
function reInitConnexion() {
	var value = "<a href='#' onclick='connexion()' class='btn  btn-lg mybutton_cyano wow fadeIn' data-wow-delay='0.5s'><span class='network-name'>Connexion</span></a>";
	
	changerInnerHtmlId("connexion", value);
}


// Affichage du formulaire pour entrer le nom de la famille
function ajouterFamille() {
  var value = "<span onclick='reInitAjouterFamille()' class='glyphicon glyphicon-chevron-up' style='margin-left:160px;'></span><br/><div class='form-group'><div class='input-group'><input type='text' class='form-control' name='nomFamilleAjoute' placeholder='Nom de la famille' required></div></div><div id='espaceFamille' class='input-group'><input type='submit' class='btn wow tada btn-embossed btn-primary' style='width:180px;' value='Ajouter cette famille'></div>";

  changerInnerHtmlId("espaceFamille", value);

}
// Re-initialisation de l'ajout de famille
function reInitAjouterFamille() {
  var value = "<button href='#'' onclick='ajouterFamille()'' class='btn wow tada btn-embossed btn-primary' style='width:180px;''>Ajouter une famille</button>";

  changerInnerHtmlId("espaceFamille", value);

}


// Fonction de smoothScroll
$(function() {

  $('.smoothScroll').click(function() {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        $('html,body').animate({
          scrollTop: target.offset().top
        }, 800); // rapidite
        return false;
      }
    }
  });
});


