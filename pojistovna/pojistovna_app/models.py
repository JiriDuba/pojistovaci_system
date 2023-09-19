from datetime import date
from django.db import models

class Pojisteni(models.Model):
    castka = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    predmet_pojisteni = models.CharField(max_length=200)
    platnost_od = models.DateTimeField(default=date.today)
    platnost_do = models.DateTimeField(default=date.today)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.id = None

    class Meta:
        verbose_name = "Pojištění"
        verbose_name_plural = "Pojištění"

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

    class Meta:
        verbose_name = "Pojištěnec"
        verbose_name_plural = "Pojištěnci"

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"



