from django.shortcuts import render
from django.http import HttpResponse

posts=[
  {
    'title':'First Post',
    'author': 'Gree',
    'date':'30th Dec 2024',
    'content':' This is a dummy data not taken from DB',

  },
  {
    'title':'Second Post',
    'author':'Greeshma',
    'date': '31st Dec 2024',
    'content':'This post was created on the last day of the year',
  }
]

#Handles navigation routes
def home(request):
  #To pass the contenst from this code as arguments into the html page
  context={
    'posts':posts
  }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html', {'title':"About"})

