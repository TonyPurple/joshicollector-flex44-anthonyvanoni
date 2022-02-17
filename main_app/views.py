from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BookingForm
import uuid
import boto3
from .models import Joshi, Item, Photo

S3_BASE_URL = 'https://s3-us-west-2.amazonaws.com/'
BUCKET = 'joshicollector'

@login_required
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

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class JoshiCreate(LoginRequiredMixin, CreateView):
  model = Joshi
  fields = ['name', 'promotion', 'style', 'nickname', 'finisher', 'age', 'itfactor', 'technique', 'power', 'speed', 'striking', 'aerial']
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  
    return super().form_valid(form)

class JoshiUpdate(LoginRequiredMixin, UpdateView):
  model = Joshi
  fields = ['name', 'promotion', 'style', 'nickname', 'finisher', 'age', 'itfactor', 'technique', 'power', 'speed', 'striking', 'aerial']

class JoshiDelete(LoginRequiredMixin, DeleteView):
  model = Joshi
  success_url = '/joshis/'

class JoshiList(LoginRequiredMixin, ListView):
  model = Joshi

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def joshis_index(request):
    joshis = Joshi.objects.filter(user=request.user)
    return render(request, 'joshis/index.html', { 'joshis': joshis })

@login_required
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

@login_required
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

@login_required
def assoc_item(request, joshi_id, item_id):
  Joshi.objects.get(id=joshi_id).items.add(item_id)
  return redirect('detail', joshi_id=joshi_id)

@login_required
def unassoc_item(request, joshi_id, item_id):
  Joshi.objects.get(id=joshi_id).items.remove(item_id)
  return redirect('detail', joshi_id=joshi_id)

class ItemList(LoginRequiredMixin, ListView):
  model = Item

class ItemDetail(LoginRequiredMixin, DetailView):
  model = Item

class ItemCreate(LoginRequiredMixin, CreateView):
  model = Item
  fields = '__all__'

class ItemUpdate(LoginRequiredMixin, UpdateView):
  model = Item
  fields = '__all__'

class ItemDelete(LoginRequiredMixin, DeleteView):
  model = Item
  success_url = '/items/'