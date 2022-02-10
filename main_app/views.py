from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import BookingForm
import uuid
import boto3
from .models import Joshi, Item, Photo

S3_BASE_URL = 'https://s3-us-west-2.amazonaws.com/'
BUCKET = 'joshicollector'

def add_photo(request, joshi_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, joshi_id=joshi_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', joshi_id=joshi_id)

class JoshiCreate(CreateView):
  model = Joshi
  fields = ['name', 'promotion', 'style', 'nickname', 'finisher', 'age', 'itfactor', 'technique', 'power', 'speed', 'striking', 'aerial']

class JoshiUpdate(UpdateView):
  model = Joshi
  fields = ['name', 'promotion', 'style', 'nickname', 'finisher', 'age', 'itfactor', 'technique', 'power', 'speed', 'striking', 'aerial']

class JoshiDelete(DeleteView):
  model = Joshi
  success_url = '/joshis/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def joshis_index(request):
    joshis = Joshi.objects.all()
    return render(request, 'joshis/index.html', { 'joshis': joshis })

def joshis_detail(request, joshi_id):
  joshi = Joshi.objects.get(id=joshi_id)
  # instantiate BookingForm to be rendered in the template
  booking_form = BookingForm()
    # Get the items the Joshi doesn't have
  items_joshi_doesnt_have = Item.objects.exclude(id__in = joshi.items.all().values_list('id'))
  return render(request, 'joshis/detail.html', { 'joshi': joshi,
   # Add the items to be displayed
    'items': items_joshi_doesnt_have,
    'booking_form': booking_form } )

def add_booking(request, joshi_id):
# create a ModelForm instance using the data in request.POST
  form = BookingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the joshi_id assigned
    new_booking = form.save(commit=False)
    new_booking.joshi_id = joshi_id
    new_booking.save()
  return redirect('detail', joshi_id=joshi_id)

def assoc_item(request, joshi_id, item_id):
  Joshi.objects.get(id=joshi_id).items.add(item_id)
  return redirect('detail', joshi_id=joshi_id)

def unassoc_item(request, joshi_id, item_id):
  Joshi.objects.get(id=joshi_id).items.remove(item_id)
  return redirect('detail', joshi_id=joshi_id)

class ItemList(ListView):
  model = Item

class ItemDetail(DetailView):
  model = Item

class ItemCreate(CreateView):
  model = Item
  fields = '__all__'

class ItemUpdate(UpdateView):
  model = Item
  fields = '__all__'

class ItemDelete(DeleteView):
  model = Item
  success_url = '/items/'