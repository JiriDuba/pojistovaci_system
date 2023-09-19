

from django.shortcuts import render
from django.views import generic
from .models import Pojisteni, Pojistenec
from .forms import PojistenecForm



# Pohled pro seznam pojištěnců
class PojistenciList(generic.ListView):

    template_name = "pojisteni/pojistenci_list.html"
    context_object_name = "pojistenci"

    def get_queryset(self):
        return Pojistenec.objects.all().order_by("-id")

# Pohled pro detail pojištěnce
class PojistenecDetail(generic.DetailView):
    model = Pojistenec
    template_name = "pojisteni/pojistenec_detail.html"

class PojistenecNovy(generic.edit.CreateView):
    form_class = PojistenecForm
    template_name = "pojisteni/pojistenec_novy.html"

    # Metoda pro GET request, zobrazí pouze formulář
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

    # Metoda pro POST request, zkontroluje formulář; pokud je validní, vytvoří nový film; pokud ne, zobrazí formulář s chybovou hláškou
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return render(request, self.template_name, {"form": form})
