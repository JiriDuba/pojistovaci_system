from django.contrib import admin
from .models import Pojisteni, Pojistenec #Importujeme si modely

#Modely registrujeme
admin.site.register(Pojisteni)
admin.site.register(Pojistenec)
