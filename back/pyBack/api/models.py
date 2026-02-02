from django.db import models

class Equipement(models.Model):
    TYPE_CHOICES = [
        ('arme', 'Arme'),
        ('défense', 'Défense'),
    ]
    
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nom

class Chevalier(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    equipement = models.ManyToManyField(Equipement, through='ChevalierEquipement')

    def __str__(self):
        return self.nom
    
class ChevalierEquipement(models.Model):
    chevalier = models.ForeignKey(Chevalier, on_delete=models.CASCADE)
    equipement = models.ForeignKey(Equipement, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('chevalier', 'equipement')
        
    def __str__(self):
        return f"{self.chevalier.nom} équipé de {self.equipement.nom}"