from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Joshi

# Add the following import
from django.http import HttpResponse

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def joshis_index(request):
    joshis = Joshi.objects.all()
    return render(request, 'joshis/index.html', { 'joshis': joshis })

def joshis_detail(request, joshi_id):
  joshi = Joshi.objects.get(id=joshi_id)
  return render(request, 'joshis/detail.html', { 'joshi': joshi } )

class JoshiCreate(CreateView):
  model = Joshi
  fields = '__all__'

class JoshiUpdate(UpdateView):
  model = Joshi
  fields = '__all__'

class JoshiDelete(DeleteView):
  model = Joshi
  success_url = '/joshis/'