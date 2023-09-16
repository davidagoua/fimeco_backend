from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


User = get_user_model()



class District(models.Model):
    nom = models.CharField(max_length=25)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.nom


class Circuit(models.Model):
    nom = models.CharField(max_length=25)
    slug = models.SlugField(null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.district.nom +' '+ self.slug


class EgliseLocal(models.Model):
    nom = models.CharField(max_length=25)
    slug = models.SlugField(null=True, blank=True)
    circuit = models.ForeignKey(Circuit, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.circuit.slug +' '+ self.slug
    

class Famille(models.Model):
    code_famille = models.CharField(max_length=20, blank=True)
    nom_famille = models.CharField(max_length=100)
    eglise_local = models.ForeignKey(EgliseLocal, on_delete=models.SET_NULL, null=True)
    pid = models.CharField(max_length=20, blank=True,)
    details = models.JSONField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.code_famille = f'{self.eglise_local}-{self.nom_famille}'
        super(Famille, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.nomFamille
    

class Membre(models.Model):
    roles = [
        ('Membre', 'Membre'),
        ('Chef de famille', 'ChefFamille')
    ]
    code_membre = models.CharField(max_length=20, blank=True,)
    famille = models.ForeignKey(Famille, on_delete=models.CASCADE)
    nom = models.CharField(max_length=25)
    prenoms = models.CharField(max_length=25)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100, default='')
    formation = models.CharField(max_length=100, default='')
    niveau_formation = models.CharField(max_length=100, default='')
    genre = models.CharField(max_length=10, choices=[('M', 'Masculin'), ('F', 'Feminin')], default='M')
    eglise_local = models.ForeignKey(EgliseLocal, on_delete=models.SET_NULL, null=True)
    pid = models.CharField(max_length=20, blank=True,)
    image = models.ImageField(upload_to="profile/")
    role = models.CharField(max_length=10, default="Membre")
    situation_matrimoniale = models.CharField(max_length=20, default="Celibataire")
    situation_familliale = models.CharField(max_length=20, default="Sans enfant")
    details = models.JSONField(null=True, blank=True)
    contact = models.CharField(max_length=20, blank=True,)

    enregistreur = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='enregistres', null=True)

    def __str__(self) -> str:
        return self.nom+' '+self.prenoms


class SouscriptionIndividu(models.Model):
    montant = models.PositiveBigIntegerField(default=0)
    numero = models.IntegerField(default=0)
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self) -> str:
        return self.membre.nom+' (Souscription)'
    

class Paiement(models.Model):
    montant = models.PositiveBigIntegerField(default=0)
    numero = models.IntegerField(default=0)
    famille = models.ForeignKey(Famille, on_delete=models.CASCADE)
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self) -> str:
        return self.membre.nom+' (Paiement)'





