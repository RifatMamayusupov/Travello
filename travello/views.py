from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Destinations, CustomUser, Trip
from django.http import JsonResponse


# class IndexTemplate(TemplateView):
#     template_name = 'index.html'

def get_context_data(request):

    dest = Destinations.objects.all()
    return render(request, 'index.html',{'destination': dest})

def give_detail(request, pk):   

    destination = get_object_or_404(Destinations, pk=pk)
    return render(request, 'destinations.html', {'destinations': destination})

def search_tag(request):

    if request.method == 'GET':
        city = request.GET['city']
        departure = request.GET['departure']
        arrival = request.GET['arrival']
        budget = request.GET['budget']
         
        data = Trip.objects.filter(city=city, departure=departure, arrival=arrival, budget=budget)
        return render(request, 'search_tag.html', {'trip': data})

def create_user(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')

        if name and email:
            cuser = CustomUser.objects.create(name=name, email=email)
            cuser.save()
            return render(request, 'index.html')
        else:
            return JsonResponse({'error': 'Name and email are required.'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)

def about(request):

    return render(request, 'about.html')

def contact(request):

    return render(request, 'contact.html')

def destinations(request):

    return render(request, 'destinations.html')

def news(request):

    return render(request, 'news.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pass']
        password1 = request.POST['pass2']
        
        if User.objects.filter(username=username).exists():
             messages.info(request, 'Username already exists!')
        elif password != password1:
             messages.info(request, 'Passwords do not match!')
        else:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.save()

    return render(request, 'register.html')
