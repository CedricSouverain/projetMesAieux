DROP Table Validation;
DROP TABLE Document;
DROP TABLE CompteFamille;
DROP TABLE Historien;
DROP TABLE Message;
DROP TABLE Personne;
DROP TABLE Utilisateur;

CREATE TABLE Utilisateur (
	idutilisateur VARCHAR2 (20) CONSTRAINT pk_utilisateur PRIMARY KEY,
	identifiant VARCHAR2 (20),
	motdepasse VARCHAR2 (20),
	adresse_mail VARCHAR2 (30));

CREATE TABLE Personne (
	idPersonne INTEGER CONSTRAINT pk_personne PRIMARY KEY,
	nom VARCHAR2(20),
	prenom VARCHAR2(20),
	date_de_naissance DATE,
	genre VARCHAR2(5), --à compléter (masculin / féminin)
	CONSTRAINT check_genre CHECK (genre BETWEEN 5 AND 5), --mettre entre Homme et femme
	nationalite VARCHAR2 (25),
	date_de_deces DATE,
	ville_de_residence VARCHAR2 (20));

CREATE TABLE Message (
	idMessage INTEGER CONSTRAINT pk_message PRIMARY KEY,
	contenu VARCHAR2 (1000),
	date_envoi_message DATE DEFAULT SYSDATE);

CREATE TABLE Historien (
	idHistorien INTEGER CONSTRAINT pk_historien PRIMARY KEY,
	nom VARCHAR2 (20),
	prenom VARCHAR2 (20),
	date_de_naissance DATE);

CREATE TABLE CompteFamille (
	idCompteFamille INTEGER CONSTRAINT pk_Comptefamille PRIMARY KEY,
	nom VARCHAR2 (20));

CREATE TABLE Document (
	idDocument INTEGER CONSTRAINT pk_document PRIMARY KEY,
	type_archive VARCHAR2(20),
	annee_archive VARCHAR2 (4));
	
CREATE TABLE Validation (
	idHistorien REFERENCES Historien,
	idDocument REFERENCES Document,
	choix VARCHAR2(3),
	CONSTRAINT check_choix CHECK (choix BETWEEN 3 AND 3),
	CONSTRAINT pk_Validation PRIMARY KEY (idHistorien, idDocument, choix));

