from django.db import models

# Create your models here.

class Domaine(models.Model):
	domains = (
			("Info","Sciences Informatiques"),
			("Ges","Sciences Administratives"),
			("Comp","Sciences Comptable")

		)
	nomDomaine = models.CharField(max_length=10,choices=domains)
	def __str__(self):
		return self.nomDomaine


class Niveau(models.Model):
	nomNiveau = models.CharField(max_length=50,unique=True)
	domaine = models.ForeignKey('Domaine')
	def __str__(self):
		return self.nomNiveau+","+self.domaine.nomDomaine

class Anneeacademique(models.Model):
	debutAnnee = models.IntegerField()
	finAnnee = models.IntegerField()
	chxActuel = (
			("1","Annee Actuelle"),
			("0","Annee Passee"),
		)
	estActuel = models.CharField(max_length=5,choices=chxActuel)
	def __str__(self):
		return str(self.debutAnnee)+"/"+str(self.finAnnee)


class Promotion(models.Model):
	niveau = models.ForeignKey('Niveau')
	anneeacademique = models.ForeignKey('Anneeacademique')
	def __str__(self):
		return self.niveau.nomNiveau+":"+str(self.anneeacademique.debutAnnee)+"/"+str(self.anneeacademique.finAnnee)


class Etudiant(models.Model):
	nom =  models.CharField(max_length=50)
	prenom =  models.CharField(max_length=50)
	email = models.EmailField(max_length=254,unique=True)
	telephone = models.CharField(max_length=15,unique=True)

	def __str__(self):
		return self.prenom+" "+self.nom


class Appartenance(models.Model):
	etudiant =  models.ForeignKey('Etudiant')
	promotion = models.ForeignKey('Promotion')
	

class Professeur(models.Model):
	nom =  models.CharField(max_length=50)
	prenom =  models.CharField(max_length=50)
	email = models.EmailField(max_length=254,unique=True)
	telephone = models.CharField(max_length=15,unique=True)

	def __str__(self):
		return self.prenom+" "+self.nom


class Matiere(models.Model):
	nomMatiere = models.CharField(max_length=50)
	def __str__(self):
		return self.nomMatiere

class Horaire(models.Model):
	#(jourMatiere,Matieres,professeur,promotion)
	jour = (
			("1","Lundi"),
			("2","Mardi"),
			("3","Mercredi"),
			("4","Jeudi"),
			("5","Vendredi"),
			("6","Samedi"),
			("7","Dimanche"),
		)
	jourMatiere = models.CharField(max_length=5,choices=jour)
	heureDebut = models.TimeField(auto_now=False, auto_now_add=False)
	heureFin = models.TimeField(auto_now=False, auto_now_add=False)
	matiere = models.ForeignKey('Matiere')
	professeur = models.ForeignKey('Professeur')
	promotion = models.ForeignKey('Promotion')


class Salle(models.Model):
	nomSalle = models.CharField(max_length=15)
	def __str__(self):
		return self.nomSalle

class UsageSalle(models.Model):
	salle = models.ForeignKey('Salle')
	promotion = models.ForeignKey('Promotion')

	def __str__(self):
		return self.salle.nomSalle


class presenceProf(models.Model):
	img_qr = models.CharField("The qrcode", max_length=100)
	nom_prof = models.CharField("Nom complet du professeur",max_length=100)
	moment = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.nom_prof

