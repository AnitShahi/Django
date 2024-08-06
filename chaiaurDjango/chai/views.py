from django.shortcuts import render
from .models import chaiVariety, Store
from .forms import ChaiVarietyForm
from django.shortcuts import get_object_or_404

# Create your views here.
def all_chai(request):
    chais = chaiVariety.objects.all()
    return render(request, 'chai/all_chai.html', {'chais': chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(chaiVariety, pk=chai_id)
    return render (request, 'chai/chai_detail.html', {'chai': chai})



def chai_store(request):
  stores = None
  if request.method == 'POST':
    form = ChaiVarietyForm(request.POST)
    if form.is_valid():
      chai_variety = form.cleaned_data['chai_variety']
      stores = Store.objects.filter(chai_varieties=chai_variety)
  else:
    form = ChaiVarietyForm()

  return render(request, 'chai/chai_stores.html', {'form': form, 'stores': stores})
