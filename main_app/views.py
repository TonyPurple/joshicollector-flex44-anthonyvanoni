from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello ♪o(*´∇｀)┌θ☆(ﾉ>_<)ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def joshis_index(request):
  return render(request, 'joshis/index.html', { 'joshis': joshis })

  # Add the Cat class & list and view function below the imports
class Joshi:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, promotion, style, nickname, age, finisher):
    self.name = name
    self.promotion = promotion
    self.style = style
    self.nickname = nickname
    self.age = age
    self.finisher = finisher

joshis = [
  Joshi('AZM', 'Stardom', 'High Speed', 'High Speed Bomb Daughter', 19, 'Azumi Sushi'),
  Joshi('Lady C', 'Stardom', 'Powerhouse', 'Human Tower', 27, 'Chokeslam'),
  Joshi('Giulia', 'Stardom', 'All-around', 'Glorious Warrior', 27, 'Glorious Buster')
]