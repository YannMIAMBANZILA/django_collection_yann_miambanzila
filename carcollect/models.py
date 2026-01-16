from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Feature(models.Model): # Ajout pour la contrainte Relation N-N
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Car(models.Model):
    # Table principale avec 7 champs (hors ID)
    model = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars') # 1-N
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # 1-N
    power_hp = models.IntegerField()
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Relation N-N requise par les consignes
    features = models.ManyToManyField(Feature, related_name='cars')

    def __str__(self):
        return f"{self.brand.name} {self.model} ({self.year})"