import random
from django.core.management.base import BaseCommand
from carcollect.models import Car, Brand, Category, Feature
from faker import Faker

class Command(BaseCommand):
    help = 'Génère des données aléatoires pour la collection'

    def handle(self, *args, **kwargs):
        fake = Faker()
        self.stdout.write("Génération des données...")

        # 1. Categories
        cats_names = ['Sportive', 'SUV de Luxe', 'Berline', 'Cabriolet', 'Hypercar']
        categories = [Category.objects.get_or_create(name=n)[0] for n in cats_names]

        # 2. Marques
        brands_data = [
            ('Ferrari', 'Italie'), ('Porsche', 'Allemagne'),
            ('Aston Martin', 'Royaume-Uni'), ('Lamborghini', 'Italie'),
            ('Bugatti', 'France')
        ]
        brands = [Brand.objects.get_or_create(name=n, country=c)[0] for n, c in brands_data]

        # 3. Features (N-N)
        feats_list = ['Sièges chauffants', 'Toit ouvrant', 'Freins Céramique', 'Carbone apparent', 'Système Hi-Fi']
        features = [Feature.objects.get_or_create(name=f)[0] for f in feats_list]

        # 4. Voitures
        for _ in range(25):
            car = Car.objects.create(
                model=fake.last_name(), # Nom de modèle aléatoire
                brand=random.choice(brands),
                category=random.choice(categories),
                power_hp=random.randint(300, 1200),
                year=random.randint(2015, 2026),
                color=fake.color_name(),
                price=random.randint(80000, 2000000)
            )
            # Ajout de 1 à 3 features aléatoires
            car.features.add(*random.sample(features, k=random.randint(1, 3)))

        self.stdout.write(self.style.SUCCESS(f'Succès : 25 voitures ajoutées à la base Oracle !'))