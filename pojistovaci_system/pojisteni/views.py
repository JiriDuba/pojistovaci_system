from django.shortcuts import render, get_object_or_404, redirect
from .models import Pojisteni, Pojistenec
from .forms import PojisteniForm, PojistenecForm


# Pohled pro seznam pojištění
def pojisteni_list(request):
    pojisteni = Pojisteni.objects.all()
    return render(request, 'pojisteni/pojisteni_list.html', {'pojisteni': pojisteni})

# Pohled pro detail pojištění
def pojisteni_detail(request, pojisteni_id):
    pojisteni = get_object_or_404(Pojisteni, pk=pojisteni_id)
    return render(request, 'pojisteni/pojisteni_detail.html', {'pojisteni': pojisteni})

# Pohled pro vytvoření pojištění
def create_pojisteni(request, pojistenec_id=None):
    if request.method == 'POST':
        form = PojisteniForm(request.POST)
        if form.is_valid():
            pojisteni = form.save()
            pojisteni_od = form.cleaned_data['platnost_od']
            pojisteni_do = form.cleaned_data['platnost_do']
            pojisteni_od_formatovany = pojisteni_od.strftime('%d:%m:%y')
            pojisteni_do_formatovany = pojisteni_do.strftime('%d:%m:%y')
            return redirect('pojisteni_detail', pojisteni_id=pojisteni.pk)
    else:
        form = PojisteniForm()
    return render(request, 'pojisteni/create_pojisteni.html', {'form': form})

# Pohled pro úpravu pojištění
def edit_pojisteni(request, pojisteni_id):
    pojisteni = get_object_or_404(Pojisteni, pk=pojisteni_id)
    if request.method == 'POST':
        form = PojisteniForm(request.POST, instance=pojisteni)
        if form.is_valid():
            pojisteni = form.save()
            return redirect('pojisteni_detail', pojisteni_id=pojisteni.pk)
    else:
        form = PojisteniForm(instance=pojisteni)
    return render(request, 'pojisteni/edit_pojisteni.html', {'form': form})

# Pohled pro smazání pojištění
def delete_pojisteni(request, pojisteni_id):
    pojisteni = get_object_or_404(Pojisteni, pk=pojisteni_id)
    if request.method == 'POST':
        pojisteni.delete()
        return redirect('pojisteni_list')
    return render(request, 'pojisteni/delete_pojisteni.html', {'pojisteni': pojisteni})
