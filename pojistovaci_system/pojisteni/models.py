from django.db import models
from datetime import datetime, date

class Pojisteni(models.Model):
    castka = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    predmet_pojisteni = models.CharField(max_length=200)
    platnost_od = models.DateField(default=datetime.now)
    platnost_do = models.DateField(default=datetime.now)

    def __str__(self):
        return f"Pojištění č. {self.id}: {self.predmet_pojisteni}"

class Pojistenec(models.Model):
    jmeno = models.CharField(max_length=100)
    prijmeni = models.CharField(max_length=100)
    email = models.EmailField()
    telefon = models.CharField(max_length=20)
    ulice_cislo = models.CharField(max_length=100)
    mesto = models.CharField(max_length=100)
    psc = models.CharField(max_length=10)
    pojisteni = models.ManyToManyField(Pojisteni, related_name="pojisteni")

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"
