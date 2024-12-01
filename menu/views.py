from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')  

def philosophy_view(request):
    return render(request, 'philosophy.html')

def contact_view(request):
    return render(request, 'contact.html')

def thank_you_view(request):
    return render(request, 'thank_you.html')

def menu_view(request): 
    return render(request, 'menu.html')